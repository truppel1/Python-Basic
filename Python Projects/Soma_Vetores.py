n: int
valores: float
soma: float = 0
media: float = 0
i: int
j: int

n = int(input("Quantos numeros você vai digitar? "))
vet = [0 for x in range(n)]

i: int
for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

for i in range(0, n):
    soma = soma + vet[i]

media = soma / n
print()
print("VALORES = ", end='')
for i in range(0, n):
    print(f"{vet[i]:.1f} ", end="")

print(f"\nSOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")
