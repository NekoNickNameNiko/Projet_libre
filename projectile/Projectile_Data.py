import pygame

# Initialise un dictionnaire contenant les images des projectiles de chaque opérateurs
projectile_image = {"Typhon": pygame.transform.scale(pygame.image.load("game_img/img_projectile/fleche.png").convert_alpha(),(30, 10)),
                    "Jessica": pygame.transform.scale(pygame.image.load("game_img/img_projectile/ball.png").convert_alpha(),(10, 3)),
                    "Haze": pygame.transform.scale(pygame.image.load("game_img/img_projectile/fire_ball.png").convert_alpha(),(30, 10)),
                    "Steward": pygame.transform.scale(pygame.image.load("game_img/img_projectile/fire_ball.png").convert_alpha(),(30, 10))}


# Initialise un dictionnaire indiquant les données des projectiles pour chaque opérateurs
projectile_data = {"Typhon":           {"damage":1045, # dégât
                                        "speed": 30, # vitesse de déplacement du projectile
                                        "type": "physic", # élément/type de projectile
                                        "penetration": 0.5}, # pénétration

                   "Jessica":          {"damage":475, # dégât
                                        "speed": 30, # vitesse de déplacement du projectile
                                         "type": "physic", # élément/type de projectile
                                         "penetration": 0}, # pénétration

                   "Haze":              {"damage":583, # dégât
                                         "speed": 25, # vitesse de déplacement du projectile
                                         "type": "magic", # élément/type de projectile
                                         "penetration": 0.2}, # pénétration

                    "Steward":           {"damage": 470, # dégât
                                          "speed": 25, # vitesse de déplacement du projectile
                                          "type": "magic", # élément/type de projectile
                                          "penetration": 0}} # pénétration
