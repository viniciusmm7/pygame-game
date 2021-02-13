import pygame

pygame.init()
pygame.mixer.init()

from config import *
from assets import *
from main_screen import *

window = pygame.display.set_mode((int(window_width), int(window_height)))
TITLE  = 'INSPER > FGV'
pygame.display.set_caption(TITLE)

main_menu()
pygame.quit()
pygame.mixer.quit()