from operateur.operateur import operateur_base
import pygame
import os



class typhon(operateur_base):
    def __init__(self,x,y):
        super().__init__(x,y,867,70,1310,23)
        self.typhon_imgs_front = []
        self.typhon_imgs_back = []
        self.tower = []
        self.animation_count = 0

        #Charger l'image de typhon
        for x in range(1,25):
            if x < 10:
                self.typhon_imgs_front.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 0"+ str(x) + ".png")).convert_alpha(),
                    (180, 180)))
            else:
                self.typhon_imgs_front.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 "+ str(x) + ".png")).convert_alpha(),
                    (180, 180)))

        for x in range(1,25):
            if x < 10:
                self.typhon_imgs_back.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/back-Attack_Loop-x1 (3)/提丰-默认-背面-Attack_Loop-x1 (3)_00"+ str(x) + ".png")).convert_alpha(),
                    (180, 180)))
            else:
                self.typhon_imgs_back.append(pygame.transform.scale(
                    pygame.image.load(
                        os.path.join("img_operator/typhon_ilg/back-Attack_Loop-x1 (3)/提丰-默认-背面-Attack_Loop-x1 (3)_0"+ str(x) + ".png")).convert_alpha(),
                    (180, 180)))
                
    def draw(self,fenetre,direction_y):
        """
        draws the operator
        :param win: surface
        :return: None
        """        
        #On vérifie si le count ne dépasse pas la list des images
        if self.animation_count >= len(self.typhon_imgs_front):
            self.animation_count = 0

        #On prend l'image en question
        img_front = self.typhon_imgs_front[self.animation_count]
        img_back  = self.typhon_imgs_back[self.animation_count]

        #on verifie si l'ennemi est en haut ou en bas de l'operater
        if self.y < direction_y:
            fenetre.blit(img_front, (self.x-pygame.Surface.get_width(img_front), self.y-pygame.Surface.get_height(img_front)//2))
        else:
            fenetre.blit(img_back, (self.x-pygame.Surface.get_width(img_back), self.y-pygame.Surface.get_height(img_back)//2))
        self.animation_count += 1
                