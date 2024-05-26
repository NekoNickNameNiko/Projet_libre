import pygame
import math
import os
from menu import Menu

remove_icon  = pygame.transform.scale(pygame.image.load(os.path.join("game_img/game_asset/remove.png")).convert_alpha(),(40,40))
remove_icon1  = pygame.transform.scale(pygame.image.load(os.path.join("game_img/game_asset/remove.png")).convert_alpha(),(40,40))

class operateur_base:
    def __init__(self,x,y,cooldown,cost,name):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.cd = cooldown
        self.cost = cost
        self.name = name

        self.selected = False
        self.deployed = False
        self.placed = False
        self.inRange = False
        self.left = False
        self.moving = False
        self.in_attack = False
        self.fired = False
        
        self.menu = Menu()
        self.menu.add_btn(self.x -30,self.y+15,remove_icon,self.name+"_remove",self.cost,self.cd)
        self.menu.add_btn(self.x +20,self.y-20,remove_icon1,self.name+"_skill",self.cost,self.cd)
        
        self.place_color = (0,0,255, 100)

    def draw_emplacement(self,fenetre):
        """Dessine l'emplacement de l'opérateur avant son déployement"""
        if self.moving == True and self.deployed == False:
            self.img = self.operateur_imgs_idle[0]
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, self.place_color, (self.range, self.range), self.range, 0)
            fenetre.blit(surface, (self.x - self.range, self.y - self.range))
            fenetre.blit(self.img, (self.x-pygame.Surface.get_width(self.img)//2, self.y-pygame.Surface.get_height(self.img)//2-25))

    def draw_radiu(self,fenetre):
        """Dessine la porté d'attaque de l'opérateur"""
        if self.selected == True:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)

            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            fenetre.blit(surface, (self.x - self.range, self.y - self.range))
            self.menu.draw(fenetre)
            


    def click(self, X, Y):
        """Vérifie si l'utilisateur a appuyé sur l'opérateur ou non"""
        if self.deployed == True:
            self.img = self.operateur_imgs_idle[0]
            if X >= self.x - pygame.Surface.get_width(self.img)//4  and X <= self.x + pygame.Surface.get_width(self.img)//4:
                if Y >= self.y - pygame.Surface.get_height(self.img)//4 and Y <= self.y + pygame.Surface.get_height(self.img)//4:
                    return True
            return False

    def remove(self):
        """Retire l'opérateur"""
        self.placed = False
        self.deployed = False
        self.move(100,100)
        self.cd = 60
    
    def move(self, x, y):
        """
        Bouge l'opérateur en x, y
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update(self.name)

    def collide(self, otheroperateur):
        """
        Détecte si y'a colision ou non avec l'autre opérateur
        """
        x2 = otheroperateur.x
        y2 = otheroperateur.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True
    

    def fire(self,count, lent):
        if count == lent:
            self.fired = True
        else:
            self.fired = False
        


