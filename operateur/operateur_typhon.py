from operateur.operateur import operateur_base
import pygame
import os

typhon_imgs = []
#Charger l'image de typhon
for x in range(1,26):
    if x < 10:
        typhon_imgs.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 0"+ str(x) + ".png")).convert_alpha(),
            (90, 90)))
    else:
        typhon_imgs.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("img_typhon/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 "+ str(x) + ".png")).convert_alpha(),
            (90, 90)))


class typhon(operateur_base):
    def __init__(self,x,y):
        super().__init__(x,y,867,70,1310,23)
        self.typhon_imgs = typhon_imgs[:]
        self.animation_count = 0



                
    def draw(self,fenetre):
        super().draw(fenetre)
        # load archer tower images
        if self.animation_counter >= len(self.typhon_imgs):
            self.animation_counter = 0
        
        typhon = self.typhon_imgs[self.animation_counter]
        fenetre.blit(typhon,(self.x +self.weidth/2-(typhon.get_width()/2),(self.y +self.height/2-(typhon.get_width()/2))))
        self.animation_counter += 1
                