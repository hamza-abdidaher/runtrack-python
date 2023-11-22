def nombre (nombre):
    if nombre > 0:
        print(f"{nombre} est positif")
    elif nombre < 0:
        print(f"{nombre} est négatif")
    else:
        print(f"{nombre} est nul")

nombre_utilisateur = float(input("Entrez un nombre : "))

nombre (nombre_utilisateur)
