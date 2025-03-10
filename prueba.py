import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import requests
import time

ubicaciones_universidad = {
    "la cafetería": {
         "la cafetería": "En este momento estás en la cafetería",
         "la porteria": "Desde la cafeteria, avanza hacia el edificio A. Baja las escaleras que están a mano derecha y llegarás a la porteria",
         "la enfermeria": "Desde la cafeteria, avanza hacia las escaleras del edificio B y baja por ese pasillo, justo en medio encontrarás la enfermería a mano derecha.",
         "la clínica": "Desde la cafeteria, avanza hacia el edificio A. Baja las escaleras y encontrarás la clínica a mano derecha.",
        "la biblioteca": "Desde la cafetería, avanza hacia el Edificio A. Luego, sube las escaleras y, a mano derecha, encontrarás la biblioteca.",
        "los cubículos udies": "Desde la cafetería, avanza hacia las escaleras del Edificio A. Luego, sube hasta el segundo piso y, a mano izquierda, encontrarás los cubículos UDIES.",
        "la decanatura": "Desde la cafetería, avanza hacia las escaleras del Edificio A. Luego, sube hasta el tercer piso y, a mano izquierda, encontrarás la Decanatura.",
        "la sala de informática": "Desde la cafetería, avanza hacia las escaleras del Edificio A. Luego, sube hasta el tercer piso, avanza, gira a la derecha y en el pasillo de en frente encontrarás las tres Salas de Informática.",
        "el laboratorio de telemática": "Desde la cafetería, avanza hacia las escaleras del Edificio A. Luego, sube hasta el cuarto piso, gira hacia la izquierda y al fondo encontrarás el Laboratorio de Telemática.",
        "el almacén": "Desde la cafetería, avanza hacia las escaleras del Edificio A. Luego, sube hasta el cuarto piso, gira hacia la izquierda y en la mitad del pasillo encontrarás el Almacén.",
        "el laboratorio de comunicaciones": "Desde la cafetería, avanza hacia las escaleras del Edificio A. Luego, sube hasta el cuarto piso, gira a la derecha, avanza hasta la puerta que tienes en frente y ahí encontrarás el Laboratorio de Comunicaciones.",
        "el laboratorio de antenas": "Desde la cafetería, avanza hacia las escaleras del Edificio A. Luego, sube hasta el cuarto piso, gira a la derecha, avanza por el pasillo, gira nuevamente a la derecha y al lado del Laboratorio de Comunicaciones encontrarás el Laboratorio de Antenas."
    }
}

ubicaciones_universidad_discapacitados = {
    "la cafetería": {
        "la cafetería": "En este momento estás en la cafetería",
        "la porteria":"Desde la cafetería, avanza cuatro pasos hacia adelante, gira a la derecha y continúa dieciséis pasos. Luego, gira a la izquierda, avanza dos pasos y ¡cuidado! baja dos escalones pequeños. Sigue veinte pasos hacia adelante, baja otros dos escalones pequeños, avanza doce pasos más y prepárate para descender una escalera de diez escalones. Al finalizar, habrás llegado a la portería.",
        "la enfermeria": "Desde la cafetería, avanza cuatro pasos hacia adelante, gira a la derecha y continúa treinta pasos. Luego, gira a la izquierda y avanza seis pasos. ¡Cuidado! Baja siete escalones, avanza cinco pasos y desciende otros seis escalones. Continúa cinco pasos más y, a tu derecha, encontrarás la enfermería.",
        "la clínica": "Desde la cafetería, avanza cuatro pasos hacia adelante, gira a la derecha y continúa treinta pasos. Luego, gira a la izquierda y avanza seis pasos. ¡Cuidado! Baja siete escalones, avanza cinco pasos y desciende otros seis escalones. Continúa veintisiete pasos hacia adelante y encontrarás la clínica de odontología.",
        "la biblioteca": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos. ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, sube diez escalones y, tras ocho pasos hacia el frente, a mano derecha se encuentra la biblioteca.",
        "los cubiculos udies": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos. ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, sube diez escalones y, tras diez pasos hacia el frente, a mano izquierda se encuentran los cubículos UDIES.",
        "la decanatura": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos. ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, sube diez escalones, gira a la derecha y sube otros diez escalones. Gira nuevamente a la derecha, sube diez escalones más, avanza cuatro pasos hacia adelante y, a mano izquierda, encontrarás la decanatura.",
        "la sala de informatica": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos. ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, sube diez escalones, gira a la derecha y sube otros diez escalones. Gira nuevamente a la derecha, sube diez escalones más, avanza ocho pasos hacia adelante y luego treinta pasos hacia la derecha. En el pasillo que está en frente, encontrarás las tres salas de informática.",
        "el laboratorio de telematica": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos. ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, luego sube diez escalones y gira a la derecha. Sube otros diez escalones, gira nuevamente a la derecha y sube diez escalones más. Gira una vez más a la derecha y sube diez escalones. Finalmente, gira a la derecha, sube diez escalones más, avanza cuatro pasos hacia el frente y sube los seis escalones que están a tu izquierda. Avanza veinte pasos más y frente a ti encontrarás el laboratorio de telemática.",
        "el almacen": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos.  ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, luego sube diez escalones y gira a la derecha. Sube otros diez escalones, gira nuevamente a la derecha y sube diez escalones más. Gira una vez más a la derecha y sube diez escalones. Finalmente, gira a la derecha, sube diez escalones más, avanza cuatro pasos hacia el frente y sube los seis escalones que están a tu izquierda. Avanza catorce pasos más y a mano derecha encontrarás el almacén.",
        "el laboratorio de comunicaciones": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos. ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, luego sube diez escalones y gira a la derecha. Sube otros diez escalones, gira nuevamente a la derecha y sube diez escalones más. Gira una vez más a la derecha y sube diez escalones. Finalmente, gira a la derecha, sube diez escalones más, avanza nueve pasos hacia adelante y treinta y un pasos hacia la derecha. Enfrente encontrarás el laboratorio de comunicaciones.",
        "el laboratorio de antenas": "Desde la cafetería, avanza cuatro pasos hacia adelante, luego diez pasos hacia la derecha. Gira a la izquierda y avanza dos pasos. ¡Cuidado! Hay dos escalones pequeños. Continúa veinte pasos hacia adelante y nuevamente encontrarás dos escalones pequeños. Avanza doce pasos más, luego sube diez escalones y gira a la derecha. Sube otros diez escalones, gira nuevamente a la derecha y sube diez escalones más. Gira una vez más a la derecha y sube diez escalones. Finalmente, gira a la derecha, sube diez escalones más, avanza nueve pasos hacia adelante y treinta y un pasos hacia la derecha. Luego, gira a la derecha, avanza unos pasos y encontrarás el laboratorio de antenas al lado del laboratorio de comunicaciones."
        }
    }

