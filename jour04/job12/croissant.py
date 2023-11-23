def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

# Demander à l'utilisateur d'entrer une liste de chiffres
entree_utilisateur = input("Entrez une liste de chiffres séparés par des espaces : ")
ma_liste = list(map(int, entree_utilisateur.split()))

print("Liste avant le tri:", ma_liste)

# Appeler la fonction pour trier la liste
tri_bulles(ma_liste)

print("Liste après le tri:", ma_liste)
