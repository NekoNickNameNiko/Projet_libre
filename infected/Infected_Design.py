import pygame
import os
from Class_Infected import Infected

class Infected_Slime:

    def __init__(self):
        super().__init__()
        self.slime_animation = []

        for x in range(0,7):
            self.slime_animation.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("C:/Users/PC/Documents/Tower Defense/Projet_libre-main/infected/img_infected/Slime/enemy_1007_slime-"+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))

        self.current_frame = 0

    def update_img(self):
        # Changer l'image du slime pour la suivante dans l'animation
        for i in range(len(self.slime_animation)):
            Infected.image = self.slime_animation[i]


