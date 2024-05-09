import pygame
from pygame.math import Vector2
import os

class Infected(pygame.sprite.Sprite):

    def __init__(self, image,waypoints):
        super().__init__()
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        infected_group_wave_1 = pygame.sprite.Group()
        infected_group_wave_2 = pygame.sprite.Group()
        infected_group_wave_3 = pygame.sprite.Group()
        infected_group_wave_4 = pygame.sprite.Group()
        infected_group_wave_5 = pygame.sprite.Group()
        infected_group_wave_6 = pygame.sprite.Group()
        infected_group_wave_7 = pygame.sprite.Group()

        self.slime = Infected_Slime()


    # METHODE: Update/Appel les Méthodes de la classe
    def update(self):
        self.move()
        self.slime.update_img()

    # METHODE: Faire que les Infected suivent le chemin donné
    def move(self):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.position
            distance = self.movement.length()
            if distance > 0:  # Vérifie si la distance à parcourir n'est pas égale à 0
                if distance >= self.speed:
                    self.position += self.movement.normalize() * self.speed
                else:
                    self.position += self.movement.normalize() * distance

                self.rect.center = self.position
            else:
                # Si le vecteur de mouvement est de longueur zéro, passez au prochain waypoint
                self.target_waypoint += 1


class Infected_Slime:

    def __init__(self):
        super().__init__()
        self.slime_animation = []

        for x in range(0,7):
            self.slime_animation.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("infected/img_infected/Slime/enemy_1007_slime-"+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))

        self.current_frame = 0
        self.image = self.slime_animation[self.current_frame]

    def update_img(self):
        # Changer l'image du slime pour la suivante dans l'animation
        self.current_frame = (self.current_frame + 1) % len(self.slime_animation)
        Infected.image = self.slime_animation[self.current_frame]


