from random import choice, randint

import pygame

# Инициализация PyGame:
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки
SPEED = 5

# Центр игрвого поля
SCREEN_CENTER = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject():
    """Базовый класс, с общими атрибутами игровых объектов."""
    def __init__(self, position=SCREEN_CENTER, body_color=None):
        self.position = position
        self.body_color = body_color
    
    def draw(self):
        """Метод-заглушка, для отрисовки объектов в дочерних классах."""
        pass

class Apple(GameObject):
    """Класс, описывающий яблоко и действия с ним."""
    def __init__(self, position=SCREEN_CENTER, body_color=APPLE_COLOR):
        super().__init__(position, body_color)
        self.randomize_position()
        print(self.position)
    
    def randomize_position(self, block_grid = [SCREEN_CENTER]):
        """Метод, определяющий появление яблока в случайной пизиции на игровом поле."""
        x_coor, y_coor = self.position
        
        # Проверка координат яблока, на несоответствие координатам змеи 
        while (x_coor, y_coor) in block_grid:
            x_coor = randint(0, GRID_WIDTH - 1) * GRID_SIZE
            y_coor = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        self.position = (x_coor, y_coor)
            
        
    def draw(self, surface):
        """Метод для отрисовки яблока."""
        rect = pygame.Rect(
            (self.position[0], self.position[1]),
            (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, описывающий змейку и действия с ней."""
    def __init__(self, position=SCREEN_CENTER, body_color=SNAKE_COLOR):
        super().__init__(position, body_color)
        self.reset()

    def reset(self):
          self.length = 1
          self.positions = [self.position]
          self.direction = RIGHT
          self.next_direction = None
          self.last = None
 

    def update_direction(self):
        """Метод обновления направления после нажатия на кнопку."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None
    
    def move(self):
        #self.reset()
        pass
        # self.head_position = self.get_head_position()
        # self.new_head = (
        #     (self.head_position[0] + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH,
        #     (self.head_position[1] + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT
        #      )
        # if self.new_head in self.positions[1:]:
        # elif self.new_head not in self.positions:
        #     self.positions.insert(0, self.new_head)


    # Метод draw класса Snake
    def draw(self, surface):
        for position in self.positions[:-1]:
            rect = (
                pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            )
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(
                (self.last[0], self.last[1]),
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)


    def get_head_position(self):
        return self.positions[0]
    
       


# Функция обработки действий пользователя
def handle_keys(game_object: Snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    snake = Snake()

    
    

    while True:
        clock.tick(SPEED)
        handle_keys(snake)

        # Тут опишите основную логику игры.

        snake.update_direction()
        snake.move()
        apple.draw(screen)
        snake.draw(screen)


        pygame.display.update()

  


if __name__ == '__main__':
    main()


# Метод draw класса Apple
# def draw(self, surface):
#     rect = pygame.Rect(
#         (self.position[0], self.position[1]),
#         (GRID_SIZE, GRID_SIZE)
#     )
#     pygame.draw.rect(surface, self.body_color, rect)
#     pygame.draw.rect(surface, BORDER_COLOR, rect, 1)

# # Метод draw класса Snake
# def draw(self, surface):
#     for position in self.positions[:-1]:
#         rect = (
#             pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
#         )
#         pygame.draw.rect(surface, self.body_color, rect)
#         pygame.draw.rect(surface, BORDER_COLOR, rect, 1)

#     # Отрисовка головы змейки
#     head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(surface, self.body_color, head_rect)
#     pygame.draw.rect(surface, BORDER_COLOR, head_rect, 1)

#     # Затирание последнего сегмента
#     if self.last:
#         last_rect = pygame.Rect(
#             (self.last[0], self.last[1]),
#             (GRID_SIZE, GRID_SIZE)
#         )
#         pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

# Функция обработки действий пользователя
# def handle_keys(game_object):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and game_object.direction != DOWN:
#                 game_object.next_direction = UP
#             elif event.key == pygame.K_DOWN and game_object.direction != UP:
#                 game_object.next_direction = DOWN
#             elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
#                 game_object.next_direction = LEFT
#             elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
#                 game_object.next_direction = RIGHT

# Метод обновления направления после нажатия на кнопку
# def update_direction(self):
#     if self.next_direction:
#         self.direction = self.next_direction
#         self.next_direction = None
