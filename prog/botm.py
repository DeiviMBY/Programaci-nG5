#Aqui tenemos el bot regex mejorado donde graba en fichero lo escrito por bot y usuario
#importamos las librerias necesarias
import re
from io import open
def bot():
    patrones = [] #Creamos la lista de patrones con respuestas regex
    patrones.insert(len(patrones), {
        "patron":re.compile("¿Quien es tu creador?"),
        "respuesta":"Me creo  Manuel López :)",
        "respuesta2": ""
        })
    patrones.insert(len(patrones), {
        "patron":re.compile("(.*)ola, soy\s(.+)$"),
        "respuesta":"Muy buenas, ",
        "respuesta2":".Soy Botarate. "
        })
    patrones.insert(len(patrones), {
        "patron": re.compile("¿Que sabes de\s(.+)$"),
        "respuesta": "Pues la verdad de eso se poco",
        "respuesta2": ""

    })
    ui = ""
    while ui.upper() != "SALIR":
        archivo = open("convesacion.txt", "a")
        ui = input("> ")
        archivo.write(">" + ui + '\n') #Aqui ya se guarda en el archivo la linea de entrada
        response = None
        for patron in patrones: #Aqui le damos las instrucciones para la busqueda de coincidencias dentro de su "memora"
            coincidencia = patron["patron"].findall(ui)
            if len(coincidencia) > 0:
                response = patron["respuesta"]+ coincidencia[0][1] +patron["respuesta2"]
        if response == None:
            response = "Mi programador no me ha enseñado todavia a responder eso :("
        response = response[:-1]
        archivo.write(">" + response + '\n') #Aqui se guarda en el arcxhivo la linea de salida
        print(response)

