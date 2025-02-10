import cv2
import numpy as np
import random

# Инициализация параметров игры
width, height = 600, 400
snake_size = 10
snake_speed = 100  # Задержка в миллисекундах

# Начальные позиции змейки и еды
snake_pos = [[100, 50], [90, 50], [80, 50]]  # Начальная позиция змейки (3 сегмента)
food_pos = [random.randrange(1, (width // snake_size)) * snake_size,
            random.randrange(1, (height // snake_size)) * snake_size]  # Позиция еды
food_spawn = True

# Направление движения
direction = 'RIGHT'
change_to = direction

# Инициализация окна игры
cv2.namedWindow('Snake Game')

# Основной цикл игры
while True:
    # Проверка нажатия клавиш
    key = cv2.waitKey(snake_speed)  # Задержка между кадрами
    if key == ord('w'):
        change_to = 'UP'
    elif key == ord('s'):
        change_to = 'DOWN'
    elif key == ord('a'):
        change_to = 'LEFT'
    elif key == ord('d'):
        change_to = 'RIGHT'
    elif key == 27:  # Esc для выхода из игры
        break

    # Проверка на изменение направления
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Обновление позиции змейки
    if direction == 'UP':
        new_head = [snake_pos[0][0], snake_pos[0][1] - snake_size]
    elif direction == 'DOWN':
        new_head = [snake_pos[0][0], snake_pos[0][1] + snake_size]
    elif direction == 'LEFT':
        new_head = [snake_pos[0][0] - snake_size, snake_pos[0][1]]
    elif direction == 'RIGHT':
        new_head = [snake_pos[0][0] + snake_size, snake_pos[0][1]]

    # Проверяем выход за границы перед добавлением новой головы
    if (new_head[0] < 0 or new_head[0] >= width or
            new_head[1] < 0 or new_head[1] >= height):
        print("Game Over: Out of bounds.")
        break

    # Проверка столкновения со своей же змейкой
    if new_head in snake_pos:
        print("Game Over: Collision with self.")
        break

    # Обновляем позицию змейки
    snake_pos.insert(0, new_head)

    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width // snake_size)) * snake_size,
                    random.randrange(1, (height // snake_size)) * snake_size]
        food_spawn = True

    # Отрисовка игрового поля
    game_window = np.zeros((height, width, 3), dtype=np.uint8)

    for pos in snake_pos:
        cv2.rectangle(game_window, (pos[0], pos[1]), (pos[0] + snake_size, pos[1] + snake_size), (0, 255, 0), -1)

    cv2.rectangle(game_window, (food_pos[0], food_pos[1]), (food_pos[0] + snake_size, food_pos[1] + snake_size),
                  (255, 0, 0), -1)

    # Отображение окна с игрой
    cv2.imshow('Snake Game', game_window)

# Закрытие окна при завершении игры
cv2.destroyAllWindows()