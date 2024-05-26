from game import Game
import pygame
import os

start_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_img/game_asset", "button_play.png")).convert_alpha(),(300,80))

class MainMenu:
    def __init__(self, fenetre):
        self.width = 1350
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_img/game_asset", "start_menu_bg.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.fenetre = fenetre
        self.btn = (self.width/3, 450, start_btn.get_width(), start_btn.get_height())

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            pygame.display.set_caption('Arknight fps '+str(round(clock.get_fps(),0)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # check if hit start btn
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.fenetre)
                            game.run()
                            del game
            self.draw()

        pygame.quit()

    def draw(self):
        self.fenetre.blit(self.bg, (0,0))
        self.fenetre.blit(start_btn, (self.btn[0], self.btn[1]))
        pygame.display.update()