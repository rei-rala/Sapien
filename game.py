import sys
import random
import pygame as pg
from materiales.materials import *
from tabla import TABLA_OPERACIONES
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
wrong_answer = pg.mixer.Sound(wrong_answer)
wrong_answer.set_volume(0.1)
clock_tick = pg.mixer.Sound(clock_tick)
clock_tick.set_volume(0.1)

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

# BUTTON RECT
class Button_rect(Text):
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
            elif type(to_blit) == Button_rect:
                pg.draw.rect(SCREEN, to_blit.btn_color, (btn_self_center[0], btn_self_center[1], to_blit.btn_size[0], to_blit.btn_size[1]))
                to_blit.area = [btn_self_center[0], btn_self_center[0]+to_blit.btn_size[0], btn_self_center[1], btn_self_center[1]+to_blit.btn_size[1]]
            # THIS SCREEN.BLIT GOES AFTER EACH FIGURE IS DRAWN
            SCREEN.blit(text, text_rect)
        return draw()

# Screen animation between options
def screen_animation(type='OUT', color_from=BACKGROUND, color_target=BLACK):
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
            pg.display.update()
            pg.time.wait(25)
    elif type == 'OUT':
        for i in animation_out:
            SCREEN.fill(color_target)
            pg_blit(i)
            pg.display.update()
            pg.time.wait(25)
    return pg.display.update()

# Smaller animation after chosing
def choose_animation(type=None):
    
    def set(color, text):
        animation_1 = [
            Button_round(text='', btn_color=(color[0]*0.30, color[1]*0.30, color[2]*0.30), btn_size=(WIDTH*0.05, HEIGHT*0.05)),
            Button_round(text='', btn_color=(color[0]*0.50, color[1]*0.50, color[2]*0.50), btn_size=(WIDTH*0.10, HEIGHT*0.20)),
            Button_round(text='', btn_color=(color[0]*0.60, color[1]*0.60, color[2]*0.60), btn_size=(WIDTH*0.20, HEIGHT*0.30)),
            Button_round(text='', btn_color=(color[0]*0.70, color[1]*0.70, color[2]*0.70), btn_size=(WIDTH*0.30, HEIGHT*0.30)),
            Button_round(text='', btn_color=(color[0]*0.80, color[1]*0.80, color[2]*0.80), btn_size=(WIDTH*0.40, HEIGHT*0.40)),
            Button_round(text='', btn_color=(color[0]*0.90, color[1]*0.90, color[2]*0.90), btn_size=(WIDTH*0.50, HEIGHT*0.50)),
            Button_round(text=text, btn_color=(color[0]*1.00, color[1]*1.00, color[2]*1.00), btn_size=(WIDTH*0.60, HEIGHT*0.60))
        ]
        animation_2 = [
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*1.15, HEIGHT*1.15)),
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*0.95, HEIGHT*0.95)),
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*0.90, HEIGHT*0.90)),
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*0.85, HEIGHT*0.85)),
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*0.80, HEIGHT*0.80)),
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*0.75, HEIGHT*0.75)),
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*0.70, HEIGHT*0.70)),
            Button_round(text='', btn_color=BLACK, btn_size=(WIDTH*0.62, HEIGHT*0.62)),
            Button_round(text='', btn_color=(color[0]*1.00, color[1]*1.00, color[2]*1.00), btn_size=(WIDTH*0.55, HEIGHT*0.55)),
            Button_round(text='', btn_color=(color[0]*1.00, color[1]*1.00, color[2]*1.00), btn_size=(WIDTH*0.40, HEIGHT*0.40)),
            Button_round(text='', btn_color=(color[0]*1.00, color[1]*1.00, color[2]*1.00), btn_size=(WIDTH*0.30, HEIGHT*0.30)),
            Button_round(text='', btn_color=(color[0]*1.00, color[1]*1.00, color[2]*1.00), btn_size=(WIDTH*0.20, HEIGHT*0.20)),
            Button_round(text='', btn_color=(color[0]*1.00, color[1]*1.00, color[2]*1.00), btn_size=(WIDTH*0.10, HEIGHT*0.10)),
            Button_round(text='', btn_color=(color[0]*1.00, color[1]*1.00, color[2]*1.00), btn_size=(WIDTH*0.05, HEIGHT*0.05))
        ]
        for i in animation_1:
            pg_blit(i)
            pg.display.update()
            pg.time.wait(25)
        pg.time.wait(700)
        #for i in animation_2:
        #    pg_blit(i)
        #    pg.display.update()
        #    pg.time.wait(35)
        #pg.time.wait(1000)
        screen_animation(color_from=BLACK, color_target=BACKGROUND)

    if type == 'OK':
        set(GREEN, 'Respuesta correcta!')
    elif type == 'BAD':
        set(RED, 'Respuesta incorrecta :(')
    elif type == 'TIMESUP':
        set( (255, 233, 0) , 'Se acabo el tiempo :/' )
    
    return pg.display.update(), pg.time.wait(100)
    
