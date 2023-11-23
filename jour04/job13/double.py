def supprimer_doublons(liste):
    liste_unique = []
    for element in liste:
        if element not in liste_unique:
            liste_unique.append(element)
    return liste_unique

# Liste initiale avec des doublons
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appeler la fonction pour supprimer les doublons
ma_liste_sans_doublons = supprimer_doublons(ma_liste)

# Afficher la liste après suppression des doublons
print("Liste sans doublons:", ma_liste_sans_doublons)
