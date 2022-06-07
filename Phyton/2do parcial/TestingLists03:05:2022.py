frutas= ["manzana", "mango", "plátano", "melon", "fresa"]

print(frutas)
print(len(frutas))
print(frutas[2])

frutas.append("fresa")
print(frutas)

frutas.append("melon")
print(frutas)

frutas.sort()
print(frutas)

compra=input("ingresa una fruta: ")
frutas.append(compra)

print(frutas)
print(dir(frutas))