# THIS FUNCTION CHECKS IF THE MOUSE IS IN THE AREA OF OBJECT, QUANTITY ARGUMENT IS FOR THE COUNT, OBJECTS ARGUMENT MUST BE A LIST OF OBJECTS
def in_area(quantity, objects, x, y):
    if quantity == 1:
        if x in range(objects.area[0], objects.area[1]) and y in range(objects.area[2], objects.area[3]):
            #logger.info(f'In area {objects.__str__()}')
            return True
    else:
        for object in objects:
            if x in range(object.area[0], object.area[1]) and y in range(object.area[2], object.area[3]):
                #logger.info(f'In area {object.__str__()}')
                return True

# -------------------- Game instructions -----------------------------

def check_winner():
    def msj(ganador):
        if WINNER in PLAYER_LIST:
            screen_animation(color_from=BACKGROUND,color_target=BLACK)
            SCREEN.fill(BLACK)
            #time.sleep(1)
            
            #print(f'y el ganador es...')
            welcome = Text(text='Sapien', font_family=permanentmarker, size=25, color=BACKGROUND, x_ax=position_x_dot10, y_ax=position_y_dot10)
            text1 = Text(text='y el ganador es...', font_family=roboto_light, size=50, color=BACKGROUND, y_ax=position_y_quarter1)
            for i in (welcome, text1):
                pg_blit(i)
            pg.display.update()
            pg.time.wait(1000)
        
            #time.sleep(1)
            #print(f'\ncon {ganador.puntos} puntos, producto de {ganador.aciertos} aciertos: \n')
            pg_blit( Text(text=f'con {ganador.puntos} puntos, producto de {ganador.aciertos} aciertos', font_family=roboto_light, size=40, color=BLUE, y_ax=position_y_center-50) )
            pg.display.update()
            pg.time.wait(2000)


            #time.sleep(2)
            the_winner = Button(text=f'{ganador.nombre}', font_family=roboto_light, size=60, color=BLUE, btn_size=[210,70], y_ax=position_y_center+50)
            pg_blit(the_winner)
            pg.display.update()
            
            pg_blit( Text(text=f'Presiona la tecla "Q" para salir', font_family=roboto_regular, size=35, color=BLUE, y_ax=position_y_dot80) )
            pg.display.update()
            #print(f'\n{bcolors.WARNING}{ganador.nombre}!!!{bcolors.ENDC}\n')
        elif WINNER == 'SOLO'  :
            screen_animation(color_from=BACKGROUND,color_target=BLACK)
            SCREEN.fill(BLACK)
            #time.sleep(1)
            
            #print(f'y el ganador es...')
            welcome = Text(text='Sapien', font_family=permanentmarker, size=25, color=BACKGROUND, x_ax=position_x_dot10, y_ax=position_y_dot10)
            text1 = Text(text=f'Has jugado solo {PLAYER_LIST[0].nombre}', font_family=roboto_light, size=50, color=BACKGROUND, y_ax=position_y_quarter1)
            for i in (welcome, text1):
                pg_blit(i)
            pg.display.update()
            pg.time.wait(500)
        
            #time.sleep(1)
            #print(f'\ncon {ganador.puntos} puntos, producto de {ganador.aciertos} aciertos: \n')
            pg_blit( Text(text=f'Has ganado {PLAYER_LIST[0].puntos} puntos, producto de {PLAYER_LIST[0].aciertos} aciertos', font_family=roboto_light, size=40, color=BLUE, y_ax=position_y_center-50) )
            pg.display.update()
            
            pg_blit( Text(text=f'Presiona la tecla "Q" para salir', font_family=roboto_regular, size=35, color=BLUE, y_ax=position_y_dot80) )
            pg.display.update()

            #time.sleep(2)
            pg.display.update()
        elif WINNER == 'EMPATE!':
        
            screen_animation(color_from=BACKGROUND,color_target=BLACK)
            SCREEN.fill(BLACK)
            #time.sleep(1)
            
            #print(f'y el ganador es...')
            welcome = Text(text='Sapien', font_family=permanentmarker, size=25, color=BACKGROUND, x_ax=position_x_dot10, y_ax=position_y_dot10)
            text1 = Text(text='Hubo un empate!', font_family=roboto_light, size=50, color=BACKGROUND, y_ax=position_y_quarter1+200)
            for i in (welcome, text1):
                pg_blit(i)
            pg.display.update()
            pg.time.wait(1000)
        
            #time.sleep(1)
            #print(f'\ncon {ganador.puntos} puntos, producto de {ganador.aciertos} aciertos: \n')

            #time.sleep(2)
            
            pg_blit( Text(text=f'Presiona la tecla "Q" para salir', font_family=roboto_regular, size=35, color=BLUE, y_ax=position_y_dot80) )
            pg.display.update()
        else:
            print('Okay, hubo un error extranio')
    base = -999
    for i in PLAYER_LIST:
        if len(PLAYER_LIST) == 1:
            print('Jaja jugaste solo (?')
            WINNER = 'SOLO'
        elif i.puntos == base:
            WINNER = 'EMPATE!'
        elif i.puntos > base:
            base = i.puntos
            WINNER = i
    msj(WINNER)
    #time.sleep(1.5)
    for i in PLAYER_LIST:
        print(f'Puntos de {i.nombre}: {i.puntos}')
        if i.errores == []:
            print(f'Jugador {i.nombre} no tuvo errores!')
        else:
            print(f'Errores de {i.nombre}: {i.errores}')
    
    second = 0
    info_running = True
    while info_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    pass
            elif event.type == pg.KEYDOWN and event.key == ord('q'):
                #logger.info(f'Quitted by pressing "{chr(event.key)}"')
                sys.exit()
                    #logger.info(f'{second} seconds have elapsed in main screen')


