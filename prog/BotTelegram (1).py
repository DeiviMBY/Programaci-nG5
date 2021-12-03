# importación de las librerias necesarias para realizar el bot
import telebot
import random

# Declaración de variable Token y botelegram, en la que token sera el token dado por BotFather y bot telegram sera la
# variable principal para la ejecución del bot

TOKEN = "2115968597:AAFSX3X9tmLXsyOzS8KrTeb5d70uxUZ1zuA"  # <- Token generado con el @BotFather
Botelegram = telebot.TeleBot(TOKEN)  # Creamos nuestra instancia "bot" a partir de ese TOKEN


# Función para cuando se escriba el comando "inicio" se muestre un mensaje de bienvenida por pantalla
@Botelegram.message_handler(commands=['inicio'])
def bienvenida(message):
    Botelegram.reply_to(message, "Oido cocina, Tú diras...")

# Función para que cuando se escriba el comando "ods" muestre un ojetivo de desarrollo sostenible
@Botelegram.message_handler(commands=['ods'])
def objetivo(objetivos):
    aleat = random.randint(1, 17)
# Conjunto de condiciones para aleatorizar le objetivo que se mostrará en pantalla
    if aleat == 1:
        Botelegram.reply_to(objetivos,
                            "Erradicar la pobreza en todas sus formas sigue siendo uno de los principales desafíos que enfrenta la humanidad. Si bien la cantidad de personas que viven en la extrema pobreza disminuyó en más de la mitad entre 1990 y 2015, aún demasiadas luchan por satisfacer las necesidades más básicas.")
    elif aleat == 2:
        Botelegram.reply_to(objetivos,
                            "Debido al rápido crecimiento económico y al aumento de la productividad agrícola en las últimas dos décadas, el número de personas desnutridas disminuyó casi a la mitad. Muchos países en desarrollo que sufrían hambrunas están ahora en condiciones de satisfacer las necesidades nutricionales de los más vulnerables. Regiones como Asia Central y Oriental y América Latina y el Caribe han avanzado enormemente en la erradicación del hambre.")
    elif aleat == 3:
        Botelegram.reply_to(objetivos,
                            "Hemos logrado grandes avances en la lucha contra varias de las principales causas de muerte y enfermedad. La esperanza de vida ha aumentado drásticamente, las tasas de mortalidad infantil y materna han disminuido, hemos cambiado el curso del VIH y la mortalidad debida a la malaria se ha reducido a la mitad.")
    elif aleat == 4:
        Botelegram.reply_to(objetivos,
                            "Desde 2000 se ha registrado un enorme progreso en la meta relativa a la educación primaria universal. La tasa total de matrícula alcanzó el 91% en las regiones en desarrollo en 2015 y la cantidad de niños que no asisten a la escuela disminuyó casi a la mitad a nivel mundial. También ha habido aumentos significativos en las tasas de alfabetización y más niñas que nunca antes asisten hoy a la escuela. Sin duda, se trata de logros notables.")
    elif aleat == 5:
        Botelegram.reply_to(objetivos,
                            "Poner fin a todas las formas de discriminación contra las mujeres y niñas no es solo un derecho humano básico, sino que además es crucial para el desarrollo sostenible. Se ha demostrado una y otra vez que empoderar a las mujeres y niñas tiene un efecto multiplicador y ayuda a promover el crecimiento económico y el desarrollo a nivel mundial.")
    elif aleat == 6:
        Botelegram.reply_to(objetivos,
                            "La escasez de agua afecta a más del 40 por ciento de la población mundial, una cifra alarmante que probablemente crecerá con el aumento de las temperaturas globales producto del cambio climático. Aunque 2.100 millones de personas han conseguido acceso a mejores condiciones de agua y saneamiento desde 1990, la decreciente disponibilidad de agua potable de calidad es un problema importante que aqueja a todos los continentes.")
    elif aleat == 7:
        Botelegram.reply_to(objetivos,
                            "Entre 2000 y 2016, la cantidad de personas con acceso a energía eléctrica aumentó de 78 a 87 por ciento, y el número de personas sin enegía bajó a poco menos de mil millones.")
    elif aleat == 8:
        Botelegram.reply_to(objetivos,
                            "Durante los últimos 25 años, la cantidad de trabajadores que viven en condiciones de pobreza extrema ha disminuido drásticamente, pese al impacto de la crisis económica de 2008 y las recesiones globales. En los países en desarrollo, la clase media representa hoy más del 34% del empleo total, una cifra que casi se triplicó entre 1991 y 2015.")
    elif aleat == 9:
        Botelegram.reply_to(objetivos,
                            "La inversión en infraestructura y la innovación son motores fundamentales del crecimiento y el desarrollo económico. Con más de la mitad de la población mundial viviendo en ciudades, el transporte masivo y la energía renovable son cada vez más importantes, así como también el crecimiento de nuevas industrias y de las tecnologías de la información y las comunicaciones.")
    elif aleat == 10:
        Botelegram.reply_to(objetivos,
                            "La desigualdad de ingresos está en aumento - el 10 por ciento más rico de la población se queda hasta con el 40 por ciento del ingreso mundial total, mientras que el 10 por ciento más pobre obtiene solo entre el 2 y el 7 por ciento del ingreso total. En los países en desarrollo, la desigualdad ha aumentado un 11 por ciento, si se considera el aumento de la población.")
    elif aleat == 11:
        Botelegram.reply_to(objetivos,
                            "Más de la mitad de la población mundial vive hoy en zonas urbanas. En 2050, esa cifra habrá aumentado a 6.500 millones de personas, dos tercios de la humanidad. No es posible lograr un desarrollo sostenible sin transformar radicalmente la forma en que construimos y administramos los espacios urbanos.")
    elif aleat == 12:
        Botelegram.reply_to(objetivos,
                            "El consumo de una gran proporción de la población mundial sigue siendo insuficiente para satisfacer incluso sus necesidades básicas. En este contexto, es importante reducir a la mitad el desperdicio per cápita de alimentos en el mundo a nivel de comercio minorista y consumidores para crear cadenas de producción y suministro más eficientes. Esto puede aportar a la seguridad alimentaria y llevarnos hacia una economía que utilice los recursos de manera más eficiente.")
    elif aleat == 13:
        Botelegram.reply_to(objetivos,
                            "Las pérdidas anuales promedio causadas solo por catástrofes relacionadas al clima alcanzan los cientos de miles de millones de dólares, sin mencionar el impacto humano de las catástrofes geofísicas, el 91 por ciento de las cuales son relacionadas al clima, y que entre 1998 y 2017 tomaron la vida de 1,3 millones de personas, y dejaron a 4.400 millones heridas. El objetivo busca movilizar US$ 100.000 millones anualmente hasta 2020, con el fin de abordar las necesidades de los países en desarrollo en cuanto a adaptación al cambio climático e inversión en el desarrollo bajo en carbono.")
    elif aleat == 14:
        Botelegram.reply_to(objetivos,
                            "Los medios de vida de más de 3.000 millones de personas dependen de la biodiversidad marina y costera. Sin embargo, el 30% de las poblaciones de peces del mundo está sobreexplotado, alcanzando un nivel muy por debajo del necesario para producir un rendimiento sostenible.")
    elif aleat == 15:
        Botelegram.reply_to(objetivos,
                            "Los medios de vida de más de 3.000 millones de personas dependen de la biodiversidad marina y costera. Sin embargo, el 30% de las poblaciones de peces del mundo está sobreexplotado, alcanzando un nivel muy por debajo del necesario para producir un rendimiento sostenible.")
    elif aleat == 16:
        Botelegram.reply_to(objetivos,
                            "Sin paz, estabilidad, derechos humanos y gobernabilidad efectiva basada en el Estado de derecho, no es posible alcanzar el desarrollo sostenible. Vivimos en un mundo cada vez más dividido. Algunas regiones gozan de niveles permanentes de paz, seguridad y prosperidad, mientras que otras caen en ciclos aparentemente eternos de conflicto y violencia. De ninguna manera se trata de algo inevitable y debe ser abordado.")
    elif aleat == 17:
        Botelegram.reply_to(objetivos,
                            "Los Objetivos de Desarrollo Sostenible solo se pueden lograr con el compromiso decidido a favor de alianzas mundiales y cooperación. La Asistencia Oficial para el Desarrollo se mantuvo estable pero por debajo del objetivo, a US$147.000 millones en 2017, mientras que las crisis humanitarias provocadas por conflictos o desastres naturales continúan demandando más recursos y ayuda financiera. Muchos países también requieren de esta asistencia para estimular el crecimiento y el intercambio comercial.")

