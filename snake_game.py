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
    def update(self):
        global apple
        for square in self.body:
            if self.head.colliderect(square): # Check for self-collision
                self.dead = True
                return
            if self.head.x not in range(0, WIDTH) or self.head.y not in range(0, HEIGHT): # Check for wall collision
                self.dead = True
                return
        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple() # Reset apple position
        self.body.append(self.head.copy()) # Move body segments
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head) # Remove head from body list to avoid self-collision

class Apple:
    def __init__(self):
        self.x = random.randint(0, (WIDTH-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.y = random.randint(0, (HEIGHT-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
    def update(self):
        pygame.draw.rect(screen, '#ff0000', self.rect) # Draw apple    
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, '#3c3c3c', rect, 1)
draw_grid() # execute game loop

score = FONT.render('Score: 0', True, '#ffffff')
score_rect = score.get_rect(center=(WIDTH//2, BLOCK_SIZE//20))

snake = Snake()
apple = Apple()

while True: # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.ydir != 1:
                snake.xdir = 0
                snake.ydir = -1
            elif event.key == pygame.K_DOWN and snake.ydir != -1:
                snake.xdir = 0
                snake.ydir = 1
            elif event.key == pygame.K_LEFT and snake.xdir != 1:
                snake.xdir = -1
                snake.ydir = 0
            elif event.key == pygame.K_RIGHT and snake.xdir != -1:
                snake.xdir = 1
                snake.ydir = 0
    snake.update() # Draw everything
    screen.fill('#000000')
    apple.update() # Draw apple
    score = FONT.render(f'Score: {len(snake.body)+1}', True, '#ffffff') # Update score
    pygame.draw.rect(screen, '#00ff00', snake.head) # Draw snake head        
    for square in snake.body:
        pygame.draw.rect(screen, '#00ff00', square) # Draw snake
    screen.blit(score, score_rect) # Draw score
    if snake.head.x == apple.x and snake.head.y == apple.y: # Check for collision with apple
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE)) # Grow snake
        apple = Apple() # Spawn new apple
    draw_grid()
    pygame.display.update()
    clock.tick(10)