def transformar_audio_en_texto():
    r = sr.Recognizer()  

    with sr.Microphone() as origen:
        r.pause_threshold = 1  
        print("Ya puedes hablar")

        while True:  
            try:
                audio = r.listen(origen)
                pedido = r.recognize_google(audio, language="es-co")
                print("El audio convertido a texto es: " + pedido)
                return pedido.lower()
            
            except sr.UnknownValueError:
                print("No te entiendo, repite otra vez")
                hablar("No te entendí, intenta de nuevo.")

def hablar(mensaje):
    engine = pyttsx3.init() #sirve para la transformacion de voz a texto
    engine.setProperty("voice", n)
    engine.say(mensaje)
    engine.runAndWait()
    
engine = pyttsx3.init() #para inicializar la escucha
for voz in engine.getProperty("voices"):
    print(voz)

n="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"


def obtener_ruta_estandar(origen, destino):
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

def obtener_ruta_discapacitados(origen, destino):
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
    print(dia)
    
    dia_semana = dia.weekday()
    print(dia_semana)
    

    semana  = {0: "Lunes", 1:"Martes", 2:"Miercoles", 3:"Jueves", 4:"Viernes",
               5: "Sabado", 6: "Domingo"}

    hablar(f'Hoy es {semana[dia_semana]} {dia}')


def solicitar_hora():
    hora = datetime.datetime.now()
    hora = f'Son exactamente las {hora.hour} con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    hablar(hora)

def obtener_clima(ciudad):
    api_key = "b19460c95233eca9a770d116d31c3202"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    respuesta = requests.get(url).json()
    if respuesta['cod'] == 200:
        temperatura = respuesta['main']['temp']
        print(f"La temperatura en {ciudad} es de {temperatura}°C")
        hablar(f"La temperatura en {ciudad} es de {temperatura} grados")
    else:
        hablar("No pude obtener el clima")


def saludo_alexa():
    hora = datetime.datetime.now()
    if hora.hour <6 and hora.hour >=19:
        saludo = "Buenas noches"
    elif hora.hour >= 6 and hora.hour <12:
        saludo = "Buenos días"
    else:
        saludo = "Buenas tardes"
    hablar(f'{saludo}, mi nombre es Alexa. Soy la asistente virtual de la Santoto, di Iniciar para empezar esta emocionante aventura..')   
    
def preguntar_discapacidad_visual():
    hablar("¿Eres una persona con discapacidad visual? Si ves poquito tirando a nada, di 'Si'. Si ves bien aunque no viste sus mentiras, di 'No'.")
    while True:
        respuesta = transformar_audio_en_texto().lower()

        if "sí" in respuesta:
            hablar("Entendido. Activaré funciones accesibles para ti.")
            desplegar_menu_discapacitados()
            return True
        elif "no" in respuesta:
            hablar("Gracias por tu respuesta. Continuemos.")
            desplegar_menu_estandar()
            return False
        else:
            hablar("No entendí bien. Intenta de nuevo. Recuerda, di 1 para sí y 2 para no.")
    
    
