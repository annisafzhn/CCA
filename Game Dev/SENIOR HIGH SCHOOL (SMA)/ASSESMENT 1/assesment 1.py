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
pygame.display.set_caption("Space Shooter - Assessment")

clock = pygame.time.Clock()

ASSET_DIR = Path(__file__).parent / "assets"

background = pygame.image.load(
    str(ASSET_DIR / "space_background.png")
).convert()

ship_image = pygame.image.load(
    str(ASSET_DIR / "player_ship.png")
).convert_alpha()

laser_image = pygame.image.load(
    str(ASSET_DIR / "laser.png")
).convert_alpha()

asteroid_images = [
    pygame.image.load(
        str(ASSET_DIR / "asteroid_1.png")
    ).convert_alpha(),
    pygame.image.load(
        str(ASSET_DIR / "asteroid_2.png")
    ).convert_alpha(),
    pygame.image.load(
        str(ASSET_DIR / "asteroid_3.png")
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

        self.position = pygame.Vector2(self.rect.center)
        self.velocity = pygame.Vector2(0, 0)

        self.acceleration = 600
        self.max_speed = 350

        # Retention factor per 1/60-second frame.
        self.friction = 0.90

    def update(self, dt):
        keys = pygame.key.get_pressed()

        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction.x -= 1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction.x += 1

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            direction.y -= 1

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            direction.y += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()

            self.velocity += (
                direction * self.acceleration * dt
            )

            # Limit the player's speed.
            if self.velocity.length() > self.max_speed:
                self.velocity.scale_to_length(self.max_speed)

        else:
            # Apply frame-rate-independent friction
            # when no movement key is pressed.
            self.velocity *= self.friction ** (dt * FPS)

        # Update position using delta time.
        self.position += self.velocity * dt

        # Keep the player inside the screen.
        half_width = self.rect.width / 2
        half_height = self.rect.height / 2

        if self.position.x < half_width:
            self.position.x = half_width
            self.velocity.x = max(0, self.velocity.x)

        elif self.position.x > WIDTH - half_width:
            self.position.x = WIDTH - half_width
            self.velocity.x = min(0, self.velocity.x)

        if self.position.y < half_height:
            self.position.y = half_height
            self.velocity.y = max(0, self.velocity.y)

        elif self.position.y > HEIGHT - half_height:
            self.position.y = HEIGHT - half_height
            self.velocity.y = min(0, self.velocity.y)

        self.rect.center = (
            round(self.position.x),
            round(self.position.y)
        )


# ============================================================
# LASER
# ============================================================

class Laser(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()

        self.image = laser_image
        self.rect = self.image.get_rect(center=position)

        self.position = pygame.Vector2(self.rect.center)
        self.speed = 500

    def update(self, dt):
        self.position.y -= self.speed * dt

        self.rect.center = (
            round(self.position.x),
            round(self.position.y)
        )

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
            midtop=(
                random.randint(0, WIDTH - self.image.get_width()),
                -self.image.get_height()
            )
        )

        self.position = pygame.Vector2(self.rect.center)
        self.speed = random.randint(120, 220)

    def update(self, dt):
        self.position.y += self.speed * dt

        self.rect.center = (
            round(self.position.x),
            round(self.position.y)
        )

        if self.rect.top > HEIGHT:
            self.kill()


# ============================================================
# SPRITE GROUPS
# ============================================================

all_sprites = pygame.sprite.Group()
lasers = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


# ============================================================
# ASTEROID SPAWNING
# ============================================================

spawn_timer = 0
spawn_interval = 0.8


# ============================================================
# GAME LOOP
# ============================================================

running = True

while running:

    dt = min(clock.tick(FPS) / 1000, 0.05)

    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser = Laser(player.rect.midtop)

                all_sprites.add(laser)
                lasers.add(laser)

    # --------------------------------------------------------
    # SPAWN ASTEROIDS
    # --------------------------------------------------------

    spawn_timer += dt

    while spawn_timer >= spawn_interval:
        spawn_timer -= spawn_interval

        asteroid = Asteroid()

        all_sprites.add(asteroid)
        asteroids.add(asteroid)

    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    all_sprites.update(dt)

    # --------------------------------------------------------
    # COLLISIONS — RECTANGLE-BASED STARTER
    # Replace these with pixel-perfect collision detection.
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


# ============================================================
# QUIT
# ============================================================

pygame.quit()