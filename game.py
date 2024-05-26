import pygame
import os
import numpy as np
from random import randint
from game_img.load_img import*
from operateur.list_operateur import Operateurlist
from infected.Class_Infected import Infected
from infected.Enemy_Data import*
from projectile.Class_Projectile import*
from projectile.Projectile_Data import*
from menu import Menu

# Initialise les Infected
infected_group = pygame.sprite.Group()
SPAWN_Cooldown_infected = 1000

# Initialise les projectiles
projectile_group = pygame.sprite.Group()

# Initialisation des icones des opérateurs 
typhon_icon  = pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_operator/typhon_ilg/icon_typhon.png")).convert_alpha(),(90,90))
jessica_icon  = pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_operator/Jessica/头像_杰西卡.png")).convert_alpha(),(90,90))
haze_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_operator/img_haze/头像_夜烟.png")).convert_alpha(),(90,90))
steward_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_img/img_operator/img_steward/头像_史都华德.png")).convert_alpha(),(90,90))

#Draw timer (5:00)
band = pygame.Surface((100, 50), pygame.SRCALPHA)
band_color = (0, 0, 0, 128)  # Bande Noir à 50% de transparence
band.fill(band_color)
# Afficher le nombre de vie restant au joueur
band_2 = pygame.Surface((150, 50), pygame.SRCALPHA)
band_2_color = (0, 0, 0, 128)  # Bande Noir à 50% de transparence
band_2.fill(band_2_color)
# Afficher les coins de déploiement (dp)
band_3 = pygame.Surface((170, 90), pygame.SRCALPHA)
band_3_color = (0, 0, 0, 128)  # Bande Noir à 50% de transparence
band_3.fill(band_3_color)

# Affiche win ou lose
band_lose = pygame.Surface((1200, 200), pygame.SRCALPHA)
band_lose_color = (0, 0, 0, 128)  # Bande Noir à 50% de transparence
text_lose = pygame.font.Font(None, 100).render("Defeat will only make you stronger", True, (255, 255, 255))
band_lose.fill(band_lose_color)
text_rect_lose = text_lose.get_rect()
text_rect_lose.center = 1200/2, 425

band_win = pygame.Surface((1200, 200), pygame.SRCALPHA)
band_win_color = (0, 0, 0, 128)  # Bande Noir à 50% de transparence
text_win = pygame.font.Font(None, 100).render("Well play, you are the best", True, (255, 255, 255))
band_win.fill(band_win_color)
text_rect_win = text_win.get_rect()
text_rect_win.center = 1200/2, 425

text1 = pygame.font.Font(None, 50).render("Dp:", True, (255, 255, 255))


