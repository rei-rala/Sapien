# Import and initialize the pg library

import sys
import pygame as pg
from materiales.materials import *
from gral import *
from string import ascii_letters

ord_ascii_letters = list()
for l in ascii_letters:
    ord_ascii_letters.append(ord(l)) 
ord_ascii_letters.append(32)

# pygame start
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
checkmark = pg.mixer.Sound(checkmark)
checkmark.set_volume(0.1)

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
    def __init__(self, font_family=roboto_regular, size=25, text='BTN IPSUM', color=LETTERS, x_ax=position_x_center, y_ax=position_y_center, btn_color=WHITE, btn_size=[200, 45], area=None, value=None):
        Text.__init__(self, font_family, size, text, color, x_ax, y_ax)
        self.btn_color = btn_color
        self.btn_size = btn_size
        self.area = area
        self.value = value

    def __str__(self):
        return f'''
{__class__.__name__} '{self.text}':
Position= {self.x_axis, self.y_axis}
Format= FF({self.font_family}), Size {self.size}, Text color {self.color}
Button= Color{self.btn_color}, Size{self.btn_size}
'''

# ROUND-BUTTON
class Button_round(Text):
    def __init__(self, font_family=roboto_regular, size=30, text='BTN IPSUM', color=LETTERS, x_ax=position_x_center, y_ax=position_y_center, btn_color=WHITE, btn_size=[75, 75], area=None, value=None):
        Text.__init__(self, font_family, size, text, color, x_ax, y_ax)
        self.btn_color = btn_color
        self.btn_size = btn_size
        self.area = area
        self.value = value

    def __str__(self):
        return f'''
{__class__.__name__} '{self.text}':
Position= {self.x_axis, self.y_axis}
Format= FF({self.font_family}), Size {self.size}, Text color {self.color}
Button= Color{self.btn_color}, Size{self.btn_size}
'''

