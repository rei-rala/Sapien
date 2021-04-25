# Import and initialize the pg library

import sys
import pygame as pg
from materiales.materials import *
from gral import *

pg.init()

# Set up the drawing window
SCREEN = pg.display.set_mode([WIDTH, HEIGHT])
# Window caption
pg.display.set_caption("Sapien")
# Sound effects
mouse_click = pg.mixer.Sound(s_click)
mouse_click.set_volume(0.1)
hover = pg.mixer.Sound(hover_option)
hover.set_volume(0.1)
# Timer capture
pg.time.set_timer(pg.USEREVENT, 1000)


# CLASS TEXT
class Text:
    def __init__(self, font_family=roboto_light, size=25, text='LOREM IPSUM', color=LETTERS, x_ax=position_x_center, y_ax=position_y_center):
        self.font_family = font_family
        self.size = size
        self.text = text
        self.color = color
        self.x_axis = x_ax
        self.y_axis = y_ax

    def __str__(self):
        return f'''
{__class__.__name__} '{self.text}':
Position= {self.x_axis, self.y_axis}
Format= FF({self.font_family}), Size {self.size}, Text "{self.text}", Text color {self.color}
'''

# BUTTON
class Button(Text):
    def __init__(self, font_family=roboto_regular, size=25, text='BTN IPSUM', color=LETTERS, x_ax=position_x_center, y_ax=position_y_center, btn_color=WHITE, btn_size=[200, 45], area=None):
        Text.__init__(self, font_family, size, text, color, x_ax, y_ax)
        self.btn_color = btn_color
        self.btn_size = btn_size
        self.area = area

    def __str__(self):
        return f'''
{__class__.__name__} '{self.text}':
Position= {self.x_axis, self.y_axis}
Format= FF({self.font_family}), Size {self.size}, Text color {self.color}
Button= Color{self.btn_color}, Size{self.btn_size}
'''

# ROUND-BUTTON
class Button_round(Text):
    def __init__(self, font_family=roboto_regular, size=30, text='BTN IPSUM', color=LETTERS, x_ax=position_x_center, y_ax=position_y_center, btn_color=WHITE, btn_size=[75, 75], area=None):
        Text.__init__(self, font_family, size, text, color, x_ax, y_ax)
        self.btn_color = btn_color
        self.btn_size = btn_size
        self.area = area

    def __str__(self):
        return f'''
{__class__.__name__} '{self.text}':
Position= {self.x_axis, self.y_axis}
Format= FF({self.font_family}), Size {self.size}, Text color {self.color}
Button= Color{self.btn_color}, Size{self.btn_size}
'''

