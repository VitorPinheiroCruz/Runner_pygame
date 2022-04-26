import pygame
from sys import exit
# import random

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()  # estabelece os FPS
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'black')  # .render(text, AA, color)

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600,300))
# snail_x_pos = 600
# snail_y_pos = 270

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom= (80, 300))
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Vc clicou no x')
            pygame.quit()
            exit()

    screen.blit(ground_surface, (0, 300))
    screen.blit(sky_surface, (0, 0))  # .blit(surface, position)
    screen.blit(text_surface, (300, 50))
    # snail_x_pos -= 4
    # if snail_x_pos < -50:
    #     snail_x_pos = 800
    #     snail_y_pos = random.randint(270, 360)
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)
    snail_rect.x -= 4
    if snail_rect.right < 0: snail_rect.left = 800

    1:03:50

    pygame.display.update()
    clock.tick(60)
