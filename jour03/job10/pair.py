def verifier_pair_impair(nombre):
    try:
        nombre = int(nombre)
        if nombre >= 0:
            return "Pair" if nombre % 2 == 0 else "Impair"
        else:
            return "Veuillez entrer un nombre entier positif"
    except ValueError:
        return "Veuillez entrer un nombre entier"

nombre_utilisateur = input("Entrez un nombre entier : ")

resultat = verifier_pair_impair(nombre_utilisateur)

print("Le nombre est :", resultat)
