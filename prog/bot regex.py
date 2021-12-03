# Primero importamos los recursos necesarios para que el bot funcione perfectamente
import re
import os
import pickle
from botm import bot
import datetime
from nltk.chat.util import Chat
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from collections import Counter


def op1():  # Aqui tenemos el bot de respuestas simples:
    # Aqui declaramos las cuestiones grabadas para el bot de respuestas simples
    cuestiones = {"Hola": ">Muy buenas, usuario. Soy Botarate",

                  "Qué sabes de zoología": ">Pues la verdad que de eso poco.",

                  "Qué sabes de ciberseguridad": ">Pues la verdad que de eso poco.",

                  "Hola, soy Alex": ">Encantado Alex, yo soy Botarate",

                  "Perdon": ">No pasa nada",

                  "hola|hey|buenas": ">Hola qué tal",

                  "Qué quieres que haga ?": ">Nada, que me pruebes y hables conmigo",

                  "¿Qué día es hoy?": ">¡Hoy es un gran día!",

                  "Alt": ">Lo siento, me lo repites de una forma de la que lo entienda?"}
    entrada = ""
    print("\t\t Hola que quieres saber de mi, te escucho\n")

    while entrada.casefold() != "salir".casefold():
        entrada = input("\t\t>")

        if entrada in cuestiones:
            print("\t\t>", cuestiones.get(entrada))

        elif entrada.casefold() == "salir":
            print("\t\t>¡Adiós y buen día!\n")

        else:
            print("\t\t>", cuestiones.get("Alt"))


def op4(): #Aqui vamos a crear la funcion para que introduzca los datos al pdf
    sp = ''':.[]´`'(),>'''  #Aqui ponemos signos de puntuación que queremos eliminar donde nos vendra bien para estos dos casos:
    textoArchivo = open("conversacion.txt", "r")
    c = canvas.Canvas("pdf.pdf", pagesize=A4)
    c.drawImage('imgprin.jpg', 25, 480, 480, 270)
    mensaje = textoArchivo.read()
    texto = str(mensaje)
    textobject = c.beginText()
    textobject.setTextOrigin(20, 400)
    textobject.setFont("Helvetica-Oblique", 13)
    for i in textoArchivo: #Aqui vamos a darle las pautas a seguir para poder escribir correctamente en el pdf
        i = i.replace("\n", "") #no podemos usar un .drawString ya que es demasiado largo
        textobject.setCharSpace(0.5)
        textobject.setWordSpace(1)
        textobject.textLine(i)
        textobject.moveCursor(5, 10)
    textobject.setFillGray(0.4)
    textobject.setLeading(20)
    textobject.textLines(texto)
    c.drawText(textobject)
    date = datetime.date.today() #Creamos variable con la fecha actual
    c.drawString(20, 185, f"La conversacion es del {date}") # Y la mostramos en pantalla.
    dv = texto
    es = texto
    cc = 0
    for ap in es:
        if ap.isalpha(): #Contamos las letras
            cc += 1
    for dvp in dv:
        if dvp in sp: #Caso 1: vamos a contar cuantas palabras hay pero los signos son un impedimento
            dv = dv.replace(dvp, " ")
    dvs = dv.split()
    cp = len(dvs)
    dvsc = Counter(dvs)
    pmr = dvsc.most_common(1)
    pmr = str(pmr)
    for pmrm in pmr:
        if pmrm in sp: #Caso 2: para eliminar los signos de puntuacion para contar los caracteres
            pmr = pmr.replace(pmrm, " ")
    pmr = pmr.split()
    pmr1 = pmr[0]
    pmr2 = pmr[1]
    # Cadenas para mostrar por pantalla cuantos caracteres hay, cuantas palabras y cual de ellas es la que mas se reepite
    c.drawString(20, 170, f"Consta de {cc} caracteres.")
    c.drawString(20, 155, f"Esta compuesta por {cp} palabras.")
    c.drawString(20, 140, f"La palabra {pmr1} aparece {pmr2} veces.")
    textoArchivo.close()
    c.showPage()
    c.save()
    os.system("pdf.pdf")

# Aqui tenemos el bot con respuestas REGEX con sus respectivas respuestas grabadas en el codigo aprovechando el formato de respuessta REGEX
def op2():
    patrones = []
    patrones.insert(len(patrones), {
        "patron": re.compile("¿Quien es tu creador?"),
        "respuesta": "Me creo  Manuel López :)",
        "respuesta2": ""
    })
    patrones.insert(len(patrones), {
        "patron": re.compile("(.*)ola, soy\s(.+)$"),
        "respuesta": "Muy buenas, ",
        "respuesta2": ". Soy Botarate. "
    })
    patrones.insert(len(patrones), {
        "patron": re.compile("¿Que sabes de\s(.+)$"),
        "respuesta": "Pues la verdad de eso se poco",
        "respuesta2": ""

    })
    ui = ""
    while ui.upper() != "SALIR":
        ui = input("> ")
        response = None
        for patron in patrones:
            coincidencia = patron["patron"].findall(ui)
            if len(coincidencia) > 0:
                response = patron["respuesta"] + coincidencia[0][1] + patron["respuesta2"]
        if response == None:
            response = "Mi programador no me ha enseñado todavia a responder eso :("
        response = response[:-1]
        print(response)

# Aqui definimos la funcion para el menu de opciones
def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Opción: "))
            correcto = True
        except ValueError:
            print('Error, introduce un número de los disponibles')
    return num

# Programa principal
salir = False
opcion = 0

while not salir:
    # Se imprime el menú de Opciones
    print("===============")
    print("APLICACIÓN BOT-ARATE")
    print("===============")
    print("1) Bot simple")
    print("2) Bot simple con respuestas REGEX")
    print("3) Bot simple mejorado desde fichero")
    print("4) Informe de la conversación (PDF)")
    print("5) Salir")

    opcion = pedirNumeroEntero()
    if opcion == 1:
        op1()
    if opcion == 2:
        op2()
    if opcion == 3:
        bot()
    if opcion == 4:
        op4()
    if opcion == 5:
        salir = True
