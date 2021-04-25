import time

def countdown(seconds):
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)

# FRAMES PER SECOND
FPS = 45

# WINDOW
WIDTH = 960
HEIGHT = 540

# COLORS, RGB
BACKGROUND = (239, 239, 239)
LETTERS = (7, 7, 7)

WHITE = (255, 255, 255)
BLACK = (0,0,0)

RED = (209, 52, 91)
GREEN = (0, 255, 0)
BLUE = (52, 84, 209)

LIGHTBLUE = (52, 209, 191)

WRONG_COLOR = (2204, 153, 141)
RIGHT_COLOR = (22, 244, 208)


 # FONTS
roboto_light = './materiales/fonts/Roboto-Light.ttf'
roboto_light_italic = './materiales/fonts/Roboto-LightItalic.ttf'
roboto_thin = './materiales/fonts/Roboto-Thin.ttf'
roboto_regular = './materiales/fonts/Roboto-Regular.ttf'
permanentmarker = './materiales/fonts/PermanentMarker-Regular.ttf'

# SOUNDS
s_click = './materiales/sounds/Mouse_Click_4-fesliyanstudios.com.mp3'
hover_option = './materiales/sounds/generic-rollover-or-navigational-tone-4-sound-effect-85983277.mp3'

# ITEM POSITIONING
position_x_center = WIDTH//2
position_y_center = HEIGHT//2
position_x_quarter1 = WIDTH//4
position_x_quarter3 = WIDTH//4*3
position_y_quarter1 = HEIGHT//4
position_y_quarter3 = HEIGHT//4*3

position_x_dot10 = WIDTH//10
position_x_dot20 = WIDTH//10*2
position_x_dot30 = WIDTH//10*3
position_x_dot40 = WIDTH//10*4
position_x_dot50 = WIDTH//10*5
position_x_dot60 = WIDTH//10*6
position_x_dot70 = WIDTH//10*7
position_x_dot80 = WIDTH//10*8
position_x_dot90 = WIDTH//10*9

position_y_dot10 = HEIGHT//10
position_y_dot20 = HEIGHT//10*2
position_y_dot30 = HEIGHT//10*3
position_y_dot40 = HEIGHT//10*4
position_y_dot50 = HEIGHT//10*5
position_y_dot60 = HEIGHT//10*6
position_y_dot70 = HEIGHT//10*7
position_y_dot80 = HEIGHT//10*8
position_y_dot90 = HEIGHT//10*9