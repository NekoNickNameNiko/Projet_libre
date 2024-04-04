import pygame


class operateur:
    def __init__(self,x,y,damage,cooldown,heal,cost):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.damage = damage 
        self.cd = cooldown
        self.heal = heal 
        self.cost = cost
        self.images = []
        self.animation_count = 1
        self.selected = False
        self.deployed = False
        self.colision = False

    def draw(self, fenetre):
        """
        draws the operator
        :param win: surface
        :return: None
        """
        self.animation_count += 1
        self.img = self.images
        if self.animation_count >= len(self.images):
            self.animation_count = 0
        fenetre.blit(self.img, (self.x-self.img.get_width()//2, self.y-self.img.get_height()//2))

    
    def click(self, X, Y):
        """
        returns if tower has been clicked on
        and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.image
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False
    
    def remove(self):
        self.deployed = False
        return False
    
    def move(self):
        pass

