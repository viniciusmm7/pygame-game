import pygame, main_screen

from config import *
from assets import load_assets
from game_over_screen import *
from languages_screen import *
from select_size_screen import *

MUTED   = False
UNMUTED = True
sound = UNMUTED

def settings():
    global sound
    RUNNING = 1
    QUIT    = 0
    MUTE_CLICK = X_CLICK = LANGUAGES_CLICK = SIZE_CLICK = False

    state = RUNNING

    assets = load_assets()
    
    while state != QUIT:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mute_btn.collidepoint(x, y):
                    MUTE_CLICK = True

                if languages_btn.collidepoint(x, y):
                    LANGUAGES_CLICK = True
                
                if x_btn.collidepoint(x, y):
                    X_CLICK = True

                if size_btn.collidepoint(x, y):
                    SIZE_CLICK = True

            if event.type == pygame.MOUSEBUTTONUP:
                ''' Mute/Unmute button event '''
                if mute_btn.collidepoint(x, y):
                    if sound == UNMUTED:
                        pygame.mixer.music.pause()
                        sound = MUTED
                        MUTE_CLICK = False
                    else:
                        pygame.mixer.music.unpause()
                        sound = UNMUTED
                        MUTE_CLICK = False
                else:
                    MUTE_CLICK = False

                ''' Languages button event '''
                if languages_btn.collidepoint(x, y):
                    languages()
                    LANGUAGES_CLICK = False
                else:
                    LANGUAGES_CLICK = False

                ''' X button event '''
                if x_btn.collidepoint(x, y):
                    main_screen.main_menu()
                    X_CLICK = False
                else:
                    X_CLICK = False

                ''' Size button event '''
                if size_btn.collidepoint(x, y):
                    select_size()
                    SIZE_CLICK = False
                else:
                    SIZE_CLICK = False

        languages_btn = pygame.draw.rect(window, INSPER_RED, (play_btn_pos_left, window_height / 4, main_menu_btn_w, main_menu_btn_h))
        x_btn         = pygame.draw.rect(window, INSPER_RED, (20, 20, main_menu_btn_h, main_menu_btn_h))
        mute_btn      = pygame.draw.rect(window, INSPER_RED, (play_btn_pos_left + 2/5 * main_menu_btn_h, window_height / 8, main_menu_btn_h, main_menu_btn_h))
        size_btn      = pygame.draw.rect(window, INSPER_RED, (play_btn_pos_left, window_height / 3, main_menu_btn_w, main_menu_btn_h))
        window.blit(assets['background_day'], (0, 0))

        if LANGUAGES_CLICK == False:
            window.blit(assets['languages_img_0'], (play_btn_pos_left, window_height/4))
        else:
            window.blit(assets['languages_img_1'], (play_btn_pos_left, window_height/4))
        
        if X_CLICK == False:
            window.blit(assets['x_img_0'], (20, 20))
        else:
            window.blit(assets['x_img_1'], (20, 20))
            
        if sound == UNMUTED:
            window.blit(assets['unmuted_img_0'], (play_btn_pos_left + 2/5 * main_menu_btn_h, window_height / 8))
        else:
            window.blit(assets['muted_img_0'], (play_btn_pos_left + 2/5 * main_menu_btn_h, window_height / 8))

        if SIZE_CLICK == False:
            window.blit(assets['select_size_img_0'], (play_btn_pos_left, window_height * 3/8))
        else:
            window.blit(assets['select_size_img_1'], (play_btn_pos_left, window_height * 3/8))
                
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    pygame.mixer.quit()