import pygame

from assets import *
from config import *
from main_screen import *
from pause_screen import *

def confirm_exit():
    RUNNING = 1
    QUIT    = 0
    NO_CLICK = YES_CLICK = False    
    state = RUNNING

    assets = load_assets()
    
    while state != QUIT:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_btn.collidepoint(x, y):
                    YES_CLICK = True

                if no_btn.collidepoint(x, y):
                    NO_CLICK = True

            if event.type == pygame.MOUSEBUTTONUP:
                if yes_btn.collidepoint(x, y):
                    state = QUIT
                else:
                    YES_CLICK = False

                if no_btn.collidepoint(x, y):
                    return False
                else:
                    NO_CLICK = False
            
        window.blit(assets['background_day'], (0, 0))
        window.blit(assets['score_font'].render('ARE YOU SURE?', True, INSPER_RED), other_text_pos_0)
        if YES_CLICK == False:
            yes_btn = window.blit(assets['yes_img_0'], (play_btn_pos_left, btns_layer))
        else:
            yes_btn = window.blit(assets['yes_img_1'], (play_btn_pos_left, btns_layer))

        if NO_CLICK == False:
            no_btn = window.blit(assets['no_img_0'], (quit_btn_pos_left, btns_layer))
        else:
            no_btn = window.blit(assets['no_img_1'], (quit_btn_pos_left, btns_layer))
            
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    pygame.mixer.quit()