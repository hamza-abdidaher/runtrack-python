montant_initial = float(input("Montant initial de l'investissement : "))
taux_rendement_annuel = float(input("Taux de rendement annuel en pourcentage : "))


gain_annuel = montant_initial * (taux_rendement_annuel / 100)


print(f"Le gain annuel pour un investissement de {montant_initial} euros avec un taux de rendement de {taux_rendement_annuel}% est de {gain_annuel} euros.")
