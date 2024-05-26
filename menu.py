import pygame


class Button:
    def __init__(self,menu, x, y, img, name, cost, cd):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.menu = menu
        self.cd = cd
        self.cost = cost

    def click(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, fenetre):
        fenetre.blit(self.img, (self.x, self.y))

    def update(self):   
        self.x = self.menu.x - 50
        self.y = self.menu.y - 110

class Menu:
    def __init__(self):
        self.buttons = []
        self.items = 0

    def add_btn(self,x,y, img, name, cost,cd):
        self.items += 1
        btn_x = x
        btn_y = y
        self.buttons.append(Button(self, btn_x, btn_y, img, name, cost,cd))

    def draw(self, fenetre):
        for item in self.buttons:
                item.draw(fenetre)

    def get_clicked(self, X, Y):
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name
        return None
    
    def skill_get_clicked(self, X, Y,selected):
        if selected:
            for btn in self.buttons:
                if btn.click(X,Y):
                    return btn.name
        return None

    def get_item_cost(self, name):
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1
    
    def update(self,name):
        for btn in self.buttons:
            if btn.name == name+"_skill":
                btn.update()
            if btn.name == name+"_remove":
                btn.update()
        return -1
    

