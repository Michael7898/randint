import random

def jeu_devine_le_nombre():
    nombre_aleatoire = random.randint(0, 10)
    essais_restants = 3

    print("Bienvenue dans le jeu Devine le nombres!")
    print("Je pense à un nombres entre 0 et 10. Tu as 3 essais pour le deviner.")

    while essais_restants > 0:
        essai = int(input("Entre ta proposition : "))

        if essai == nombre_aleatoire:
            print("Bravo! Tu as deviné le nombre correctement.")
            return  # Termine la fonction
        else:
            essais_restants -= 1
            print("Ce n'est pas le bon nombre. Il te reste {} essais.".format(essais_restants))

    print("Dommage! Le nombres à deviner était", nombre_aleatoire)

# Appel du jeu
jeu_devine_le_nombre()
