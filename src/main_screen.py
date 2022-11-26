import pygame

from config import FPS, INSPER_RED, window, play_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h, settings_btn_pos_left, quit_btn_pos_left, game_name, game_name_pos, clock
from assets import load_assets
from game_screen import game
# from options_screen import settings
from confirm_exit_screen import confirm_exit


def main_menu():
    RUNNING = 1
    QUIT = 0
    PLAY_CLICK = OPTIONS_CLICK = QUIT_CLICK = False
    state = RUNNING

    assets = load_assets()

    while state != QUIT:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(x, y):
                    PLAY_CLICK = True

                if settings_btn.collidepoint(x, y):
                    OPTIONS_CLICK = True

                if quit_btn.collidepoint(x, y):
                    QUIT_CLICK = True

            if event.type == pygame.MOUSEBUTTONUP:
                if play_btn.collidepoint(x, y):
                    game()
                    PLAY_CLICK = False
                else:
                    PLAY_CLICK = False

                if settings_btn.collidepoint(x, y):
                    # settings()
                    OPTIONS_CLICK = False
                else:
                    OPTIONS_CLICK = False

                if quit_btn.collidepoint(x, y):
                    confirm_exit()
                    QUIT_CLICK = False
                else:
                    QUIT_CLICK = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    confirm_exit()

        play_btn = pygame.draw.rect(
            window, INSPER_RED, (play_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))
        settings_btn = pygame.draw.rect(
            window, INSPER_RED, (settings_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))
        quit_btn = pygame.draw.rect(
            window, INSPER_RED, (quit_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))

        window.blit(assets['background_day'], (0, 0))
        window.blit(game_name, game_name_pos)

        if PLAY_CLICK == False:
            window.blit(assets['play_img_0'], (play_btn_pos_left, btns_layer))
        else:
            window.blit(assets['play_img_1'], (play_btn_pos_left, btns_layer))

        if OPTIONS_CLICK == False:
            window.blit(assets['options_img_0'],
                        (settings_btn_pos_left, btns_layer))
        else:
            window.blit(assets['options_img_1'],
                        (settings_btn_pos_left, btns_layer))

        if QUIT_CLICK == False:
            window.blit(assets['quit_img_0'], (quit_btn_pos_left, btns_layer))
        else:
            window.blit(assets['quit_img_1'], (quit_btn_pos_left, btns_layer))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    pygame.mixer.quit()
