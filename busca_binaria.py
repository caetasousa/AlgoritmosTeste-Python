def busca(inicio, fim, array, buscando):
    meio = int((fim + inicio) / 2)
    if array[meio] == buscando:
        return array[meio]
    
    if array[meio] > buscando:
        print(array[meio])

        return busca(inicio, meio , array, buscando)
    return busca(meio, fim, array, buscando)



array = [10,20,30,40,50,60,70,80,90,100,110]
a = busca(0, len(array), array, 100)

print(a)
print()
print(len(array))