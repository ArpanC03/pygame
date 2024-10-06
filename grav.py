import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Black Hole Swallowing Planets")

# Colors
DEEP_BLUE = (10, 10, 50)
WHITE = (255, 255, 255)

# Load images and sounds
black_hole_image = pygame.image.load("blackhole.png").convert_alpha()
planet_image = pygame.image.load("planets.png").convert_alpha()
# swallow_sound = pygame.mixer.Sound("swallow.wav")

# Scaling images
black_hole = pygame.transform.scale(black_hole_image, (100, 100))
planet = pygame.transform.scale(planet_image, (50, 50))

# Black hole attributes
black_hole_pos = [400, 300]
black_hole_radius = 50

# Planet attributes
planet_pos = [random.randint(0, screen_width), random.randint(0, screen_height)]
planet_radius = 25

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Move black hole with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        black_hole_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        black_hole_pos[0] += 5
    if keys[pygame.K_UP]:
        black_hole_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        black_hole_pos[1] += 5

    # Check collision between black hole and planet
    dist = math.hypot(black_hole_pos[0] - planet_pos[0], black_hole_pos[1] - planet_pos[1])
    if dist < black_hole_radius + planet_radius:
        planet_pos = [random.randint(0, screen_width), random.randint(0, screen_height)]
        score += 1
        # swallow_sound.play()
        
        # Increase black hole radius every 10 points
        if score % 10 == 0:
            black_hole_radius += 10
            black_hole = pygame.transform.scale(black_hole_image, (black_hole_radius * 2, black_hole_radius * 2))

    # Drawing
    screen.fill(DEEP_BLUE)
    screen.blit(planet, (planet_pos[0] - planet_radius, planet_pos[1] - planet_radius))
    screen.blit(black_hole, (black_hole_pos[0] - black_hole_radius, black_hole_pos[1] - black_hole_radius))
    
    # Display score
    score_text = font.render(f"Planets Swallowed: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    
    pygame.time.delay(1000 // 60)
