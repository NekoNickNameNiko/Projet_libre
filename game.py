import pygame
import pygame_gui
from operateur.operateur_typhon import typhon
from infected.Class_Infected import Infected
import sys
import os


# Création de la fenêtre et son nom
pygame.init()
fenetre = pygame.display.set_mode((1200, 650))

# Création d'un gestionnaire d'interface (pygame GUI)
manager_ui = pygame_gui.UIManager((1200, 650))

# Initialise les Infected
infected_image = pygame.image.load("./infected/img_infected/Slime/enemy_1007_slime-0.png").convert_alpha()
infected_image_redimensionnee = pygame.transform.scale(infected_image, (150, 150))
infected_waypoint = [(1000, 325), (700, 325), (700, 100), (200, 100)]

infected_group = pygame.sprite.Group()
infected = Infected(infected_image_redimensionnee, infected_waypoint)
infected_group.add(infected)

class Game(pygame.sprite.Sprite):
    """
    Classe principal du projet
    """
    def __init__(self):
        super().__init__()
        self.weights =1200
        self.height =700
        self.fenetre = pygame.display.set_mode((self.weights, self.height))

        self.infected = []


        self.operater = [typhon(300,300)]
        self.limite_operator = 5
        self.lives = 3
        self.dp = 5
        self.bg = pygame.image.load("map.png",'bg.png')
        self.bg = pygame.transform.scale(self.bg,(self.weights,self.height))
        self.choose_typhon  = pygame.transform.scale(pygame.image.load(os.path.join("img_operator/typhon_ilg/icon_typhon.png")).convert_alpha(),(70,70))


    def run(self):
        """
        Lancement du jeu
        """
        run = True
        clock = pygame.time.Clock()
        
        while run:
            manager_ui.update(clock.tick(60) / 1000.0)  # FPS 60 images par seconde
            pygame.display.set_caption('Arknight fps'+str(round(clock.get_fps(),0)))

            # Dessiner le gestionnaire d'interface utilisateur
            pygame.display.flip()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
            
            self.draw()
        pygame.quit()

    def draw(self):
        """
        Déssine les éléments du jeu
        """
        self.fenetre.blit(self.bg,(0,0))

        infected_group.draw(fenetre)
        
        #dessiner les opérateurs
        for op in self.operater :
            op.attack(self.fenetre,infected_group)

        infected.update()
        pygame.display.update()



Game = Game()
Game.run()

