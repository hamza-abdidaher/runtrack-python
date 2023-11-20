# variables représentant un produit
nom_produit = "console de jeux"
prix_unitaire = 500.0
quantite_stock = 50

# produit affiché de manière formatée

print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_stock} unités")
print("\n")

# Demander à l'utilisateur la quantité de console acheter
quantite_acheter = int(input("Combien d'unités souhaitez-vous acheter ? "))

# MAJ du stock
if quantite_acheter <= quantite_stock:
    quantite_stock -= quantite_acheter
    print(f"Vous avez acheté {quantite_acheter} unité(s).")
    print(f"Nouvelle quantité en stock : {quantite_stock} unités")
else:
    print("Stock insuffisant. Veuillez choisir une quantité inférieure ou égale au stock actuel.")

# l'inflation (augmentation de 10%)
prix_unitaire *= 1.1

# info apres MAJ du produit
print("\nInformations mises à jour du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire (après inflation) : {prix_unitaire:.2f} euros")
print(f"Quantité en stock : {quantite_stock} unités")
