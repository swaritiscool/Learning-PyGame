import pygame
import os

# Defining constant values with caps
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame First Project :)")

BG_COLOR = (40, 70, 100)
BLACK = (0,0,0)
RED = (255, 3, 3)

FPS = 60
SPEED = 7
BULLET_SPEED = 9

SPACE_SHIP_SIZE = (55*1.5, 40*1.5)

MAX_BULLETS = 20

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

def shooter_yellow(key_pressed, yellow, bullets_yellow):
    clock = pygame.time.Clock()
    if key_pressed[pygame.K_LCTRL] and len(bullets_yellow) < MAX_BULLETS:
        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2, 10, 5)
        bullets_yellow.append(bullet)
        clock.tick(10)

def shooter_red(key_pressed, red, bullets_red):
    clock = pygame.time.Clock()
    if key_pressed[pygame.K_RCTRL] and len(bullets_red) < MAX_BULLETS:
        bullet = pygame.Rect(red.x - red.width, red.y + red.height/2, 10, 5)
        bullets_red.append(bullet)
        clock.tick(10)

def draw_window(yellow, red, bullets_yellow, bullets_red):
    WIN.fill(BG_COLOR)
    pygame.draw.rect(WIN, BLACK, (WIDTH/2 - 2, 0, 4, HEIGHT))
    WIN.blit(YELLOW_SPACE_SHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACE_SHIP, (red.x, red.y))

    for bullet in bullets_yellow:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in bullets_red:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()

def handle_bullets(bullets_yellow, bullets_red, yellow, red):
    for bullet in bullets_yellow:
        bullet.x += BULLET_SPEED
        if red.colliderect(bullet):
            bullets_yellow.remove(bullet)

    for bullet in bullets_red:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):
            bullets_red.remove(bullet)

def main():
    red = pygame.Rect(650, 100, 55*1.5, 40*1.5)
    yellow = pygame.Rect(250, 100, 55*1.5, 40*1.5)
    clock = pygame.time.Clock()
    running = True
    bullets_yellow = []
    bullets_red = []
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key_pressed = pygame.key.get_pressed()
        shooter_yellow(key_pressed, yellow, bullets_yellow)
        shooter_red(key_pressed, red, bullets_red)
        handle_bullets(bullets_yellow, bullets_red, yellow, red)
        yellow_movement(key_pressed, yellow)
        red_movement(key_pressed, red)
        draw_window(yellow, red, bullets_yellow, bullets_red)

    pygame.quit()

if __name__ == "__main__":
    main()
