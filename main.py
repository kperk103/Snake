import pygame, sys, random, time
from pygame.locals import *

pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock()

# Keeps track of the number of apples the snake has gotten
count = 0

# Keeps track of if the difficulty has been chosen yet
start = 0

# Sets the colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setting game board size, color, and name
BOARD = pygame.display.set_mode((795, 600))
BOARD.fill(BLACK)
pygame.display.set_caption("Snake")

# Setting fonts and messages for end of game
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)
final_score = font_small.render("Final Score: ", True, BLACK)


class Apple(pygame.sprite.Sprite):
    # Creating an apple image and placing it in a random position
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Apple.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(15, 780), random.randint(15, 585))

    # Moves apple to a random position on the board
    def move(self):
        self.rect.center = (random.randint(15, 780), random.randint(15, 585))

    # Places the apple onto the game board
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Snake(pygame.sprite.Sprite):
    # Creates snake body
    def __init__(self):
        super().__init__()
        self.body = list()

        # Head of snake
        self.image = pygame.image.load("Green.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.body.append(self.image.get_rect())
        self.body[0].center = (67.5, 300)

        # Creating initial snake body
        self.image1 = pygame.image.load("Green.png")
        self.image1 = pygame.transform.scale(self.image1, (15, 15))
        self.body.append(self.image1.get_rect())
        self.body[1].center = (52.5, 300)

        self.image1 = pygame.image.load("Green.png")
        self.image1 = pygame.transform.scale(self.image1, (15, 15))
        self.body.append(self.image1.get_rect())
        self.body[2].center = (37.5, 300)

        self.image1 = pygame.image.load("Green.png")
        self.image1 = pygame.transform.scale(self.image1, (15, 15))
        self.body.append(self.image1.get_rect())
        self.body[3].center = (22.5, 300)

        self.image1 = pygame.image.load("Green.png")
        self.image1 = pygame.transform.scale(self.image1, (15, 15))
        self.body.append(self.image1.get_rect())
        self.body[4].center = (7.5, 300)

    # Moves snake body according to key input
    def take_step(self):
        pressed_keys = pygame.key.get_pressed()

        # if up arrow is pressed
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            for x in reversed(range(1, len(self.body))):
                self.body[x].center = self.body[x-1].center
            self.body[0].move_ip(0, -15)

        # if down arrow is pressed
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
            for x in reversed(range(1, len(self.body))):
                self.body[x].center = self.body[x-1].center
            self.body[0].move_ip(0, 15)

        # if left arrow is pressed
        elif pressed_keys[K_LEFT] or pressed_keys[K_a]:
            for x in reversed(range(1, len(self.body))):
                self.body[x].center = self.body[x-1].center
            self.body[0].move_ip(-15, 0)

        # if right arrow is pressed
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            for x in reversed(range(1, len(self.body))):
                self.body[x].center = self.body[x-1].center
            self.body[0].move_ip(15, 0)

    # Increases the snake length by one block
    def grow(self):
        self.image1 = pygame.image.load("Green.png")
        self.image1 = pygame.transform.scale(self.image1, (15, 15))
        self.body.append(self.image1.get_rect())
        self.body[len(self.body) - 1].center = (self.body[len(self.body) - 2].x, self.body[len(self.body) - 2].y)

    # Places the snake onto the game board
    def draw(self, surface):
        surface.blit(self.image, self.body[0])
        for x in range(1, len(self.body)):
            surface.blit(self.image1, self.body[x])


# Displays game over and final score before quitting the game
def game_over():
    BOARD.fill(RED)
    BOARD.blit(game_over_text, (225, 250))
    BOARD.blit(final_score, (330, 325))
    scores = font_small.render(str(count), True, BLACK)
    BOARD.blit(scores, (455, 325))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Displays the menu
def menu():
    BOARD.fill(BLACK)
    BOARD.blit(font_small.render("Hi! Welcome to Snake!", True, WHITE), (270, 100))
    BOARD.blit(font_small.render("Choose your difficulty:", True, WHITE), (270, 140))
    BOARD.blit(font_small.render("Press 1 for easy", True, WHITE), (270, 250))
    BOARD.blit(font_small.render("Press 2 for medium", True, WHITE), (270, 290))
    BOARD.blit(font_small.render("Press 3 for hard", True, WHITE), (270, 330))
    BOARD.blit(font_small.render("Press 4 for extreme", True, WHITE), (270, 370))


# Setting up Sprites
S1 = Snake()
A1 = Apple()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()

    # Displays the menu until a key has been pressed
    if pressed_keys[K_1] is False and pressed_keys[K_2] is False and pressed_keys[K_3] is False and \
            pressed_keys[K_4] is False and start == 0:
        menu()
    else:
        # Indicates the game has started
        start = 1

        # Sets the speed of the snake based on the given input
        if pressed_keys[K_1]:
            FPS = 15
        if pressed_keys[K_3]:
            FPS = 45
        if pressed_keys[K_4]:
            FPS = 90

        # Moves the snake and draws the game board
        S1.take_step()
        BOARD.fill(BLACK)
        S1.draw(BOARD)
        A1.draw(BOARD)

        # To be run if Snake gets Apple
        if S1.body[0].x - 15 < A1.rect.x < S1.body[0].x + 15 and S1.body[0].y - 15 < A1.rect.y < S1.body[0].y + 15:
            A1.move()
            S1.grow()
            count += 1

        # Ends the game if the snake runs into itself
        for part in range(1, len(S1.body)):
            if S1.body[0].x - 15 < S1.body[part].x < S1.body[0].x + 15 and S1.body[0].y - 15 < S1.body[part].y < S1.body[0].y + 15:
                game_over()

        # Ends the game if the snake runs into the edge
        if S1.body[0].left <= 0 or S1.body[0].right >= 795 or S1.body[0].top <= 0 or S1.body[0].bottom >= 600:
            game_over()

    # Displays the player's current score
    scores = font_small.render(str(count), True, WHITE)
    BOARD.blit(scores, (10, 10))

    # Updates the display
    pygame.display.update()
    FramePerSec.tick(FPS)
