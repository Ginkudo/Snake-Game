import pygame
import sys
import random # Initialize Pygame
pygame.init() # Set up display
WIDTH, HEIGHT = 800, 800 # Colors

BLOCK_SIZE = 50
FONT = pygame.font.SysFont('font.ttf', BLOCK_SIZE*2)
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set up game variables
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, '#3c3c3c', rect, 1)
draw_grid() # execute game loop

while True: # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0, 0, 0))
    draw_grid()
    pygame.display.update()
    clock.tick(10)