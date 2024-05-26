import pygame
from operateur.operateur_haze import haze
from operateur.operateur_jessica import jessica
from operateur.operateur_typhon import typhon
from operateur.operateur_steward import steward
import numpy as np
import math


class Operateurlist:
    def __init__(self,main):

        self.main = main
        self.operateurlist = []
        self.name_list = ["Typhon", "Jessica","Haze","Steward"]

        self.moving_object = None
        self.valid_place = [(215, 367), (414, 351), (476, 237), (754, 432), (1057, 327), (1023, 443)]
        self.valid_place = np.array(self.valid_place)

        self.limite_operateur = 6
        self.selected_operateur = None


    def add_operateur(self,name):
        """
        Selectionne l'opérateur qu'on a choisi
        """
        try: #Choisir la class en question
            self.obj = self.operateurlist[self.name_list.index(name)]
            self.moving_object = self.obj
            self.obj.moving = True
        except Exception as e:
            print(str(e) + " NOT VALID NAME")
    
    def move_to_operateur(self):
        """
        Bouge l'opérateur selectionné pour suivre la sourie durant le déplacement"""
        pos = pygame.mouse.get_pos()
        self.moving_object.move(pos[0], pos[1])
        if self.point_to_line(self.moving_object): # Bouge l'opérateur pour suivre la sourie
            pos2 = self.valid_place[self.return_closest_point(self.moving_object)]
            self.moving_object.move(pos2[0]+5, pos2[1]-20) # Bouge l'opérateur pour suivre la sourie
        
        #Détecte si l'opérateur qu'on veut placé touche ou non un opérateur déjà déployée
        #Et change la couleur du cercle si vert ou rouge
        collide = False  
        for operateur in self.operateurlist:
            if operateur != self.moving_object:
                if operateur.collide(self.moving_object):
                    collide = True
                    operateur.place_color = (200, 0, 0, 100)
                    self.moving_object.place_color = (200, 0, 0, 100) #Rouge
                else: 
                    operateur.place_color = (50,205,50, 100) #Vert
                    if not collide:
                        self.moving_object.place_color = (50,205,50, 100)
                        if self.point_to_line(self.moving_object):
                            self.moving_object.place_color = (50,205,50, 100)
                        else:
                            self.moving_object.place_color = (200, 0, 0, 100)
                
    def point_to_line(self, operateur):
        """
        Regarde si on rapproche l'opérateur en movement à coté d'une casse valide ou non.
        """
        x_op = operateur.x
        y_op = operateur.y
        for x,y in self.valid_place:
            if math.sqrt((x_op-x)**2 + (y_op-y)**2) < 50:   
                return True
        return False

    
    def move_and_click(self):
        """
        Vérifie si on à appuyé sur un opérateur déjà déployé ou encore si on déplace déjà un opérateur.
        """
        pos = pygame.mouse.get_pos()
        if self.moving_object:
            not_allowed = False #Initialise le variable not_allowed
            for operateur in self.operateurlist:  
                if operateur != self.moving_object: #Vérifie si l'opérateur est bien celui qu'on a choisi
                    if operateur.collide(self.moving_object) :
                        not_allowed = True
            #Vérifie si on peut placer l'opérateur à l'emplacement qu'on veut
            if not not_allowed and self.point_to_line(self.moving_object):
                if self.moving_object.name in self.name_list: #Place l'opérateur
                    self.moving_object.placed = True
                    pos2 = self.valid_place[self.return_closest_point(self.moving_object)]
                    self.moving_object.move(pos2[0]+5, pos2[1]-20)
                    self.limite_operateur -= 1
                    self.main.dp -= self.cost

                #reset le variable moving_object
                self.moving_object.moving = False
                self.moving_object = None
        else:
            # Regarde si tu a appuyé sur l'icon d'un opérateur
            operator_menu = self.main.menu.get_clicked(pos[0], pos[1])
            if operator_menu:
                self.cost = self.main.menu.get_item_cost(operator_menu) 
                for op in self.operateurlist: 
                    if op.name == operator_menu:
                        if op.deployed:
                            pass #Fonction retirée
                        else:
                            if self.main.dp >= self.cost and not op.deployed and self.limite_operateur > 0: #Vérifie les conditions 
                                self.add_operateur(operator_menu)                                           #placer l'opérateur
            
            for operateur in self.operateurlist:
                if operateur.menu.skill_get_clicked(pos[0], pos[1],operateur.selected) == (operateur.name+"_skill"):
                    pass
                if operateur.menu.skill_get_clicked(pos[0], pos[1],operateur.selected) == (operateur.name+"_remove"):
                    self.main.dp += int(operateur.cost*0.5)
                    operateur.remove()
                    self.limite_operateur += 1
                    self.selected_operateur = None 
            
            # Regarde si tu a appuyé sur un opérateur déjà déployé ou non
            btn_clicked = None
            if self.selected_operateur:
                btn_clicked = self.selected_operateur.click(pos[0], pos[1])
                if btn_clicked:
                    self.selected_operateur.selected = True
            
            if not(btn_clicked):
                for op in self.operateurlist:
                    if op.click(pos[0], pos[1]):
                        op.selected = True
                        self.selected_operateur = op
                    else:
                        op.selected = False
    
    def return_closest_point(self,operateur):
        """
        Revoie les coordonnées du point valide le plus proche
        """
        distances = np.linalg.norm(self.valid_place-(operateur.x,operateur.y), axis=1)
        min_index = np.argmin(distances)
        return min_index

    
    def update_operateur(self):
        """
        Met à jour les images et coordonnées des opérateurs.
        """
        Typhon = typhon(100,100)
        Jessica = jessica(100,100)
        Haze = haze(100,100)
        Steward = steward(100,100)
        self.operateurlist = [Typhon,Jessica,Haze,Steward]