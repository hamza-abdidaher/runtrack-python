def draw_oi width = int(input("entrer width: "))
    height = int(input("entrer height: "))

    # Dessiner le rectangle
    for i in range(height):
        if i == 0 or i == height - 1:
            print('-' * width)
        else:
            print('|' + ' ' * (width - 2) + '|')

# Appeler la fonction pour dessiner le rectangle en utilisant les entrées de l'utilisateur
draw_rectangle()

