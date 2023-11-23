L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Utiliser une compréhension de liste pour filtrer les valeurs dans l'intervalle [25, 90]
# puis utiliser la fonction built-in `functools.reduce()` pour calculer le produit
from functools import reduce
import operator

valeurs_intervalle = [nombre for nombre in L if 25 <= nombre <= 90]
produit_valeurs_intervalle = reduce(operator.mul, valeurs_intervalle, 1)

print("Produit des valeurs dans l'intervalle [25, 90]:", produit_valeurs_intervalle)
