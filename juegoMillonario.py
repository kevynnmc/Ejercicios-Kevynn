import random
preguntas = {
    1:[
        {'pregunta':'¿Cuál es el continente donde se encuentra Egipto?',
         'opciones':['a) África', 'b) América', 'c) Europa', 'd) Asia'],
         'respuesta':'a'},
        {'pregunta':'¿Quién escribió "Don Quijote de la Mancha"?',
         'opciones':['a) Gabriel García Márquez','b) Mario Vargas Llosa', 'c) Miguel de Cervantes', 'd) Julio Cortázar'],
         'respuesta':'c'}
    ],
    2:[
        {'pregunta':'¿Cuál es la capital de Francia?',
         'opciones':['a) Madrid','b) Roma', 'c) París', 'd) Berlín'],
         'respuesta':'c'},
        {'pregunta':'¿Cuál es el planeta más cercano al Sol?',
         'opciones':['a) Venus','b) Tierra', 'c) Marte', 'd) Mercurio'],
         'respuesta':'d'}
    ],
    3:[
        {'pregunta':'¿Quién pintó La Última Cena?',
         'opciones':['a) Miguel Ángel', 'b) Leonardo da Vinci', 'c) Picasso', 'd) Dalí'],
         'respuesta':'b'},
        {'pregunta':'¿Cuál es el idioma oficial de Brasil?',
         'opciones':['a) Español', 'b) Portugués', 'c) Inglés', 'd) Francés'],
         'respuesta':'b'}
    ],
    4:[
        {'pregunta':'¿Cuál es la capital de Mongolia?',
         'opciones':['a) Ulán Bator', 'b) Katmandú', 'c) Hanoi', 'd) Bangkok'],
         'respuesta':'a'},
        {'pregunta':'¿Qué físico estudió la teoría de la relatividad?',
         'opciones':['a) Newton', 'b) Einstein', 'c) Tesla', 'd) Galileo'],
         'respuesta':'b'}
    ],
    5:[
        {'pregunta':'¿Qué es el bosón de Higgs?',
         'opciones':['a) Una partícula elemental', 'b) Un planeta', 'c) Una estrella', 'd) Un átomo'],
         'respuesta':'a'},
        {'pregunta':'¿Quién escribió "Crimen y castigo"?',
         'opciones':['a) Tolstói', 'b) Dostoyevski', 'c) Pushkin', 'd) Chejov'],
         'respuesta':'b'}
    ],
    6:[
        {'pregunta':'¿Cuál es el río más largo del mundo?',
         'opciones':['a) Amazonas', 'b) Nilo', 'c) Yangtsé', 'd) Misisipi'],
         'respuesta':'a'},
        {'pregunta':'¿En qué año se fundó la ONU?',
         'opciones':['a) 1945', 'b) 1939', 'c) 1950', 'd) 1960'],
         'respuesta':'a'}
    ],
    7:[
        {'pregunta':'¿Cuál es la fórmula química del agua?',
         'opciones':['a) CO2', 'b) H2O', 'c) O2', 'd) NaCl'],
         'respuesta':'b'},
        {'pregunta':'¿Qué tipo de energía se produce en una célula fotovoltaica?',
         'opciones':['a) Eléctrica', 'b) Nuclear', 'c) Química', 'd) Térmica'],
         'respuesta':'a'}
    ],
    8:[
        {'pregunta':'¿Qué año marcó el fin de la Segunda Guerra Mundial?',
         'opciones':['a) 1943', 'b) 1945', 'c) 1948', 'd) 1950'],
         'respuesta':'b'},
        {'pregunta':'¿Cuál es el teorema fundamental del cálculo?',
         'opciones':['a) Teorema de Pitágoras', 'b) La integral y derivada son inversas', 'c) Teorema de Tales', 'd) Ley de gravitación universal'],
         'respuesta':'b'}
    ],
    9:[
        {'pregunta':'¿Qué país tiene la bandera con una hoja de arce?',
         'opciones':['a) Canadá', 'b) Australia', 'c) Reino Unido', 'd) Sudáfrica'],
         'respuesta':'a'},
        {'pregunta':'¿Quién descubrió América?',
         'opciones':['a) Marco Polo', 'b) Cristóbal Colón', 'c) Vasco da Gama', 'd) Hernán Cortés'],
         'respuesta':'b'}
    ],
    10:[
        {'pregunta':'¿Qué instrumento mide la presión atmosférica?',
         'opciones':['a) Barómetro', 'b) Termómetro', 'c) Higrómetro', 'd) Anemómetro'],
         'respuesta':'a'},
        {'pregunta':'¿Qué es un pentágono?',
         'opciones':['a) Un triángulo', 'b) Un cuadrado', 'c) Una figura con cinco lados', 'd) Una figura con ocho lados'],
         'respuesta':'c'}
    ],
    11:[
        {'pregunta':'¿Cuál es el metal más ligero?',
         'opciones':['a) Plomo', 'b) Aluminio', 'c) Litio', 'd) Hierro'],
         'respuesta':'c'},
        {'pregunta':'¿Cuál es la moneda oficial de Japón?',
         'opciones':['a) Yen', 'b) Dólar', 'c) Euro', 'd) Won'],
         'respuesta':'a'}
    ],
    12:[
        {'pregunta':'¿En qué país se encuentra la Torre Eiffel?',
         'opciones':['a) España', 'b) Francia', 'c) Italia', 'd) Alemania'],
         'respuesta':'b'},
        {'pregunta':'¿Cuál es el idioma más hablado en el mundo?',
         'opciones':['a) Inglés', 'b) Chino Mandarín', 'c) Español', 'd) Hindi'],
         'respuesta':'b'}
    ],
    13:[
        {'pregunta':'¿Quién es conocido como "El padre de la computación"?',
         'opciones':['a) Alan Turing', 'b) Charles Babbage', 'c) Bill Gates', 'd) Steve Jobs'],
         'respuesta':'b'},
        {'pregunta':'¿Cuál es la capital de Australia?',
         'opciones':['a) Sídney', 'b) Canberra', 'c) Melbourne', 'd) Brisbane'],
         'respuesta':'b'}
    ],
    14:[
        {'pregunta':'¿Qué elemento tiene el símbolo "Fe"?',
         'opciones':['a) Flúor', 'b) Fósforo', 'c) Hierro', 'd) Francio'],
         'respuesta':'c'},
        {'pregunta':'¿Qué deporte se juega en Wimbledon?',
         'opciones':['a) Fútbol', 'b) Tenis', 'c) Rugby', 'd) Cricket'],
         'respuesta':'b'}
    ],
    15:[
        {'pregunta':'¿Cuál es el océano más grande?',
         'opciones':['a) Atlántico', 'b) Pacífico', 'c) Índico', 'd) Ártico'],
         'respuesta':'b'},
        {'pregunta':'¿Quién escribió "La Odisea"?',
         'opciones':['a) Homero', 'b) Virgilio', 'c) Sófocles', 'd) Esquilo'],
         'respuesta':'a'}
    ],
    16:[
        {'pregunta':'¿Qué gas es esencial para la respiración humana?',
         'opciones':['a) Nitrógeno', 'b) Oxígeno', 'c) Dióxido de carbono', 'd) Helio'],
         'respuesta':'b'},
        {'pregunta':'¿Qué país tiene la mayor población?',
         'opciones':['a) India', 'b) China', 'c) Estados Unidos', 'd) Indonesia'],
         'respuesta':'b'}
    ],
    17:[
        {'pregunta':'¿Qué instrumento mide la temperatura?',
         'opciones':['a) Barómetro', 'b) Termómetro', 'c) Higrómetro', 'd) Altímetro'],
         'respuesta':'b'},
        {'pregunta':'¿Qué civilización construyó las pirámides de Egipto?',
         'opciones':['a) Mayas', 'b) Aztecas', 'c) Egipcios', 'd) Incas'],
         'respuesta':'c'}
    ],
    18:[
        {'pregunta':'¿Cuál es el país más grande del mundo por superficie?',
         'opciones':['a) Canadá', 'b) China', 'c) Estados Unidos', 'd) Rusia'],
         'respuesta':'d'},
        {'pregunta':'¿Quién pintó "La noche estrellada"?',
         'opciones':['a) Vincent van Gogh', 'b) Pablo Picasso', 'c) Claude Monet', 'd) Salvador Dalí'],
         'respuesta':'a'}
    ],
    19:[
        {'pregunta':'¿Cuál es el nombre del satélite natural de la Tierra?',
         'opciones':['a) Luna', 'b) Phobos', 'c) Europa', 'd) Titán'],
         'respuesta':'a'},
        {'pregunta':'¿En qué año llegó el hombre a la luna?',
         'opciones':['a) 1965', 'b) 1969', 'c) 1972', 'd) 1959'],
         'respuesta':'b'}
    ],
    20:[
        {'pregunta':'¿Qué científico formuló las leyes de la gravedad?',
         'opciones':['a) Galileo', 'b) Newton', 'c) Einstein', 'd) Tesla'],
         'respuesta':'b'},
        {'pregunta':'¿Cuál es la capital de Canadá?',
         'opciones':['a) Toronto', 'b) Vancouver', 'c) Montreal', 'd) Ottawa'],
         'respuesta':'d'}
    ]
}

