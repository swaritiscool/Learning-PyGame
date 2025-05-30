import pygame
import os

# Defining constant values with caps
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame First Project :)")

BG_COLOR = (40, 70, 100)

FPS = 60
SPEED = 7

SPACE_SHIP_SIZE = (55*1.5, 40*1.5)

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('Assets', "spaceship_yellow.png"))
YELLOW_SPACE_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACE_SHIP, SPACE_SHIP_SIZE), 90)
RED_SPACE_SHIP = pygame.image.load(os.path.join('Assets', "spaceship_red.png"))
RED_SPACE_SHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACE_SHIP, SPACE_SHIP_SIZE), -90)
SPACE = pygame.image.load(os.path.join('Assets', "space.png"))

def yellow_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a]:
        if yellow.x > 0:
            yellow.x -= SPEED
    if key_pressed[pygame.K_d]:
        if yellow.x < 350:
            yellow.x += SPEED
    if key_pressed[pygame.K_s]:
        if yellow.y < 420:
            yellow.y += SPEED
    if key_pressed[pygame.K_w]:
        if yellow.y > 0:
            yellow.y -= SPEED

def red_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT]:
        if red.x > 485:
            red.x -= SPEED
    if key_pressed[pygame.K_RIGHT]:
        if red.x < 840:
            red.x += SPEED
    if key_pressed[pygame.K_DOWN]:
        if red.y < 420:
            red.y += SPEED
    if key_pressed[pygame.K_UP]:
        if red.y > 0:
            red.y -= SPEED

def draw_window(yellow, red):
    WIN.fill(BG_COLOR)
    WIN.blit(YELLOW_SPACE_SHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACE_SHIP, (red.x, red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(650, 100, 55*1.5, 40*1.5)
    yellow = pygame.Rect(250, 100, 55*1.5, 40*1.5)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key_pressed = pygame.key.get_pressed()
        yellow_movement(key_pressed, yellow)
        red_movement(key_pressed, red)
        draw_window(yellow, red)

    pygame.quit()

if __name__ == "__main__":
    main()
