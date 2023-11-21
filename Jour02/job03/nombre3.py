# 0 à 100
for nombre in range(101):
    # ne pas affiché 26, 37 et 88
    if nombre not in [26, 37, 88]:
        print(nombre)
