"""Exercícios - Python 

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

plataformas para treinar sua lógica: site - uri

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais qual 
será o valor do mesmo com desconto de (??)%.
04 - área de um círculo - pi = 3,141592
05 - conversão de reais para dolar
06 -  conversão de dolar para reais

"""

"""
#Exercício 01 - área do retângulo

print("Calcule a area de um retangulo")

base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("Qual o tamanho da altura do seu retangulo? ")
area = float(base) * float(altura)

print(f'O seu retangulo possui area: {area} m2')
"""

"""
#Exercício 02 - área do quadrado

print("Calcule a area do quadrado")

base = input("Qual o valor da Base?")
altura = input("Qual o valor da Altura?")

area = float(base) * float(altura)

print(f"O seu quadrado possui uma area de {area} m2")
"""

"""
#Exercício 03 - Se o produto que você quer avaliar custa (??) reais qual 
será o valor do mesmo com desconto de (??)%.

print("Calcule o desconto")

valor = input("Qual o valor do produto? ")
desconto = input("Qual a porcentagem do desconto? ")

#O valor que sobra é a porcentagem, então no final se subtrai o valor da porcentagem do valor do produto

porcentagem = (int(desconto) / 100) * float(valor)

final = float(valor) - float(porcentagem)

print(f"O valor final é R${final}")
"""

"""
#Exercício 04 - área de um círculo - pi = 3.141592

pi = 3.141592
raio = input("Qual o valor do raio? ")

area = float(pi) * (float(raio) ** 2)

print(f"A area do circulo eh {area}")
"""
"""
#Exercício 05 - conversão de reais para dolar

print("Converta Real para Dolar")

real = input("Quantos Reais queres converter para Dolar? R%")
dolar = 4.87

conversao = float(real) / float(dolar)

print(f"Convertendo R${real} voce tera ${conversao}")
"""
"""
#Exercício 06 - conversão de dolar para reais

print("Converta Dolar para Real")

dolar = input("Quantos Dolares queres converter para Real? $")
real = 4.87

conversao = float(dolar) * float(real)

print(f"convertendo ${dolar} voce tera R${conversao}")
"""
