import pygame, sys

clock   = pygame.time.Clock()
FPS     = 120
VOLUME  = 1.0 # Have to be a float number between 0 and 1
STILL   = 0
JUMPING = MOVING = LEFT = 1
RIGHT   = 2

# ----- Geometry
window_width  = 1000
window_height = 1000
hero_width    = 75
hero_height   = 75
enemy_width   = int(hero_width * 2/3)
enemy_height  = int(hero_height * 2/3)
gravity       = window_height // 450
vi_jump       = 18 * gravity

# ----- Generating Main Window
window = pygame.display.set_mode((int(window_width), int(window_height)))
TITLE  = 'INSPER > FGV'
pygame.display.set_caption(TITLE)

# ----- Colors
RED        = (255, 0, 0)
GREEN      = (0, 255, 0)
BLUE       = (0, 0, 255)
PINK       = (255, 0, 255)
PURPLE     = (140, 0, 255)
ORANGE     = (255, 140, 0)
YELLOW     = (255, 255, 0)
BLACK      = (0, 0, 0)
WHITE      = (255, 255, 255)
INSPER_RED = (192, 0, 38)
DARK_GREEN = (0, 192, 38)
DARK_BLUE  = (38, 0, 192)
LIGHT_GREY = (190, 190, 190)
DARK_GREY  = (120, 120, 120)

# ----- Text
game_name_text_size = window_height // 15
game_name_font      = pygame.font.SysFont('ravie', game_name_text_size)
game_name_text      = TITLE
game_name_pos       = (window_width / 2 - 37/4 * game_name_text_size / 2, window_height / 5)
game_name           = game_name_font.render(game_name_text, True, INSPER_RED)

main_menu_btn_text_size = window_height // 25
main_menu_btn_font      = pygame.font.SysFont('ravie', main_menu_btn_text_size)
main_menu_btn_w         = window_width // 5
main_menu_btn_h         = window_height // 10

other_text_pos_0 = (window_width / 3, window_height / 5)
other_text_pos_1 = (window_width / 3 - 20, window_height / 3)

# ----- Generate geometry
btns_layer            = int(window_height * 8/10)
play_btn_pos_left     = int(window_width  * 5/11 - main_menu_btn_w / 4)
settings_btn_pos_left = int(window_width  * 2/11 - main_menu_btn_w / 4)
quit_btn_pos_left     = int(window_width  * 8/11 - main_menu_btn_w / 4)