import pygame
import numpy as np

# Define the point charges
q1 = 1e-6  # Charge 1 in Coulombs
q2 = -1e-6  # Charge 2 in Coulombs
r1 = np.array([100, 100])  # Position of charge 1
r2 = np.array([200, 200])  # Position of charge 2
k = (9e9)

q_test = 1e-6
r_test = np.array([150.0, 150.0])
v_test = np.array([0.0, 0.0])

dt = 0.01


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the forces on the test charge
    F1 = k * q1 * q_test / np.linalg.norm(r_test - r1)**3 * (r_test - r1)
    F2 = k * q2 * q_test / np.linalg.norm(r_test - r2)**3 * (r_test - r2)
    F = F1 + F2

    # Update the velocity and position of the test charge
    v_test += F * dt / q_test
    r_test += v_test * dt

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the charges
    pygame.draw.circle(screen, (255, 0, 0), r1.astype(int), 10)
    pygame.draw.circle(screen, (0, 0, 255), r2.astype(int), 10)
    pygame.draw.circle(screen, (0, 255, 0), r_test.astype(int), 5)

    # Update the screen
    pygame.display.flip()

pygame.quit()