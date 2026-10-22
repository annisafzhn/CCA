# Space Shooter — Developer Notes

Welcome to the Space Shooter project!

This file contains technical notes and reminders to help you understand the existing codebase. Use it as a reference while working on your project.

## 1. Understanding the Codebase

The project uses object-oriented programming and Pygame sprite groups.

Some useful places to explore:

- `Player`: player movement and keyboard input.
- `Laser`: laser movement and screen boundaries.
- `Asteroid`: asteroid movement and spawning.
- Main game loop: event handling, updating sprites, collision checks, and drawing.

**Think about it:** Which class should be responsible for movement? Where should collision detection take place?

## 2. Movement Physics

The starter code uses `pygame.Vector2` to represent position and velocity.

Useful concepts:

- **Position:** Where an object is located.
- **Velocity:** How quickly and in which direction an object moves.
- **Acceleration:** How velocity changes over time.
- **Delta time (`dt`):** The elapsed time between frames.

A common relationship in movement physics is:

`velocity += acceleration * dt`

Position can then be updated using:

`position += velocity * dt`

These relationships are useful starting points, but the final movement behavior depends on how your code handles input, velocity limits, and other movement conditions.

**Think about it:**
- Does your movement behave consistently at different frame rates?
- Does diagonal movement feel different from horizontal movement?
- What happens when the player releases the movement keys?

## 3. Friction

Friction in a game can gradually reduce an object's velocity.

One simple approach is to multiply velocity by a retention factor between `0` and `1`.

For example, a factor closer to `1` retains more velocity, while a smaller factor reduces velocity more quickly.

Remember that applying the same factor once per frame can make the result depend on frame rate. Consider how elapsed time affects your implementation.

**Think about it:**
- Does the player stop immediately or slow down gradually?
- Does friction behave consistently when the frame rate changes?
- Is friction applied when the player is actively moving, when no input is pressed, or under both conditions?

## 4. Pixel-Perfect Collision

Rectangle collision checks are convenient, but a sprite's rectangular boundary may include transparent pixels.

Pygame provides mask-based collision detection for checking overlapping opaque pixels.

Useful API references:

- `pygame.mask.from_surface(surface)`
- `pygame.sprite.collide_mask(sprite1, sprite2)`
- `pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)`
- `pygame.sprite.spritecollide(sprite, group, dokill)`

A mask represents the opaque pixels of a surface. For a static sprite image, its mask can generally be created once and reused.

**Think about it:**
- Does every sprite involved in a collision have access to the correct image and mask?
- Which existing collision checks handle laser–asteroid and player–asteroid interactions?
- How can you preserve the current sprite-group behavior while changing the collision method?

Official Pygame documentation:
- [Mask module](https://www.pygame.org/docs/ref/mask.html)
- [Sprite module](https://www.pygame.org/docs/ref/sprite.html)
- [Time module](https://www.pygame.org/docs/ref/time.html)
- [Vector2 reference](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2)

## 5. Working with Assets

The project loads images from an `assets` directory relative to the Python file.

If you choose to use custom assets:

- Keep all required files in your project.
- Update image-loading paths when filenames or folder locations change.
- Use surfaces with appropriate transparency for sprites.
- Check that collision behavior still matches the visible shape of each sprite.

## 6. Debugging Checklist

When something does not behave as expected, investigate one issue at a time.

- Does the game start without an error?
- Are all image files loaded successfully?
- Are position and velocity updated in the expected order?
- Are collision checks using the intended sprites and groups?
- Does the game still behave correctly after changing assets?

Use the Python terminal and error messages to identify problems instead of guessing.

**Final reminder:** Understanding why your code works is just as important as getting it to run.
