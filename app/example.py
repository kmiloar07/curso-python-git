num = 3
var = print("par" if (num % 2 == 0) else "impar")

"""edad = 0
while edad < 18:
   edad = edad + 1
   print("Felicidades, tienes:"+ str(edad))

while True:
    entrada = input("Ingrese algo")
    if entrada == "adios":
        break
    else:
        print("entrada")

edad = 0
while edad < 18:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print("Felicidades, tienes", str(edad))"""

def varios(param1, param2, *otros):
    for val in otros:
        print(val)

varios(1, 2, 3, 4)

def varios(param1, param2, **otros):
    for i in otros.items():
        print(i)
varios(1, 2, tercero = 3)