import pygame

pygame.init()
pygame.mixer.init()

from config import window_width, window_height
from assets import load_assets
from main_screen import main_menu

window = pygame.display.set_mode((int(window_width), int(window_height)))
TITLE  = 'INSPER > FGV'
pygame.display.set_caption(TITLE)

main_menu()
pygame.quit()
pygame.mixer.quit()