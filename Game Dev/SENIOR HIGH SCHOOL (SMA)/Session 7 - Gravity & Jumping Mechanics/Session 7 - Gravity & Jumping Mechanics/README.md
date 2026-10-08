# Session 07 — Gravity & Jumping Mechanics

## Space Shooter: Building Responsive Jumping with Physics

This version continues the Space Shooter OOP project from Session 06.

The starter code is the **Session 06 result**. It keeps the custom physics system from the previous session so students can build gravity and jumping mechanics on top of it.

## Starting Point

The Player already has:

- `velocity` to store current movement
- `acceleration` to change velocity
- `friction` to reduce velocity over time
- `position` using `pygame.Vector2`
- `rect` for drawing and collision
- movement using `velocity * dt`

## Movement Model

```text
Input
  ↓
Acceleration
  ↓
Velocity
  ↓
Friction
  ↓
Position
```

In Session 07, students extend this system with gravity and jumping:

```text
Gravity
   ↓
Vertical Velocity
   ↓
Vertical Position
   ↓
Jump / Fall / Land
```

### Core Physics from Session 06

```python
self.velocity += acceleration * dt
```

```python
self.velocity *= self.friction
```

```python
self.position += self.velocity * dt
```

## Session 07 Goals

Students will build:

- Gravity for downward movement
- A jump using upward vertical velocity
- Ground detection
- A controllable jump height
- More responsive jumping through optional mechanics

### Main Session 07 Formulas

Gravity changes vertical velocity:

```python
velocity.y += gravity * dt
```

Jump starts with upward velocity:

```python
velocity.y = -jump_strength
```

Velocity changes vertical position:

```python
position.y += velocity.y * dt
```

When the player reaches the ground, downward velocity should be stopped:

```python
velocity.y = 0
```

## Project Flow

```text
BUILD
  ↓
RUN
  ↓
OBSERVE
  ↓
MODIFY
  ↓
REPEAT
```

Recommended build order:

1. Add gravity
2. Add jumping
3. Add ground detection
4. Tune the physics
5. Optional: add variable jump height or coyote time

## Controls

- WASD / Arrow Keys = Move
- Space = Jump / Session 07

## Folder Structure

```text
Session_07_Gravity_Jumping/
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

Then:

```powershell
python space_shooter.py
```

## Main Lesson

The main idea of Session 07 is:

```text
GRAVITY
   ↓
VELOCITY
   ↓
POSITION
```

Gravity changes vertical velocity.  
Velocity changes the player's position.  
Jumping starts by giving the player upward velocity.

The goal is not only to make the jump work, but to make the movement feel good to play.
