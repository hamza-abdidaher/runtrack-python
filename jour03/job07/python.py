def identifier_developpeur(langage):
    if langage.lower() == "javascript":
        print("Tu es un développeur web")
    elif langage.lower() == "python":
        print("Tu es un développeur IA")
    elif langage.lower() == "java":
        print("Tu es un développeur logiciel")
    elif langage.lower() == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

langage_utilisateur = input("Entrez le langage de programmation : ")

identifier_developpeur(langage_utilisateur)
