import pygame, random
from assets import *
from config import *

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