# -*- coding: utf-8 -*-

import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import requests
import time
from gtts import gTTS
import pygame
import os

pygame.init()  # Inicializar pygame antes de usar el mezclador
pygame.mixer.init()

ubicaciones_universidad = {
    "la cafeterÃ­a": {
        "la biblioteca": "Si estÃ¡s en frente de la cafeterÃ­a principal, sube las escaleras que estÃ¡n a tu izquierda para llegar a la biblioteca."
    },
    "la biblioteca": {
        "la cafeterÃ­a": "Desde la biblioteca, baja las escaleras y estarÃ¡s frente a la cafeterÃ­a principal."
    }
}

def hablar(mensaje):
    tts = gTTS(text=mensaje, lang='es', slow = False)  # Asegurar espaÃ±ol colombiano
    filename = "audio.mp3"
    tts.save(filename)
    if not pygame.mixer.get_init():  # Verificar si pygame.mixer estÃ¡ inicializado
            pygame.mixer.init()
    #pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
        
    #pygame.mixer.quit()
    os.remove(filename)

def transformar_audio_en_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 1
        try:
            print("Escuchando...")
            audio = r.listen(origen, timeout=3, phrase_time_limit=5)
            pedido = r.recognize_google(audio, language="es")
            print("El audio convertido a texto es: " + pedido)
            return pedido
        except sr.UnknownValueError:
            print("No te entiendo, repite otra vez")
            return ""

def obtener_ruta(origen, destino):
    origen = origen.lower().strip()
    destino = destino.lower().strip()

    print(f"Origen: {origen}, Destino: {destino}")

    if origen in ubicaciones_universidad:
        if destino in ubicaciones_universidad[origen]:
            ruta = ubicaciones_universidad[origen][destino]
            print(ruta)
            hablar(ruta)
        else:
            mensaje = f"No tengo información sobre cómo ir de {origen} a {destino}. Prueba con otro destino."
            print(mensaje)
            hablar(mensaje)
    else:
        mensaje = f"No tengo registrado el lugar {origen}. Intenta de nuevo."
        print(mensaje)
        hablar(mensaje)

def solicitar_dia():
    dia = datetime.date.today()
    semana = ["Lunes", "Martes", "MiÃ©rcoles", "Jueves", "Viernes", "SÃ¡bado", "Domingo"]
    hablar(f'Hoy es {semana[dia.weekday()]} {dia}')

def solicitar_hora():
    hora = datetime.datetime.now()
    hablar(f'Son exactamente las {hora.hour} con {hora.minute} minutos y {hora.second} segundos')

def obtener_clima(ciudad):
    api_key = "b19460c95233eca9a770d116d31c3202"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    respuesta = requests.get(url).json()
    if respuesta['cod'] == 200:
        temperatura = respuesta['main']['temp']
        descripcion = respuesta['weather'][0]['description']
        hablar(f"La temperatura en {ciudad} es de {temperatura} grados y el clima es {descripcion}")
    else:
        hablar("No pude obtener el clima")

def saludo_alexa():
    hora = datetime.datetime.now().hour
    if hora < 6 or hora > 20:
        saludo = "Buenas noches"
    elif hora < 13:
        saludo = "Buenos dÃ­as"
    else:
        saludo = "Buenas tardes"
    hablar(f'{saludo}, mi nombre es Alexa. Soy la asistente virtual de la Santoto. Di "Iniciar" para empezar esta emocionante aventura.')
    while pygame.mixer.music.get_busy():  # Esperar a que termine de hablar
        time.sleep(0.1)
    time.sleep(1)  # Dar un breve tiempo antes de mostrar el mensaje
    print("Hola, ya puedes hablar")

def preguntar_discapacidad_visual():
    hablar("Â¿Eres una persona con discapacidad visual? Di 'SÃ­' o 'No'.")
    while True:
        respuesta = transformar_audio_en_texto().lower()
        if "sÃ­" in respuesta:
            hablar("Entendido. ActivarÃ© funciones accesibles para ti.")
            return True
        elif "no" in respuesta:
            hablar("Gracias por tu respuesta. Continuemos.")
            return False
        else:
            hablar("No entendÃ­ bien. Intenta de nuevo.")

def iniciar_alexa():
    saludo_alexa()
    while True:
        solicitud = transformar_audio_en_texto()
        if solicitud and "iniciar" in solicitud.lower():
            preguntar_discapacidad_visual()
            desplegar_menu()
            break

def decir_menu():
    hablar("Hola! Estas son las opciones disponibles: Ruta, Clima, DÃ­a, Hora, Buscar, Reproducir mÃºsica, Broma, AdiÃ³s")

def desplegar_menu():
    decir_menu()
    while True:
        solicitud = transformar_audio_en_texto().lower()
        if "clima" in solicitud:
            ciudad = solicitud.replace("clima en", "").strip()
            obtener_clima(ciudad)
        elif "dÃ­a" in solicitud:
            solicitar_dia()
        elif "hora" in solicitud:
            solicitar_hora()
        elif "buscar" in solicitud:
            hablar('Buscando en Internet')
            solicitud = solicitud.replace('buscar sobre', '').strip()
            pywhatkit.search(solicitud)
        elif "reproducir" in solicitud:
            hablar('Reproduciendo en YouTube')
            pywhatkit.playonyt(solicitud.replace("reproducir", "").strip())
        elif "broma" in solicitud:
            hablar(pyjokes.get_joke('es'))
        elif "ruta" in solicitud:
            hablar("Â¿DÃ³nde te encuentras en este momento?")
            origen = transformar_audio_en_texto().strip()
            hablar("Â¿A dÃ³nde quieres ir?")
            destino = transformar_audio_en_texto().strip()
            obtener_ruta(origen, destino)
        elif "adiÃ³s" in solicitud:
            hablar("Nos vemos, cualquier cosa me chiflas")
            break

iniciar_alexa()
