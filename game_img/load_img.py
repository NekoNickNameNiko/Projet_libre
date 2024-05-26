import pygame
import os


#Liste des images des différents éléments du jeu
#----------------------------------------------------------------
#Liste des images de typhons
typhon_imgs_start = []
typhon_imgs_idle = []
typhon_imgs_begin_attack = []
typhon_imgs_front_attack = []
typhon_imgs_back_attack = []
typhon_imgs_down_attack = []

#Liste des images de Jessica
Jessica_imgs_start = []
Jessica_imgs_idle = []
Jessica_imgs_front_attack = []
Jessica_imgs_back_attack = []

#Liste des images de Haze
Haze_imgs_start = []
Haze_imgs_idle = []
Haze_imgs_front_attack = []
Haze_imgs_back_attack = []

#Liste des images de steward
steward_imgs_start = []
steward_imgs_idle = []
steward_imgs_front_attack = []
steward_imgs_back_attack = []
#Liste des images des monstres
slime_animation_move = []
slime_animation_dead = []
spider_animation_move = []
spider_animation_dead = []
demon_animation_move = []
demon_animation_dead = []
BOSS_animation_move = []
BOSS_animation_dead = []
#Fonction de chargement avant le lancement du jeu
#----------------------------------------------------------------
progression = 0
smallfont = pygame.font.SysFont("comicansme",25)
text = smallfont.render("loading:"+ str(int(0)),True, "white")

def update_load(progression):
    global text
    if progression < 100:
        text = smallfont.render("loading:"+ str(int(progression)),True, "white")
    else:
        text = smallfont.render("loading:"+ str(int(100)),True, "white")

