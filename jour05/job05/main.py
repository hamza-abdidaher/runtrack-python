def chiffrement_cesar(message, decalage=3):
    resultat = ""
    for char in message:
        if char.isalpha():
            min_maj_offset = ord('a') if char.islower() else ord('A')
            resultat += chr((ord(char) - min_maj_offset + decalage) % 26 + min_maj_offset)
        else:
            resultat += char
    return resultat

def dechiffrement_cesar(message, decalage=3):
    # Le déchiffrement César est similaire au chiffrement avec un décalage négatif
    return chiffrement_cesar(message, -decalage)

# Demander à l'utilisateur d'entrer le message
message_original = input("Veuillez entrer le message : ")

# Appliquer le chiffrement César avec le décalage par défaut de 3
message_chiffre = chiffrement_cesar(message_original)

# Appliquer le déchiffrement César avec le décalage par défaut de 3
message_dechiffre = dechiffrement_cesar(message_chiffre)

# Afficher les résultats
print(f"Message chiffré : {message_chiffre}")

