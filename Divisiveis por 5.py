soma_pares = 0
soma_impares = 0

for _ in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print("A soma dos números pares é:", soma_pares)
print("A soma dos números ímpares é:", soma_impares)

