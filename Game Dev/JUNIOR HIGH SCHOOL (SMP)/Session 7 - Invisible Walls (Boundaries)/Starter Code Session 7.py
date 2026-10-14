import pygame

pygame.init()

# Game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Session 7 - Invisible Walls")

clock = pygame.time.Clock()

# Player settings
player_x = 375
player_y = 500

player_width = 50
player_height = 50
player_speed = 20

running = True

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                player_x += player_speed

            if event.key == pygame.K_LEFT:
                player_x -= player_speed

    # Draw everything
    screen.fill((20, 20, 30))

    pygame.draw.rect(
        screen,
        (50, 200, 255),
        (player_x, player_y, player_width, player_height)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