def pg_blit(to_blit):
    text = pg.font.Font(to_blit.font_family, to_blit.size).render(
        to_blit.text, True, to_blit.color)
    text_rect = text.get_rect(center=(to_blit.x_axis, to_blit.y_axis))
    if type(to_blit) == Text:
        return SCREEN.blit(text, text_rect)
    elif type(to_blit) in (Button, Button_round):
        btn_self_center = [to_blit.x_axis-to_blit.btn_size[0] //
                           2, to_blit.y_axis-to_blit.btn_size[1]//2]
        def draw():
            if type(to_blit) == Button_round:
                pg.draw.rect(SCREEN, to_blit.btn_color, (
                    btn_self_center[0], btn_self_center[1], to_blit.btn_size[0], to_blit.btn_size[1]), border_radius=75)
                to_blit.area = [btn_self_center[0], btn_self_center[0]+to_blit.btn_size[0],
                                btn_self_center[1], btn_self_center[1]+to_blit.btn_size[1]]
            else:
                pg.draw.rect(SCREEN, to_blit.btn_color, (
                    btn_self_center[0], btn_self_center[1], to_blit.btn_size[0], to_blit.btn_size[1]), border_radius=15)
                to_blit.area = [btn_self_center[0], btn_self_center[0]+to_blit.btn_size[0],
                                btn_self_center[1], btn_self_center[1]+to_blit.btn_size[1]]
            SCREEN.blit(text, text_rect)
        return draw()

def in_area(quantity, objects, x, y):
    if quantity == 1:
        if x in range(objects.area[0], objects.area[1]) and y in range(objects.area[2], objects.area[3]):
            print(f'In area {objects.__str__()}')
            return True
    else:
        for object in objects:
            if x in range(object.area[0], object.area[1]) and y in range(object.area[2], object.area[3]):
                print(f'In area {object.__str__()}')
                return True


def set_rounds():
    nice_transition_bro = [
        Button_round(text='', btn_color=(125,125,125), btn_size=(WIDTH*1.05, HEIGHT*1.05)),
        Button_round(text='', btn_color=(110,110,110), btn_size=(WIDTH*0.95, HEIGHT*0.95)),
        Button_round(text='', btn_color=(105,105,105), btn_size=(WIDTH*0.90, HEIGHT*0.90)),
        Button_round(text='', btn_color=(95,95,95), btn_size=(WIDTH*0.85, HEIGHT*0.85)),
        Button_round(text='', btn_color=(82,82,82), btn_size=(WIDTH*0.80, HEIGHT*0.80)),
        Button_round(text='', btn_color=(71,71,71), btn_size=(WIDTH*0.75, HEIGHT*0.75)),
        Button_round(text='', btn_color=(61,61,61), btn_size=(WIDTH*0.70, HEIGHT*0.70)),
        Button_round(text='', btn_color=(53,53,53), btn_size=(WIDTH*0.65, HEIGHT*0.65)),
        Button_round(text='', btn_color=(46,46,46), btn_size=(WIDTH*0.60, HEIGHT*0.60)),
        Button_round(text='', btn_color=(40,40,40), btn_size=(WIDTH*0.55, HEIGHT*0.55)),
        Button_round(text='', btn_color=(34,34,34), btn_size=(WIDTH*0.50, HEIGHT*0.50)),
        Button_round(text='', btn_color=(29,29,29), btn_size=(WIDTH*0.45, HEIGHT*0.45)),
        Button_round(text='', btn_color=(25,25,25), btn_size=(WIDTH*0.40, HEIGHT*0.40)),
        Button_round(text='', btn_color=(21,21,21), btn_size=(WIDTH*0.35, HEIGHT*0.35)),
        Button_round(text='', btn_color=(18,18,18), btn_size=(WIDTH*0.30, HEIGHT*0.30)),
        Button_round(text='', btn_color=(15,15,15), btn_size=(WIDTH*0.25, HEIGHT*0.25)),
        Button_round(text='', btn_color=(13,13,13), btn_size=(WIDTH*0.20, HEIGHT*0.20)),
        Button_round(text='', btn_color=(11,11,11), btn_size=(WIDTH*0.15, HEIGHT*0.15)),
        Button_round(text='', btn_color=(9,9,9), btn_size=(WIDTH*0.10, HEIGHT*0.10)),
        Button_round(text='', btn_color=(7,7,7), btn_size=(WIDTH*0.05, HEIGHT*0.05)),
        Button_round(text='', btn_color=(0,0,0), btn_size=(0,0)),
    ]


    for each in nice_transition_bro:
        SCREEN.fill(BACKGROUND)
        pg_blit(each)

        time.sleep(0.025)
        pg.display.update()




def set_players():
    pg.display.flip()

    # NICE INTRO, BRO
    nice_intro_bro = [
        Button_round(text='', btn_color=(209,52,91), btn_size=(WIDTH*0.05, HEIGHT*0.05)),
        Button_round(text='', btn_color=(209,52,91), btn_size=(WIDTH*0.15, HEIGHT*0.15)),
        Button_round(text='', btn_color=(102,30,50), btn_size=(WIDTH*0.20, HEIGHT*0.20)),
        Button_round(text='', btn_color=(107,31,52), btn_size=(WIDTH*0.25, HEIGHT*0.25)),
        Button_round(text='', btn_color=(112,32,54), btn_size=(WIDTH*0.30, HEIGHT*0.30)),
        Button_round(text='', btn_color=(117,33,56), btn_size=(WIDTH*0.35, HEIGHT*0.35)),
        Button_round(text='', btn_color=(123,34,58), btn_size=(WIDTH*0.40, HEIGHT*0.40)),
        Button_round(text='', btn_color=(129,35,61), btn_size=(WIDTH*0.45, HEIGHT*0.45)),
        Button_round(text='', btn_color=(113,36,64), btn_size=(WIDTH*0.50, HEIGHT*0.50)),
        Button_round(text='', btn_color=(142,37,67), btn_size=(WIDTH*0.55, HEIGHT*0.55)),
        Button_round(text='', btn_color=(149,40,70), btn_size=(WIDTH*0.60, HEIGHT*0.60)),
        Button_round(text='', btn_color=(156,42,73), btn_size=(WIDTH*0.65, HEIGHT*0.65)),
        Button_round(text='', btn_color=(164,44,76), btn_size=(WIDTH*0.70, HEIGHT*0.70)),
        Button_round(text='', btn_color=(172,46,79), btn_size=(WIDTH*0.75, HEIGHT*0.75)),
        Button_round(text='', btn_color=(181,48,83), btn_size=(WIDTH*0.80, HEIGHT*0.80)),
        Button_round(text='', btn_color=(191,50,87), btn_size=(WIDTH*0.85, HEIGHT*0.85)),
        Button_round(text='', btn_color=(200,52,91), btn_size=(WIDTH*0.90, HEIGHT*0.90)),
        Button_round(text='', btn_color=RED, btn_size=(WIDTH*0.95, HEIGHT*0.95)),
        Button(text='', btn_color=RED, btn_size=(WIDTH, HEIGHT)),        
    ]

    for _ in nice_intro_bro:
        pg_blit(_)
        time.sleep(0.025)
        pg.display.update()

    pg.display.flip()
    SCREEN.fill(RED)
    pg.display.update()

    players_mesagge = [
    Text(text='Sapien', font_family=permanentmarker, size=30, color=LETTERS, x_ax=position_x_dot10-20, y_ax=position_y_dot10-20),
    Text(text='Seleccione cantidad de jugadores', font_family=roboto_regular, size=40, color=BACKGROUND, y_ax=position_y_quarter1-20),
    Text(text='Utilice las esferas a continuacion', font_family=roboto_light, size=30, color=BACKGROUND, y_ax=position_y_dot40)
    ]

    for each in players_mesagge:
        pg_blit(each)

    time.sleep(5)
    set_rounds()


def info():
    pg.display.flip()
    SCREEN.fill(BACKGROUND)

    second = 0
    game_info = Button(font_family=roboto_regular, btn_color=BLUE, btn_size=[
                       WIDTH*0.95, HEIGHT*0.95], text='')
    title = Text(font_family=roboto_light_italic, size=50,
                 color=WHITE, text='Sapien,', y_ax=position_y_quarter1-50)
    lines = [
        'Sapien es un juego matematico multijugador en el cual se les',
        'presentaran diferentes operaciones matematicas para las cuales',
        'tendras opciones para responder, ganara el jugador que mayor',
        'numero de puntos posea.',
        'Nota: Los errores quitan puntos'
    ]

    _continue = Button(text='Okay', color=BLACK,
                       btn_color=GREEN, y_ax=position_y_quarter3+50)

    for each in (game_info, title, _continue):
        pg_blit(each)

    line_pos = HEIGHT//3-15
    for i in range(len(lines)):
        i = Text(size=30, text=lines[i], color=BACKGROUND, y_ax=line_pos)
        line_pos += 50
        pg_blit(i)

    pg.display.update()

    run = True
    while run:
        for event in pg.event.get():
            rel_x, rel_y = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEMOTION and second % 1 == 0:
                if second % 2 == 0 and in_area(1, (_continue), rel_x, rel_y):
                    print(f'Mouse moved X={rel_x}  Y={rel_y}')
                    time.sleep(0.25)
                    run = False
                    set_players()
            elif event.type == pg.MOUSEBUTTONDOWN and second % 0.5 == 0:
                if second % 1 == 0 and in_area(1, (_continue), rel_x, rel_y):
                    print(f'Clicked X={rel_x}  Y={rel_y}')
                    hover.play()
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    print(f'{second} seconds have elapsed in main screen')

def main_screen():
    SCREEN.fill(BACKGROUND)
    welcome = Text(text='Sapien', font_family=permanentmarker,
                   size=140, color=BLUE, y_ax=position_y_quarter1)
    game_btn = Button(text='New Game', color=BLACK, btn_color=GREEN,
                      x_ax=position_x_quarter1, y_ax=position_y_quarter3)
    quit_btn = Button(text='Quit Game', color=WHITE, btn_color=RED,
                      x_ax=position_x_quarter3, y_ax=position_y_quarter3)
    first_roundbtn = Button_round(text='69', btn_color=BLUE, color=BACKGROUND)

    for i in (welcome, game_btn, quit_btn, first_roundbtn):
        pg_blit(i)
    pg.display.update()

    second = 0
    while True:
        for event in pg.event.get():
            rel_x, rel_y = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEMOTION and second % 1 == 0:
                if second % 2 == 0 and in_area(2, (game_btn, quit_btn), rel_x, rel_y):
                    print(f'Mouse moved X={rel_x}  Y={rel_y}')
                    time.sleep(0.25)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if second % 0.5 == 0 and in_area(1, (game_btn), rel_x, rel_y):
                    print(f'Clicked X={rel_x}  Y={rel_y}')
                    if in_area(1, (game_btn), rel_x, rel_y):
                        hover.play()
                        time.sleep(0.1)
                        info()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if second % 0.5 == 0 and in_area(1, (quit_btn), rel_x, rel_y):
                    print(f'Clicked X={rel_x}  Y={rel_y}')
                    if in_area(1, (quit_btn), rel_x, rel_y):
                        hover.play()
                        time.sleep(0.1)
                        sys.exit()
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    print(f'{second} seconds have elapsed in main screen')
            elif event.type == pg.KEYDOWN and event.key == ord('q'):
                print(f'Quitted by pressing "{chr(event.key)}"')
                sys.exit()


if __name__ == '__main__':
    main_screen()

# Quit after everything...
pg.quit()
sys.exit()
