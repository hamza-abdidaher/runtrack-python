def afficher_produits(type, saison):
    if type.lower() == "fruits":
        if saison.lower() == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison.lower() == "ete":
            print("Poire, fraise, cassis")
        else:
            print("Saison non reconnue pour les fruits")
    elif type.lower() == "legume":
        if saison.lower() == "hiver":
            print("Carotte, topinambour, endive")
        elif saison.lower() == "ete":
            print("Artichaut, aubergine, navet")
        else:
            print("Saison non reconnue pour les légumes")
    else:
        print("Type non reconnu")

# Demande à l'utilisateur de saisir le type et la saison
type_utilisateur = input("Entrez le type (fruits ou legume) : ")
saison_utilisateur = input("Entrez la saison (hiver ou ete) : ")

# Appel de la fonction avec les choix de l'utilisateur
afficher_produits(type_utilisateur, saison_utilisateur)

