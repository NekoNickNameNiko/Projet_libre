from Operateur import operateur
import pygame
import os

class typhon(operateur):
    def __init__(self,x,y):
        super().__init__(x,y,867,70,1310,23)
        self.typhon_imgs = []
        self.tower = []
        self.animation_count = 0

        for x in range(1,26):
            if x < 10:
                self.typhon_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 0"+ str(x) + ".png")).convert_alpha(),
                    (90, 90)))
            else:
                self.typhon_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("img_typhon/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 "+ str(x) + ".png")).convert_alpha(),
                    (90, 90)))
                
    def draw(self,fenetre):
        super().draw(fenetre)
        # load archer tower images
        if self.animation_counter >= len(self.typhon_imgs):
            self.animation_counter = 0
        typhon = self.typhon_imgs[self.animation_counter]
        fenetre.blit(typhon,(self.x +self.weidth/2-(typhon.get_width()/2),(self.y +self.height/2-(typhon.get_width()/2))))
        self.animation_counter += 1
                
test = typhon(300,300)