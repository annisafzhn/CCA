import pygame
import random

pygame.init()

# =========================
# WINDOW
# =========================

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter - OOP")

clock = pygame.time.Clock()

# =========================
# PLAYER CLASS
# =========================

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((50, 200, 255))

        self.rect = self.image.get_rect(
            center=(400, 525)
        )

        self.speed = 300

    def update(self, dt):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt

        # Keep player inside screen
        self.rect.x = max(
            0,
            min(self.rect.x, 750)
        )


# =========================
# LASER CLASS
# =========================

class Laser(pygame.sprite.Sprite):

    def __init__(self, position):

        super().__init__()

        self.image = pygame.Surface((6, 20))
        self.image.fill((255, 50, 50))

        self.rect = self.image.get_rect(
            center=position
        )

        self.speed = 500

    def update(self, dt):

        self.rect.y -= self.speed * dt

        # Remove laser when it leaves screen
        if self.rect.bottom < 0:
            self.kill()


# =========================
# ASTEROID CLASS
# =========================

class Asteroid(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((150, 150, 150))

        x = random.randint(25, 775)

        self.rect = self.image.get_rect(
            center=(x, -25)
        )

        self.speed = 200

    def update(self, dt):

        self.rect.y += self.speed * dt

        # Remove asteroid when it leaves screen
        if self.rect.top > 600:
            self.kill()


# =========================
# SPRITE GROUPS
# =========================

all_sprites = pygame.sprite.Group()

lasers = pygame.sprite.Group()

asteroids = pygame.sprite.Group()


# =========================
# CREATE PLAYER
# =========================

player = Player()

all_sprites.add(player)


# =========================
# ASTEROID SPAWN TIMER
# =========================

spawn_timer = 0


# =========================
# GAME LOOP
# =========================

running = True

while running:

    # Delta Time
    dt = clock.tick(60) / 1000

    # =========================
    # EVENTS
    # =========================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Shoot laser
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                laser = Laser(
                    player.rect.midtop
                )

                all_sprites.add(laser)
                lasers.add(laser)

    # =========================
    # SPAWN ASTEROIDS
    # =========================

    spawn_timer += dt

    if spawn_timer >= 1:

        asteroid = Asteroid()

        all_sprites.add(asteroid)
        asteroids.add(asteroid)

        spawn_timer = 0

    # =========================
    # UPDATE
    # =========================

    all_sprites.update(dt)

    # =========================
    # COLLISION
    # =========================

    pygame.sprite.groupcollide(
        lasers,
        asteroids,
        True,
        True
    )

    # =========================
    # DRAW
    # =========================

    screen.fill((10, 10, 30))

    all_sprites.draw(screen)

    pygame.display.flip()


pygame.quit()