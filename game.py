import pygame
from operateur.operateur_typhon import typhon

class Game:
    """
    Classe principal du projet
    """
    def __init__(self):
        self.weights =1200
        self.height =700
        self.fenetre = pygame.display.set_mode((self.weights, self.height))
        self.infected = []
        self.operater = [typhon(300,300)]
        self.lives = 3
        self.dp = 5
        self.bg = pygame.image.load("map.png")
        self.clicks = []

    def run(self):
        """
        Lancement du jeu
        """
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            
            self.draw()
        pygame.quit()

    def draw(self):
        """
        Déssine les éléments du jeu
        """
        self.fenetre.blit(self.bg,(0,0))
        pygame.display.update()

    #dessiner les opérateurs
        for op in self.operater :
            op.draw(self.fenetre)

        pygame.display.update()

Game = Game()
Game.run()
