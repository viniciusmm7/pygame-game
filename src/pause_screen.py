import pygame

from main_screen import main_menu
from assets import load_assets
from config import FPS, INSPER_RED, window, clock, play_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h, window_height
from game_screen import game


def pause():
    RUNNING = 1
    QUIT = 0
    RESUME_CLICK = MENU_CLICK = False
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
                if menu_btn.collidepoint(x, y):
                    MENU_CLICK = True

                if resume_btn.collidepoint(x, y):
                    RESUME_CLICK = True

            if event.type == pygame.MOUSEBUTTONUP:
                if menu_btn.collidepoint(x, y):
                    main_menu()
                else:
                    MENU_CLICK = False

                if resume_btn.collidepoint(x, y):
                    return False
                else:
                    RESUME_CLICK = False

        menu_btn = pygame.draw.rect(
            window, INSPER_RED, (play_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))
        resume_btn = pygame.draw.rect(window, INSPER_RED, (play_btn_pos_left, btns_layer -
                                      window_height / 2 + main_menu_btn_h/4, main_menu_btn_w, main_menu_btn_h))
        window.blit(assets['background_day'], (0, 0))

        if RESUME_CLICK == False:
            window.blit(assets['resume_img_0'], (play_btn_pos_left,
                        btns_layer - window_height / 2 + main_menu_btn_h/4))
        else:
            window.blit(assets['resume_img_1'], (play_btn_pos_left,
                        btns_layer - window_height / 2 + main_menu_btn_h/4))

        if MENU_CLICK == False:
            window.blit(assets['quit_img_0'], (play_btn_pos_left, btns_layer))
        else:
            window.blit(assets['quit_img_1'], (play_btn_pos_left, btns_layer))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    pygame.mixer.quit()