def question(p, selection, reset_seconds):
    screen_animation(type='IN', color_from=BLACK, color_target=BACKGROUND)
    SCREEN.fill(BACKGROUND)

    currently_playing = Button(text=f'       {p.nombre} - R {p.round}/{ cant_rounds[0] }', size=15, btn_size=[200,25] ,color=BACKGROUND, btn_color=BLACK, x_ax=position_x_dot10*0.65, y_ax=position_y_dot10*0.65)
    text1 = Text(text=f'DADA LA SIGUIENTE OPERACION', font_family=roboto_thin ,size=30, color=LETTERS, y_ax=position_y_quarter1)
   
    pg_blit(currently_playing)
    pg.display.update()
    pg.time.wait(1000)
    pg_blit(text1)
    pg.display.update()
    pg.time.wait(1000)

    text_OP = Text(text=f' {selection} ', font_family=roboto_thin ,size=45, color=BLUE, y_ax=position_y_center*0.75)
    text2 = Text(text=f'¿Cual es el resultado?', font_family=roboto_thin ,size=30, color=LETTERS, y_ax=position_y_center*1.1)

    
    pg_blit(text_OP)
    pg.display.update()
    pg.time.wait(1000)
    pg_blit(text2)
    pg.display.update()


    def randomize(n, m):
        zzz, yyy = random.randint(-20,20), round(random.uniform(0.85, 1.15),2)
        zzz = round(TABLA_OPERACIONES[selection]+zzz)
        yyy = round(TABLA_OPERACIONES[selection]*yyy)
        tries = 0
        while round(TABLA_OPERACIONES[selection])==zzz or round(TABLA_OPERACIONES[selection])==yyy and tries != 3:
            #logger.info(tries)
            tries += 1
            if n == 1:
                return (TABLA_OPERACIONES[selection]+random.randint(1,25))
            elif m == 1:
                return (TABLA_OPERACIONES[selection]+random.randint(-7,-1))
        else:
            if n ==  1:
                #logger.info(zzz)
                return zzz
            elif m == 1:
                #logger.info(yyy)
                return yyy

    btn1 = Button_round(text=f'{int(round(randomize(1,0)))}', color=BACKGROUND, btn_color=BLUE, x_ax=position_x_dot30, y_ax=position_y_dot70, value=int(round(randomize(1,0))) )
    btn2 = Button_round(text=f'{int(TABLA_OPERACIONES[selection])}', color=BACKGROUND, btn_color=BLUE, x_ax=position_x_dot50, y_ax=position_y_dot70, value=int(TABLA_OPERACIONES[selection]))
    btn3 = Button_round(text=f'{int(round(randomize(0,1)))}', color=BACKGROUND, btn_color=BLUE, x_ax=position_x_dot70, y_ax=position_y_dot70, value=int(round(randomize(0,1))) )

    index_shuffle = [0,1,2]
    random.shuffle(index_shuffle)

    shuffled_options = {index_shuffle[0]:btn1, index_shuffle[1]:btn2, index_shuffle[2]:btn3}

    shuffled_options[0].x_axis=position_x_dot30
    shuffled_options[1].x_axis=position_x_dot50
    shuffled_options[2].x_axis=position_x_dot70
    
    for key in shuffled_options:  
        pg_blit(shuffled_options[key])
    pg.display.update()

    
    def timer(seconds):
        if seconds == 0:
            show_this = Button(text='3', color=LETTERS, btn_color=LIGHTBLUE, btn_size=[60,60],size=30, x_ax=position_x_dot90+50, y_ax=position_y_dot90, value=int(TABLA_OPERACIONES[selection]))
        elif seconds == 1:
            show_this = Button(text='2', color=LETTERS, btn_color=LIGHTBLUE,btn_size=[65,65],size=34, x_ax=position_x_dot90+50, y_ax=position_y_dot90, value=int(TABLA_OPERACIONES[selection]))
        elif seconds == 2:
            show_this = Button(text='1', color=LETTERS, btn_color=LIGHTBLUE,btn_size=[70,70], size=37, x_ax=position_x_dot90+50, y_ax=position_y_dot90, value=int(TABLA_OPERACIONES[selection]))
        elif seconds == 3:
            show_this = Button(text='0!', color=BACKGROUND, btn_color=RED,btn_size=[75,75], size=40, x_ax=position_x_dot90+50, y_ax=position_y_dot90, value=int(TABLA_OPERACIONES[selection]))
        else:
            return
        if seconds in (0,1,2,3):
            clock_tick.play()
        return pg_blit(show_this), pg.display.update()
    
    second, countdown = 0, 0
    question_running = True
    while question_running:
        for event in pg.event.get():
            rel_x, rel_y = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                question_running = False
                sys.exit()
            elif event.type == pg.MOUSEMOTION and in_area(3, (btn1, btn2, btn3), rel_x, rel_y):
                if second % 2 == 0:
                    #logger.info(f'Mouse moved X={rel_x}  Y={rel_y}')
                    pass
            elif event.type == pg.MOUSEBUTTONDOWN and second % 0.5 == 0 and in_area(3, (btn1, btn2, btn3), rel_x, rel_y):
                if in_area(1, (btn2), rel_x, rel_y):
                    p.aciertos += 1
                    p.puntos += 2
                    checkmark.play()
                    #logger.info(f'Jugador {p.nombre} +1 acierto ({p.aciertos}), +2 puntos ({p.puntos})')
                    choose_animation(type='OK')
                    #logger.info('Respuesta Correcta')
                    question_running = False
                elif in_area(2, (btn1, btn3), rel_x, rel_y): 
                    if in_area(1, (btn1), rel_x, rel_y): 
                        clock_tick.stop()
                        choose_animation(type='BAD')
                        wrong_answer.play()
                        #logger.info('Respuesta incorrecta')
                        p.puntos -= 1
                        p.errores.append(f'En round {p.round} -> {selection} = {btn1.value}')
                        question_running = False
                    elif in_area(1, (btn3), rel_x, rel_y): 
                        clock_tick.stop()
                        wrong_answer.play()
                        choose_animation(type='BAD')
                        #logger.info('Respuesta incorrecta')
                        p.puntos -= 1
                        p.errores.append(f'En round {p.round} -> {selection} = {btn2.value}')
                        question_running = False
                    #logger.info(f'Anadido error Nro {len(p.errores)} en round {p.round} para jugador {p.nombre}: {select} = {str(respuesta)}')
                    #logger.info(f'Jugador {p.nombre} -1 puntos ({p.puntos}), total errores: {len(p.errores)}')

            # yep... all the 'animations' take time from timers, you can see it while player one plays his first round, so:
            elif event.type == pg.USEREVENT:
                second += 1

                if p.nombre == PLAYER_LIST[0].nombre and p.round==1:
                    if 13 >= second >= 10:
                        countdown += 1
                else:
                    if 10 >= second >= 7:
                        countdown += 1
                        
                timer(countdown)
                #logger.info(f'{second} seconds have elapsed in main screen')
                #logger.info(f'{countdown} (countdown) seconds have elapsed in main screen') 
                pass
                if countdown >= 3:
                    clock_tick.set_volume(0.0)
                    if countdown == 3:
                        choose_animation(type='TIMESUP')
                        wrong_answer.play()
                        #logger.info(f'Se acabo el tiempo.')
                        p.puntos -= 1
                        p.errores.append(f'En round {p.round} -> {selection}')
                        question_running = False


