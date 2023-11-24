def draw_diagonal_carpet(n):
    for i in range(n+1):
        for j in range(n+1):
            if j == n - i:
                print('/', end='')
            else:
                print('_', end='')
        print()

# Demander à l'utilisateur d'entrer la taille du tapis
taille_tapis = int(input("Veuillez entrer la taille du tapis : "))

# Appeler la fonction pour dessiner le tapis en utilisant l'entrée de l'utilisateur
draw_diagonal_carpet(taille_tapis)
