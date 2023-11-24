def distance_toilettes():
    marches = int(input("Entrez le nombre de marches du phare : "))
    hauteur_marche = int(input("Entrez la hauteur de chaque marche en cm : "))

    distance_journaliere = (marches * 4 * hauteur_marche) / 100  # Convertir en mètres (aller-retour)
    distance_hebdomadaire = distance_journaliere * 7

    print(f"Pour {marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_hebdomadaire:.2f} m par semaine.")

# Appeler la fonction pour permettre à l'utilisateur d'entrer les valeurs
distance_toilettes()
