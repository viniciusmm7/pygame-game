# ===== Initializing =====
# ----- Import and launch packages
import pygame, random
from os import path

pygame.init()
pygame.mixer.init()
clock   = pygame.time.Clock()
FPS     = 60
VOLUME  = 1.0 # Have to be a float number between 0 and 1
STILL   = 0
JUMPING = MOVING = 1

# ----- Geometry
window_width  = 1000
window_height = 1000
hero_width    = 150
hero_height   = 150
enemy_width   = int(hero_width * 2/3)
enemy_height  = int(hero_height * 2/3)
gravity       = window_height // 225
vi_jump       = 13 * gravity

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

# ----- Assets
pygame.mixer.music.load('assets/music/other_pause_theme.wav')
##pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)
def load_assets():
    assets = {}
    ''' Game related imgs '''
    assets['enemy_img']         = pygame.image.load('assets/img/enemy.png').convert_alpha()
    assets['enemy_img']         = pygame.transform.scale(assets['enemy_img'], (enemy_width, enemy_height))
    assets['enemy_left_img_0']  = pygame.image.load('assets/img/enemy_left_0.png').convert_alpha()
    assets['enemy_left_img_0']  = pygame.transform.scale(assets['enemy_left_img_0'], (enemy_width, enemy_height))
    assets['enemy_left_img_1']  = pygame.image.load('assets/img/enemy_left_1.png').convert_alpha()
    assets['enemy_left_img_1']  = pygame.transform.scale(assets['enemy_left_img_1'], (enemy_width, enemy_height))
    assets['enemy_right_img_0'] = pygame.image.load('assets/img/enemy_right_0.png').convert_alpha()
    assets['enemy_right_img_0'] = pygame.transform.scale(assets['enemy_right_img_0'], (enemy_width, enemy_height))
    assets['enemy_right_img_1'] = pygame.image.load('assets/img/enemy_right_1.png').convert_alpha()
    assets['enemy_right_img_1'] = pygame.transform.scale(assets['enemy_right_img_1'], (enemy_width, enemy_height))

    assets['hero_left_img']     = pygame.image.load('assets/img/hero_left.png').convert_alpha()
    assets['hero_left_img']     = pygame.transform.scale(assets['hero_left_img'], (hero_width, hero_height))
    assets['hero_right_img']    = pygame.image.load('assets/img/hero_right.png').convert_alpha()
    assets['hero_right_img']    = pygame.transform.scale(assets['hero_right_img'], (hero_width, hero_height))

    assets['bullet_left_img']   = pygame.image.load('assets/img/bullet_left.png').convert_alpha()
    assets['bullet_left_img']   = pygame.transform.scale(assets['bullet_left_img'], (hero_height//3, hero_width//3))
    assets['bullet_right_img']  = pygame.image.load('assets/img/bullet_right.png').convert_alpha()
    assets['bullet_right_img']  = pygame.transform.scale(assets['bullet_right_img'], (hero_height//3, hero_width//3))

    ''' Other imgs '''
    assets['background_day']    = pygame.image.load('assets/img/background_day.png').convert()
    assets['background_day']    = pygame.transform.scale(assets['background_day'], (window_width, window_height))
    assets['background_day_1']  = pygame.image.load('assets/img/background_day_1.png').convert()
    assets['background_day_1']  = pygame.transform.scale(assets['background_day_1'], (7*window_width, window_height))
    assets['background_night']  = pygame.image.load('assets/img/background_night.png').convert()
    assets['background_night']  = pygame.transform.scale(assets['background_night'], (window_width, window_height))
    assets['play_img_0']        = pygame.image.load('assets/img/play_0.png').convert_alpha()
    assets['play_img_0']        = pygame.transform.scale(assets['play_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['play_img_1']        = pygame.image.load('assets/img/play_1.png').convert_alpha()
    assets['play_img_1']        = pygame.transform.scale(assets['play_img_1'], (main_menu_btn_w, main_menu_btn_h))
    assets['options_img_0']     = pygame.image.load('assets/img/options_0.png').convert_alpha()
    assets['options_img_0']     = pygame.transform.scale(assets['options_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['options_img_1']     = pygame.image.load('assets/img/options_1.png').convert_alpha()
    assets['options_img_1']     = pygame.transform.scale(assets['options_img_1'], (main_menu_btn_w, main_menu_btn_h))
    assets['quit_img_0']        = pygame.image.load('assets/img/quit_0.png').convert_alpha()
    assets['quit_img_0']        = pygame.transform.scale(assets['quit_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['quit_img_1']        = pygame.image.load('assets/img/quit_1.png').convert_alpha()
    assets['quit_img_1']        = pygame.transform.scale(assets['quit_img_1'], (main_menu_btn_w, main_menu_btn_h))
    assets['languages_img_0']   = pygame.image.load('assets/img/language_0.png').convert_alpha()
    assets['languages_img_0']   = pygame.transform.scale(assets['languages_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['languages_img_1']   = pygame.image.load('assets/img/language_1.png').convert_alpha()
    assets['languages_img_1']   = pygame.transform.scale(assets['languages_img_1'], (main_menu_btn_w, main_menu_btn_h))
    assets['resume_img_0']      = pygame.image.load('assets/img/resume_0.png').convert_alpha()
    assets['resume_img_0']      = pygame.transform.scale(assets['resume_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['resume_img_1']      = pygame.image.load('assets/img/resume_1.png').convert_alpha()
    assets['resume_img_1']      = pygame.transform.scale(assets['resume_img_1'], (main_menu_btn_w, main_menu_btn_h))
    assets['yes_img_0']         = pygame.image.load('assets/img/yes_0.png').convert_alpha()
    assets['yes_img_0']         = pygame.transform.scale(assets['yes_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['yes_img_1']         = pygame.image.load('assets/img/yes_1.png').convert_alpha()
    assets['yes_img_1']         = pygame.transform.scale(assets['yes_img_1'], (main_menu_btn_w, main_menu_btn_h))
    assets['no_img_0']          = pygame.image.load('assets/img/no_0.png').convert_alpha()
    assets['no_img_0']          = pygame.transform.scale(assets['no_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['no_img_1']          = pygame.image.load('assets/img/no_1.png').convert_alpha()
    assets['no_img_1']          = pygame.transform.scale(assets['no_img_1'], (main_menu_btn_w, main_menu_btn_h))
    assets['x_img_0']           = pygame.image.load('assets/img/x_0.png').convert_alpha()
    assets['x_img_0']           = pygame.transform.scale(assets['x_img_0'], (main_menu_btn_h, main_menu_btn_h))
    assets['x_img_1']           = pygame.image.load('assets/img/x_1.png').convert_alpha()
    assets['x_img_1']           = pygame.transform.scale(assets['x_img_1'], (main_menu_btn_h, main_menu_btn_h))
    assets['muted_img_0']       = pygame.image.load('assets/img/muted_0.png').convert_alpha()
    assets['muted_img_0']       = pygame.transform.scale(assets['muted_img_0'] , (main_menu_btn_h, main_menu_btn_h))
    assets['muted_img_1']       = pygame.image.load('assets/img/muted_1.png').convert_alpha()
    assets['muted_img_1']       = pygame.transform.scale(assets['muted_img_1'] , (main_menu_btn_h, main_menu_btn_h))
    assets['unmuted_img_0']     = pygame.image.load('assets/img/unmuted_0.png').convert_alpha()
    assets['unmuted_img_0']     = pygame.transform.scale(assets['unmuted_img_0'] , (main_menu_btn_h, main_menu_btn_h))
    assets['unmuted_img_1']     = pygame.image.load('assets/img/unmuted_1.png').convert_alpha()
    assets['unmuted_img_1']     = pygame.transform.scale(assets['unmuted_img_1'] , (main_menu_btn_h, main_menu_btn_h))
    assets['select_size_img_0'] = pygame.image.load('assets/img/size_0.png').convert_alpha()
    assets['select_size_img_0'] = pygame.transform.scale(assets['select_size_img_0'], (main_menu_btn_w, main_menu_btn_h))
    assets['select_size_img_1'] = pygame.image.load('assets/img/size_1.png').convert_alpha()
    assets['select_size_img_1'] = pygame.transform.scale(assets['select_size_img_1'], (main_menu_btn_w, main_menu_btn_h))
##    assets['save_img_0']        = pygame.image.load('assets/img/save_btn_img_0.png').convert_alpha()
##    assets['save_img_0']        = pygame.transform.scale(assets['save_img_0'], (main_menu_btn_w, main_menu_btn_h))
##    assets['save_img_1']        = pygame.image.load('assets/img/save_btn_img_1.png').convert_alpha()
##    assets['save_img_1']        = pygame.transform.scale(assets['save_img_1'], (main_menu_btn_w, main_menu_btn_h))
    explosion_anim = []
    for i in range(9):
        filename = 'assets/img/regularExplosion0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets['explosion_anim'] = explosion_anim

    assets['score_font']     = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

    ''' Sfx '''
    assets['boom_sound']     = pygame.mixer.Sound('assets/sfx/expl3.wav')
    assets['destroy_sound']  = pygame.mixer.Sound('assets/sfx/expl6.wav')
    assets['pew_sound']      = pygame.mixer.Sound('assets/sfx/pew.wav')
    
    return assets

''' Classes '''
class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image        = assets['hero_right_img']
        self.mask         = pygame.mask.from_surface(self.image)
        self.rect         = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom  = window_height - 155
        self.speedx       = 0
        self.speedy       = 0
        self.groups       = groups
        self.assets       = assets
        self.state        = STILL

        self.last_shot    = pygame.time.get_ticks()
        self.shoot_ticks  = 100

    def update(self):
        self.speedy += gravity
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > window_width:
            self.rect.right = window_width
            
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > window_height - 155:
            self.rect.bottom = window_height - 155
            self.speedy      = 0
            self.state       = STILL

    def shoot(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:
            self.last_shot = now
            new_bullet = Bullet(self.assets, self.rect.centery, self.rect.centerx)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_bullets'].add(new_bullet)
            self.assets['pew_sound'].play()

    def jump(self):
        if self.state == STILL:
            self.speedy -= vi_jump
            self.state   = JUMPING


class Camera(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image     = assets['background_day_1']
        self.mask      = pygame.mask.from_surface(self.image)
        self.rect      = self.image.get_rect()
        self.rect.left = 0
        self.rect.top  = 0
        self.speedx    = 0
        self.state     = STILL

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < window_width:
            self.rect.right = window_width

        if self.rect.left > 0:
            self.rect.left = 0

    def move(self):
        if self.state == STILL:
            self.state = MOVING


class Enemy(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image       = assets['enemy_img']
        self.mask        = pygame.mask.from_surface(self.image)
        self.rect        = self.image.get_rect()
        self.rect.x      = random.randint(int(window_width * 2/3), window_width - enemy_width)
        self.rect.bottom = window_height - 155
        self.speedx      = 8
        self.state       = STILL

    def update(self):
        self.rect.x -= self.speedx

        if self.rect.right < 0 or self.rect.left > window_width:
            self.rect.x      = random.randint(int(window_width * 2/3), window_width - enemy_width)
            self.rect.bottom = window_height - 155
            self.speedx      = 8

    def paralax(self):
        if self.state == STILL:
            self.rect.x -= self.speedx
            self.state = MOVING

class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_right_img']
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect  = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedx       = 25

    def update(self):
        self.rect.x += self.speedx
        
        if self.rect.left > window_width:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        pygame.sprite.Sprite.__init__(self)

        self.explosion_anim = assets['explosion_anim']

        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect  = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 50

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1

            if self.frame == len(self.explosion_anim):
                self.kill()
            else:
                center           = self.rect.center
                self.image       = self.explosion_anim[self.frame]
                self.rect        = self.image.get_rect()
                self.rect.center = center

''' Functions '''
def main_menu():
    RUNNING = 1
    QUIT    = 0
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
                    settings()
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

        play_btn     = pygame.draw.rect(window, INSPER_RED, (play_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))
        settings_btn = pygame.draw.rect(window, INSPER_RED, (settings_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))
        quit_btn     = pygame.draw.rect(window, INSPER_RED, (quit_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))

        window.blit(assets['background_day'], (0, 0))
        window.blit(game_name, game_name_pos)
        
        if PLAY_CLICK == False:
            window.blit(assets['play_img_0'], (play_btn_pos_left, btns_layer))
        else:
            window.blit(assets['play_img_1'], (play_btn_pos_left, btns_layer))

        if OPTIONS_CLICK == False:
            window.blit(assets['options_img_0'], (settings_btn_pos_left, btns_layer))
        else:
            window.blit(assets['options_img_1'], (settings_btn_pos_left, btns_layer))

        if QUIT_CLICK == False:
            window.blit(assets['quit_img_0'], (quit_btn_pos_left, btns_layer))
        else:
            window.blit(assets['quit_img_1'], (quit_btn_pos_left, btns_layer))
        
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


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
                    game()
                else:
                    YES_CLICK = False

                if no_btn.collidepoint(x, y):
                    main_menu()
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


def game():
    EXPLODING = 2
    RUNNING   = 1
    QUIT      = 0
    
    state = RUNNING

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_meteors'] = all_enemies
    groups['all_bullets'] = all_bullets

    camera = Camera(groups, assets)
    player = Hero(groups, assets)
    enemy = Enemy(assets)
    
    all_sprites.add(player)
    all_sprites.add(camera)

    score = 0
    lives = 15
    number_of_enemies = 3
    keys_down = {}

    for i in range(number_of_enemies):
        enemy = Enemy(assets)
        all_sprites.add(enemy)
        all_enemies.add(enemy)
    
    while state != QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                
                if event.key == pygame.K_ESCAPE:
                    pause()

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.jump()

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    camera.speedx += 8
                    enemy.speedx -= 8
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    camera.speedx -= 8
                    enemy.speedx += 8
                    
                if event.key == pygame.K_SPACE:
                    player.shoot()

            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        camera.speedx -= 8
                        enemy.speedx += 8

                    if event.key == pygame.K_RIGHT:
                        camera.speedx += 8
                        enemy.speedx -= 8

        all_sprites.update()

        if state == RUNNING:
            hits = pygame.sprite.groupcollide(all_enemies, all_bullets, True, True, pygame.sprite.collide_mask)
            for enemy in hits:
                assets['destroy_sound'].play()
                e = Enemy(assets)
                all_sprites.add(e)
                all_enemies.add(e)

                explosion = Explosion(enemy.rect.center, assets)
                all_sprites.add(explosion)

                score += 100
                if score % 1000 == 0:
                    lives += 1

            hits = pygame.sprite.spritecollide(player, all_enemies, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                assets['boom_sound'].play()
                player.kill()
                lives -= 1
                explosion = Explosion(player.rect.center, assets)
                all_sprites.add(explosion)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosion.frame_ticks * len(explosion.explosion_anim) + 50

        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    game_over()
                else:
                    state = RUNNING
                    player = Hero(groups, assets)
                    all_sprites.add(player)
                    enemy = Enemy(assets)
                    all_sprites.add(enemy)
                    all_enemies.add(enemy)

        window.blit(assets['background_day_1'], (0, 0))
        all_sprites.draw(window)

        text_surface = assets['score_font'].render('{:08d}'.format(score), True, WHITE)
        text_rect    = text_surface.get_rect()
        text_rect.midtop = (window_width/2, 10)
        window.blit(text_surface, text_rect)

        text_surface = assets['score_font'].render(chr(9829) * lives, True, INSPER_RED)
        text_rect    = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


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
                    main_menu()
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


def select_size():
    RUNNING = 1
    QUIT    = 0

    X_CLICK = False
    state   = RUNNING

    assets  = load_assets()
    
    while state != QUIT:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

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

def pause():
    RUNNING = 1
    QUIT    = 0
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

        menu_btn = pygame.draw.rect(window, INSPER_RED, (play_btn_pos_left, btns_layer, main_menu_btn_w, main_menu_btn_h))
        resume_btn = pygame.draw.rect(window, INSPER_RED, (play_btn_pos_left, btns_layer - window_height / 2 + main_menu_btn_h/4, main_menu_btn_w, main_menu_btn_h))
        window.blit(assets['background_day'], (0, 0))
        
        if RESUME_CLICK == False:
            window.blit(assets['resume_img_0'], (play_btn_pos_left, btns_layer - window_height / 2 + main_menu_btn_h/4))
        else:
            window.blit(assets['resume_img_1'], (play_btn_pos_left, btns_layer - window_height / 2 + main_menu_btn_h/4))

        if MENU_CLICK == False:
            window.blit(assets['quit_img_0'], (play_btn_pos_left, btns_layer))
        else:
            window.blit(assets['quit_img_1'], (play_btn_pos_left, btns_layer))
        
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

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

main_menu()
pygame.mixer.quit()