# blit to screen (show)
def pg_blit(to_blit):
    text = pg.font.Font(to_blit.font_family, to_blit.size).render(to_blit.text, True, to_blit.color)
    text_rect = text.get_rect(center=(to_blit.x_axis, to_blit.y_axis))
    # IF ITS A TEXT, IT WILL ONLY BLIT TEXT
    if type(to_blit) == Text:
        return SCREEN.blit(text, text_rect)
    elif type(to_blit) in (Button, Button_round):
        btn_self_center = [to_blit.x_axis-to_blit.btn_size[0] // 2, to_blit.y_axis-to_blit.btn_size[1]//2]
        def draw():
            # DRAWS A FIGURE ACCORDING TO THE CLASS INPUT
            if type(to_blit) == Button_round:
                pg.draw.rect(SCREEN, to_blit.btn_color, (btn_self_center[0], btn_self_center[1], to_blit.btn_size[0], to_blit.btn_size[1]), border_radius=75)
                to_blit.area = [btn_self_center[0], btn_self_center[0]+to_blit.btn_size[0],btn_self_center[1], btn_self_center[1]+to_blit.btn_size[1]]
            elif type(to_blit) == Button:
                pg.draw.rect(SCREEN, to_blit.btn_color, (btn_self_center[0], btn_self_center[1], to_blit.btn_size[0], to_blit.btn_size[1]), border_radius=15)
                to_blit.area = [btn_self_center[0], btn_self_center[0]+to_blit.btn_size[0], btn_self_center[1], btn_self_center[1]+to_blit.btn_size[1]]
            # THIS SCREEN.BLIT GOES AFTER EACH FIGURE IS DRAWN
            SCREEN.blit(text, text_rect)
        return draw()

# Screen animation between opctions
def screen_animation(type='OUT', color_from=BACKGROUND, color_target=BLACK, speed=0.015):
    animation_in = [
        Button_round(text='', btn_color=(color_target[0]*0.10, color_target[1]*0.10, color_target[2]*0.10), btn_size=(WIDTH*0.05, HEIGHT*0.05)),
        Button_round(text='', btn_color=(color_target[0]*0.15, color_target[1]*0.15, color_target[2]*0.15), btn_size=(WIDTH*0.15, HEIGHT*0.15)),
        Button_round(text='', btn_color=(color_target[0]*0.20, color_target[1]*0.20, color_target[2]*0.20), btn_size=(WIDTH*0.20, HEIGHT*0.20)),
        Button_round(text='', btn_color=(color_target[0]*0.25, color_target[1]*0.25, color_target[2]*0.25), btn_size=(WIDTH*0.25, HEIGHT*0.25)),
        Button_round(text='', btn_color=(color_target[0]*0.30, color_target[1]*0.30, color_target[2]*0.30), btn_size=(WIDTH*0.30, HEIGHT*0.30)),
        Button_round(text='', btn_color=(color_target[0]*0.35, color_target[1]*0.35, color_target[2]*0.35), btn_size=(WIDTH*0.35, HEIGHT*0.35)),
        Button_round(text='', btn_color=(color_target[0]*0.40, color_target[1]*0.40, color_target[2]*0.40), btn_size=(WIDTH*0.40, HEIGHT*0.40)),
        Button_round(text='', btn_color=(color_target[0]*0.45, color_target[1]*0.45, color_target[2]*0.45), btn_size=(WIDTH*0.45, HEIGHT*0.45)),
        Button_round(text='', btn_color=(color_target[0]*0.50, color_target[1]*0.50, color_target[2]*0.50), btn_size=(WIDTH*0.50, HEIGHT*0.50)),
        Button_round(text='', btn_color=(color_target[0]*0.55, color_target[1]*0.55, color_target[2]*0.55), btn_size=(WIDTH*0.55, HEIGHT*0.55)),
        Button_round(text='', btn_color=(color_target[0]*0.60, color_target[1]*0.60, color_target[2]*0.60), btn_size=(WIDTH*0.60, HEIGHT*0.60)),
        Button_round(text='', btn_color=(color_target[0]*0.65, color_target[1]*0.65, color_target[2]*0.65), btn_size=(WIDTH*0.65, HEIGHT*0.65)),
        Button_round(text='', btn_color=(color_target[0]*0.70, color_target[1]*0.70, color_target[2]*0.70), btn_size=(WIDTH*0.70, HEIGHT*0.70)),
        Button_round(text='', btn_color=(color_target[0]*0.75, color_target[1]*0.75, color_target[2]*0.75), btn_size=(WIDTH*0.75, HEIGHT*0.75)),
        Button_round(text='', btn_color=(color_target[0]*0.80, color_target[1]*0.80, color_target[2]*0.80), btn_size=(WIDTH*0.80, HEIGHT*0.80)),
        Button_round(text='', btn_color=(color_target[0]*0.85, color_target[1]*0.85, color_target[2]*0.85), btn_size=(WIDTH*0.85, HEIGHT*0.85)),
        Button_round(text='', btn_color=(color_target[0]*0.90, color_target[1]*0.90, color_target[2]*0.90), btn_size=(WIDTH*0.90, HEIGHT*0.90)),
        Button_round(text='', btn_color=color_target, btn_size=(WIDTH*0.95, HEIGHT*0.95)),
        Button_round(text='', btn_color=color_target, btn_size=(WIDTH, HEIGHT))        
    ]
    animation_out = [
        Button_round(text='', btn_color=(color_from[0]*1.00, color_from[1]*1.00, color_from[2]*1.00), btn_size=(WIDTH*1.05, HEIGHT*1.05)),
        Button_round(text='', btn_color=(color_from[0]*0.95, color_from[1]*0.95, color_from[2]*0.95), btn_size=(WIDTH*0.95, HEIGHT*0.95)),
        Button_round(text='', btn_color=(color_from[0]*0.90, color_from[1]*0.90, color_from[2]*0.90), btn_size=(WIDTH*0.90, HEIGHT*0.90)),
        Button_round(text='', btn_color=(color_from[0]*0.85, color_from[1]*0.85, color_from[2]*0.85), btn_size=(WIDTH*0.85, HEIGHT*0.85)),
        Button_round(text='', btn_color=(color_from[0]*0.80, color_from[1]*0.80, color_from[2]*0.80), btn_size=(WIDTH*0.80, HEIGHT*0.80)),
        Button_round(text='', btn_color=(color_from[0]*0.75, color_from[1]*0.75, color_from[2]*0.75), btn_size=(WIDTH*0.75, HEIGHT*0.75)),
        Button_round(text='', btn_color=(color_from[0]*0.70, color_from[1]*0.70, color_from[2]*0.70), btn_size=(WIDTH*0.70, HEIGHT*0.70)),
        Button_round(text='', btn_color=(color_from[0]*0.65, color_from[1]*0.65, color_from[2]*0.65), btn_size=(WIDTH*0.65, HEIGHT*0.65)),
        Button_round(text='', btn_color=(color_from[0]*0.60, color_from[1]*0.60, color_from[2]*0.60), btn_size=(WIDTH*0.60, HEIGHT*0.60)),
        Button_round(text='', btn_color=(color_from[0]*0.55, color_from[1]*0.55, color_from[2]*0.55), btn_size=(WIDTH*0.55, HEIGHT*0.55)),
        Button_round(text='', btn_color=(color_from[0]*0.50, color_from[1]*0.50, color_from[2]*0.50), btn_size=(WIDTH*0.50, HEIGHT*0.50)),
        Button_round(text='', btn_color=(color_from[0]*0.45, color_from[1]*0.45, color_from[2]*0.45), btn_size=(WIDTH*0.45, HEIGHT*0.45)),
        Button_round(text='', btn_color=(color_from[0]*0.40, color_from[1]*0.40, color_from[2]*0.40), btn_size=(WIDTH*0.40, HEIGHT*0.40)),
        Button_round(text='', btn_color=(color_from[0]*0.35, color_from[1]*0.35, color_from[2]*0.35), btn_size=(WIDTH*0.35, HEIGHT*0.35)),
        Button_round(text='', btn_color=(color_from[0]*0.30, color_from[1]*0.30, color_from[2]*0.30), btn_size=(WIDTH*0.30, HEIGHT*0.30)),
        Button_round(text='', btn_color=(color_from[0]*0.25, color_from[1]*0.25, color_from[2]*0.25), btn_size=(WIDTH*0.25, HEIGHT*0.25)),
        Button_round(text='', btn_color=(color_from[0]*0.20, color_from[1]*0.20, color_from[2]*0.20), btn_size=(WIDTH*0.20, HEIGHT*0.20)),
        Button_round(text='', btn_color=(color_from[0]*0.15, color_from[1]*0.15, color_from[2]*0.15), btn_size=(WIDTH*0.15, HEIGHT*0.15)),
        Button_round(text='', btn_color=(color_from[0]*0.10, color_from[1]*0.10, color_from[2]*0.10), btn_size=(WIDTH*0.10, HEIGHT*0.10)),
        Button_round(text='', btn_color=(color_from[0]*0.05, color_from[1]*0.05, color_from[2]*0.05), btn_size=(WIDTH*0.05, HEIGHT*0.05)),
        Button_round(text='', btn_color=(color_from[0]*0.00, color_from[1]*0.00, color_from[2]*0.00), btn_size=(0,0)),
    ]

    if type == 'IN':
        for i in animation_in:
            pg_blit(i)
            time.sleep(speed)
            pg.display.update()
    elif type == 'OUT':
        for i in animation_out:
            SCREEN.fill(color_target)
            pg_blit(i)
            time.sleep(speed)
            pg.display.update()
    return pg.display.update()

# THIS FUNCTION CHECKS IF THE MOUSE IS IN THE AREA OF OBJECT, QUANTITY ARGUMENT IS FOR THE COUNT, OBJECTS ARGUMENT MUST BE A LIST OF OBJECTS
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

# -------------------- Game instructions -----------------------------

def player_names():
    pg.display.flip()
    player_name = list()
    player_name.append('')
    print(player_name)
    
    def name_refresh(index, key, action):
        if action == 'add':
            player_name[index] += key
            print(player_name[index])
        elif action == 'backspace':
            player_name[index] = player_name[index][0:len(player_name[index])-1]
            print(player_name[index])
    
    for i in range(0,2):
        player_names_running = True
        player_name.append('')
    #    pg.SCREEN(BACKGROUND)
        while player_names_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key== 8 and len(player_name[i]) != 0:
                    key = chr(event.key)
                    name_refresh(i, key, 'backspace')
                elif event.type == pg.KEYDOWN and event.key in ord_ascii_letters:
                    key = chr(event.key)
                    name_refresh(i, key, 'add')
                elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and len(player_name) != 0:
                    player_created = Jugador(player_name[i])
                    PLAYER_LIST.append(player_created)
                    print(PLAYER_LIST)
                    player_names_running = False
            continue

def countdown_animation(seconds_animation=3):
    target_screen = (BLUE, BLACK, (119,136,153), WHITE)
    letters = (WHITE, BLACK, BLACK)
    
    for i in range(seconds_animation):
        screen_animation(color_from=target_screen[i], color_target=target_screen[i+1], speed=0.01)
        
        pg_blit( Text(text=str(-i+3), font_family=permanentmarker, size=180+i*100, color=letters[i] ))
        pg.display.update()
        time.sleep(1)
    player_names()  

def set_rounds():
    pg.display.flip()
    # NICE TRANSITION, BRO
    screen_animation(type='OUT', color_from=RED, color_target=BLUE, speed=0.015)
    
    sapien_title = Text(text='Sapien', font_family=permanentmarker, size=25, color=BLACK, x_ax=position_x_dot10, y_ax=position_y_dot10)
    choose_playerst1 = Text(text='Selecciona la cantidad de rounds', font_family=roboto_regular, size=35, color=BACKGROUND, y_ax=position_y_quarter1)
    choose_playerst2 = Text(text='Utilice las esferas debajo', font_family=roboto_light_italic, size=25, color=BACKGROUND, y_ax=position_y_dot40)
    choose_1 = Button_round(text='1', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot20, y_ax=position_y_dot60, value=1)
    choose_2 = Button_round(text='2', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot40, y_ax=position_y_dot60, value=2)
    choose_3 = Button_round(text='3', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot60, y_ax=position_y_dot60, value=3)
    choose_4 = Button_round(text='4', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot80, y_ax=position_y_dot60, value=4)
    choose_5 = Button_round(text='5', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot20, y_ax=position_y_dot80, value=5)
    choose_6 = Button_round(text='6', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot40, y_ax=position_y_dot80, value=6)
    choose_7 = Button_round(text='7', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot60, y_ax=position_y_dot80, value=7)
    choose_8 = Button_round(text='8', color=BLACK, btn_color=BACKGROUND, x_ax=position_x_dot80, y_ax=position_y_dot80, value=8)

    for i in (sapien_title,choose_playerst1, choose_playerst2, choose_1, choose_2, choose_3, choose_4, choose_5, choose_6, choose_7, choose_8):
        pg_blit(i)
    pg.display.update()
    second = 0
    set_rounds_running = True
    while set_rounds_running:
        for event in pg.event.get():
            rel_x, rel_y = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEMOTION and in_area(8, (choose_1, choose_2, choose_3, choose_4, choose_5, choose_6, choose_7, choose_8), rel_x, rel_y):
                if second % 2 == 0:
                    print(f'Mouse moved X={rel_x}  Y={rel_y}')
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(8, (choose_1, choose_2, choose_3, choose_4, choose_5, choose_6, choose_7, choose_8), rel_x, rel_y):
                    print(f'Clicked! X={rel_x}, Y={rel_y}')
                    checkmark.play()
                    time.sleep(0.1)

                    def choose_rounds(button_class):
                        cant_rounds.append(button_class.value)
                        print(f'Cantidad de rounds: {cant_rounds}')

                    if in_area(1, (choose_1), rel_x, rel_y): print('JUGADORES 1'), choose_rounds(choose_1)
                    elif in_area(1, (choose_2), rel_x, rel_y): print('JUGADORES 2'), choose_rounds(choose_2)
                    elif in_area(1, (choose_3), rel_x, rel_y): print('JUGADORES 3'), choose_rounds(choose_3)
                    elif in_area(1, (choose_4), rel_x, rel_y): print('JUGADORES 4'), choose_rounds(choose_4)
                    elif in_area(1, (choose_5), rel_x, rel_y): print('JUGADORES 5'), choose_rounds(choose_5)
                    elif in_area(1, (choose_6), rel_x, rel_y): print('JUGADORES 6'), choose_rounds(choose_6)
                    elif in_area(1, (choose_7), rel_x, rel_y): print('JUGADORES 7'), choose_rounds(choose_7)
                    elif in_area(1, (choose_8), rel_x, rel_y): print('JUGADORES 8'), choose_rounds(choose_8)


                    set_rounds_running = False
                    countdown_animation()
                    
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    print(f'{second} seconds have elapsed in main screen')
            elif event.type == pg.KEYDOWN and event.key == ord('q'):
                print(f'Quitted by pressing "{chr(event.key)}"')
                sys.exit()


def set_players():
    pg.display.flip()
    # NICE TRANSITION, BRO
    screen_animation(type='IN', color_from=WHITE, color_target=RED, speed=0.015)

    sapien_title = Text(text='Sapien', font_family=permanentmarker, size=25, color=BLACK, x_ax=position_x_dot10, y_ax=position_y_dot10)
    choose_playerst1 = Text(text='Selecciona la cantidad de jugadores', font_family=roboto_regular, size=35, color=BLACK, y_ax=position_y_quarter1)
    choose_playerst2 = Text(text='Utilice las esferas debajo', font_family=roboto_light_italic, size=25, color=BLACK, y_ax=position_y_dot40)
    choose_1 = Button_round(text='1', color=BACKGROUND, btn_color=BLACK, x_ax=position_x_dot20, y_ax=position_y_dot70, value=1)
    choose_2 = Button_round(text='2', color=BACKGROUND, btn_color=BLACK, x_ax=position_x_dot40, y_ax=position_y_dot70, value=2)
    choose_3 = Button_round(text='3', color=BACKGROUND, btn_color=BLACK, x_ax=position_x_dot60, y_ax=position_y_dot70, value=3)
    choose_4 = Button_round(text='4', color=BACKGROUND, btn_color=BLACK, x_ax=position_x_dot80, y_ax=position_y_dot70, value=4)

    for i in (sapien_title,choose_playerst1, choose_playerst2, choose_1, choose_2, choose_3, choose_4):
        pg_blit(i)
    pg.display.update()

    second = 0
    set_players_running = True
    while set_players_running:
        for event in pg.event.get():
            rel_x, rel_y = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEMOTION and in_area(4, (choose_1, choose_2, choose_3, choose_4), rel_x, rel_y):
                if second % 2 == 0:
                    print(f'Mouse moved X={rel_x}  Y={rel_y}')
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(4, (choose_1, choose_2, choose_3, choose_4), rel_x, rel_y):
                    print(f'Clicked! X={rel_x}, Y={rel_y}')
                    checkmark.play()
                    time.sleep(0.1)

                    def choose_players(button_class):
                        cant_jugadores.append(button_class.value)
                        print(cant_jugadores)

                    if in_area(1, (choose_1), rel_x, rel_y): print('JUGADORES 1'), choose_players(choose_1)
                    elif in_area(1, (choose_2), rel_x, rel_y): print('JUGADORES 2'), choose_players(choose_2)
                    elif in_area(1, (choose_3), rel_x, rel_y): print('JUGADORES 3'), choose_players(choose_3)
                    elif in_area(1, (choose_4), rel_x, rel_y): print('JUGADORES 4'), choose_players(choose_4)

                    set_players_running = False
                    set_rounds()
                    
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    print(f'{second} seconds have elapsed in main screen')
            elif event.type == pg.KEYDOWN and event.key == ord('q'):
                print(f'Quitted by pressing "{chr(event.key)}"')
                sys.exit()


def info():
    pg.display.flip()
    screen_animation(type='IN', color_target=BLUE)
    SCREEN.fill(BACKGROUND)

    second = 0
    game_info = Button(font_family=roboto_regular, btn_color=BLUE, btn_size=[WIDTH*0.95, HEIGHT*0.95], text='')
    title = Text(font_family=roboto_light_italic, size=50,color=WHITE, text='Sapien,', y_ax=position_y_quarter1-50)
    lines = [
        'Sapien es un juego matematico multijugador en el cual se les',
        'presentaran diferentes operaciones matematicas para las cuales',
        'tendras opciones para responder, ganara el jugador que mayor',
        'numero de puntos posea.',
        'Nota: Los errores quitan puntos'
    ]

    _continue = Button(text='Okay', color=BLACK, btn_color=GREEN, y_ax=position_y_quarter3+50)

    for i in (game_info, title, _continue):
        pg_blit(i)

    line_pos = HEIGHT//3-15
    for i in range(len(lines)):
        i = Text(size=30, text=lines[i], color=BACKGROUND, y_ax=line_pos)
        line_pos += 50
        pg_blit(i)
    pg.display.update()

    info_running = True
    while info_running:
        for event in pg.event.get():
            rel_x, rel_y = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEMOTION and in_area(1, (_continue), rel_x, rel_y):
                if second % 0.5 == 0:
                    print(f'Mouse moved: X={rel_x}  Y={rel_y}')
            elif event.type == pg.MOUSEBUTTONDOWN and second % 0.5 == 0 and in_area(1, (_continue), rel_x, rel_y):
                print(f'Clicked: X={rel_x}  Y={rel_y}')
                hover.play()
                info_running = False
                set_players()
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    print(f'{second} seconds have elapsed in main screen')


def main_screen():
    SCREEN.fill(BACKGROUND)
    welcome = Text(text='Sapien', font_family=permanentmarker, size=140, color=BLUE, y_ax=position_y_quarter1)
    game_btn = Button(text='New Game', color=BLACK, btn_color=GREEN, x_ax=position_x_quarter1, y_ax=position_y_quarter3)
    quit_btn = Button(text='Quit Game', color=WHITE, btn_color=RED, x_ax=position_x_quarter3, y_ax=position_y_quarter3)

    for i in (welcome, game_btn, quit_btn):
        pg_blit(i)
    pg.display.update()

    second = 0
    main_running = True
    while main_running:
        for event in pg.event.get():
            rel_x, rel_y = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEMOTION and second % 1 == 0:
                if second % 2 == 0 and in_area(2, (game_btn, quit_btn), rel_x, rel_y):
                    print(f'Mouse moved X={rel_x}  Y={rel_y}')
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(1, (game_btn), rel_x, rel_y):
                if second % 0.5 == 0:
                    print(f'Clicked X={rel_x}  Y={rel_y}')
                    hover.play()
                    main_running = False
                    info()
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(1, (quit_btn), rel_x, rel_y):
                if second % 0.5 == 0:
                    print(f'Clicked X={rel_x}  Y={rel_y}')
                    hover.play()
                    main_running = False
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