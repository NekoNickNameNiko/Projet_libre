import pygame
import os
from game_img.load_img import*
from infected.Enemy_Data import*


# Classe pour les Slimes
class Infected_Slime:

    def __init__(self):
        super().__init__()
        
        # attributs d'[animations] 
        self.slime_animation_move = slime_animation_move[:]
        self.slime_animation_dead = slime_animation_dead[:]
        self.current_frame_move = 0
        self.current_frame_dead = 0
        self.frame_counter = 0


# Classe pour les Spiders
class Infected_Spider:

    def __init__(self):
        super().__init__()

        # attributs d'[animations]
        self.spider_animation_move = spider_animation_move[:]
        self.spider_animation_dead = spider_animation_dead[:]
        self.current_frame_move = 0
        self.current_frame_dead = 0
        self.frame_counter = 0

        # attributs [skill]
        self.skill_used = False

    # METHODE: compétence spéciale du spider --> augmente sa vitesse de déplacement de 25% si Health <= 35%
    def skill(self,health,speed):
        if health <= (enemy_data["spider"]["health"])*0.35 and self.skill_used == False:
            speed = (enemy_data["spider"]["speed"])*1.25
            self.skill_used = True
        return speed


# Classe pour les Démons
class Infected_Demon:

    def __init__(self):
        super().__init__()

        # attributs d'[animations]
        self.demon_animation_move = demon_animation_move[:]
        self.demon_animation_dead = demon_animation_dead[:]
        self.current_frame_move = 0
        self.current_frame_dead = 0
        self.frame_counter = 0

        # attribut [skill]
        self.skill_used = False

    # METHODE: compétence spéciale du démon --> augmente ses HP à 40% si Health <= 20%
    def skill(self,health):
        if health <= (enemy_data["demon"]["health"])*0.2 and self.skill_used == False:
            health = (enemy_data["demon"]["health"])*0.4
            self.skill_used = True
        return health


# Classe pour le BOSS
class Infected_BOSS:

    def __init__(self):
        super().__init__()

        # attributs d'[animations]
        self.BOSS_animation_move = BOSS_animation_move[:]
        self.BOSS_animation_dead = BOSS_animation_dead[:]
        self.current_frame_move = 0
        self.current_frame_dead = 0
        self.frame_counter = 0

        # attribut [skill]
        self.skill_used = False

    # METHODE: compétence spéciale du BOSS --> augmente sa resistence si Health <= 50%
    def skill(self,health,resistance):
        if health <= (enemy_data["BOSS"]["health"])*0.5 and self.skill_used == False:
            # [resistance physique +200] et [resistance magique *2] 
            resistance = {"physic":enemy_data["BOSS"]["resistance"]["physic"] + 200, "magic": enemy_data["BOSS"]["resistance"]["magic"] * 2}
            self.skill_used = True # Compétence utilisé
        return resistance



