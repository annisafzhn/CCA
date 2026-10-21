import pygame
import random

pygame.init()

# 1. Create the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge the Block")

clock = pygame.time.Clock()

# 2. Create the player
player_width = 50
player_height = 50
player_x = 375
player_y = 520
player_speed = 7

# 3. Create one falling block
block_width = 50
block_height = 50
block_x = random.randint(0, screen_width - block_width)
block_y = 0
block_speed = 5

running = True

while running:
    # A. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # B. Read keyboard input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    # TODO 1: Keep the player inside the screen.
    # Hint: The player's X position must stay between 0 and 750.


    # TODO 2: Make the block move down.
    # Hint: Increase block_y by block_speed.


    # TODO 3: When the block passes the bottom of the screen,
    # move it back to the top and choose a new X position.
    # Hint: Check whether block_y is greater than screen_height.


    # C. Draw the background and objects
    screen.fill((30, 30, 45))
    pygame.draw.rect(
        screen, (70, 180, 255),
        (player_x, player_y, player_width, player_height)
    )
    pygame.draw.rect(
        screen, (255, 90, 90),
        (block_x, block_y, block_width, block_height)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
