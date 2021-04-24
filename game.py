# Import and initialize the pg library
import pygame as pg
import time

def countdown(seconds):
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)

# FRAMES PER SECOND
FPS = 45

# COLORS, RGB
BACKGROUND = (239, 239, 239)
LETTERS = (7, 7, 7)

WHITE = (255, 255, 255)
BLACK = (0,0,0)

RED = (209, 52, 91)
GREEN = (0, 255, 255)
BLUE = (52, 84, 209)

LIGHTBLUE = (52, 209, 191)

WRONG_COLOR = (2204, 153, 141)
RIGHT_COLOR = (22, 244, 208)


 # FONTS
roboto_light_italic = './materiales/fonts/Roboto-LightItalic.ttf'
roboto_light = './materiales/fonts/Roboto-Light.ttf'
permanentmarker = './materiales/fonts/PermanentMarker-Regular.ttf'

# WINDOW
WIDTH = 960
HEIGHT = 540

# POSITIONING
center_x = WIDTH//2
center_y = HEIGHT//2
quarter_x_1 =  WIDTH//4
quarter_x_3 =  WIDTH//4*3
quarter_y_1 = HEIGHT//4
quarter_y_3 = HEIGHT//4*3


# FLIP ACTUALIZA TODA LA PANTALLA
#pg.display.flip()
# UPDATE PERMITE ACTUALIZAR DE A SEGMENTOS
#pg.display.update()


def main():
    pg.init()
    
    # PYGAME INTERNAL CLOCK
    clock = pg.time.Clock()
    
    # Set up the drawing window
    SCREEN = pg.display.set_mode([WIDTH, HEIGHT])

    # Nombre de la ventana
    pg.display.set_caption("Sapien")
    


    # CLASS TEXT
    class Text:
        def __init__(self, font_family=roboto_light, size=25, text='LOREM IPSUM', color=LETTERS, x_axis=center_x, y_axis=center_y):
            self.font_family = font_family
            self.size = size
            self.text = text
            self.color = color
            text = pg.font.Font(self.font_family, self.size).render(self.text, True,self.color)
            text_rect = text.get_rect(center=(x_axis, y_axis))
            SCREEN.blit(text, text_rect)

    
    # BUTTON
    class Button(Text):
        def __init__(self, font_family=roboto_light, size=25, text='BTN IPSUM', color=LETTERS ,x_axis=center_x, y_axis=center_y, btn_color=WHITE, btn_size=[200,45]):
            btn_x_axis = x_axis-btn_size[0]//2
            btn_y_axis = y_axis-btn_size[1]//2
            
            Text.__init__(self, font_family, size, text, color)
            text = pg.font.Font(self.font_family, self.size).render(self.text, True,self.color)
            text_rect = text.get_rect(center=(x_axis, y_axis))



            pg.draw.rect(SCREEN, btn_color,(btn_x_axis, btn_y_axis, btn_size[0], btn_size[1]), border_radius=15)
            SCREEN.blit(text, text_rect)
        


    poop=True
    # Welcome Screen
    while (poop):
        def main_screen():
            SCREEN.fill(BACKGROUND)
            welcome = Text(text='Sapien', font_family=permanentmarker, size=120, color=BLUE,y_axis=quarter_y_1)

            game_btn = Button(text='New Game',)
            #game_btn.SHOW_BUTTON(btn_size=[150,45], x_axis=quarter_x_1+100, y_axis=quarter_y_3, btn_color=LIGHTBLUE)

            quit_btn = Button(text='Quit game')
            #quit_btn.SHOW_BUTTON(btn_size=[150,45], x_axis=quarter_x_3-100, y_axis=quarter_y_3, btn_color=RED, behaviour='quit')
            
            
            pg.display.update()
            countdown(3)
        poop=False
            
            #if ev.type == pg.MOUSEBUTTONDOWN:              
            #    #if the mouse is clicked on the
            #    # button the game is terminated
            #    if x_axis=quarter_x_1+100 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            #        pg.quit()


    def new_screen():
        pg.display.flip()
        SCREEN.fill(BLACK)
        print('Aqui en NEW_SCREEN()')
        pg.display.update()
    
    
    main_screen()
    new_screen()







    # Run until the user asks to quit
    running = True
    while running:
        clock.tick(FPS)
        # STOP RUNNING IF USER QUITS THE PROGRAM
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()

    
    # Done! Time to quit.
        # break


pg.quit()

if __name__ == '__main__':
    main()