import random
comodines_usados = []

def usar_5050(pregunta):
    correcta = pregunta['respuesta']
    opciones = ['a', 'b', 'c', 'd']
    eliminar = random.sample([o for o in opciones if o != correcta], 2)
    return [op for op in pregunta['opciones'] if op[0] not in eliminar]
    
def llamada_amigo(pregunta):
    correcta = pregunta['respuesta']
    if random.random() < 0.8:
        sugerencia = correcta
    else:
        sugerencia = random.choice([o for o in ['a', 'b', 'c', 'd'] if o != correcta])
    return f"Tu amigo cree que la respuesta es: {sugerencia}"

def consulta_publico(pregunta):
    correcta = pregunta['respuesta']
    votos = {o: 0 for o in ['a', 'b', 'c', 'd']}
    votos[correcta] = 70
    restante = 30
    for opcion in votos:
        if opcion != correcta:
            voto = random.randint(0, restante)
            votos[opcion] = voto
            restante -= voto
    votos[correcta] += restante
    return "Votos del público:\n" + "\n".join(f"{opcion}: {porcentaje}%" for opcion, porcentaje in votos.items())

def jugar():
    puntos = 0
    for nivel in sorted(preguntas):
        for pregunta in preguntas[nivel]:
            print("\n" + pregunta['pregunta'])
            for opcion in pregunta['opciones']:
                print(opcion)

            while True:
                respuesta_usuario = input("Respuesta (a/b/c/d) o comodín (1=50/50, 2=Amigo, 3=Público): ").lower()

                if respuesta_usuario in ['a', 'b', 'c', 'd']:
                    if respuesta_usuario == pregunta['respuesta']:
                        print("¡Correcto!")
                        puntos += 1
                    else:
                        print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}")
                        print(f"Puntaje final: {puntos}")
                        return
                    break

                elif respuesta_usuario in ['1', '2', '3']:
                    comodin_elegido = int(respuesta_usuario)
                    if comodin_elegido in comodines_usados:
                        print("Ya usaste ese comodín.")
                        continue
                    comodines_usados.append(comodin_elegido)

                    if comodin_elegido == 1:
                        opciones_restantes = usar_5050(pregunta)
                        print("Opciones después del 50/50:")
                        for opcion in opciones_restantes:
                            print(opcion)
                    elif comodin_elegido == 2:
                        print(llamada_amigo(pregunta))
                    else:
                        print(consulta_publico(pregunta))
                else:
                    print("Intenta nuevamente.")
    print(f"Felicidades! Tu puntaje total fue: {puntos}")
jugar()


