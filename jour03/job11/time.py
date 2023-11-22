def time_to_text():
    try:
        
        heures = int(input("Entrez le nombre d'heures : "))
        
        
        minutes = int(input("Entrez le nombre de minutes : "))
        
        if heures >= 0 and minutes >= 0:
            
            if heures == 0 and minutes == 0:
                print("0 heures et 0 minutes")
            elif heures == 0:
                print(f"{minutes} minute{'s' if minutes > 1 else ''}")
            elif minutes == 0:
                print(f"{heures} heure{'s' if heures > 1 else ''}")
            else:
                print(f"{heures} heure{'s' if heures > 1 else ''} et {minutes} minute{'s' if minutes > 1 else ''}")
        else:
            print("Veuillez entrer des valeurs positives.")
    except ValueError:
        print("Veuillez entrer des nombres entiers.")


time_to_text()
