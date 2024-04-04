import pygame
import pygame_gui
import sys
import os
"test test "
class Enemy(pygame.sprite.Sprite):

    def __init__(self, image, path):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.path = path  # Chemin que l'ennemi va suivre
        self.position = 0  # Indice de la position actuelle sur le chemin
        self.speed = 1  # Vitesse de déplacement de l'ennemi
        

    def update(self):
        self.move()

    def move(self):
        n = self.position
        if self.rect != self.path[n]:
            if self.rect.x != self.path[n][0]:
                self.rect.x += 1
            if self.rect.y != self.path[n][1]:
                self.rect.y += 1
        if n < 4:
            self.position += 1




# Initialise le temps
clock = pygame.time.Clock()

# Création de la fenêtre et son nom
pygame.init()
fenetre = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Arknight')

# Création d'un gestionnaire d'interface (pygame GUI)
manager_ui = pygame_gui.UIManager((1200, 650))


ennemy_image = pygame.image.load("enemy_1.png").convert_alpha()
enemy_path = [(50, 50), (200, 50), (200, 200), (300, 200), (300, 300)]

enemy_group = pygame.sprite.Group()
enemy = Enemy(ennemy_image,enemy_path)
enemy_group.add(enemy)

# Boucle principale
while True:

    fenetre.fill("grey100")

    # relève les différents événements, mouvements de l'utilisateur
    for event in pygame.event.get():

        # EVENEMENT : si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pos)

    enemy_group.draw(fenetre,(100,100))
    enemy.update()

    manager_ui.update(clock.tick(60) / 1000.0)  # FPS 60 images par seconde

    # Dessiner le gestionnaire d'interface utilisateur
    pygame.display.flip()
    pygame.display.update()