#Exercício 1: Soma de Dois Números
"""
print("Digite dois numeros para serem somados")

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

Resultado = print(f"{num1} + {num2} = {num1 + num2}")

"""
#Exercício 2: Verificador de Números Pares
"""
print ("Digite um numero para saber se é par ou impar")

numero = int(input("Digite o numero: "))

if (numero % 2) == 0:
    print(f"O numero {numero} é par")

else:
    print(f"O numero {numero} é impar")
"""
"""
#Exercício 3: Calculadora de Média

med1 = float(input("Digite a primeira nota: "))
med2 = float(input("Digite a segunda nota: "))
med3 = float(input("Digite a terceira nota: "))

media = (med1 + med2 + med3) / 3

print(media)
"""
"""
#Exercício 4: Conversor de Temperatura
#Crie um programa que converte a temperatura de Celsius para Fahrenheit. O usuário deve inserir a temperatura em Celsius.

celsius = float(input("Digite a temperatura em celsius: "))

fah = ()

temp =(celsius * 1.8) + 32

temperatura = print(f"A temperatura em Fahrenheit é: {temp}")
"""

#Exercício 5: Calculadora de Fatorial
"""
numero = int(input("insira um numero: "))

fatorial = 1

if numero <0:
    print(f"O {numero} não é fatorail")
    
else:
    for x in range(1, numero +1):
        fatorial = fatorial*x
    print(f"O fatorial de {numero} é: {fatorial}")
"""

#Exercício 6: Verificador de Palíndromos
"""
XXX
def verifica_palindromo(palavra):
    # Converte a palavra para minúsculas para facilitar a comparação
    palavra = palavra.lower()
    
    # Remove espaços em branco da palavra
    palavra = palavra.replace(" ", "")
    
    # Verifica se a palavra é um palíndromo
    if palavra == palavra[::-1]:
        return True
    else:
        return False

# Solicita que o usuário insira uma palavra
palavra_usuario = input("Digite uma palavra para verificar se é um palíndromo: ")

# Chama a função e imprime o resultado
if verifica_palindromo(palavra_usuario):
    print(f"{palavra_usuario} é um palíndromo!")
else:
    print(f"{palavra_usuario} não é um palíndromo.")

XXX
"""
"""
#Exercício 7: Contador de Vogais

def contar_vogais(palavra):
    # Converte a palavra para minúsculas para facilitar a contagem
    palavra = palavra.lower()
    
    # Inicializa o contador de vogais
    contador_vogais = 0
    
    # Lista de vogais
    vogais = "aeiou"
    
    # Itera sobre cada caractere na palavra
    for caractere in palavra:
        # Verifica se o caractere é uma vogal
        if caractere in vogais:
            contador_vogais += 1
    
    return contador_vogais

# Solicita que o usuário insira uma palavra
palavra_usuario = input("Digite uma palavra para contar as vogais: ")

# Chama a função e imprime o resultado
num_vogais = contar_vogais(palavra_usuario)
print(f"A palavra '{palavra_usuario}' possui {num_vogais} vogais.")
"""

