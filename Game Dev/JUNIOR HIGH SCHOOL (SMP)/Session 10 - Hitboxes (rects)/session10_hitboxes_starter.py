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
# Keep the image-loading code from Session 9.
# Use your own image filenames and asset paths.

# Example:
# background = pygame.image.load("assets/background.png")
# player_image = pygame.image.load("assets/player.png")

# If you resized your images in Session 9, keep that code too.


# ==================================================
# 3. PLAYER SETTINGS
# ==================================================
player_x = 375
player_y = 450
player_speed = 5

# ==================================================
# 4. CREATE THE PLAYER HITBOX
# ==================================================
# HINT 1:
# Create a Rect based on your player image.
# Use: player_image.get_rect()
#
# HINT 2:
# Set the hitbox position to match the player.
# Use: player_rect.topleft = (player_x, player_y)
#
# Write your code below:


# ==================================================
# 5. GAME LOOP
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

    # C. UPDATE THE HITBOX POSITION
    # HINT:
    # The hitbox must follow the player.
    # Update player_rect.topleft using player_x and player_y.
    # Write your code below:


    # D. DRAW THE BACKGROUND
    # Keep your Session 9 background drawing code here.
    # Example: screen.blit(background, (0, 0))


    # E. DRAW THE PLAYER
    # Keep your Session 9 player drawing code here.
    # Example: screen.blit(player_image, (player_x, player_y))


    # F. DEBUG: SHOW THE HITBOX
    # HINT:
    # Use pygame.draw.rect(screen, color, player_rect, 2)
    # This is only for checking the hitbox while developing.
    # Write your code below:


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
