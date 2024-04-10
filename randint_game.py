import random  # Importe le module random pour générer des nombres aléatoires.

def jeu_devine_le_nombre():  # Définition de la fonction pour le jeu de devinettes.
    nombre_aleatoire = random.randint(0, 10)  # Génère un nombre aléatoire entre 0 et 10.
    essais_restants = 3  # Initialise le nombre d'essais à 3.

    # Affiche le message de bienvenue et les règles du jeu.
    print("Bienvenue dans le jeu Devine le nombres!")
    print("Je pense à un nombres entre 0 et 10. Tu as 3 essais pour le deviner.")

    while essais_restants > 0:  # Tant qu'il reste des essais...
        essai = int(input("Entre ta proposition : "))

        if essai > 10 or essai < 0:  # Vérifie si l'entrée est hors des limites
            print("Veuillez sélectionner un chiffre entre 0 et 10 !!!!!!!!!!!!!!!!")
        elif essai == nombre_aleatoire:  # Si l'essai correspond au nombre aléatoire...
            print("Bravo! Tu as deviné le nombre correctement.")  # Félicite l'utilisateur.
            return  # Quitte la fonction, car le jeu est terminé après une bonne réponse.
        else:  # Si l'essai ne correspond pas au nombre aléatoire...
            essais_restants -= 1  # Réduit le nombre d'essais restants de 1.
            # Informe l'utilisateur qu'il s'est trompé et lui dit combien d'essais il lui reste.
            print(f"Ce n'est pas le bon nombre. Il te reste {essais_restants} essais.")

    # Si tous les essais sont utilisés sans deviner le nombre, informe l'utilisateur du nombre correct.
    print("Dommage! Le nombres à deviner était", nombre_aleatoire)


if __name__ == "__main__":  # Si le script est exécuté directement (pas importé)...
    jeu_devine_le_nombre()  # Appelle la fonction pour démarrer le jeu.
