
a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))

maior = max(a, b, c)
soma_dos_menores = a + b + c - maior

if maior < soma_dos_menores:
    print("Formam um triângulo.")
else:
    print("Não formam um triângulo.")
    print(a, b, c)

