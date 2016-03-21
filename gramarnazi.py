# -*- coding: utf-8 -*-

adverbios = ["mas", "poco", "pocos", "poca", " pocas ", "mucho", "mucha",
"muchos", "muchas", "suficiente", "bastante", "suficientes", "bastantes",
"practicamente", "rapidamente", "realmente", "suavemente", "obviamente",
"mejor", "peor", "deprisa", "lento", "bien", "mal", "tan", "tanto", "mas",
"menos", "mejor", "continuamente", "previamente", "mutuamente", 
"absolutamente", "ademas", "tantas", "muy", "probablemente"]

relleno = ["base fundamental", "bifucarse en dos direcciones", 
"chivo joven", "aterido de frio", "aterida de frio", "constalacion de estrellas",
"falso pretexto", "divisa extranjera", "divisas extranjeras", "insistir reiteradamente",
"kilos de peso", "kg de peso", "mendrugo de pan", "prever con atenlacion",
"soler ir a menudo", "vigente actualidad", "utopia inalcanzable", "historia a sus espaldas",
"el paso del tiempo", "crece por momentos", "lo dicho previamente", "se ayudaran mutuamente",
"sectores juveniles", "presentes en nuestro mundo", "mi persona", "del mismo", "de la misma",
"ello", "a su persona", "ejerce de", "se encuentra", "en las inmediaciones", "rigurosidad",
"me embarga", "contener las lagrimas", "me invade", "llanamente", "de alguna manera",
"como es natural", "bien es", "a nivel de", "en base a", "de cara a", "en principio",
"podriamos anadir", "hay que destacar", "en ese sentido", "sin lugar a dudas", 
"interesa destacar", "existente", "producto estrella"
"disfrutar de un buen libro", "se encuentra ubicado",
"la provincia de", "parte integrante", "proporcionado por",
"pura y llanamente", "tantos", "tantas"]

adjetivos = ["azul", "rojo", "verde", "artesanales", "buen", "amarillo", 
"roja", "amarilla", "naranja", "grande", "pequeno", "alto", "alta", "baja", 
"exhaustivo", "esencial", "extensos", " rico", "inmortales", "dulce", 
"urbano", "angosto", "empinadas", "caotica", "multicolores", 
"asombrosas", "tranquila", "abandonados", "solitarios", "forestal", 
"contento", "triste", "bonito", "seca", "seco", "estupendo", "bueno", 
"dificil", "cutre", "guapo", "hermoso", "hermosa", "intempestivas", 
"melancolico", "extranas", "encanto", "bello", "extraordinario", 
"impresionantes", "colosal", "conocidos", "populares", "antiguo", 
"turquesa", "enorme", "sonada", " ideal", "buena", "sublime", "cromatico", 
"rosaceos"," rosas ", "musi", "artesanales", "islamico", "famosas", 
"memorable", "gran", "efimero", "escasos", "hermosos", "fundamental", "famosos",
 "rosas", "irreales", "grande", "gigantescas", "sencilla", 
 "verdadera", "estrella", "guiadas", "campero", "barato",
 "musicales", "rupestre", "blanco", "escarpado", "financiera",
 "real", "salariales", "imposible"]

abstractas =["capacidades", "fortalezcan", "pueblos", "personas", "pobreza"
"violencia", "inequidad", "realidad", "procesos", "modelo de desarrollo", "desarrollo",
"ciudadania", "participacion", "soluciones", "innovacion", "partivipativa", "problemas",
"deseos", "libertad", "condicionamientos"]

preposiciones = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 
'de', 'desde', 'en', 'entre', 'hacia', 'hasta', 'para', 
'por', 'segun', 'sin', 'so', 'sobre', 'tras']

circunloquios = ["llevar a cabo", "prestar atencion", "hacer saber", 
"que tiene", "que no tiene"]

verbos_pobres = ["tener", "hacer", "haber", "ser", 
"poner", "tiene", "hace", "pone", "es", "tienen", 
"tuvo", "tuve", "tuvieron", "estan", "disfrutar", "haciendo",
"tiene"]

nexos = ["cuando", "luego", "en primer lugar", "primero", "en segundo lugar",
"por un lado", "por otro lado"]

pasiva = ["fue", "por la", "por el", "fueron"]

gritos = "!"

preguntas = "?"

file = raw_input('Escribe el nombre del archivo: ')
try:
	handle = open(file)


except:
	print('no se encuentra el archivo')
	exit()

text = handle.read() # lee el texto
texto = text.split() # divide el texto en palabras
frases = text.split(".")
comas = text.split(",")
contafrases = len(frases)
contacomas = len(comas) - 1 #cada coma genera dos elementos

import string

contapalabras = 0
contadjetivos = 0
contadverbios = 0
contalargas = 0
contapreposiciones = 0
contaverbospobres = 0
contapasivas = 0