def draw(fenetre,progression):
    fenetre.fill((0,0,0))
    fenetre_rect = fenetre.get_rect()
    fenetre_rect.center = fenetre_rect.center
    pygame.draw.rect(fenetre,"WHITE",(fenetre_rect.center[0]-200,fenetre_rect.center[1],400,26),5)
    
    if (progression) < 100:
        pygame.draw.rect(fenetre,"white",[fenetre_rect.center[0]-200,fenetre_rect.center[1],progression*4,25])
    else:
        pygame.draw.rect(fenetre,"white",[fenetre_rect.center[0]-200,fenetre_rect.center[1],400,25])
    fenetre.blit(text,((1200 - fenetre.get_width() // 2-50, 700 - fenetre.get_height() // 2-25)))
    pygame.display.update()

#Mettre à jour la barre de chargement
def update(self):
    global progression       
    progression += (1/308)*100
    update_load(progression)
    draw(self.fenetre,progression)
    

#Chargement des images
#------------------------------------------------
def load_img(self):
    global progression ,typhon_imgs_start ,typhon_imgs_idle ,typhon_imgs_begin_attack ,typhon_imgs_front_attack ,typhon_imgs_back_attack ,typhon_imgs_down_attack
    global slime_animation, spider_animation
    
    #----------------------------------------------------------------
    #Charger l'image de typhon
    for x in range(1,25): 
        if x < 10:
            typhon_imgs_front_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 0"+ str(x) + ".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            typhon_imgs_front_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/front-Attack_Loop-x1/Attack_Loop-x1 "+ str(x) + ".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(1,25):
        if x < 10:
            typhon_imgs_back_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/back-Attack_Loop-x1/提丰-默认-背面-Attack_Loop-x1 (3)_00"+ str(x) + ".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            typhon_imgs_back_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/back-Attack_Loop-x1/提丰-默认-背面-Attack_Loop-x1 (3)_0"+ str(x) + ".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(1,25):
        if x < 10:
            typhon_imgs_down_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/down-Attack_Loop-x1/提丰-默认-正面-Attack_Down_Loop-x1_00"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            typhon_imgs_down_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/down-Attack_Loop-x1/提丰-默认-正面-Attack_Down_Loop-x1_0"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                (170, 170)))
            update(self)
    
    for x in range(1,17):
        if x < 10:
            typhon_imgs_begin_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/front-begin-Attack/0000"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            typhon_imgs_begin_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/front-begin-Attack/000"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(11):
        if x < 10:
            typhon_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/提丰-默认-正面-Start/提丰-默认-正面-Start-x1_00"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            typhon_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/提丰-默认-正面-Start/提丰-默认-正面-Start-x1_0"+ str(x) + "-removebg-preview.png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(61):
        if x < 10:
            typhon_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/提丰-默认-正面-Idle-x1/提丰-默认-正面-Idle-x1_00"+ str(x) + ".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            typhon_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img/img_operator/typhon_ilg/提丰-默认-正面-Idle-x1/提丰-默认-正面-Idle-x1_0"+ str(x) + ".png")).convert_alpha(),
                (170, 170)))
            update(self)

    #----------------------------------------------------------------
    #Charge l'image de jessica
    for x in range(11):
        if x < 10:
            Jessica_imgs_front_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-正面-Attack-x1\杰西卡-君子兰-正面-Attack-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            Jessica_imgs_front_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-正面-Attack-x1\杰西卡-君子兰-正面-Attack-x1_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(11):
        if x < 10:
            Jessica_imgs_back_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-背面-Attack-x1\杰西卡-君子兰-背面-Attack-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            Jessica_imgs_back_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-背面-Attack-x1\杰西卡-君子兰-背面-Attack-x1_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(11):
        if x < 10:
            Jessica_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-正面-Start-x1\杰西卡-君子兰-正面-Start-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            Jessica_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-正面-Start-x1\杰西卡-君子兰-正面-Start-x1_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(21):
        if x < 10:
            Jessica_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-正面-Idle-x1\杰西卡-君子兰-正面-Idle-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            Jessica_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\Jessica\杰西卡-君子兰-正面-Idle-x1\杰西卡-君子兰-正面-Idle-x1_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
    
    #----------------------------------------------------------------
    #Charge l'image de Haze
    for x in range(10):
        Haze_imgs_front_attack.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("game_img\img_operator\img_haze\夜烟-默认-正面-Attack_Loop-x1\夜烟-默认-正面-Attack_Loop-x1_00"+str(x)+".png")).convert_alpha(),
            (170, 170)))
        update(self)

    for x in range(10):
        Haze_imgs_back_attack.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("game_img\img_operator\img_haze\夜烟-默认-背面-Attack_Loop-x1\夜烟-默认-背面-Attack_Loop-x1_00"+str(x)+".png")).convert_alpha(),
            (170, 170)))
        update(self)

    for x in range(21):
        if x < 10:
            Haze_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_haze\夜烟-默认-正面-Start-x1\夜烟-默认-正面-Start-x0.5_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            Haze_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_haze\夜烟-默认-正面-Start-x1\夜烟-默认-正面-Start-x0.5_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(21):
        if x < 10:
            Haze_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_haze\夜烟-默认-正面-Idle-x1\夜烟-默认-正面-Idle-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            Haze_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_haze\夜烟-默认-正面-Idle-x1\夜烟-默认-正面-Idle-x1_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    #----------------------------------------------------------------
    #Charge l'image de Steward
    for x in range(9):
        if x < 10:
            steward_imgs_front_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_steward\史都华德-风雪邀请-正面-Attack-x1\史都华德-风雪邀请-正面-Attack-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(9):
        if x < 10:
            steward_imgs_back_attack.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_steward\史都华德-风雪邀请-背面-Attack-x1\史都华德-风雪邀请-背面-Attack-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)


    for x in range(11):
        if x < 10:
            steward_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_steward\史都华德-风雪邀请-正面-Start-x1\史都华德-风雪邀请-正面-Start-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            steward_imgs_start.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_steward\史都华德-风雪邀请-正面-Start-x1\史都华德-风雪邀请-正面-Start-x1_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    for x in range(14):
        if x < 10:
            steward_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_steward\史都华德-风雪邀请-正面-Idle-x1\史都华德-风雪邀请-正面-Idle-x1_00"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)
        else:
            steward_imgs_idle.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_img\img_operator\img_steward\史都华德-风雪邀请-正面-Idle-x1\史都华德-风雪邀请-正面-Idle-x1_0"+str(x)+".png")).convert_alpha(),
                (170, 170)))
            update(self)

    #----------------------------------------------------------------
    # Initialise Infected Animations
    # Image Slime Move
    for x in range(7):
        slime_animation_move.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_img/img_infected/Slime/Move/enemy_1007_slime_2-"+ str(x) +".png")).convert_alpha(),
                (70, 70)))
        update(self)

    # Image Slime Dead
    for x in range(3):
        slime_animation_dead.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_img/img_infected/Slime/Mort/enemy_1007_slime_3-"+ str(x) +".png")).convert_alpha(),
                (70, 70)))
        update(self)

    # Image Spider Move
    for x in range(7):
        spider_animation_move.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "game_img/img_infected/Spider/Move/enemy_1021_bslime_2-"+ str(
                        x) + ".png")).convert_alpha(),(70, 70)))

    # Image Spider Dead
    for x in range(6):
        spider_animation_dead.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "game_img/img_infected/Spider/Mort/enemy_1021_bslime_3-" + str(
                        x) + ".png")).convert_alpha(), (70, 70)))

    # Image Demon Move
    for x in range(12):
        demon_animation_move.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "game_img/img_infected/Demon/Move/enemy_1010_demon_2-" + str(
                        x) + ".png")).convert_alpha(), (80, 80)))
        update(self)

    # Image Demon Dead
    for x in range(7):
        demon_animation_dead.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "game_img/img_infected/Demon/Mort/enemy_1010_demon_3-" + str(
                        x) + ".png")).convert_alpha(), (80, 80)))
        update(self)

    # Image BOSS Move
    for x in range(9):
        BOSS_animation_move.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "game_img/img_infected/BOSS/Move/enemy_1061_zomshd_2-" + str(
                        x) + ".png")).convert_alpha(), (90, 90)))
        update(self)

    # Image BOSS Dead
    for x in range(6):
        BOSS_animation_dead.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "game_img/img_infected/BOSS/Mort/enemy_1061_zomshd_3-" + str(
                        x) + ".png")).convert_alpha(), (130,130)))
        update(self)

    progression = 100
    update(self)
    self.loading_finish = True