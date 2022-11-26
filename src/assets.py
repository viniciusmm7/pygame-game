import pygame
from config import enemy_width, enemy_height, hero_width, hero_height, window_width, window_height, main_menu_btn_w, main_menu_btn_h

pygame.mixer.init()
pygame.mixer.music.load('../assets/music/other_pause_theme.wav')
pygame.mixer.music.play(loops=-1)


__assets = {}
__explosion_anim = []

def __load_enemy_sprites():
    __assets['enemy_img'] = pygame.image.load(
        '../assets/img/enemy.png').convert_alpha()
    __assets['enemy_img'] = pygame.transform.scale(
        __assets['enemy_img'], (enemy_width, enemy_height))
    __assets['enemy_left_img_0'] = pygame.image.load(
        '../assets/img/enemy_left_0.png').convert_alpha()
    __assets['enemy_left_img_0'] = pygame.transform.scale(
        __assets['enemy_left_img_0'], (enemy_width, enemy_height))
    __assets['enemy_left_img_1'] = pygame.image.load(
        '../assets/img/enemy_left_1.png').convert_alpha()
    __assets['enemy_left_img_1'] = pygame.transform.scale(
        __assets['enemy_left_img_1'], (enemy_width, enemy_height))
    __assets['enemy_right_img_0'] = pygame.image.load(
        '../assets/img/enemy_right_0.png').convert_alpha()
    __assets['enemy_right_img_0'] = pygame.transform.scale(
        __assets['enemy_right_img_0'], (enemy_width, enemy_height))
    __assets['enemy_right_img_1'] = pygame.image.load(
        '../assets/img/enemy_right_1.png').convert_alpha()
    __assets['enemy_right_img_1'] = pygame.transform.scale(
        __assets['enemy_right_img_1'], (enemy_width, enemy_height))

def __load_hero_sprites():
    __assets['hero_left_img'] = pygame.image.load(
        '../assets/img/hero_left.png').convert_alpha()
    __assets['hero_left_img'] = pygame.transform.scale(
        __assets['hero_left_img'], (hero_width, hero_height))
    __assets['hero_right_img'] = pygame.image.load(
        '../assets/img/hero_right.png').convert_alpha()
    __assets['hero_right_img'] = pygame.transform.scale(
        __assets['hero_right_img'], (hero_width, hero_height))

