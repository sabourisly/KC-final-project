import pygame
import time
import random

pygame.font.init()


# backround code

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("survive the jungle")

BG = pygame.transform.scale(
    pygame.image.load("survive the jungle-wallpaper-preview.jpg"), (WIDTH, HEIGHT)
    )


# characters code

PREY_IMG = pygame.image.load("prey.survive_the_jungle.png")
ANIMAL_IMG = pygame.image.load("predator.survive_the_jungle.png")



PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_WIDTH = 50
STAR_HEIGHT = 50
STAR_VEL = 3

PREY_IMG = pygame.transform.scale(PREY_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))
ANIMAL_IMG = pygame.transform.scale(ANIMAL_IMG, (STAR_WIDTH, STAR_HEIGHT))


FONT = pygame.font.SysFont("comicsans", 30)


#the codes for organizing the bg and characters and time on the screen 

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    WIN.blit(PREY_IMG, (player.x, player.y))

    for star in stars:
        WIN.blit(ANIMAL_IMG, (star.x, star.y))

    pygame.display.update()


# main game loop and commands for the game

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(
                lost_text,
                (
                    WIDTH / 2 - lost_text.get_width() / 2,
                    HEIGHT / 2 - lost_text.get_height() / 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


# call for game loop and commands

if __name__ == "__main__":
    main()