vec=[]
elementos = int(input("Ingrese la cantidad de elementos del vector: "))
if elementos<=200 and 1<=elementos:
    for i in range(elementos):
        elemento = input("Ingrese el elemento {0}: ".format(i+1))
        while elemento.isnumeric() == False:
            elemento = (input("Ingrese un numero valido"))
        vec.append(elemento)
    vec_ordenado = []
    for i in vec:
        if i not in vec_ordenado:
            vec_ordenado.append(i)
    vec_ordenado.sort(key=int)
    print(vec_ordenado)
else:
    print("Fuera de rango")