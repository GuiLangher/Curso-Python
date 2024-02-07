"""
nome = "Curso Python"
valor = range(10)

print(nome)
print(valor)


lista = list(range(10))
print(lista)

lista1 = list("Curso de Python")
print(lista1)
"""
"""
texto = "meunome@gmail.com"
lista3 = list(texto)
print(lista3)

texto = texto.split("@")
print(texto)
"""
"""
carrinho_de_compras = ["produto1", "produto2", "porduto3"]
carrinho_de_compras.clear()

print(carrinho_de_compras)

for x in range(len(carrinho_de_compras)):
    print(x, carrinho_de_compras[x])
"""

lista = ["ana", "Pedro", "Marta", "Clarice", "beatriz", "ana clara"]
#sort serve para ordenão, nesse exemplo colocando em ordem alfabetica 
lista.sort(key = str.lower)
print(lista)