# Función para que cuando se escriba el comando "ods" muestre una cita de las mostradas en el aula virtual
@Botelegram.message_handler(commands=['cita'])
def cita(citas):
    aleat = random.randint(1, 14)
# Conjunto de condiciones para aleatorizar la cita que se mostrará en pantalla
    if aleat == 1:
        Botelegram.reply_to(citas,
                            "Al no ser los únicos, decidimos ser los mejores. (Gorka Lomeña)")
    elif aleat == 2:
        Botelegram.reply_to(citas,
                            "Con demasiada frecuencia damos a los estudiantes respuestas para recordar en lugar de problemas para resolver (Roger Lewin)")
    elif aleat == 3:
        Botelegram.reply_to(citas,
                            "Con demasiada frecuencia damos a los estudiantes respuestas para recordar en lugar de problemas para resolver (Roger Lewin)")
    elif aleat == 4:
        Botelegram.reply_to(citas,
                            "Pensar es el trabajo más difícil que existe. Quizá esa sea la razón por la que haya tan pocas personas que lo practiquen. (Henry Ford)")
    elif aleat == 5:
        Botelegram.reply_to(citas,
                            "No es que sea muy inteligente. Es simplemente que estoy más tiempo con los problemas. (Albert Einstein)")
    elif aleat == 6:
        Botelegram.reply_to(citas,
                            "Programar no es un talento; es una habilidad. En tu mano está desarrollarla. (Codecademy)")
    elif aleat == 7:
        Botelegram.reply_to(citas,
                            "No digas: “Es imposible”. Di: “No lo he hecho todavía”. (Proverbio japonés)")
    elif aleat == 8:
        Botelegram.reply_to(citas,
                            "La experiencia demuestra que el éxito de un curso de programación depende críticamente de la elección de los ejemplos que se utilice. (Niklaus Wirth)")
    elif aleat == 9:
        Botelegram.reply_to(citas,
                            "Al ordenador le importa tres leches tu problema, así que el esfuerzo por que éste realice un proceso por el cual se resuelve dicho problema lo tienes que hacer TÚ. Y el esfuerzo consiste en dárselo mascado para que lo lleve a cabo una y otra vez. (Alex Tolón)")
    elif aleat == 10:
        Botelegram.reply_to(citas,
                            "Las raíces del estudio son amargas. Los frutos, dulces. (Cicerón)")
    elif aleat == 11:
        Botelegram.reply_to(citas,
                            "")
    elif aleat == 12:
        Botelegram.reply_to(citas,
                            "Las raíces del estudio son amargas. Los frutos, dulces. (Cicerón)")
    elif aleat == 13:
        Botelegram.reply_to(citas,
                            "La práctica te perfecciona. Descubre cuánta práctica necesitas tú. (Alex Tolón)")
    elif aleat == 14:
        Botelegram.reply_to(citas,
                            "Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)")

# Función para cuando se escriba el comando "inicio" se muestre un mensaje de despedida por pantalla
@Botelegram.message_handler(commands=['final'])
def final(fin):
    Botelegram.reply_to(fin, "Que pases un buen dia")

# Función que hace que el bot este continuamente atento a cual de los comandos se escriben en el chat de telegram
Botelegram.polling()