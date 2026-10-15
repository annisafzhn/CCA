# Session 08 — Pixel-Perfect Collisions

## Space Shooter: Making Collisions More Precise

This session continues the Space Shooter OOP project from the previous session.

The starter code keeps the existing movement system, sprite groups, lasers, and asteroids. Students will upgrade the collision detection from rectangle-based checks to pixel-perfect collision checks using `pygame.mask`.

## Starting Point

The starter code already has:

- `Player`, `Laser`, and `Asteroid` classes
- `pygame.sprite.Group()` to manage sprites
- `rect` for drawing, positioning, and rectangle-based collision
- `pygame.Vector2` to store positions
- movement using delta time (`dt`)
- rectangle-based collision checks between lasers, asteroids, and the player

## The Collision Problem

A sprite's `Rect` is a rectangular boundary. It does not match every detail of the visible sprite shape.

Rectangle collision checks whether two rectangles overlap:

```python
player.rect.colliderect(enemy.rect)
```

This method is fast and useful, but it may detect a collision even when the visible parts of irregular sprites do not touch.

## Pixel-Perfect Collision

A collision mask represents the opaque pixels of a sprite. Transparent areas are ignored.

### Step 1 — Create a Mask

Create a mask from the sprite image:

```python
self.mask = pygame.mask.from_surface(self.image)
```

### Step 2 — Check the Collision

Check whether two sprite masks overlap:

```python
pygame.sprite.collide_mask(player, enemy)
```

This returns a collision point when the masks overlap, or `None` when they do not.

Both sprites need suitable images and masks for accurate results. If a sprite's image changes, its mask may need to be updated as well.

## Using Sprite Groups

To check one sprite against a group using pixel-perfect collision:

```python
hits = pygame.sprite.spritecollide(
    player,
    enemies,
    False,
    pygame.sprite.collide_mask
)
```

- `pygame.mask.from_surface()` creates a mask from an image.
- `pygame.sprite.collide_mask()` checks mask overlap between two sprites.
- `pygame.sprite.spritecollide()` checks a sprite against a group.
- `colliderect()` checks rectangle overlap.

## Session 08 Goals

Students will:

- Understand the limitations of rectangle-based collision detection.
- Compare rectangle collisions and pixel-perfect collisions.
- Create collision masks using `pygame.mask`.
- Detect collisions between irregular sprite shapes.
- Upgrade and test collision detection in an existing game.
- Consider accuracy and performance when choosing a collision method.

## Project Flow

```text
BUILD
  ↓
RUN
  ↓
TEST
  ↓
COMPARE
  ↓
IMPROVE
```

Recommended build order:

1. Find a collision that feels inaccurate.
2. Create masks for the relevant sprites.
3. Replace the appropriate rectangle collision check with mask-based detection.
4. Test different sprite positions.
5. Compare the results before and after the change.
6. Optional: compare performance and decide which objects need pixel-perfect collision.

## Controls

- WASD / Arrow Keys = Move
- Space = Shoot

## Folder Structure

```text
Session_08_Pixel_Perfect_Collisions/
├── space_shooter.py
├── README.md
└── assets/
    ├── space_background.png
    ├── player_ship.png
    ├── laser.png
    ├── asteroid_1.png
    ├── asteroid_2.png
    └── asteroid_3.png
```

## Run

Install Pygame if needed:

```powershell
pip install pygame
```

Then run:

```powershell
python space_shooter.py
```

## Main Lesson

The main idea of Session 08 is:

```text
RECTANGLE COLLISION
        ↓
   COLLISION MASK
        ↓
PIXEL-PERFECT COLLISION
```

Rectangle collisions are fast and useful for simple shapes. Pixel-perfect collisions use masks to check whether opaque pixels overlap, making them more precise for irregular sprite shapes. Because mask checks can require more processing, use them where precision matters.
