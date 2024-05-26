import pygame
from operateur.operateur import operateur_base
from game_img.load_img import*
from math import*

class typhon(operateur_base):
    def __init__(self,x,y):
        super().__init__(x,y,70,23,"Typhon")

        #Initialisation des images
        self.typhon_imgs_start = typhon_imgs_start[:]
        self.operateur_imgs_idle = typhon_imgs_idle[:]
        self.typhon_imgs_begin_attack = typhon_imgs_begin_attack[:]
        self.typhon_imgs_front_attack = typhon_imgs_front_attack[:]
        self.typhon_imgs_back_attack = typhon_imgs_back_attack[:]
        self.typhon_imgs_down_attack = typhon_imgs_down_attack[:]

        #Initialisation des compteurs d'images
        self.animation_count_start =0
        self.animation_count = 0 #! le begin/front/down utilise la meme animation_count
        self.animation_count_begin = 0 
        self.animation_count_idle = 0

        #Vérifie si l'opérateur est en phase d'attaque
        self.range = 300


    def deployer(self,fenetre):
        """
        Faire les animations de déployement avant tous les autres.
        """
        #initialise les images utilisé
        self.start = self.typhon_imgs_start[self.animation_count_start//3]

        if self.deployed == False and self.animation_count_start >= len(self.typhon_imgs_start)*3-1:
            self.animation_count_start = 0
            self.deployed = True
        else:
            if self.deployed == False:
                if self.animation_count_start >= len(self.typhon_imgs_start)*3-1:
                    self.animation_count_start = 0
                self.animation_count_start += 1 
                fenetre.blit(self.start, (self.x-pygame.Surface.get_width(self.start)//2, self.y-pygame.Surface.get_height(self.start)//2-25))



    def draw_attack(self,fenetre, enemy):
        """
        permet de générer la bonne animation selon l'emplacement de l'ennemie dans la porte
        """

        en_x ,en_y = enemy.position

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
        
        if self.animation_count >= len(self.typhon_imgs_front_attack)*2:
            self.animation_count = 0

        #initialise les images utilisé
        self.img_front = self.typhon_imgs_front_attack[self.animation_count//2]
        self.img_back  = self.typhon_imgs_back_attack[self.animation_count//2]
        self.img_down  = self.typhon_imgs_down_attack[self.animation_count//2]
        self.img_begin = self.typhon_imgs_begin_attack[self.animation_count_begin]

        #Condition qui vérifie quelle animations lancer
        if self.animation_count_begin == len(self.typhon_imgs_begin_attack)-1:
            self.fire(self.animation_count,10)
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

    def draw_idle(self,fenetre):
        """
        permet genere l'animation d'attente quand aucun ennemie n'est dans la porté de tir
        """
        #réinitialise l'animation
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
            if self.animation_count_idle >= len(self.operateur_imgs_idle)*4:
                self.animation_count_idle = 0
        
        self.idle = self.operateur_imgs_idle[self.animation_count_idle//4]
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


    def attack(self,fenetre,ennemi):
        """
        Fait appel aux méthodes pour generer les animations selon l'emplacement de l'ennemie dans le champ ou encore hors du champ
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
        """
        Renvoie le premier ennemi de la liste enemy_older.
        """
        if self.enemy_older:
            return self.enemy_older[0]

