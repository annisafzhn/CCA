import random
from pathlib import Path

import pygame


# ============================================================
# SETUP
# ============================================================

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Gravity & Jumping")

clock = pygame.time.Clock()

# Always load assets relative to this .py file.
ASSET_DIR = Path(__file__).parent / "assets"

background = pygame.image.load(
    ASSET_DIR / "space_background.png"
).convert()

ship_image = pygame.image.load(
    ASSET_DIR / "player_ship.png"
).convert_alpha()

laser_image = pygame.image.load(
    ASSET_DIR / "laser.png"
).convert_alpha()

asteroid_images = [
    pygame.image.load(
        ASSET_DIR / "asteroid_1.png"
    ).convert_alpha(),

    pygame.image.load(
        ASSET_DIR / "asteroid_2.png"
    ).convert_alpha(),

    pygame.image.load(
        ASSET_DIR / "asteroid_3.png"
    ).convert_alpha(),
]


# ============================================================
# PLAYER
# ============================================================

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = ship_image
        self.rect = self.image.get_rect(
            center=(WIDTH // 2, HEIGHT - 80)
        )

        # Vector2 stores the player's precise position.
        self.position = pygame.Vector2(self.rect.center)

        # NEW: Velocity stores the current movement.
        self.velocity = pygame.Vector2(0, 0)

        # Physics settings.
        self.acceleration = 600
        self.friction = 0.90

    def update(self, dt):

        keys = pygame.key.get_pressed()

        # NEW: Acceleration is created from player input.
        acceleration = pygame.Vector2(0, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            acceleration.x -= self.acceleration

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            acceleration.x += self.acceleration

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            acceleration.y -= self.acceleration

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            acceleration.y += self.acceleration

        # NEW: Acceleration changes velocity.
        self.velocity += acceleration * dt

        # NEW: Friction gradually reduces velocity.
        self.velocity *= self.friction

        # NEW: Velocity changes the position.
        self.position += self.velocity * dt

        # Keep the ship inside the screen.
        self.position.x = max(
            40,
            min(self.position.x, WIDTH - 40)
        )

        self.position.y = max(
            45,
            min(self.position.y, HEIGHT - 45)
        )

        # Rect is still used for drawing and collision.
        self.rect.center = self.position


# ============================================================
# LASER
# ============================================================

class Laser(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        self.image = laser_image
        self.rect = self.image.get_rect(center=position)

        # Vector2 stores the laser position.
        self.position = pygame.Vector2(self.rect.center)

        self.speed = 500

    def update(self, dt):

        self.position.y -= self.speed * dt
        self.rect.center = self.position

        if self.rect.bottom < 0:
            self.kill()


# ============================================================
# ASTEROID
# ============================================================

class Asteroid(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = random.choice(asteroid_images)
        self.rect = self.image.get_rect(
            center=(
                random.randint(40, WIDTH - 40),
                -50
            )
        )

        # Vector2 stores the asteroid position.
        self.position = pygame.Vector2(self.rect.center)

        self.speed = random.randint(120, 220)

    def update(self, dt):

        self.position.y += self.speed * dt
        self.rect.center = self.position

        if self.rect.top > HEIGHT:
            self.kill()


# ============================================================
# SPRITE GROUPS
# ============================================================

all_sprites = pygame.sprite.Group()
lasers = pygame.sprite.Group()
asteroids = pygame.sprite.Group()


# ============================================================
# CREATE PLAYER
# ============================================================

player = Player()
all_sprites.add(player)


# ============================================================
# ASTEROID SPAWN TIMER
# ============================================================

spawn_timer = 0


# ============================================================
# GAME LOOP
# ============================================================

running = True

while running:

    # Delta Time
    dt = clock.tick(FPS) / 1000

    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                laser = Laser(
                    player.rect.midtop
                )

                all_sprites.add(laser)
                lasers.add(laser)

    # --------------------------------------------------------
    # SPAWN ASTEROIDS
    # --------------------------------------------------------

    spawn_timer += dt

    if spawn_timer >= 0.8:

        asteroid = Asteroid()

        all_sprites.add(asteroid)
        asteroids.add(asteroid)

        spawn_timer = 0

    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    all_sprites.update(dt)

    # --------------------------------------------------------
    # COLLISION
    # --------------------------------------------------------

    pygame.sprite.groupcollide(
        lasers,
        asteroids,
        True,
        True
    )

    pygame.sprite.spritecollide(
        player,
        asteroids,
        True
    )

    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    screen.blit(background, (0, 0))

    all_sprites.draw(screen)

    pygame.display.flip()


pygame.quit()