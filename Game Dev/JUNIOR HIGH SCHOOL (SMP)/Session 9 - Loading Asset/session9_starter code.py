import pygame

pygame.init()

# ==================================================
# 1. SET UP THE GAME WINDOW
# ==================================================
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Sprite Game")

clock = pygame.time.Clock()

# ==================================================
# 2. LOAD YOUR IMAGES
# ==================================================
# HINT:
# Use pygame.image.load("folder/filename.png")
# Load the background and player image here.


# ==================================================
# 3. PLAYER SETTINGS
# ==================================================
player_x = 375
player_y = 450
player_speed = 5

# HINT:
# If your image is too large, you can resize it with:
# pygame.transform.scale(image, (new_width, new_height))
# Try making your player image 60 x 60.


# ==================================================
# 4. GAME LOOP
# ==================================================
running = True

while running:

    # A. HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # B. PLAYER MOVEMENT
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    # C. DRAW THE BACKGROUND
    # HINT:
    # Use screen.blit(image, (x, y))
    # The background should start at position (0, 0).


    # D. DRAW THE PLAYER
    # HINT:
    # Use screen.blit(player_image, (player_x, player_y))
    # Put this AFTER drawing the background.


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