def Sapien(p):
    p.round += 1
    SCREEN.fill(BLACK)
    welcome = Text(text='Sapien', font_family=permanentmarker, size=25, color=BLUE, x_ax=position_x_dot10, y_ax=position_y_dot10)
    select = random.choice(list(TABLA_OPERACIONES.keys()))
    key_operation = str(select)

    #logger.info(select)
    
    ##logger.debug(f'Jugador {p.nombre}, round {p.round} => Operacion aleatoria seleccionada \'{select}\' respuesta: {int(TABLA_OPERACIONES[select])}')


    jugadorX = Button(text=f'Jugador {p.nombre}', size=60, color=BACKGROUND, btn_color=BLACK, y_ax=position_y_quarter3-50)
    roundX = Button(text=f'Round Nro {p.round}', size=60, color=BACKGROUND, btn_color=BLACK, y_ax=position_y_quarter1)
    
    #logger.info(f'RONDA {p.round} \n\nJUGADOR {bcolors.WARNING} {p.nombre}{bcolors.ENDC},')
    for i in (welcome, jugadorX, roundX):
        pg_blit(i)
    pg.display.update()
    pg.time.wait(1000)
    seconds = 0
    question(p, select, seconds)

    # Elimina la opcion elegida por el sistema para evitar que haya dos juegos iguales
    TABLA_OPERACIONES.pop(key_operation)


