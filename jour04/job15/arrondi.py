def tri_a_bulles(arr):
    n = 1
    while n > 0:
        n = 0
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                n += 1

def arrondir_manuel(nombre):
    partie_entiere = int(nombre)
    partie_fractionnaire = nombre - partie_entiere

    if partie_fractionnaire >= 0.5:
        return partie_entiere + 1
    else:
        return partie_entiere


nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


nombres_arrondis = [arrondir_manuel(nombre) for nombre in nombres]

tri_a_bulles(nombres_arrondis)

print("Liste arrondie et triée:", nombres_arrondis)
