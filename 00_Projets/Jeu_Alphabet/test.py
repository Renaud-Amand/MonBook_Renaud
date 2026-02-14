import pygame
import sys

pygame.init()

# 1. On crée d'abord l'écran et la police
screen = pygame.display.set_mode((1240, 960))
pygame.display.set_caption('Jeu Apprentissage Charlène')
ma_police = pygame.font.SysFont("Arial", 250) # On le met en très gros !
petite_police = pygame.font.SysFont("Arial", 80)

alphabet = [
    ("A", "Avion"), ("B", "Ballon"), ("C", "Chat"), ("D", "Dauphin"),
    ("E", "Etoile"), ("F", "Fleur"), ("G", "Gourde"), ("H", "Hibou"),
    ("I", "Ile"), ("J", "Jardin"), ("K", "Kangourou"), ("L", "Lion"),
    ("M", "Maison"), ("N", "Nuage"), ("O", "Oiseau"), ("P", "Poisson"),
    ("Q", "Quille"), ("R", "Robot"), ("S", "Soleil"), ("T", "Tortue"),
    ("U", "Univers"), ("V", "Velo"), ("W", "Wagon"), ("X", "Xylophone"),
    ("Y", "Yaourt"), ("Z", "Zebre")
]

index = 0
en_marche = True

while en_marche:
    # A. Le dessin (On efface et on dessine la lettre actuelle)
    screen.fill((255, 255, 255))
    
    lettre, objet = alphabet[index]
     # 1. On prépare la lettre (en gros)
    image_lettre = ma_police.render(lettre, True, (0, 0, 0))
    screen.blit(image_lettre, (550, 250)) 
    
    # 2. ON AJOUTE L'OBJET (en plus petit peut-être ?)
    # On crée une police plus petite pour le mot
    image_objet = petite_police.render(objet, True, (50, 50, 50)) # Gris foncé
    # On le colle sous la lettre (on descend sur l'axe Y : 250 -> 550)
    screen.blit(image_objet, (530, 550))
    # B. On rafraîchit l'écran
    pygame.display.flip()

    # C. On attend un événement (Clavier ou quitter)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_marche = False
            
        elif event.type == pygame.KEYDOWN:
            # On change d'index seulement quand une touche est pressée !
            if index < len(alphabet) - 1:
                index = index + 1
            else:
                index = 0

pygame.quit()
sys.exit()


