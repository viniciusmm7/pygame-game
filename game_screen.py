import pygame

from config import *
from assets import *
from sprites import *
from game_over_screen import *
from pause_screen import *

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
    pygame.mixer.quit()