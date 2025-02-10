import pygame
import random

from class_snake import Snake
from class_button import Button
from class_animated_face import AnimatedSprite


pygame.init()
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')

BACKGROUND = (5, 71, 19)
ORANGE = (255, 191, 1)
RED = (255, 73, 1)
GOLDEN = (255, 232, 0)
PURPLE = (89, 1, 89)
BLUE = (31, 41, 63)
BLACK = (0, 0, 0)

search_snake = [
    pygame.image.load('../Design/Animated/Face.png').convert_alpha(),
    pygame.image.load('../Design/Animated/Face_search1.png').convert_alpha(),
    pygame.image.load('../Design/Animated/Face_search2.png').convert_alpha()
]


def check_start():
    running = True
    clock = pygame.time.Clock()
    button = Button((WIDTH // 2) - 150, (HEIGHT // 2) - 50, 100, 300, "Начать", 50)

    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.rect.collidepoint(event.pos):
                        return True

        WINDOW.fill(BACKGROUND)
        pygame.draw.line(WINDOW, PURPLE, (0, 0), (0, 600), 5)
        pygame.draw.line(WINDOW, PURPLE, (0, 600), (800, 600), 5)
        pygame.draw.line(WINDOW, PURPLE, (800, 600), (800, 0), 5)
        pygame.draw.line(WINDOW, PURPLE, (800, 0), (0, 0), 5)
        button.draw(WINDOW)

        pygame.display.update()
        clock.tick(15)



def generate_apple(body):
    coord = random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)
    while coord in body:
        coord = random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)
    return coord


def draw_snake(snake):

    # head_x, head_y = snake.body[0]
    # pygame.draw.rect(WINDOW, ORANGE, pygame.Rect(head_x, head_y, 10, 10), border_radius=2)

    for segment in snake.body[1:-1]:
        rect = pygame.Rect(segment[0], segment[1], 10, 10)
        pygame.draw.rect(WINDOW, ORANGE, rect, border_radius=3)
        pygame.draw.rect(WINDOW, BLACK, rect, 1, border_radius=3)

    tail_x, tail_y = snake.body[-1]
    rect = pygame.Rect(tail_x, tail_y, 10, 10)
    pygame.draw.rect(WINDOW, ORANGE, rect, border_radius=3)
    pygame.draw.rect(WINDOW, BLACK, rect, 1, border_radius=3)


def draw_apple(apple, color):
    pygame.draw.rect(WINDOW, color, pygame.Rect(apple[0], apple[1], 10, 10), 5)
    return color


def draw_paused(paused):
    if paused:
        font = pygame.font.Font("../Design/Fonts/ofont.ru_SAIBA-45.ttf", 74)
        text = font.render("PAUSED", True, RED)
        WINDOW.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))


def draw_count(shet, save_shet):
    font = pygame.font.Font("../Design/Fonts/ofont.ru_Pixy.ttf", 20)
    text = font.render(f'МАКСИМАЛЬНЫЙ СЧЕТ: {save_shet}', True, (255, 255, 255))
    WINDOW.blit(text, (10, 18))

    font = pygame.font.Font("../Design/Fonts/ofont.ru_Pixy.ttf", 35)
    text = font.render(f'СЧЕТ: {shet}', True, (255, 255, 255))
    WINDOW.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))


def check_is_done(event, button1, button2, snake, shet, save_shet):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if button1.rect.collidepoint(event.pos):
                snake.reset()
                apple = generate_apple(snake.body)
                if shet > save_shet:
                    save_shet = shet
                shet = 0
            elif button2.rect.collidepoint(event.pos):
                running = False

    return [apple, shet, save_shet, running]


def main():
    running = True
    snake = Snake(WIDTH, HEIGHT)
    apple = generate_apple(snake.body)
    clock = pygame.time.Clock()
    button1 = Button(WIDTH // 6, HEIGHT // 2 - 32, 70, 250, "Продолжить?", 36)
    button2 = Button(WIDTH // 1.8, HEIGHT // 2 - 32, 70, 250, "Выйти", 36)
    paused = False
    shet = 0
    current_color_apple = RED
    apple_is_draw = False
    save_shet = shet
    sprite_group = pygame.sprite.Group()
    animated_snake_face = AnimatedSprite(search_snake, 5)
    sprite_group.add(animated_snake_face)

    while running:
        is_pressed = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT and not is_pressed:
                running = False
            elif keys[pygame.K_SPACE] and not snake.check_for_boundaries():
                paused = True
            elif keys[pygame.K_n]:
                paused = False

            if not is_pressed and not paused:
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                    is_pressed = True
                elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
                    is_pressed = True
                elif (keys[pygame.K_UP] or keys[pygame.K_w]) and snake.direction != "DOWN":
                    snake.direction = "UP"
                    is_pressed = True
                elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and snake.direction != "UP":
                    snake.direction = "DOWN"
                    is_pressed = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button1.rect.collidepoint(event.pos):
                        snake.reset()
                        apple = generate_apple(snake.body)
                        if shet > save_shet:
                            save_shet = shet
                        shet = 0
                    elif button2.rect.collidepoint(event.pos):
                        running = False

        if not snake.check_for_boundaries():
            if not paused:
                snake.move()
                if snake.body[0] == apple:
                    if current_color_apple == RED:
                        shet += 1
                        snake.grow()
                    else:
                        shet += 5
                        for _ in range(5):
                            snake.grow()
                    apple = generate_apple(snake.body)
                    apple_is_draw = False

        match snake.direction:
            case "RIGHT":
                animated_snake_face.rect.center = (snake.body[0][0] + 8, snake.body[0][1] + 8)
            case "LEFT":
                animated_snake_face.rect.center = (snake.body[0][0] - 6, snake.body[0][1] + 8)
            case "UP":
                animated_snake_face.rect.center = (snake.body[0][0] + 4, snake.body[0][1] - 2)
            case _:
                animated_snake_face.rect.center = (snake.body[0][0] + 5, snake.body[0][1] + 12)

        animated_snake_face.update(snake.direction)
        WINDOW.fill(BACKGROUND)
        draw_snake(snake)
        draw_count(shet, save_shet)
        pygame.draw.line(WINDOW, PURPLE, (0, 0), (0, 600), 5)
        pygame.draw.line(WINDOW, PURPLE, (0, 600), (800, 600), 5)
        pygame.draw.line(WINDOW, PURPLE, (800, 600), (800, 0), 5)
        pygame.draw.line(WINDOW, PURPLE, (800, 0), (0, 0), 5)

        sprite_group.add(animated_snake_face)
        sprite_group.draw(WINDOW)

        if not apple_is_draw:
            if random.random() < 0.9:
                current_color_apple = draw_apple(apple, RED)
            else:
                current_color_apple = draw_apple(apple, GOLDEN)
            apple_is_draw = True
        else:
            draw_apple(apple, current_color_apple)

        if snake.check_for_boundaries():
            button1.draw(WINDOW)
            button2.draw(WINDOW)
            paused = False
        else:
            draw_paused(paused)

        pygame.display.update()
        clock.tick(15)

    pygame.quit()


if __name__ == "__main__":
    if check_start():
        main()
