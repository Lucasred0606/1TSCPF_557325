titulo = "Tabuada"
print(f"{titulo:^30}")

numero = int(input("Entre com o numero da tabuada:"))
for i in range(1,10+1):
    tabuada = i * numero
    print(f'{numero} X {i} = {tabuada}')


# tabuada = 1 * numero
# print(numero, "X", "1", "=", tabuada)
# tabuada = 2 * numero
# print(numero, "X", "2", "=", tabuada)
# tabuada = 3 * numero
# print(numero, "X", "3", "=", tabuada)

# for i in range(1,10+1):
#     tabuada = i * numero
#     print(numero, "X", i, "=", tabuada)

# for i in range(10):
#     tabuada = i * numero
#     print(numero, "X", i, "=", tabuada)

# for i in range(1,10,2):
#     tabuada = i * numero
#     print(numero, "X", i, "=", tabuada)


# for i in range(10,0,-1):
#     tabuada = i * numero
#     print(numero, "X", i, "=", tabuada)
#     print(f'{numero} X {i} = {tabuada}')
