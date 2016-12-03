import sys
import pygame
from pygame.locals import *

# Initialiser pygame
pygame.init()

# Défini le nombre de FPS (Frames Per Second)
fps = 30
fps_clock = pygame.time.Clock()

# Initialiser une fenêtre / l’écran de jeu
ecran = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Mon jeu !')

# Boucle principale
while True:

    # Verifier si il y a des événements en attente
    for event in pygame.event.get():

        # Si l'utilisateur a déclenché la fermeture de la fenêtre
        if event.type == QUIT:
            # Désinitialiser pygame
            pygame.quit()
            # Sortir du programme
            sys.exit()

    # met à jour l'écran
    pygame.display.update()
    fps_clock.tick(fps)
