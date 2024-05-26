import pygame

if __name__ == "__main__":
    pygame.init()
    #Paramètre du jeu
    width =1200
    height =700
    fenetre = pygame.display.set_mode((1200, 700))
    from main_menu import MainMenu
    mainMenu = MainMenu(fenetre)
    mainMenu.run()