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

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0 # Start moving right
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) 
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)] # Initial snake body
        self.dead = False

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, '#3c3c3c', rect, 1)
draw_grid() # execute game loop

snake = Snake()

while True: # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, '#00ff00', snake.head) # Draw snake head        
    for square in snake.body:
        pygame.draw.rect(screen, '#00ff00', square) # Draw snake

    screen.fill((0, 0, 0))
    draw_grid()
    pygame.display.update()
    clock.tick(10)