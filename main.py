import pygame, sys
from player import player



def run_game():
    #breakpoint()

    screen = pygame.display.set_mode((1024, 512))
    player_image = pygame.image.load('blue.png').convert()
    background_image = pygame.image.load('back.jpg').convert()
    print(player_image.get_rect().width)
    print(player_image.get_rect().height)
    p = player(player_image, {'width': player_image.get_rect().width, 'height': player_image.get_rect().height}, {'x': 0, 'y': 0})

    while True:

        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_RIGHT:
            #         p.change_speed((10,0))
            #     elif event.key == pygame.K_LEFT:
            #         p.change_speed((-10,0))
        
        active_keys = pygame.key.get_pressed()
        if active_keys[pygame.K_RIGHT]:
            p.change_speed((1,0))
        elif active_keys[pygame.K_LEFT]:
            p.change_speed((-1,0))

        p.move((640, 480))
        screen.blit(background_image, (0, 0))
        screen.blit(p.image, p.pos)
        pygame.display.update()
        pygame.time.delay(100)

run_game()