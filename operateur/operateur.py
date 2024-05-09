import pygame


class operateur_base:
    def __init__(self,x,y,damage,cooldown,heal,cost):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.damage = damage 
        self.cd = cooldown
        self.heal = heal 
        self.cost = cost
        self.animation_count = 1
        self.selected = False
        self.deployed = False
        self.operator_img = []


    #Dessine l'opérateur
    def draw(self, fenetre):
        """
        draws the operator
        :param win: surface
        :return: None
        """
        self.animation_count += 1
        self.img = self.operator_img
        
        if self.animation_count >= len(self.operator_img):
            self.animation_count = 0
        fenetre.blit(self.img, (self.x-pygame.Surface.get_width(self.img)//2, self.y-pygame.Surface.get_height(self.img)//2))

    def draw_radiu(self,fenetre):
        if self.selected == True:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)

            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            fenetre.blit(surface, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        img = self.operator_img
        if X <= self.x - pygame.Surface.get_width(img)//2 + self.width and X >= self.x - pygame.Surface.get_width(img)//2:
            if Y <= self.y + self.height - pygame.Surface.get_height(img)//2 and Y >= self.y - pygame.Surface.get_height(img)//2:
                return True
        return False
        
    
    def check_deployed(self):
        return self.deployed == True

    def remove(self):
        self.deployed = False
        self.cd = 60
        return self.deployed, self.cd
    
    def move(self,x,y):
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()