def pre_game(seconds_animation=3):
    target_screen = (BLUE, BLACK, (119,136,153), WHITE)
    letters = (WHITE, BLACK, BLACK)

    for i in range(seconds_animation):
        screen_animation(color_from=target_screen[i], color_target=target_screen[i+1])
        pg_blit( Text(text=str(-i+3), font_family=permanentmarker, size=180+i*150, color=letters[i] ))
        pg.display.update()
        pg.time.wait(500)
    screen_animation(type='IN',color_from=WHITE, color_target=BLACK)

    for p in PLAYER_LIST:
        for g in range(cant_rounds[0]):
            Sapien(p)
    check_winner()
     

def player_names():
    pg.display.flip()
    player_name = list()
    player_name.append('')
    #logger.info(player_name)
    
    sapien_title = Text(text='Sapien', font_family=permanentmarker, size=25, color=BLACK, x_ax=position_x_dot10, y_ax=position_y_dot10)
    pg_blit(sapien_title)

    def name_refresh(index, key, action):
        if action == 'add':
            player_name[index] += key
            #logger.info(player_name[index])
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[310,65], btn_color=GREEN))
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[305,60], btn_color=LETTERS))
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[300,55], btn_color=(45,76,200)))
            pg.display.update()
            pg.time.wait(100)
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[310,65], btn_color=LETTERS))
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[300,55], btn_color=BLUE))
        elif action == 'backspace':
            player_name[index] = player_name[index][0:len(player_name[index])-1]
            #logger.info(player_name[index])
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[310,65], btn_color=RED))
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[305,60], btn_color=LETTERS))
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[300,55], btn_color=(45,76,200)))
            pg.display.update()
            pg.time.wait(100)
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[310,65], btn_color=LETTERS))
            pg_blit(Button(text=player_name[index], size=35, color=BACKGROUND, btn_size=[300,55], btn_color=BLUE))
        pg_blit(Button(text=f'{len(player_name[index])}/10',font_family=roboto_light, size=20, btn_size=[50,50], btn_color=BACKGROUND,x_ax=position_x_dot70))
        pg_blit(Button(text='', btn_color=BACKGROUND, size=15, btn_size=[500,45], y_ax=position_y_dot60+20)) 
        pg.display.update()
    
    for i in range(0,cant_jugadores[0]):
        player_names_running = True
        player_name.append('')


    # aqui probablemente se escojera la lista de colores para el fondo de pantalla de cada jugador 
        screen_animation(type='IN', color_from=BLACK, color_target=BACKGROUND)
        SCREEN.fill(BACKGROUND)
        pg_blit(Text(font_family=roboto_thin, text=f'Ingrese nombre para J{i+1} (de {cant_jugadores[0]})', y_ax=position_y_dot40))
        position_x_player_init = position_x_quarter1
        for each in PLAYER_LIST:
            each = Button(font_family=roboto_light_italic, text=each.nombre, x_ax=position_x_player_init, y_ax=position_y_dot80)
            position_x_player_init += 250
            pg_blit(each)
        pg_blit(Button(text='', size=35, btn_size=[315,70], color=BACKGROUND, btn_color=LETTERS))
        pg_blit(Button(text='', size=35, btn_size=[300,55], color=BACKGROUND, btn_color=BLUE))
        pg.display.update()
        while player_names_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key== 8 and len(player_name[i]) != 0:
                    key = chr(event.key)
                    name_refresh(i, key, 'backspace')
                elif event.type == pg.KEYDOWN and event.key in ord_ascii_letters and len(player_name[i]) != 10:
                    key = chr(event.key)
                    name_refresh(i, key, 'add')
                elif event.type == pg.KEYDOWN and event.key in ord_ascii_letters and len(player_name[i]) == 10:
                    pg_blit(Button(text='10 caracteres maximo por favor', btn_color=BACKGROUND, size=15, btn_size=[500,45], y_ax=position_y_dot60+20)) 
                    pg.display.update()
                    pg.time.wait(100)
                    pg_blit(Button(text='', color=RED, btn_color=BACKGROUND, btn_size=[500,45], y_ax=position_y_dot80))
                    pg.display.update()
                elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and len(player_name[i]) == 0:
                    pg.display.update()
                    pg_blit(Button(text='Ingrese al menos un caracter', btn_color=BACKGROUND, size=15, btn_size=[500,45], y_ax=position_y_dot60+20))
                    pg.time.wait(100)
                    pg.display.update()
                elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and len(player_name[i]) != 0:
                    pg_blit(Button(text='', size=35, btn_size=[300,55], btn_color=BLUE))
                    pg.display.update()
                    player_created = Jugador(player_name[i])
                    PLAYER_LIST.append(player_created)
                    #logger.info(PLAYER_LIST)
                    player_names_running = False
            continue
    pre_game()


