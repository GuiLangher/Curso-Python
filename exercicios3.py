#Exercicio 1, fazer um programa que leia 5 numeros, e fale qual foi o menor e o maior entre eles

print("Digite 5 valor, o programa irá dizer qual o maior e qual o menor")

valor = int(input("Digite o 1º numero: "))
maior = valor
menor = valor

for i in range (2, 6):
    valor = int(input(f"Digite o {i}º valor: "))

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")