def __load_bullet_sprites():
    __assets['bullet_left_img'] = pygame.image.load(
        '../assets/img/bullet_left.png').convert_alpha()
    __assets['bullet_left_img'] = pygame.transform.scale(
        __assets['bullet_left_img'], (hero_height//3, hero_width//3))
    __assets['bullet_right_img'] = pygame.image.load(
        '../assets/img/bullet_right.png').convert_alpha()
    __assets['bullet_right_img'] = pygame.transform.scale(
        __assets['bullet_right_img'], (hero_height//3, hero_width//3))

def __load_background_sprites():
    __assets['background_day'] = pygame.image.load(
        '../assets/img/background_day.png').convert()
    __assets['background_day'] = pygame.transform.scale(
        __assets['background_day'], (window_width, window_height))
    __assets['background_day_1'] = pygame.image.load(
        '../assets/img/background_day_1.png').convert()
    __assets['background_day_1'] = pygame.transform.scale(
        __assets['background_day_1'], (window_width * 7, window_height))
    __assets['platform_img'] = pygame.image.load(
        '../assets/img/platform.png').convert_alpha()
    __assets['platform_img'] = pygame.transform.scale(
        __assets['platform_img'], (window_height//10, window_height//10))
    __assets['background_night'] = pygame.image.load(
        '../assets/img/background_night.png').convert()
    __assets['background_night'] = pygame.transform.scale(
        __assets['background_night'], (window_width, window_height))

def __load_play_btn_sprites():
    __assets['play_img_0'] = pygame.image.load(
        '../assets/img/play_0.png').convert_alpha()
    __assets['play_img_0'] = pygame.transform.scale(
        __assets['play_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['play_img_1'] = pygame.image.load(
        '../assets/img/play_1.png').convert_alpha()
    __assets['play_img_1'] = pygame.transform.scale(
        __assets['play_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_options_btn_sprites():
    __assets['options_img_0'] = pygame.image.load(
        '../assets/img/options_0.png').convert_alpha()
    __assets['options_img_0'] = pygame.transform.scale(
        __assets['options_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['options_img_1'] = pygame.image.load(
        '../assets/img/options_1.png').convert_alpha()
    __assets['options_img_1'] = pygame.transform.scale(
        __assets['options_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_quit_btn_sprites():
    __assets['quit_img_0'] = pygame.image.load(
        '../assets/img/quit_0.png').convert_alpha()
    __assets['quit_img_0'] = pygame.transform.scale(
        __assets['quit_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['quit_img_1'] = pygame.image.load(
        '../assets/img/quit_1.png').convert_alpha()
    __assets['quit_img_1'] = pygame.transform.scale(
        __assets['quit_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_langs_btn_sprites():
    __assets['languages_img_0'] = pygame.image.load(
        '../assets/img/language_0.png').convert_alpha()
    __assets['languages_img_0'] = pygame.transform.scale(
        __assets['languages_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['languages_img_1'] = pygame.image.load(
        '../assets/img/language_1.png').convert_alpha()
    __assets['languages_img_1'] = pygame.transform.scale(
        __assets['languages_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_resume_btn_sprites():
    __assets['resume_img_0'] = pygame.image.load(
        '../assets/img/resume_0.png').convert_alpha()
    __assets['resume_img_0'] = pygame.transform.scale(
        __assets['resume_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['resume_img_1'] = pygame.image.load(
        '../assets/img/resume_1.png').convert_alpha()
    __assets['resume_img_1'] = pygame.transform.scale(
        __assets['resume_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_yes_btn_sprites():
    __assets['yes_img_0'] = pygame.image.load(
        '../assets/img/yes_0.png').convert_alpha()
    __assets['yes_img_0'] = pygame.transform.scale(
        __assets['yes_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['yes_img_1'] = pygame.image.load(
        '../assets/img/yes_1.png').convert_alpha()
    __assets['yes_img_1'] = pygame.transform.scale(
        __assets['yes_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_no_btn_sprites():
    __assets['no_img_0'] = pygame.image.load(
        '../assets/img/no_0.png').convert_alpha()
    __assets['no_img_0'] = pygame.transform.scale(
        __assets['no_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['no_img_1'] = pygame.image.load(
        '../assets/img/no_1.png').convert_alpha()
    __assets['no_img_1'] = pygame.transform.scale(
        __assets['no_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_x_btn_sprites():
    __assets['x_img_0'] = pygame.image.load(
        '../assets/img/x_0.png').convert_alpha()
    __assets['x_img_0'] = pygame.transform.scale(
        __assets['x_img_0'], (main_menu_btn_h, main_menu_btn_h))
    __assets['x_img_1'] = pygame.image.load(
        '../assets/img/x_1.png').convert_alpha()
    __assets['x_img_1'] = pygame.transform.scale(
        __assets['x_img_1'], (main_menu_btn_h, main_menu_btn_h))

def __load_mute_btn_sprites():
    __assets['muted_img_0'] = pygame.image.load(
        '../assets/img/muted_0.png').convert_alpha()
    __assets['muted_img_0'] = pygame.transform.scale(
        __assets['muted_img_0'], (main_menu_btn_h, main_menu_btn_h))
    __assets['muted_img_1'] = pygame.image.load(
        '../assets/img/muted_1.png').convert_alpha()
    __assets['muted_img_1'] = pygame.transform.scale(
        __assets['muted_img_1'], (main_menu_btn_h, main_menu_btn_h))

def __load_unmute_btn_sprites():
    __assets['unmuted_img_0'] = pygame.image.load(
        '../assets/img/unmuted_0.png').convert_alpha()
    __assets['unmuted_img_0'] = pygame.transform.scale(
        __assets['unmuted_img_0'], (main_menu_btn_h, main_menu_btn_h))
    __assets['unmuted_img_1'] = pygame.image.load(
        '../assets/img/unmuted_1.png').convert_alpha()
    __assets['unmuted_img_1'] = pygame.transform.scale(
        __assets['unmuted_img_1'], (main_menu_btn_h, main_menu_btn_h))

def __load_size_btn_sprites():
    __assets['select_size_img_0'] = pygame.image.load(
        '../assets/img/size_0.png').convert_alpha()
    __assets['select_size_img_0'] = pygame.transform.scale(
        __assets['select_size_img_0'], (main_menu_btn_w, main_menu_btn_h))
    __assets['select_size_img_1'] = pygame.image.load(
        '../assets/img/size_1.png').convert_alpha()
    __assets['select_size_img_1'] = pygame.transform.scale(
        __assets['select_size_img_1'], (main_menu_btn_w, main_menu_btn_h))

def __load_btn_sprites():
    __load_play_btn_sprites()
    __load_options_btn_sprites()
    __load_quit_btn_sprites()
    __load_langs_btn_sprites()
    __load_resume_btn_sprites()
    __load_yes_btn_sprites()
    __load_no_btn_sprites()
    __load_x_btn_sprites()
    __load_mute_btn_sprites()
    __load_unmute_btn_sprites()
    __load_size_btn_sprites()

def __load_explosion_sprites():
    for i in range(9):
        filename = '../assets/img/regularExplosion0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (32, 32))
        __explosion_anim.append(img)
    __assets['explosion_anim'] = __explosion_anim

def __load_score_font():
    __assets['score_font'] = pygame.font.Font(
        '../assets/font/PressStart2P.ttf', 28)

def __load_sfx():
    __assets['boom_sound'] = pygame.mixer.Sound('../assets/sfx/expl3.wav')
    __assets['destroy_sound'] = pygame.mixer.Sound('../assets/sfx/expl6.wav')
    __assets['pew_sound'] = pygame.mixer.Sound('../assets/sfx/pew.wav')

def load_assets():
    ''' Dynamic sprites '''
    __load_enemy_sprites()
    __load_hero_sprites()
    __load_bullet_sprites()

    ''' Static sprites '''
    __load_background_sprites()
    __load_btn_sprites()
    
##    __assets['save_img_0'] = pygame.image.load('../assets/img/save_btn_img_0.png').convert_alpha()
##    __assets['save_img_0'] = pygame.transform.scale(__assets['save_img_0'], (main_menu_btn_w, main_menu_btn_h))
##    __assets['save_img_1'] = pygame.image.load('../assets/img/save_btn_img_1.png').convert_alpha()
##    __assets['save_img_1'] = pygame.transform.scale(__assets['save_img_1'], (main_menu_btn_w, main_menu_btn_h))

    ''' Animations '''
    __load_explosion_sprites()

    ''' Fonts '''
    __load_score_font()

    ''' Sfx '''
    __load_sfx()

    return __assets
