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