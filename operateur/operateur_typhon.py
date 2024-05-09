import pygame
from operateur.operateur import operateur_base
import os
from math import*



class typhon(operateur_base):
    def __init__(self,x,y):
        super().__init__(x,y,867,70,1310,23)
        self.typhon_imgs_start = []
        self.typhon_imgs_idle = []
        self.typhon_imgs_begin_attack = []
        self.typhon_imgs_front_attack = []
        self.typhon_imgs_back_attack = []
        self.typhon_imgs_down_attack = []

        #Initialisation des compte d'images
        self.animation_count_start =0
        self.animation_count = 0 #! le begin/front/down utilise la meme animation_count
        self.animation_count_begin = 0 
        self.animation_count_idle = 0

        self.range = 300
        self.inRange = False
        self.left = False
        #Charger l'image de typhon
        for x in range(1,25): 
            if x < 10:
                self.typhon_imgs_front_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 0"+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))
            else:
                self.typhon_imgs_front_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 "+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))

        for x in range(1,25):
            if x < 10:
                self.typhon_imgs_back_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/back-Attack_Loop-x1/提丰-默认-背面-Attack_Loop-x1 (3)_00"+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))
            else:
                self.typhon_imgs_back_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/back-Attack_Loop-x1/提丰-默认-背面-Attack_Loop-x1 (3)_0"+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))
        
        for x in range(1,25):
            if x < 10:
                self.typhon_imgs_down_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/down-Attack_Loop-x1/提丰-默认-正面-Attack_Down_Loop-x1_00"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                    (170, 170)))
            else:
                self.typhon_imgs_down_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/down-Attack_Loop-x1/提丰-默认-正面-Attack_Down_Loop-x1_0"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                    (170, 170)))

        for x in range(1,17):
            if x < 10:
                self.typhon_imgs_begin_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/front-begin-Attack/0000"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                    (170, 170)))
            else:
                self.typhon_imgs_begin_attack.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/front-begin-Attack/000"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                    (170, 170)))

        for x in range(11):
            if x < 10:
                self.typhon_imgs_start.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/提丰-默认-正面-Start/提丰-默认-正面-Start-x1_00"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                    (170, 170)))
            else:
                self.typhon_imgs_start.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/提丰-默认-正面-Start/提丰-默认-正面-Start-x1_0"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                    (170, 170)))

        for x in range(61):
            if x < 10:
                self.typhon_imgs_idle.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/提丰-默认-正面-Idle-x1/提丰-默认-正面-Idle-x1_00"+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))
            else:
                self.typhon_imgs_idle.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/提丰-默认-正面-Idle-x1/提丰-默认-正面-Idle-x1_0"+ str(x) + ".png")).convert_alpha(),
                    (170, 170)))

    def deployer(self,fenetre):
        #initialise les images utilisé
        self.start = self.typhon_imgs_start[self.animation_count_start//3]

        if self.deployed == False and self.animation_count_start >= len(self.typhon_imgs_start)*3-1:
            self.deployed = True
        else:
            if self.deployed == False:
                if self.animation_count_start >= len(self.typhon_imgs_start)*3-1:
                    self.animation_count_start = 0
                self.animation_count_start += 1 
                fenetre.blit(self.start, (self.x-pygame.Surface.get_width(self.start)//2, self.y-pygame.Surface.get_height(self.start)//2-25))


    #permet genere l'animation cohérent selon l'emplacement de l'ennemie dans la porte
    def draw_attack(self,fenetre, ennemi):
        """
        draws the operator
        :param win: surface
        :return: None
        """

        en_x ,en_y = ennemi[0], ennemi[1]

        #Chek si l'ennemi est a gauche ou non (permet de réajuster les coordonnées des animations pour 
        #qu'il n'y est pas de saut entre chaque mouvement)
        if self.left:
            add = 13
            self.add_1 = 10
        else:
            add = -13
            self.add_1 = -10

        #Inverser les images en question 
        if en_x < self.x and not self.left:
            self.left = True

            for x, img in enumerate(self.typhon_imgs_front_attack):
                self.typhon_imgs_front_attack[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.typhon_imgs_down_attack):
                self.typhon_imgs_down_attack[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.typhon_imgs_back_attack):
                self.typhon_imgs_back_attack[x] = pygame.transform.flip(img, True, False)
        elif self.left and en_x > self.x:
            self.left = False

            for x, img in enumerate(self.typhon_imgs_front_attack):
                self.typhon_imgs_front_attack[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.typhon_imgs_down_attack):
                self.typhon_imgs_down_attack[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.typhon_imgs_back_attack):
                self.typhon_imgs_back_attack[x] = pygame.transform.flip(img, True, False)

        #Si l'animation est déjà ou non en cours
        if self.animation_count_begin == len(self.typhon_imgs_begin_attack)-1:
            self.animation_count += 1
        else:
            self.animation_count_begin +=1
            #On vérifie si le count ne dépasse pas la list des images
            if self.animation_count_begin >= len(self.typhon_imgs_begin_attack):
                self.animation_count_begin = 0
        
        if self.animation_count >= len(self.typhon_imgs_front_attack)*3:
            self.animation_count = 0

        #initialise les images utilisé
        self.img_front = self.typhon_imgs_front_attack[self.animation_count//3]
        self.img_back  = self.typhon_imgs_back_attack[self.animation_count//3]
        self.img_down  = self.typhon_imgs_down_attack[self.animation_count//3]
        self.img_begin = self.typhon_imgs_begin_attack[self.animation_count_begin]

        #Condition qui vérifie quelle animations lancer
        if self.animation_count_begin == len(self.typhon_imgs_begin_attack)-1: 
            #on verifie l'angle entre l'operateur et l'infecté puis on utilise les images destinée
            if acos(abs(en_x - self.x) / abs(sqrt((en_x - self.x)**2 + (en_y - self.y)**2))) < 1/2:
                fenetre.blit(self.img_front, (self.x-pygame.Surface.get_width(self.img_front)//2+self.add_1, self.y-pygame.Surface.get_height(self.img_front)//2-25))
            else:
                #si l'enemy est en haut ou en bas de l'opérateur en question
                if self.y > en_y:
                    fenetre.blit(self.img_back, (self.x-pygame.Surface.get_width(self.img_back)//2+self.add_1+add, self.y-pygame.Surface.get_height(self.img_back)//2-23))
                else:
                    fenetre.blit(self.img_down, (self.x-pygame.Surface.get_width(self.img_down)//2+self.add_1, self.y-pygame.Surface.get_height(self.img_down)//2-25))
        else:
            #Image début de l'animation d'attaque
            fenetre.blit(self.img_begin, (self.x-pygame.Surface.get_width(self.img_begin)//2-10, self.y-pygame.Surface.get_height(self.img_begin)//2-25))


    # permet genere l'animation d'attente quand aucun ennemie n'est dans la porté de tir
    def draw_idle(self,fenetre):
        #reset l'animation
        if self.animation_count != 0:
            self.animation_count += 1
            #On vérifie si le count ne dépasse pas la list des images
            if self.animation_count >= len(self.typhon_imgs_front_attack)*3:
                self.animation_count = 0
        #Vérifie si l'animation de l'attaque est terminé avant de lancer celle pour ce remettre en attente
        if self.animation_count == 0 and self.animation_count_begin >= 1:
            self.animation_count_begin -= 1
        
        if self.animation_count == 0 and self.animation_count_begin == 0 :
            self.animation_count_idle += 1
            if self.animation_count_idle >= len(self.typhon_imgs_idle)*3:
                self.animation_count_idle = 0
        
        self.idle = self.typhon_imgs_idle[self.animation_count_idle//3]
        self.img_begin = self.typhon_imgs_begin_attack[self.animation_count_begin]

        #Permet de terminer l'action en question
        if self.animation_count != 0:
            self.img_front = self.typhon_imgs_front_attack[self.animation_count//3]
            fenetre.blit(self.img_front, (self.x-pygame.Surface.get_width(self.img_front)//2+self.add_1, self.y-pygame.Surface.get_height(self.img_front)//2-25))
        elif self.animation_count_begin != 0:
            self.add_1 = -10
            fenetre.blit(self.img_begin, (self.x-pygame.Surface.get_width(self.img_begin)//2+self.add_1, self.y-pygame.Surface.get_height(self.img_begin)//2-25))
        else:
            fenetre.blit(self.idle, (self.x-pygame.Surface.get_width(self.idle)//2-10, self.y-pygame.Surface.get_height(self.idle)//2-25))

    # Fait appel aux méthodes pour generer les animations selon l'emplacement de l'ennemie dans le champ ou encore hors du champ
    def attack(self,fenetre,ennemi):
        """
        attaque un ennemi dans la liste ennemi
        :param: ennemi
        return: int
        """
        self.inRange = False
        enemy_older = []
        for enemy in ennemi:
            x = enemy.get_height()
            y = enemy.get_width()
            dis = sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_older.append(enemy)

        if self.deployed == True:
            if len(enemy_older) > 0 :
                self.draw_attack(fenetre, enemy_older[0])
            else:
                super().draw_radiu(fenetre)
                self.draw_idle(fenetre)
        else:
            self.deployer(fenetre)