def set_rounds():
    pg.display.flip()
    # NICE TRANSITION, BRO
    screen_animation(type='OUT', color_from=RED, color_target=BLUE)
    
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
                    #logger.info(f'Mouse moved X={rel_x}  Y={rel_y}')
                    pass
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(8, (choose_1, choose_2, choose_3, choose_4, choose_5, choose_6, choose_7, choose_8), rel_x, rel_y):
                    #logger.info(f'Clicked! X={rel_x}, Y={rel_y}')
                    hover.play()
                    pg.time.wait(10)

                    def choose_rounds(button_class):
                        cant_rounds.append(button_class.value)
                        #logger.info(f'Cantidad de rounds: {cant_rounds}')
                        player_names()

                    if in_area(1, (choose_1), rel_x, rel_y): choose_rounds(choose_1) #logger.info('JUGADORES 1'), 
                    elif in_area(1, (choose_2), rel_x, rel_y): choose_rounds(choose_2) #logger.info('JUGADORES 2'), 
                    elif in_area(1, (choose_3), rel_x, rel_y): choose_rounds(choose_3) #logger.info('JUGADORES 3'), 
                    elif in_area(1, (choose_4), rel_x, rel_y): choose_rounds(choose_4) #logger.info('JUGADORES 4'), 
                    elif in_area(1, (choose_5), rel_x, rel_y): choose_rounds(choose_5) #logger.info('JUGADORES 5'), 
                    elif in_area(1, (choose_6), rel_x, rel_y): choose_rounds(choose_6) #logger.info('JUGADORES 6'), 
                    elif in_area(1, (choose_7), rel_x, rel_y): choose_rounds(choose_7) #logger.info('JUGADORES 7'), 
                    elif in_area(1, (choose_8), rel_x, rel_y): choose_rounds(choose_8) #logger.info('JUGADORES 8'), 
                    set_rounds_running = False
                    
                    
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    #logger.info(f'{second} seconds have elapsed in main screen')
                    pass
            elif event.type == pg.KEYDOWN and event.key == ord('q'):
                #logger.info(f'Quitted by pressing "{chr(event.key)}"')
                sys.exit()


