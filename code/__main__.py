import pygame
from sys import exit
from basic_file_info import *

pygame.init()
main_menu = False
menu_command = 0


class Button:
    def __init__(self, txt, pos, len_dik, image=False):
        self.text = txt
        self.pos = pos
        self.len_dik = len_dik
        self.image = image
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (self.len_dik[0], self.len_dik[1]))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], self.len_dik[0], self.len_dik[1]], 5, 5)
        if self.image:
            self.image = pygame.image.load('C:\\pokemon_game\\venv\\Scripts\\venv\\pokemon_v0\\graphics\\menu\\frontpage.png').convert()
            self.image = pygame.transform.scale(screen, (self.len_dik[0], self.len_dik[1])) # dit nog bekijken
            # screen.blit(self.image, (self.pos[0], self.pos[1])) # dit werkt nog niet
        else:
            self.text = smallfont.render(self.text, True, 'black')
            screen.blit(self.text, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def draw_menu():
    
    command = -1
    pygame.draw.rect(screen, 'black', [100, 100, 300, 300])
    pygame.draw.rect(screen, 'green', [100, 100, 300, 300], 5)
    pygame.draw.rect(screen, 'white', [120, 120, 260, 40], 0, 5)
    pygame.draw.rect(screen, 'gray', [120, 120, 260, 40], 5, 5)
    txt = smallfont.render('Menus Tutorial!', True, 'black')
    screen.blit(txt, (135, 127))
    # menu exit button
    menu = Button('Exit Menu', (120, 350))
    menu.draw()
    button1 = Button('Button 1', (120, 180))
    button1.draw()
    button2 = Button('Button 2', (120, 240))
    button2.draw()
    button3 = Button('Button 3', (120, 300))
    button3.draw()
    if menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command

    

def draw_game():
    menu_btn = Button('Main Menu', (600, 10), (190, 50), False)
    menu_btn.draw()
    menu = menu_btn.check_clicked()
    return menu

def load_game():
    screen.fill('yellow')






# building the screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pokemon 2023')
clock = pygame.time.Clock()

# stores the width of the
# screen into a variable
width = screen.get_width()
# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# front page image
menu_surf = pygame.image.load('C:\\pokemon_game\\venv\\Scripts\\venv\\pokemon_v0\\graphics\\menu\\frontpage.png').convert()
menu_surf = pygame.transform.scale(menu_surf, (int(width), int(height+50)))



# making states to see
game_state = False






# player_surf = pygame.image.load('C:\\pokemon_game\\venv\\Scripts\\venv\\BASICS_PYGAME\\UltimatePygameIntro-main\\graphics\\Player\\player_walk_1.png').convert_alpha()
# draws a rectangle around the image. it makes it possible to
# pinpoint the drawing from any point of the rectangle
# player_rect = player_surf.get_rect(midbottom = (80,300))



# building a loop to run the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
                    


                
    
    
    clock.tick(60)


    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command > 0:
            text = smallfont.render(f'Button {menu_command} pressed!', True, 'black')
            screen.blit(text, (150, 100))



      


    pygame.display.update()
   


