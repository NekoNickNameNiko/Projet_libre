import pygame
from operateur.operateur import operateur_base
from game_img.load_img import*
from math import*

class haze(operateur_base):
    def __init__(self,x,y):
        super().__init__(x,y,70,23,"Haze")
        self.Haze_imgs_start = Haze_imgs_start[:]
        self.operateur_imgs_idle = Haze_imgs_idle[:]
        self.Haze_imgs_front_attack = Haze_imgs_front_attack[:]
        self.Haze_imgs_back_attack = Haze_imgs_back_attack[:]

        #Initialisation des compteurs d'images
        self.animation_count_start =0
        self.animation_count = 0 #! le begin/front/down utilise la meme animation_count
        self.animation_count_idle = 0

        self.range = 200

    def deployer(self,fenetre):
        #initialise les images utilisé
        self.start = self.Haze_imgs_start[self.animation_count_start//2]

        if self.deployed == False and self.animation_count_start >= len(self.Haze_imgs_start)*2-1:
            self.animation_count_start = 0
            self.deployed = True
        else:
            if self.animation_count_start >= len(self.Haze_imgs_start)*2-1:
                self.animation_count_start = 0
            self.animation_count_start += 1 
            fenetre.blit(self.start, (self.x-pygame.Surface.get_width(self.start)//2, self.y-pygame.Surface.get_height(self.start)//2-25))


    #permet genere l'animation cohérent selon l'emplacement de l'ennemie dans la porte
    def draw_attack(self,fenetre, enemy):
        """
        draws the operator
        :param win: surface
        :return: None
        """

        en_x ,en_y = enemy.position

        #Chek si l'ennemi est a gauche ou non (permet de réajuster les coordonnées des animations pour 
        #qu'il n'y est pas de saut entre chaque mouvement)
        if self.left:
            add = 0
            self.add_1 = 0
        else:
            add = 0
            self.add_1 = 0

        #Inverser les images en question 
        if en_x < self.x and not self.left:
            self.left = True

            for x, img in enumerate(self.Haze_imgs_front_attack):
                self.Haze_imgs_front_attack[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.Haze_imgs_back_attack):
                self.Haze_imgs_back_attack[x] = pygame.transform.flip(img, True, False)
        elif self.left and en_x > self.x:
            self.left = False

            for x, img in enumerate(self.Haze_imgs_front_attack):
                self.Haze_imgs_front_attack[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.Haze_imgs_back_attack):
                self.Haze_imgs_back_attack[x] = pygame.transform.flip(img, True, False)

        self.animation_count += 1
        
        if self.animation_count >= len(self.Haze_imgs_front_attack)*3:
            self.animation_count = 0

        #initialise les images utilisé
        self.img_front = self.Haze_imgs_front_attack[self.animation_count//3]
        self.img_back  = self.Haze_imgs_back_attack[self.animation_count//3]

        
        self.fire(self.animation_count,15)
        #Condition qui vérifie quelle animations lancer
        #si l'enemy est en haut ou en bas de l'opérateur en question
        if self.y < en_y:
            fenetre.blit(self.img_front, (self.x-pygame.Surface.get_width(self.img_front)//2+self.add_1+add, self.y-pygame.Surface.get_height(self.img_front)//2-25))
        else:
            fenetre.blit(self.img_back, (self.x-pygame.Surface.get_width(self.img_back)//2+self.add_1, self.y-pygame.Surface.get_height(self.img_back)//2-25))

        

    # permet genere l'animation d'attente quand aucun ennemie n'est dans la porté de tir
    def draw_idle(self,fenetre):
        self.animation_count_idle += 1
        if self.animation_count_idle >= len(self.operateur_imgs_idle)*4:
            self.animation_count_idle = 0
        
        self.idle = self.operateur_imgs_idle[self.animation_count_idle//4]
        fenetre.blit(self.idle, (self.x-pygame.Surface.get_width(self.idle)//2, self.y-pygame.Surface.get_height(self.idle)//2-25))

    # Fait appel aux méthodes pour generer les animations selon l'emplacement de l'ennemie dans le champ ou encore hors du champ
    def attack(self,fenetre,ennemi):
        """
        attaque un ennemi dans la liste ennemi
        :param: ennemi
        return: int
        """
        if self.placed:
            self.inRange = False
            self.enemy_older = []
            super().draw_radiu(fenetre)
            super().draw_emplacement(fenetre)
            for enemy in ennemi:
                x,y = enemy.position
                dis = sqrt((self.x - x)**2 + (self.y - y)**2)
                if dis < self.range:
                    self.inRange = True
                    self.enemy_older.append(enemy)

            if self.deployed and not self.moving:
                if len(self.enemy_older) > 0 :
                    self.draw_attack(fenetre, self.enemy_older[0])
                else:
                    self.draw_idle(fenetre)
            else:
                self.deployer(fenetre)

    def first_enemy(self):
        if self.enemy_older:
            return self.enemy_older[0]
    
