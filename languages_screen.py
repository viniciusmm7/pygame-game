import pygame

from assets import *
from main_screen import *
from options_screen import *

def languages():
    RUNNING = 1
    QUIT    = 0

    X_CLICK = False
    state = RUNNING

    assets = load_assets()
    
    while state != QUIT:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if x_btn.collidepoint(x, y):
                    X_CLICK = True

            if event.type == pygame.MOUSEBUTTONUP:
                if x_btn.collidepoint(x, y):
                    return False
                else:
                    X_CLICK = False

        x_btn = pygame.draw.rect(window, INSPER_RED, (20, 20, main_menu_btn_h, main_menu_btn_h))
        window.blit(assets['background_day'], (0, 0))
        
        if X_CLICK == False:
            window.blit(assets['x_img_0'], (20, 20))
        else:
            window.blit(assets['x_img_1'], (20, 20))
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    pygame.mixer.quit()