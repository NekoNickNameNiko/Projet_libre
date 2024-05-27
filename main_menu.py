from game import Game
import pygame
import os

start_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_img/game_asset", "button_play.png")).convert_alpha(),(300,80))
text_accueil = pygame.font.SysFont("fantasy", 55).render("Lost World", True, (255, 255, 255))
text_rect_accueil = text_accueil.get_rect()
print(text_rect_accueil)

class MainMenu:
    def __init__(self, fenetre):
        self.width = 1200
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_img/game_asset", "start_menu_bg.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.fenetre = fenetre
        self.btn = (self.width/2- pygame.Surface.get_width(start_btn)/2, 450, start_btn.get_width(), start_btn.get_height())

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
        self.dropShadowText("Lost World",100,410,300)
        self.fenetre.blit(start_btn, (self.btn[0], self.btn[1]))
        pygame.display.update()

    def dropShadowText(self, text, size, x, y, colour=(255,255,255), drop_colour=(128,128,128), font=None):
        dropshadow_offset = 1 + (size // 15)
        text_font = pygame.font.Font(font, size)
        
        text_bitmap = text_font.render(text, True, drop_colour)
        self.fenetre.blit(text_bitmap, (x+dropshadow_offset, y+dropshadow_offset) )
        
        text_bitmap = text_font.render(text, True, colour)
        self.fenetre.blit(text_bitmap, (x, y) )