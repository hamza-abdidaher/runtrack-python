def inverser_string_utilisateur():
    chaine = input("Entrez une chaîne de caractères : ")
    
    return chaine[::-1]

resultat = inverser_string_utilisateur()
print("Chaîne inversée :", resultat)
