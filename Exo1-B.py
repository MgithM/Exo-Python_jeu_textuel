import random

joueurScore = 0
ordinateurScore = 0

cartes = ["As", "Roi", "Dame", "Valet", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]

def afficherCartes():
    print("\nCartes disponibles:")
    for i, carte in enumerate(cartes):
        print(f"{i+1}. {carte}")

def afficherCouleurs():
    print("\nCouleurs disponibles:")
    for i, couleur in enumerate(couleurs):
        print(f"{i+1}. {couleur}")

def tirerCarteAleatoire():
    return random.randint(0, 12)

def tirerCouleurAleatoire():
    return random.randint(0, 3)

print("Bienvenue dans le jeu de cartes !")

afficherCartes()
choixCarte = int(input("Choisissez une carte (1-13): "))

afficherCouleurs()
choixCouleur = int(input("Choisissez une couleur (1-4): "))

carteOrdinateur = tirerCarteAleatoire()
couleurOrdinateur = tirerCouleurAleatoire()

print(f"\nVous avez choisi la carte {cartes[choixCarte-1]} de {couleurs[choixCouleur-1]}.")
print(f"L'ordinateur a choisi la carte {cartes[carteOrdinateur]} de {couleurs[couleurOrdinateur]}.")

if choixCarte == carteOrdinateur and choixCouleur == couleurOrdinateur:
    print("\nVictoire !")
    joueurScore += 1
else:
    print("\nDommage, vous avez perdu.")
    ordinateurScore += 1

print("\nScores:")
print(f"Joueur: {joueurScore}")
print(f"Ordinateur: {ordinateurScore}")
