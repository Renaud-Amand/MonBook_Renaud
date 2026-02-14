import pygame
import sys
import os
import random

pygame.init()
pygame.mixer.init()

#On charge un son

# 1. On crée d'abord l'écran et la police
screen = pygame.display.set_mode((1240, 960))
pygame.display.set_caption('Jeu Apprentissage Charlène')
ma_police = pygame.font.SysFont("Arial", 350) # On le met en très gros !
petite_police = pygame.font.SysFont("Arial", 100)
screen_rect = screen.get_rect()
hauteur = screen_rect.height

alphabet = [
    ("A", "Avion"), ("B", "Ballon"), ("C", "Chat"), ("D", "Dauphin"),
    ("E", "Etoile"), ("F", "Fleur"), ("G", "Gourde"), ("H", "Hibou"),
    ("I", "Ile"), ("J", "Jardin"), ("K", "Kangourou"), ("L", "Lion"),
    ("M", "Maison"), ("N", "Nuage"), ("O", "Oiseau"), ("P", "Poisson"),
    ("Q", "Quille"), ("R", "Robot"), ("S", "Soleil"), ("T", "Tortue"),
    ("U", "Univers"), ("V", "Velo"), ("W", "Wagon"), ("X", "Xylophone"),
    ("Y", "Yaourt"), ("Z", "Zebre"),
]

confettis = []
for i in range(50):
    # Chaque confetti = [x, y, couleur, vitesse]
    confettis.append([random.randint(0, 800), random.randint(-400, 0), 
                      (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 
                      random.randint(2, 5)])


en_marche = True
fete_active = False
compteur_fete = 0
index = 0

#Start
while en_marche:
    # A. Le dessin (On efface et on dessine la lettre actuelle)
    screen.fill((255, 255, 255))

    if index < len(alphabet):
        lettre, objet = alphabet[index]

    else:
        texte_bravo = ma_police.render('Bravo !', True, (255, 0, 100))
        rect_bravo = texte_bravo.get_rect(center=(screen_rect.centerx, screen_rect.centery + 100))
        screen.blit(texte_bravo, rect_bravo)

        texte_info = petite_police.render("Appuie pour recommencer", True, (0, 0, 0))
        rect_info = texte_info.get_rect(center=(screen_rect.centerx, screen_rect.centery + 300))
        screen.blit(texte_info, rect_info)


    #On définit le chemin de l'image
    chemin_image = f"images/{objet}.png"

    if os.path.exists(chemin_image):
        image_brute = pygame.image.load(chemin_image).convert_alpha()
        image_dessin = pygame.transform.scale(image_brute, (300, 300))
        rect_image = image_dessin.get_rect(centerx=screen_rect.centerx, centery = 180)
        rect_image.centerx = screen_rect.centerx
        rect_image.centery = hauteur * 0.25
        screen.blit(image_dessin, rect_image)
    else:
        pass
        

     # 1. On prépare la lettre (en gros)
    image_lettre = ma_police.render(lettre, True, (0, 0, 0))
    rect_lettre = image_lettre.get_rect()
    rect_lettre.centerx = screen_rect.centerx
    rect_lettre.centery = screen_rect.centery + 50
    screen.blit(image_lettre, rect_lettre) 
    
    image_objet = petite_police.render(objet, True, (50, 50, 50))
    rect_objet = image_objet.get_rect()
    rect_objet.centerx = screen_rect.centerx
    rect_objet.bottom = screen_rect.bottom -40
    screen.blit(image_objet, rect_objet)

    if fete_active:
        for c in confettis:
            c[1] += c[3] # Vitesse de chute
            pygame.draw.rect(screen, c[2], (c[0], c[1], 12, 12)) # Confettis un peu plus gros
            
            # RECYCLAGE : Si le confetti sort en bas (960), il repart en haut
            if c[1] > 960: 
                c[1] = random.randint(-100, -10)
                c[0] = random.randint(0, 1240) # Largeur totale de ton écran

    # B. On rafraîchit l'écran
    pygame.display.flip()

    # C. On attend un événement (Clavier ou quitter)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_marche = False
            
        elif event.type == pygame.KEYDOWN:
            index = index + 1

            if index == len(alphabet):               
                fete_active = True
                compteur_fete = 0
            elif index > len(alphabet):
                index = 0
                fete_active = False
                compteur_fete = 0
             
                         
pygame.quit()
sys.exit()




            