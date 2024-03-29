import pygame, game_screen, main_screen

from assets import load_assets
from config import FPS, INSPER_RED, window, other_text_pos_0, other_text_pos_1, play_btn_pos_left, btns_layer, quit_btn_pos_left, clock

def game_over():
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
                    game_screen.game()
                else:
                    YES_CLICK = False

                if no_btn.collidepoint(x, y):
                    main_screen.main_menu()
                else:
                    NO_CLICK = False
            
        window.blit(assets['background_day'], (0, 0))
        window.blit(assets['score_font'].render('GAME OVER', True, INSPER_RED), other_text_pos_0)
        window.blit(assets['score_font'].render('PLAY AGAIN?', True, INSPER_RED), other_text_pos_1)
        
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