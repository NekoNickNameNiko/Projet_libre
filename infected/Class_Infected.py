import pygame
from pygame.math import Vector2
from infected.Infected_Design import *
from infected.Enemy_Data import *
import os

class Infected(pygame.sprite.Sprite):

    def __init__(self,enemy_type, image,waypoints):
        super().__init__()

        # attributs d'[Etats/Stats]
        self.enemy_type = enemy_type
        self.health = enemy_data.get(enemy_type)["health"]
        self.speed = enemy_data.get(enemy_type)["speed"]
        self.resistance = enemy_data.get(enemy_type)["resistance"]
        self.image = image.get(enemy_type)
        self.alive = True

        # attributs de [Coordonnés]
        self.waypoints = waypoints
        self.in_final_waypoint = False 
        self.position = Vector2(self.waypoints[0])
        self.rect = self.image.get_rect()
        self.rect.center = (self.position)
        self.target_waypoint = 1

        # attributs [Objet] des différents types d'infectés
        self.slime = Infected_Slime()
        self.spider = Infected_Spider()
        self.demon = Infected_Demon()
        self.BOSS = Infected_BOSS()


    # METHODE: Update/Appel les Méthodes de la classe
    def update(self,fenetre):
        # Arrete le deplacement du monstre durant l'affichage de l'animation de mort, sinon ce dernier bouge
        if self.health > 0:
            self.move()

        # Fait appel à la méthode remove (supprime l'infecté) et draw_health_Bar (affichage barre de vie)
        self.remove()
        self.draw_health_Bar(fenetre)

        # Fait appel aux méthodes permettant de défiler les images de déplacement ou de mort selon le type de l'infecté
        # Fait appel aux méthodes permettant d'utiliser les compétences de chaque infectés selon le type de l'infecté
        if self.enemy_type == "slime":
            self.update_slime_img() # animation
        if self.enemy_type == "spider":
            self.update_spider_img() # animation
            speed = self.spider.skill(self.health,self.speed) # compétence
            self.speed = speed
        if self.enemy_type == "demon":
            self.update_demon_img() # animation
            health = self.demon.skill(self.health) # compétence
            self.health = health
        if self.enemy_type == "BOSS":
            self.update_BOSS_img() # animation
            resistance = self.BOSS.skill(self.health,self.resistance) # compétence
            self.resistance = resistance


    # METHODE: Faire que les Infected suivent le chemin prédéfinit
    def move(self):
        # Si l'indice du waypoint est différent de l'indice de fin de la liste des waypoints
        if self.target_waypoint < len(self.waypoints):

            # Détermine le prochain waypoint [self.target] et le mouvement à effectuer [movement] 
            self.target = Vector2(self.waypoints[self.target_waypoint]) # Vector2 permet les calculs mathématiques sur les coordonnées 2D
            self.movement = self.target - self.position
            distance = self.movement.length()

            if distance > 0:  # Vérifie si la distance à parcourir n'est pas égale à 0
                # modifie la position de l'infecté selon sa vitesse
                if distance >= self.speed:
                    self.position += self.movement.normalize() * self.speed
                # dans le cas où la distance est inférieure à la vitesse, pour éviter que l'infecté ne soit immobilisé.
                else:
                    self.position += self.movement.normalize() * distance

                # met à jour le centre de l'image
                self.rect.center = self.position
            else:
                # Si le vecteur de mouvement est de longueur zéro, passez au prochain waypoint
                self.target_waypoint += 1
    

    # METHODE: définit la rotation de l'image selon la direction 
    def rotation(self):
        # Définit la distance actuel de l'infecté et son prochain waypoint
        distance = self.target - self.position
        horizontal = False
        vertical = False

        # Si la distance à parcourir a x négatif, effectue un effet miroir à l'image sinon garder l'angle originale
        if distance.x < 0:
            horizontal = True
        # effectue un effet miroir horizontalement à l'image selon la variable [horizontal] 
        self.image = pygame.transform.flip(self.img_animation, horizontal, vertical)


    # METHODE: Affiche la barre de vie 
    def draw_health_Bar(self,fenetre):
        max_health = enemy_data.get(self.enemy_type)["health"]
        # affiche quand l'infecté reçoit des dégâts
        if self.health != max_health:
            ratio = self.health / max_health

        # Définit l'emplacement de la barre de vie:
            # Si no BOSS affiche la barre de vie sur la tête des infectés
            if self.enemy_type != "BOSS":
                pygame.draw.rect(fenetre,"red",(self.position.x - 25,self.position.y - 25,50,5)) # fenetre/couleur/(x,y,longueur,hauteur)
                pygame.draw.rect(fenetre,"green",(self.position.x - 25,self.position.y - 25,50 * ratio,5)) # fenetre/couleur/(x,y,longueur,hauteur)
            # Si BOSS affiche la barre de vie en haut/centre 
            else:
                name = pygame.font.Font(None, 32).render(f"[ {self.enemy_type} ]", True, (255, 255, 255))
                fenetre.blit(name,(560,4))
                pygame.draw.rect(fenetre, "red",(350, 28, 500, 20))  # fenetre/couleur/(x,y,longueur,hauteur)
                pygame.draw.rect(fenetre, "green", (350, 28, 500 * ratio, 20))  # fenetre/couleur/(x,y,longueur,hauteur)
                # Affiche nombre de points de vie
                HP = pygame.font.Font(None, 27).render(f"{round(self.health)}/{max_health}", True, (255, 255, 255))
                fenetre.blit(HP, (570, 28))


    # METHODE: Diminue la santé de l'infecté
    def lost_life(self,damage,type,penetration):
        if type == "magic":
            damage = damage * (1-self.resistance[type]*(1-penetration)) # diminue les damages selon la resitance de l'infecté
        if type == "physic":
            if self.resistance[type] >= damage:
                damage = damage*0.05
            else:
                damage = damage - self.resistance[type]*(1-penetration)
        self.health -= damage


    # METHODE: Supprime l'infecté
    def remove(self):
        # Supprime si mort
        if self.health <= 0:
            methode = "update_"+self.enemy_type+"_img"
            getattr(self,methode) # Appel de la méthode update_img selon l'infecté, pour afficher l'animation des "MORT"
            if self.alive == False:
                self.kill() # Disparaître l'infecté après que l'animation des "MORT" ait été effectuée
        # Supprime si atteint le point d'arrivé
        if self.position == (1200,258) and self.in_final_waypoint == True:
            self.position = Vector2(1200,0)
            self.kill()


    # METHODE: Affiche l'animation du Slime
    def update_slime_img(self):
        frequence = 5
        self.slime.frame_counter += 1
        # Passage à la prochaine image tous les 5 frames
        if self.slime.frame_counter == frequence:

            # si points de vie < 0, affiche l'animation de mort
            if self.health <= 0:
                self.slime.current_frame_dead = (self.slime.current_frame_dead + 1) % len(self.slime.slime_animation_dead)
                self.img_animation = self.slime.slime_animation_dead[self.slime.current_frame_dead]
                self.rotation()
                self.slime.frame_counter = 0
                if self.slime.current_frame_dead == len(self.slime.slime_animation_dead) -1:
                    self.alive = False # dénifit que l'infecté est mort

            # sinon affiche l'animation de déplacement
            else:
                self.slime.current_frame_move = (self.slime.current_frame_move + 1) % len(self.slime.slime_animation_move)
                self.img_animation = self.slime.slime_animation_move[self.slime.current_frame_move]
                self.rotation()

                self.slime.frame_counter = 0


    # METHODE: Affiche l'animation du spider
    def update_spider_img(self):
        frequence = 4
        self.spider.frame_counter += 1
        # Passage à la prochaine image tous les 4 frames
        if self.spider.frame_counter == frequence:

            # si points de vie < 0, affiche l'animation de mort
            if self.health <= 0:
                self.spider.current_frame_dead = (self.spider.current_frame_dead + 1) % len(self.spider.spider_animation_dead)
                self.img_animation = self.spider.spider_animation_dead[self.spider.current_frame_dead]
                self.rotation()
                self.spider.frame_counter = 0
                if self.spider.current_frame_dead == len(self.spider.spider_animation_dead) -1:
                    self.alive = False # dénifit que l'infecté est mort

            # sinon affiche l'animation de déplacement
            else:
                self.spider.current_frame_move = (self.spider.current_frame_move + 1) % len(self.spider.spider_animation_move)
                self.img_animation = self.spider.spider_animation_move[self.spider.current_frame_move]
                self.rotation()

                self.spider.frame_counter = 0

    # METHODE: Affiche l'animation du démon
    def update_demon_img(self):
        frequence = 7
        self.demon.frame_counter += 1
        # Passage à la prochaine image tous les 7 frames
        if self.demon.frame_counter == frequence:

            # si points de vie < 0, affiche l'animation de mort
            if self.health <= 0:
                self.demon.current_frame_dead = (self.demon.current_frame_dead + 1)
                self.img_animation = self.demon.demon_animation_dead[self.demon.current_frame_dead]
                self.rotation()
                self.demon.frame_counter = 0
                if self.demon.current_frame_dead == len(self.demon.demon_animation_dead) -1:
                    self.alive = False # dénifit que l'infecté est mort

            # sinon affiche l'animation de déplacement
            else:
                self.demon.current_frame_move = (self.demon.current_frame_move + 1) % len(self.demon.demon_animation_move)
                self.img_animation = self.demon.demon_animation_move[self.demon.current_frame_move]
                self.rotation()

                self.demon.frame_counter = 0


    # METHODE: Affiche l'animation du BOSS
    def update_BOSS_img(self):
        frequence = 8
        self.BOSS.frame_counter += 1
        # Passage à la prochaine image tous les 8 frames
        if self.BOSS.frame_counter == frequence:

            # si points de vie < 0, affiche l'animation de mort
            if self.health <= 0:
                self.BOSS.current_frame_dead = (self.BOSS.current_frame_dead + 1) % len(self.BOSS.BOSS_animation_dead)
                self.img_animation = self.BOSS.BOSS_animation_dead[self.BOSS.current_frame_dead]
                self.rotation()
                self.BOSS.frame_counter = 0
                if self.BOSS.current_frame_dead == len(self.BOSS.BOSS_animation_dead) -1:
                    self.alive = False # dénifit que l'infecté est mort

            # sinon affiche l'animation de déplacement
            else:
                self.BOSS.current_frame_move = (self.BOSS.current_frame_move + 1) % len(self.BOSS.BOSS_animation_move)
                self.img_animation = self.BOSS.BOSS_animation_move[self.BOSS.current_frame_move]
                self.rotation()

                self.BOSS.frame_counter = 0

