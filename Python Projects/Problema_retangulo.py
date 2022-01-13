import math
import wsgiref.handlers

altura: float
base: float
area: float
soma: float
base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
perimetro = (base * 2) + (altura * 2)
raiz = (base ** 2) + (altura ** 2)
diagonal = math.sqrt(raiz)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")

