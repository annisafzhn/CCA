import pygame
import random

pygame.init()

# =========================
# WINDOW
# =========================

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter - Before Refactoring")

clock = pygame.time.Clock()

# =========================
# PLAYER
# =========================

player_x = 375
player_y = 500

player_width = 50
player_height = 50

player_speed = 5

# =========================
# LASERS
# =========================

lasers = []

laser_width = 6
laser_height = 20
laser_speed = 8

# =========================
# ASTEROIDS
# =========================

asteroids = []

asteroid_size = 50
asteroid_speed = 4

spawn_timer = 0

# =========================
# GAME LOOP
# =========================

running = True

while running:

    # Limit game to 60 FPS
    clock.tick(60)

    # =========================
    # EVENTS
    # =========================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Shoot laser
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                laser_x = player_x + player_width // 2 - laser_width // 2
                laser_y = player_y

                lasers.append([laser_x, laser_y])

    # =========================
    # PLAYER MOVEMENT
    # =========================

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player inside screen
    if player_x < 0:
        player_x = 0

    if player_x > 750:
        player_x = 750

    # =========================
    # UPDATE LASERS
    # =========================

    for laser in lasers:

        laser[1] -= laser_speed

    # Remove lasers outside screen
    lasers = [
        laser for laser in lasers
        if laser[1] > -laser_height
    ]

    # =========================
    # SPAWN ASTEROIDS
    # =========================

    spawn_timer += 1

    if spawn_timer >= 60:

        asteroid_x = random.randint(0, 750)
        asteroid_y = -asteroid_size

        asteroids.append([asteroid_x, asteroid_y])

        spawn_timer = 0

    # =========================
    # UPDATE ASTEROIDS
    # =========================

    for asteroid in asteroids:

        asteroid[1] += asteroid_speed

    # Remove asteroids outside screen
    asteroids = [
        asteroid for asteroid in asteroids
        if asteroid[1] < 600
    ]

    # =========================
    # COLLISION
    # =========================

    for laser in lasers[:]:

        laser_rect = pygame.Rect(
            laser[0],
            laser[1],
            laser_width,
            laser_height
        )

        for asteroid in asteroids[:]:

            asteroid_rect = pygame.Rect(
                asteroid[0],
                asteroid[1],
                asteroid_size,
                asteroid_size
            )

            if laser_rect.colliderect(asteroid_rect):

                lasers.remove(laser)
                asteroids.remove(asteroid)

                break

    # =========================
    # DRAW
    # =========================

    screen.fill((10, 10, 30))

    # Draw player
    pygame.draw.rect(
        screen,
        (50, 200, 255),
        (
            player_x,
            player_y,
            player_width,
            player_height
        )
    )

    # Draw lasers
    for laser in lasers:

        pygame.draw.rect(
            screen,
            (255, 50, 50),
            (
                laser[0],
                laser[1],
                laser_width,
                laser_height
            )
        )

    # Draw asteroids
    for asteroid in asteroids:

        pygame.draw.circle(
            screen,
            (150, 150, 150),
            (
                asteroid[0] + asteroid_size // 2,
                asteroid[1] + asteroid_size // 2
            ),
            asteroid_size // 2
        )

    pygame.display.flip()

pygame.quit()