class Game(pygame.sprite.Sprite):
    """
    Classe principal du projet
    """
    def __init__(self,fenetre):
        super().__init__()
        #---------------------------------------------------------
        #Paramètre du jeu
        self.fenetre = fenetre
        
        self.lives = 3
        self.lose = False
        self.lose_image = pygame.transform.scale(pygame.image.load("game_img/game_asset/you_lose.webp").convert_alpha(),(550, 400))
        self.lose_image_x = (1200 - self.lose_image.get_width()) // 2
        self.lose_image_y = 0

        
        self.win = False
        self.win_image = pygame.transform.scale(pygame.image.load("game_img/game_asset/you_win.webp").convert_alpha(),(550, 400))
        self.win_image_x = (1200 - self.win_image.get_width()) // 2
        self.win_image_y = 0

        self.dp = 10
        self.bg = pygame.image.load("game_img/game_asset/map.png")
        self.bg = pygame.transform.scale(self.bg,(self.fenetre.get_width(),self.fenetre.get_height()))
        self.life_font = pygame.font.SysFont("comicsans", 55)
        self.loading_finish = False
        self.game_started = False
        self.valid_place = [(215, 367), (414, 351), (476, 237), (754, 432), (1057, 327), (1023, 443)]
        self.valid_place = np.array(self.valid_place)

        #--------------------------------------------------------
        #Partie infecté et projectile
        
        self.infected = []
        self.infected_spawn_list = []
        self.last_infected_spawn = pygame.time.get_ticks()
        self.spawn_infected = 0
        self.wave = 1
        self.wave1_clear = False
        self.wave2_clear = False
        self.wave3_clear = False
        self.wave4_clear = False
        self.wave5_clear = False
        self.wave6_clear = False
        self.wave7_clear = False

        self.last_projectile_spawn = pygame.time.get_ticks()

        #--------------------------------------------------------
        #Partie operateur
        self.operateur_list = Operateurlist(self)

        #--------------------------------------------------------
        #Tous les interactives de l'écran
        self.menu = Menu()
        self.menu.add_btn(900,600,typhon_icon,"Typhon",21,60)
        self.menu.add_btn(700,600,haze_icon,"Haze",16,60)
        self.menu.add_btn(800,600,jessica_icon,"Jessica",12,60)
        self.menu.add_btn(600,600,steward_icon,"Steward",10,60)


    # METHODE: fait appel à toutes les fonctionnalités pour le bon fonctionnement du jeu
    def run(self):
        """
        Lancement du jeu
        """
        run = True
        clock = pygame.time.Clock()

        dp_gain = 0
        while run:
            #Vérifie si le chargement est terminée
            if self.loading_finish:

                # Initialisation du timer
                self.timer_game_duree = 5 * 60
                if self.game_started == False:
                    self.timer_start_ticks = pygame.time.get_ticks()
                    self.game_started = True

                # Temps écoulé depuis le début de la partie
                time_ecouler_secondes = (pygame.time.get_ticks() - self.timer_start_ticks) // 1000

                #Chaque seconde, gagne un point de déployement
                if int(time_ecouler_secondes)-dp_gain > 1:
                    self.dp += 1
                    dp_gain +=2

                pygame.display.set_caption('Arknight fps '+str(round(clock.get_fps(),0))) #change le nom de la fenêtre avec les fps

                # Vérifie si on bouge un object ou non
                if self.operateur_list.moving_object:
                    self.operateur_list.move_to_operateur()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        run = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if self.operateur_list.moving_object:
                                self.operateur_list.moving_object.moving = False
                                self.operateur_list.moving_object.remove()
                                self.operateur_list.moving_object = None
                    
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            # SI tu a cliqué et que tu bouge l'opérateur
                            self.operateur_list.move_and_click()
                        if event.button == 3:
                            if self.operateur_list.moving_object:
                                self.operateur_list.moving_object.moving = False
                                self.operateur_list.moving_object.remove()
                                self.operateur_list.moving_object = None
                
                # Spawn automatiquement les infectés de chaque waves selon le temps 
                if time_ecouler_secondes != 180:
                    if time_ecouler_secondes >= 130 and self.wave7_clear == False:
                        self.wave = 7
                        self.add_infected_in_spawn_list()  # remplis la liste d'infecté
                        self.wave7_clear = True
                    elif time_ecouler_secondes >= 120 and self.wave6_clear == False:
                        self.wave = 6
                        self.add_infected_in_spawn_list()  # remplis la liste d'infecté
                        self.wave6_clear = True
                    elif time_ecouler_secondes >= 100 and self.wave5_clear == False:
                        self.wave = 5
                        self.add_infected_in_spawn_list()  # remplis la liste d'infecté
                        self.wave5_clear = True
                    elif time_ecouler_secondes >= 80 and self.wave4_clear == False:
                        self.wave = 4
                        self.add_infected_in_spawn_list()  # remplis la liste d'infecté
                        self.wave4_clear = True
                    elif time_ecouler_secondes >= 50 and self.wave3_clear == False:
                        self.wave = 3
                        self.add_infected_in_spawn_list()  # remplis la liste d'infecté
                        self.wave3_clear = True
                    elif time_ecouler_secondes >= 30 and self.wave2_clear == False:
                        self.wave = 2
                        self.add_infected_in_spawn_list()  # remplis la liste d'infecté
                        self.wave2_clear = True
                    elif time_ecouler_secondes >= 10 and self.wave1_clear == False: 
                        self.wave = 1
                        self.add_infected_in_spawn_list()  # remplis la liste d'infecté
                        self.wave1_clear = True
                
                # Fait spawn automatiquement les infectés selon la liste d'infectés
                if pygame.time.get_ticks() - self.last_infected_spawn > SPAWN_Cooldown_infected:
                    if self.spawn_infected < len(self.infected_spawn_list):
                        enemy_type = self.infected_spawn_list[self.spawn_infected]
                        if enemy_type == "BOSS":
                            infected = Infected(enemy_type, infected_image, infected_waypoint[2])
                        else:
                            route = randint(0,1)
                            infected = Infected(enemy_type, infected_image, infected_waypoint[route])
                        infected_group.add(infected)
                        self.infected.append(infected)
                        self.spawn_infected += 1
                        self.last_infected_spawn = pygame.time.get_ticks()
                    else:
                        self.infected_spawn_list = []
                        self.spawn_infected = 0

                
                # Condition de lose
                if self.lives <= 0:
                    self.lose = True
                    
                    
                # Condition de win
                if len(infected_group) == 0 and time_ecouler_secondes >= 151:
                    self.win = True

                
                for enemy in self.infected:
                    if enemy.alive == False:
                        self.infected.remove(enemy)

                # Appel méthode pour faire fonctionner le jeu
                self.draw()
                self.collision_projectile_target()
                self.base_penetred()

            else:
                # Affiche la barre de chargement (pour les images) si le chargement n'est pas terminé
                load_img(self)
                self.operateur_list.update_operateur()

        pygame.quit()

    # METHODE: Dessine les différents éléments (infectés,projectiles,opérateur,time,dp,life)
    def draw(self):
        global band,band_2,band_3,text1, band_lose, band_win
        """
        Déssine les éléments du jeu
        """
        self.fenetre.blit(self.bg,(0,0))        
        self.fenetre.blit(band, (1075,20))

        
        #Calculer le temps restant (arrete le timer si win ou lose)
        time_ecouler_secondes = 0
        if self.win == False and self.lose == False:
            time_ecouler_secondes = (pygame.time.get_ticks() - self.timer_start_ticks) // 1000
        time_restant = self.timer_game_duree - time_ecouler_secondes
        minutes = time_restant // 60
        seconds = time_restant % 60

        
        # Afficher le timer
        if seconds < 10:
            timer_text = pygame.font.Font(None, 60).render(f"{minutes}:0{seconds}", True, (255, 255, 255))
        else:
            timer_text = pygame.font.Font(None, 60).render(f"{minutes}:{seconds}", True, (255,255,255))
        self.fenetre.blit(timer_text, (1084, 26))

         # Affiche l'emplacement de l'opérateur durant le déployement
        if self.operateur_list.moving_object:
            self.operateur_list.moving_object.draw_emplacement(self.fenetre)

        
        self.fenetre.blit(band_2, (50, 20))
        self.fenetre.blit(band_3, (1000, 580))

        text = self.life_font.render(str(self.dp), 1, (255, 255, 0)) # Dessine le nombre de dp
        
        self.fenetre.blit(text1, (1010, 585))
        self.fenetre.blit(text, (1045, 600))

        life = pygame.font.Font(None, 50).render(f"Life:{self.lives}/{3}", True, (255, 255, 255))
        self.fenetre.blit(life, (60, 29))

        # Ajoute les infectées dans le sprite des infectées
        infected_group.draw(self.fenetre)
        infected_group.update(self.fenetre)

        #Ajoute les projectiles dans le sprite des projectiles
        projectile_group.draw(self.fenetre)
        projectile_group.update()

        #dessiner les opérateurs et ses projectiles
        for op in self.operateur_list.operateurlist:
            op.attack(self.fenetre,self.infected)
            if infected_group:
                if op.deployed and op.fired :
                    projectile = Projectile(op.name,(op.x,op.y-20),op.first_enemy() ,projectile_image)
                    projectile_group.add(projectile)
                    self.last_projectile_spawn = pygame.time.get_ticks()

        #Dessine les boutons
        self.menu.draw(self.fenetre)

        
        # Afficher l'écran de défaite
        if self.lose == True:
            self.fenetre.blit(band_lose, (0, 325))
            self.fenetre.blit(self.lose_image, (self.lose_image_x, self.lose_image_y))
            self.fenetre.blit(text_lose,text_rect_lose)

        # Afficher l'écran de victoire
        if self.win == True:
            self.fenetre.blit(band_win, (0, 325))
            self.fenetre.blit(self.win_image, (self.win_image_x, self.win_image_y))
            self.fenetre.blit(text_win,text_rect_win)

        pygame.display.update()


    # Ajoute les infectés à invoqués du wave actuelle dans une liste
    def add_infected_in_spawn_list(self):
        infected = enemy_spawn_data[self.wave - 1] # Relève le dictionnaire contenant les infectés
        for enemy_type in infected: 
            infected_spawned = infected[enemy_type] # détermine le nombre d'infectés à faire spawn pour chaque type d'infecté
            for i in range(infected_spawned):  
                self.infected_spawn_list.append(enemy_type) # ajoute le nom des infectés à faire spawn dont la quantité de nom dépend de la variable [infected_spawned]


    # METHODE: détecte les collisions entre tous les projectile et leurs cibles (définit en tant qu'attribut)
    def collision_projectile_target(self):
        for projectile in projectile_group.sprites():
            projectile.detect_collision() # Appel methode: Detecte les collisions entre le projectile et sa cible
            if projectile.collide == True:
                projectile.target.lost_life(projectile.damage,projectile.type,projectile.penetration) # Appel methode: diminue les HP de l'infecté selon les stats du projectile 
                projectile.kill() # Supprime le projectile du sprite

    # METHODE: détecte si un infecté à pénétrer dans la base 
    def base_penetred(self):
        for infected in infected_group.sprites():
            # Si dans la base : diminue les points de vie du joueur
            if infected.position == (1200,258): 
                self.lives -= 1
                infected.in_final_waypoint = True


