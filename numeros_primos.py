print(60 * "-")

numero = int(input("insira o um numero para descobrir se ele é primo: "))

if numero >1:
    for x in range(2,numero):
        if(numero % x) == 0:
            print("Esse numero não é primo")
            break
    else:
        print("esse numero é primo")
else:
    print("Esse numero é menor ou igual a 1")

print(60 * "-")
