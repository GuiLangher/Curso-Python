
numero = int(input("insira o numero: "))

fatorial = 1

if numero <0:
    print(f"O fatorial de {numero} é 1")
else:
    for x in range(1,numero+1):
        fatorial = fatorial*x
    print(f"O fatorial de {numero} é: {fatorial}")
