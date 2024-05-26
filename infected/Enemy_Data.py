import pygame
import os

# Initialise la posture par defaut des infectés
infected_image = {"slime": pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_infected/Slime/Move/enemy_1007_slime_2-0.png")).convert_alpha(),(70, 70)),
                  "spider": pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_infected/Spider/Move/enemy_1021_bslime_2-0.png")).convert_alpha(),(70, 70)),
                  "demon": pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_infected/Demon/Move/enemy_1010_demon_2-0.png")).convert_alpha(),(80, 80)),
                  "BOSS": pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_infected/BOSS/Move/enemy_1061_zomshd_2-0.png")).convert_alpha(),(90, 90))}

# Chemins que prendront les infectés
infected_waypoint = [[(0, 315),(51, 331),(89, 358),(126, 383),(167, 410),(206, 413),(256, 411),(288, 406),(309, 373),(313, 347),(319, 311),(350, 288),(397, 261),(448, 278),(507, 300),(516, 362),(543, 397),(571, 424),(605, 448),(659, 465),(711, 475),(764, 478),(807, 470),(860, 453),(889, 429),(934, 411),(966, 356),(967, 365),(988, 370),(1035, 374),(1091, 372),(1127, 347),(1148, 312),(1176, 258),(1200,258)],
                     [(572, 0),(547, 44),(528, 83),(496, 112),(451, 146),(402, 174),(371, 209),(397, 261),(508, 295),(545, 257),(581, 233),(621, 217),(675, 196),(735, 193),(796, 197),(840, 206),(884, 224),(917, 246),(934, 276),(952, 295),(964, 331),(967, 365),(970, 365),(988, 370),(1035, 374),(1091, 372),(1127, 347),(1148, 312),(1176, 258),(1200,258)],
                     [(707, 362),(653, 414),(686, 478),(740, 487),(807, 478),(877, 454),(930, 420),(958, 362),(932, 300),(898, 245),(837, 221),(766, 207),(683, 206),(608, 228),(546, 269),(503, 324),(530, 405),(596, 452),(686, 478),(740, 487),(807, 478),(877, 454),(930, 420),(958, 362),(932, 300),(898, 245),(837, 221),(766, 207),(683, 206),(608, 228),(546, 269),(503, 324),(530, 405),(596, 452),(686, 478),(711, 475),(764, 478),(807, 470),(860, 453),(889, 429),(934, 411),(966, 356),(967, 365),(988, 370),(1035, 374),(1091, 372),(1127, 347),(1148, 312),(1176, 258),(1200,258)]]


# Initialise les infectés qu'apparaitront durant les différents WAVE
enemy_spawn_data = [
    # WAVE N°1
    {"slime": 4,
     "spider":0,
     "demon": 0,
     "BOSS": 0},

    # WAVE N°2
    {"slime": 3,
     "spider": 2,
     "demon": 0,
     "BOSS": 0},

    # WAVE N°3
    {"slime": 6,
     "spider": 4,
     "demon": 0,
     "BOSS": 0},

    # WAVE N°4
    {"slime": 5,
     "spider": 3,
     "demon": 1,
     "BOSS": 0},

    # WAVE N°5
    {"slime": 4,
     "spider": 4,
     "demon": 2,
     "BOSS": 0},

    # WAVE N°6
    {"slime": 3,
     "spider": 0,
     "demon": 3,
     "BOSS": 1},
    
    # WAVE N°7
    {"slime": 4,
     "spider": 3,
     "demon": 0,
     "BOSS": 0}]

# Données des différents types d'infectés
enemy_data = {"slime":     {"health":950, # point de vie
                            "speed": 1, # vitesse de déplacement
                            "resistance": {"physic":0,"magic":0}}, #(type d'element, soustraction/pourcentage de resistance)

              "spider":    {"health":1450, # point de vie
                            "speed": 1.2, # vitesse de déplacement
                            "resistance": {"physic":50,"magic":0}}, #(type d'element, soustraction/pourcentage de resistance)

              "demon":     {"health":5500, # point de vie
                            "speed": 0.8, # vitesse de déplacement
                            "resistance": {"physic":350 ,"magic":0.5}}, #(type d'element, soustraction/pourcentage de resistance)

              "BOSS":      {"health":16000, # point de vie
                            "speed": 1, # vitesse de déplacement
                            "resistance": {"physic":450,"magic":0.3}}} #(type d'element, soustraction/pourcentage de resistance )