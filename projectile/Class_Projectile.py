import pygame
import math
from projectile.Projectile_Data import*


class Projectile(pygame.sprite.Sprite):

    def __init__(self,projectile_type,position,target,image):
        super().__init__()

        # attributs d'[attaque]
        self.target = target #cible 
        self.collide = False #collision

        # attributs d'[Etat/Stats] 
        self.projectile_type = projectile_type
        self.damage = projectile_data.get(projectile_type)["damage"]
        self.speed = projectile_data.get(projectile_type)["speed"]
        self.type = projectile_data.get(projectile_type)["type"]
        self.penetration = projectile_data.get(projectile_type)["penetration"]
        self.original_image = image.get(projectile_type)
        self.image = self.original_image

        # attributs de [Coordonnées]
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.center = position

    # METHODE: Appel des autres méthodes pour le bon fonctionnement du jeu
    def update(self):
        self.move()
        self.rotation()

    # METHODE: permet le déplacement du projectile | position initiale: opérateur position
                                                #  | position finale: infecté ciblé position (attribut target)
    def move(self):

        # Détermine le mouvement à effectuer [format (x,y)]
        self.movement = self.target.position - self.position
        distance = self.movement.length()

        if distance > 0: # Vérifie si la distance à parcourir n'est pas égale à 0

            # modifie la position de l'infecté selon sa vitesse
            if distance >= self.speed:
                self.position += self.movement.normalize() * self.speed
            # dans le cas où la distance est inférieure à la vitesse, pour éviter que le projectile ne soit immobilisé.
            else:
                self.position += self.movement.normalize() * distance

            self.rect.center = self.position # met à jour le centre de l'image


    # METHODE: modifie l'angle de l'image selon sa direction (emplacement de sa cible)
    def rotation(self):
        # Calcule la distance entre le prochain waypoint et l'ennemie
        distance = self.target.position - self.position

        # Détermine l'angle de rotation selon la distance (vers la direction où se trouve le prochain waypoint)
        angle = math.degrees(math.atan2(-distance[1],distance[0]))
        self.image = pygame.transform.rotate(self.original_image,angle) # Effectue la rotation de l'image selon l'angle

        # Mise à jour des et coordonnées de l'image
        self.rect = self.image.get_rect()
        self.rect.center = self.position


    # METHODE: Détecte s'il y a collision avec sa cible
    def detect_collision(self):
        if self.rect.colliderect(self.target.rect):
            self.collide = True




