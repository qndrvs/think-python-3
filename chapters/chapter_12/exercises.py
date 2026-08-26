## EXERCISES
import random
filename: str = 'data/pg43.txt'
def clean_word(word: str) -> str: return word.strip('.’;,-“”:?—‘!()_').lower()
def clean_line(line: str) -> list: return line.replace('-', ' ').split()

# 1. Ask a virtual assistant
"""
a. Can you rewrite this using setdefault?
    def add_bigram(bigram):
        first, second = bigram
        successor_map.setdefault(first, []).append(second)
b. What are the differences between large language models like GPT and Markov chain text analysis?
    Son fundamentalmente distintos en mecanismo, aunque comparten el objetivo superficial de "predecir la siguiente palabra". Las diferencias clave:

    1. Orden y memoria del contexto
    Una cadena de Markov de orden k (como tu bigrama, que es orden 1) predice la siguiente palabra basándose únicamente en las últimas k palabras. No tiene noción de nada más allá de esa ventana fija. Un LLM como GPT usa una arquitectura transformer con mecanismo de self-attention, que le permite condicionar la predicción sobre todo el contexto dentro de su ventana de contexto (que puede ser de miles a cientos de miles de tokens), ponderando dinámicamente qué partes de ese contexto son relevantes para cada predicción — no es una ventana fija de tamaño k con pesos uniformes.

    2. Representación del "estado"
    En tu implementación, el estado es literalmente la tupla de palabras anteriores (una clave discreta en un diccionario). En un LLM, cada palabra/token se representa como un vector de alta dimensión (embedding) aprendido, y el "estado" tras procesar el contexto es una representación vectorial continua y distribuida — no una clave discreta. Esto le permite capturar relaciones semánticas (que "rey" y "reina" están relacionados) que una tabla de frecuencias de bigramas no puede representar en absoluto.

    3. Cómo se estiman las probabilidades
    Tu modelo de Markov calcula probabilidades por conteo de frecuencias observadas directamente del corpus (frecuentista puro, sin generalización). Un LLM aprende una función mediante descenso de gradiente sobre miles de millones de parámetros, que generaliza a secuencias que nunca vio literalmente en el entrenamiento, porque aprende regularidades estructurales y semánticas, no solo co-ocurrencias exactas.

    4. Costo de entrenamiento e inferencia
    Construir tu tabla de bigramas es O(n) en el tamaño del corpus, y la inferencia es una consulta a diccionario O(1). Entrenar un LLM requiere cómputo masivo (GPUs/TPUs durante semanas o meses) y la inferencia requiere una pasada completa por la red (multiplicaciones de matrices en cada una de las decenas de capas del transformer).

    5. Coherencia de largo alcance
    Debido al punto 1, un modelo de Markov de orden bajo genera texto que es localmente plausible (bigrama a bigrama suena "natural") pero globalmente incoherente — no puede mantener un tema, referencia, o estructura gramatical compleja a lo largo de un párrafo, porque olvida todo excepto las últimas k palabras. Un LLM puede mantener coherencia temática y referencial a lo largo de contextos mucho más largos, precisamente porque atiende a todo el contexto simultáneamente.

    Relación formal: de hecho, se puede ver a los LLMs como una generalización masiva de las cadenas de Markov — ambos son, en el fondo, modelos que definen una distribución de probabilidad sobre la siguiente palabra condicionada a lo anterior. La diferencia no es conceptual en ese nivel, sino en cómo se aproxima y parametriza esa distribución condicional: tabla de conteos discretos vs. red neuronal profunda con atención.
"""


# 2. Exercise
trigram_counter: dict = {}
window: list = []

def count_trigram(words: list):
    key: tuple = tuple(words)
    trigram_counter[key] = 1 if key not in trigram_counter else trigram_counter[key] + 1

def procces_word_trigram(word: str):
    window.append(word)
    if len(window) == 3:
        count_trigram(window)
        window.pop(0)

reader = open(filename, encoding='utf-8')
for line in reader:
    if line.startswith('***'): break
for line in reader:
    if line.startswith('***'): break
    for word in clean_line(line):
        word = clean_word(word)
        procces_word_trigram(word)
reader.close()

print(sorted(trigram_counter.items(), reverse = True, key = lambda x: x[1])[:4])


# 3. Exercise
successor_map: dict = {}
window: list = []

def add_trigram(words: list):
    key: tuple = tuple(words[:2])
    if key not in successor_map:
        successor_map[key] = words[2:]
    else:
        successor_map[key].append(words[2])

def procces_word_trigram(word: str):
    window.append(word)
    if len(window) == 3:
        add_trigram(window)
        window.pop(0)

reader = open(filename, encoding='utf-8')
for line in reader:
    if line.startswith('***'): break
for line in reader:
    if line.startswith('***'): break
    for word in clean_line(line):
        word = clean_word(word)
        procces_word_trigram(word)
reader.close()

print(successor_map)


# 4. Exercise
bigram: tuple = random.choice(list(successor_map))
print(' '.join(bigram), end = ' ')
for i in range(47):
    succesors: list = successor_map[(bigram)]
    next_word: str = random.choice(succesors)
    print(next_word, end = ' ')
    bigram: tuple = (bigram[1], next_word)
print()


# EXTRA
successor_map = {}
window = []
def add_4gram(words: list):
    key: tuple = tuple(words[:3])
    if key not in successor_map:
        successor_map[key] = words[3:]
    else:
        successor_map[key].append(words[3])
def procces_word_4gram(word: str):
    window.append(word)
    if len(window) == 4:
        add_4gram(window)
        window.pop(0)
reader = open(filename, encoding='utf-8')
for line in reader:
    if line.startswith('***'): break
for line in reader:
    if line.startswith('***'): break
    for word in clean_line(line):
        word = clean_word(word)
        procces_word_4gram(word)
reader.close()
bigram: tuple = random.choice(list(successor_map))
print(' '.join(bigram), end = ' ')
for i in range(46):
    succesors: list = successor_map[(bigram)]
    next_word: str = random.choice(succesors)
    print(next_word, end = ' ')
    bigram: tuple = (bigram[1], bigram[2], next_word)