
import random
# Afficher le message d'accueil du jeu
print("Bienvenue dans le jeu de devinette de nombre !")
print("Les règles sont simples. Je vais penser à un nombre, et vous allez essayer de le deviner.")

# Générer un nombre aléatoire entre 1 et 10
number = random.randint(1, 10)

# Définir une variable pour vérifier si l'utilisateur a deviné correctement
isGuessRight = False

# Boucle jusqu'à ce que l'utilisateur devine correctement
while not isGuessRight:
    # Demander à l'utilisateur de deviner un nombre entre 1 et 10
    guess = input('Devinez un nombre entre 1 et 10 ! ')
    
    # Vérifier si la devinette de l'utilisateur est correcte
    if int(guess) == number:
        print("Félicitations ! Vous avez deviné, {} était le bon numéro.".format(guess))
        isGuessRight = True
    else:
        # Indiquer que la devinette n'est pas correcte et demander de réessayer
        print("Réessayez, {} n'est pas le bon numéro.".format(guess))

# Boucle qui imprime les nombres de 0 jusqu'au nombre généré
for x in range(0, number):
    print(x)