def iniciar_alexa():
    
    comenzar = True
    while comenzar:
        saludo_alexa()
        time.sleep(20)#Saludo cada 20 segundos
        solicitud = transformar_audio_en_texto()

        if solicitud:
            solicitud = solicitud.lower()
            if "iniciar" in solicitud:
                discapacidad_visual = preguntar_discapacidad_visual()
                
        else:
            continue


def decir_menu():
    
    hablar(""" 
        Estas son las opciones que tienes disponibles:
            
        Primero: Si quieres saber como llegar a algun lugar di, "ruta"
        Segundo: Si quieres saber el clima di "clima... en "... y luego el nombre de tu ciudad. 
        Tercero: Si quieres saber que día es hoy, di "día".
        Cuarto: Si quieres saber la hora, di "hora".
        Quinto: Si quieres buscar algo en internet, di "buscar sobre"... y luego el tema que deseas.
        Sexto: Si quieres reproducir una canción , di "reproducir" y luego el nombre de la canción.
        Septimo: Si quieres escuchar un chiste, di "broma". 
        Octavo: Si terminaste di, "adios"
           
           """)
    
def desplegar_menu_estandar():
    
    decir_menu()
    
    while True:
        
        solicitud =  transformar_audio_en_texto().lower()
        
        if not solicitud:
            hablar("No entendí bien, intenta de nuevo.")
            continue
        
        if 'clima en' in solicitud:
            ciudad = solicitud.replace("clima en", "").strip()
            obtener_clima(ciudad)
            continue
        
        elif 'día' in solicitud:
            solicitar_dia()
            continue
        
        elif 'hora' in solicitud:
            solicitar_hora()
            continue
        
        elif 'buscar' in solicitud:
            hablar('Ya mismo estoy en eso ')
            solicitud = solicitud.replace('buscar sobre', '')
            pywhatkit.search(solicitud)
            hablar('Esto es lo que he encontrado...')
            continue
        
        elif 'reproducir' in solicitud:
            hablar('Amo escuchar musica... tienes buen gusto, y dice!')
            pywhatkit.playonyt(solicitud)
            continue
        
        elif 'broma' in solicitud:
            hablar(pyjokes.get_joke('es'))
            continue
        
        elif "ruta" in solicitud:
            hablar("Con Alexa, puedes ir a casi cualquier lugar de la Sede Bucaramanga, eso sí, cuidado con las escaleras!!!")
            hablar("¿A dónde quieres ir desde la cafetería?")
            
            destino = transformar_audio_en_texto().strip()
            
            if destino:
                obtener_ruta_estandar("la cafetería", destino)
            else:
                hablar("No entendí bien, intenta de nuevo.")
            continue
            
        elif 'adiós' in solicitud:
            hablar("Nos vemos socio, cualquier cosa me chifla")
            break

def desplegar_menu_discapacitados():
    
    decir_menu()
    
    while True:
        
        solicitud =  transformar_audio_en_texto().lower()
        if not solicitud:  # Validación para evitar errores con solicitudes vacías
            hablar("No entendí bien, intenta de nuevo.")
            continue
        
        if 'clima en' in solicitud:
            ciudad = solicitud.replace("clima en", "").strip()
            obtener_clima(ciudad)
            continue
        
        elif 'día' in solicitud:
            solicitar_dia()
            continue
        
        elif 'hora' in solicitud:
            solicitar_hora()
            continue
        
        elif 'buscar' in solicitud:
            hablar('Ya mismo estoy en eso ')
            solicitud = solicitud.replace('buscar sobre', '')
            pywhatkit.search(solicitud)
            hablar('Esto es lo que he encontrado...')
            continue
        
        elif 'reproducir' in solicitud:
            hablar('Amo escuchar musica... tienes buen gusto, y dice!')
            pywhatkit.playonyt(solicitud)
            continue
        
        elif 'broma' in solicitud:
            hablar(pyjokes.get_joke('es'))
            continue
        
        elif "ruta" in solicitud:
            hablar("Con Alexa, puedes ir a casi cualquier lugar de la Sede Bucaramanga, eso sí, cuidado con las escaleras!!!")
            hablar("¿A dónde quieres ir desde la cafetería?")
            
            destino = transformar_audio_en_texto().strip()
            
            if destino:
                obtener_ruta_discapacitados("la cafetería", destino)
            else:
                hablar("No entendí bien, intenta de nuevo.")
            continue
            
        elif 'adiós' in solicitud:
            hablar("Nos vemos socio, cualquier cosa me chifla")
            break
        
iniciar_alexa()