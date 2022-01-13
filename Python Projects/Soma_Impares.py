x: int
y: int
menor: int
i: int
soma: int

print("Digite dois numeros:")
x = int(input())
y = int(input())

while x != y:
    soma = 0
    if x > y:
        menor = x
        x = y
        y = menor

    for i in range(x+1, y):
        if i % 2 != 0:
            soma = soma + i

    print(f"SOMA DOS IMPARES: {soma}")

    print("Digite dois numeros:")
    x = int(input())
    y = int(input())
