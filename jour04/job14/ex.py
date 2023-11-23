def my_long_word(longueur_minimale, phrase):
    mots = []  
    mot_actuel = ""  


    def ajouter_mot(mot):
        nonlocal mots
        mots.append(mot)

    
    def longueur(chaine):
        count = 0
        for _ in chaine:
            count += 1
        return count

    i = 0
    while i < longueur(phrase):
        caractere = phrase[i]
        if caractere.isalnum():
            
            mot_actuel += caractere
        elif mot_actuel:
            
            if longueur(mot_actuel) > longueur_minimale:
                ajouter_mot(mot_actuel)
            mot_actuel = ""  

        i += 1

    
    if mot_actuel and longueur(mot_actuel) > longueur_minimale:
        ajouter_mot(mot_actuel)

    return " ".join(mots)  


phrase_utilisateur = input("Entrez une chaîne de caractères : ")


chiffre_utilisateur = int(input("Entrez un chiffre : "))


resultat = my_long_word(chiffre_utilisateur, phrase_utilisateur)

print("Output:", resultat)
