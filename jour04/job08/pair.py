L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Utiliser la fonction sum() et une compréhension de liste pour calculer la somme des valeurs paires
somme_valeurs_paires = sum(nombre for nombre in L if nombre % 2 == 0)

print("Somme des valeurs paires dans la liste:", somme_valeurs_paires)