def set_players():
    pg.display.flip()
    # NICE TRANSITION, BRO
    screen_animation(type='IN', color_from=WHITE, color_target=RED)

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
                    #logger.info(f'Mouse moved X={rel_x}  Y={rel_y}')
                    pass
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(4, (choose_1, choose_2, choose_3, choose_4), rel_x, rel_y):
                    #logger.info(f'Clicked! X={rel_x}, Y={rel_y}')
                    hover.play()
                    pg.time.wait(10)

                    def choose_players(button_class):
                        cant_jugadores.append(button_class.value)
                        #logger.info(cant_jugadores)

                    if in_area(1, (choose_1), rel_x, rel_y): choose_players(choose_1) #logger.info('JUGADORES 1'), 
                    elif in_area(1, (choose_2), rel_x, rel_y): choose_players(choose_2) #logger.info('JUGADORES 2'), 
                    elif in_area(1, (choose_3), rel_x, rel_y): choose_players(choose_3) #logger.info('JUGADORES 3'), 
                    elif in_area(1, (choose_4), rel_x, rel_y): choose_players(choose_4) #logger.info('JUGADORES 4'), 

                    set_players_running = False
                    set_rounds()
                    
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    #logger.info(f'{second} seconds have elapsed in main screen')
                    pass
            elif event.type == pg.KEYDOWN and event.key == ord('q'):
                #logger.info(f'Quitted by pressing "{chr(event.key)}"')
                sys.exit()


def info():
    pg.display.flip()
    screen_animation(type='IN', color_target=BLUE)
    SCREEN.fill(BACKGROUND)

    second = 0
    game_info = Button(font_family=roboto_regular, btn_color=BLUE, btn_size=[WIDTH*0.90, HEIGHT*0.90], text='')
    title = Text(font_family=roboto_light_italic, size=50,color=WHITE, text='Sapien,', y_ax=position_y_quarter1-50)
    lines = [
        'Sapien es un juego matematico multijugador en el cual se les',
        'presentaran diferentes operaciones matematicas, para las',
        'cuales tendras opciones para responder.',
        'El jugador mas puntos tenga, ganara',
        '',
        'Nota: Los errores quitan puntos'
    ]

    _continue = Button(text='Okay', color=BLACK, btn_color=GREEN, y_ax=position_y_quarter3+60)

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
                    #logger.info(f'Mouse moved: X={rel_x}  Y={rel_y}')
                    pass
            elif event.type == pg.MOUSEBUTTONDOWN and second % 0.5 == 0 and in_area(1, (_continue), rel_x, rel_y):
                #logger.info(f'Clicked: X={rel_x}  Y={rel_y}')
                hover.play()
                info_running = False
                set_players()
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    pass
                    #logger.info(f'{second} seconds have elapsed in main screen')


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
                    #logger.info(f'Mouse moved X={rel_x}  Y={rel_y}')
                    pass
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(1, (game_btn), rel_x, rel_y):
                if second % 0.5 == 0:
                    #logger.info(f'Clicked X={rel_x}  Y={rel_y}')
                    hover.play()
                    main_running = False
                    info()
            elif event.type == pg.MOUSEBUTTONDOWN and in_area(1, (quit_btn), rel_x, rel_y):
                if second % 0.5 == 0:
                    #logger.info(f'Clicked X={rel_x}  Y={rel_y}')
                    hover.play()
                    main_running = False
                    pg.time.wait(10)
                    sys.exit()
            elif event.type == pg.USEREVENT:
                second += 1
                if second % 5 == 0:
                    #logger.info(f'{second} seconds have elapsed in main screen')
                    pass
            elif event.type == pg.KEYDOWN and event.key == ord('q'):
                #logger.info(f'Quitted by pressing "{chr(event.key)}"')
                sys.exit()


if __name__ == '__main__':
    main_screen()


# Quit after everything...
pg.quit()
sys.exit()