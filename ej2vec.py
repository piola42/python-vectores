vec = []
total = 0
contador = 0
cantidad = int(input("Ingrese la cantidad de temperaturas: "))
for i in range(cantidad):
    print("Ingrese la temperatura",i+1)
    vec.append(float(input()))
    total+=vec[i]
media = total/cantidad
print("La media es:",media)
print("Las temperaturas mayores a la media son:")
for i in vec:
    if i>=media:
        contador+=1
        print(i)
