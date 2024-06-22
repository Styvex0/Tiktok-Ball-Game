import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tiktok Game 1")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Circle settings
circle_center = (width // 2, height // 2)
circle_radius = 200

# Ball settings
ball_radius = 10
ball_color = red
ball_pos = [width // 2, height // 2 - circle_radius + ball_radius]
ball_speed = [3, 2]
gravity = 0.2  # Less intense gravity

# Clock to control the frame rate
clock = pygame.time.Clock()
fps = 60

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity
    ball_speed[1] += gravity

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check for collision with circle's edge
    dist_from_center = math.sqrt(
        (ball_pos[0] - circle_center[0])**2 + (ball_pos[1] - circle_center[1])**2
    )
    
    if dist_from_center >= circle_radius - ball_radius:
        # Calculate angle of incidence
        angle = math.atan2(ball_pos[1] - circle_center[1], ball_pos[0] - circle_center[0])
        
        # Reflect ball direction
        ball_speed[0] = -ball_speed[0] * 0.9  # Simulate energy loss
        ball_speed[1] = -ball_speed[1] * 0.9  # Simulate energy loss
        gravity = -gravity  # Reverse gravity
        
        # Ensure the ball doesn't stick to the edge
        ball_pos[0] = circle_center[0] + (circle_radius - ball_radius) * math.cos(angle)
        ball_pos[1] = circle_center[1] + (circle_radius - ball_radius) * math.sin(angle)

        # Increase ball size
        ball_radius += 1
        if ball_radius >= circle_radius:
            running = False  # End game if ball radius exceeds circle radius

    # Check for collision with window boundaries
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= width:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] - ball_radius <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball_pos[1] + ball_radius >= height:
        ball_speed[1] = -ball_speed[1] * 0.9  # Simulate bounce with energy loss
        ball_pos[1] = height - ball_radius  # Prevent sinking below the window
        gravity = -gravity  # Reverse gravity

    # Clear screen
    screen.fill(black)

    # Draw circle
    pygame.draw.circle(screen, white, circle_center, circle_radius, 2)

    # Draw ball
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
sys.exit()
