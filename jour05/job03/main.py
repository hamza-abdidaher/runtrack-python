def draw_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            print(spaces + '_')
        elif i == height - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print(spaces + '/' + ' ' * (2 * i) + '\\')

# Demander à l'utilisateur d'entrer la hauteur du triangle
hauteur = int(input("Veuillez entrer la hauteur du triangle : "))

# Appeler la fonction pour dessiner le triangle en utilisant l'entrée de l'utilisateur
draw_triangle(hauteur)
