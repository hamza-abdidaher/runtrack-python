def afficher_deuxieme_element():
    fruits = ["pomme", "cerise", "orange"]
    
    if len(fruits) >= 2:
        deuxieme_element = fruits[1]
        print(deuxieme_element)
    else:
        print("La liste ne contient pas assez d'éléments pour afficher le deuxième élément.")

afficher_deuxieme_element()
