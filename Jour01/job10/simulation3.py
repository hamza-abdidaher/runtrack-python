montant_initial = float(input("Montant initial de l'investissement : "))
taux_rendement_annuel = float(input("Taux de rendement annuel en pourcentage : "))


gain_annuel_initial = montant_initial * (taux_rendement_annuel / 100)


print(f"Le gain annuel initial pour un investissement de {montant_initial} euros avec un taux de rendement de {taux_rendement_annuel}% est de {gain_annuel_initial} euros.")
print("\n")

montant_initial += 5000

taux_rendement_annuel += 2

nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)

print(f"Après avoir augmenté le capital de 5 000 euros et le taux de rendement de 2%, le nouveau gain annuel est de {nouveau_gain_annuel} euros.")
print("\n")

montant_initial -= 0.10 * montant_initial

taux_rendement_annuel -= 1

montant_final = montant_initial * (1 + taux_rendement_annuel / 100)

print(f"Après avoir retiré 10% du montant total et diminué le rendement de 1%, le montant final de l'investissement est de {montant_final} euros.")
