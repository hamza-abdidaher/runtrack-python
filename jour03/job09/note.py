def evaluer_note(note):
    if 15 <= note <= 20:
        return "Très bien"
    elif 11 <= note <= 14:
        return "Bon élève"
    elif 8 <= note <= 10:
        return "Élève moyen"
    elif 0 <= note <= 7:
        return "Élève devant faire des efforts"
    else:
        return "Note invalide"
    
note = float(input("Entrez la note de l'élève : "))
commentaire = evaluer_note(note)
print(commentaire)