dictpalabras = dict()
dictadjetivos = dict()
dictadverbios = dict()
dictpreposiciones = dict()
dictlargas = dict()
dictverbospobres = dict()
dictpasivas = dict()


for palabra in texto:
	palabra = palabra.translate(None, string.punctuation)
	palabra = palabra.lower()
	dictpalabras[palabra] = dictpalabras.get(palabra,0) + 1
	contapalabras = contapalabras + 1
	#print palabra, dictpalabras[palabra]
	
	# Busca adjetivos
	if palabra in adjetivos: # busca adverbios en el listado de palabras
	 	dictadjetivos[palabra] = dictadjetivos.get(palabra,0) + 1 # anade 1 a la clave valor cuando encuentra un adverbio y actualiza el resultado si lo encuentra mas veces	
		contadjetivos = contadjetivos + 1

	# Busca adverbios
	if palabra in adverbios:
		dictadverbios[palabra] = dictadverbios.get(palabra,0) + 1
		contadverbios = contadverbios + 1
		#print palabra, dictadverbios[palabra]

	# Busca preposiciones
	if palabra in preposiciones:
 	 	dictpreposiciones[palabra] = dictpreposiciones.get(palabra,0) + 1
 	 	contapreposiciones = contapreposiciones + 1

 	# Busca verbos pobres
 	if palabra in verbos_pobres:
 		dictverbospobres[palabra] = dictverbospobres.get(palabra,0) + 1
 		contaverbospobres = contaverbospobres + 1

 	# Posibilidad de pasivas
 	if palabra in pasiva:
 		dictpasivas[palabra] = dictpasivas.get(palabra,0) + 1
 		contapasivas = contapasivas + 1


 	if len(palabra) > 7:
 		dictlargas[palabra] = dictlargas.get(palabra,0) + 1
 		contalargas = contalargas + 1
 		#print palabra, dictlargas[palabra]


# lista_palabras = sorted(dictpalabras.items())
# print lista_palabras

# for word,count in sorted(dictpalabras.items()): # ordena las palabras del texto a traves del diccionario de palabras
# 	print word,count

lista_palabras = list()

for word,count in dictpalabras.items(): #lista las palabras del diccionario por el valor, no por la palabra
	lista_palabras.append( (count,word) ) #anade una tupla

#print lista_palabras
#lista_palabras.sort() # ordena las palabras por el valor de menor a mayor

lista_palabras.sort(reverse=True) # ordena las palabras por valor de mayor a menor

for v,k in lista_palabras[:50]:
	print v,k
	#print k, round(float(v) / float(contapalabras) * 100), '%'


# Orden adverbios
print 'Lista de adverbios:'
lista_adverbios = list()

for word,count in dictadverbios.items():
	lista_adverbios.append((count, word))

lista_adverbios.sort(reverse=True)

for conta,value in lista_adverbios:
	print conta, value

# Orden adjetivos

print 'Lista adjetivos'

lista_adjetivos = list()

for k, v in dictadjetivos.items():
	lista_adjetivos.append((v,k))

lista_adjetivos.sort(reverse=True)

for v, k in lista_adjetivos:
	print v,k


# Orden palabras largas
# print 'Lista de palabras largas'

# lista_largas = list()
# for word,count in dictlargas.items():
# 	lista_largas.append((count, word))

# lista_largas.sort(reverse=True)

# for c,w in lista_largas:
# 	print c,w


# print 'Frases: ',contafrases
print 'Media de palabras por frase: ',contapalabras / contafrases
print 'Ritmo frases: ',round(float(contafrases) / float(contacomas)), 'coma por frase'
# #print 'Comas: ',contacomas
print 'Adjetivos: ',contadjetivos,'(',round(float(contadjetivos) / float(contapalabras) * 100),'%)'
print 'Adverbios: ',contadverbios
print 'Preposiciones: ', contapreposiciones
print 'Media de preposiciones por frase: ', float(contafrases) / float(contapreposiciones)
print 'Palabras largas: ', contalargas, '(',round(float(contalargas) / float(contapalabras) * 100), '%)'
# print 'Palabras: ', contapalabras
print 'Verbos auxiliares: ', contaverbospobres,'(',round(float(contaverbospobres) / float(contapalabras) * 100),'%)'
print 'Posibilidades de pasiva: ', contapasivas

















#print dictadverbios
#print 'Frases: ',contafrases

# Encuentra el adjetivo mas usado
# Bigadjetivo = None
# Bigcountadjetivo = None

# for clave, valor in dictadjetivos.items():
# 	if Bigadjetivo is None:
# 		Bigadjetivo = clave
# 		Bigcountadjetivo = valor

# 	elif Bigcountadjetivo < valor:
# 		Bigadjetivo = clave
# 		Bigcountadjetivo = valor

# print Bigadjetivo, Bigcountadjetivo


