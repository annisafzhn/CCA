import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_x = 100
player_y = 250

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_x += 5

    screen.fill((20, 20, 30))

    pygame.draw.rect(
        screen,
        (50, 200, 255),
        (player_x, player_y, 50, 50)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()