import pygame
print(pygame.__version__)

import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
cols, rows = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Màu sắc
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# Các hình khối
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0],
     [1, 1, 1]],     # J
    [[0, 0, 1],
     [1, 1, 1]],     # L
    [[1, 1],
     [1, 1]],        # O
    [[0, 1, 1],
     [1, 1, 0]],     # S
    [[0, 1, 0],
     [1, 1, 1]],     # T
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

# Lớp cho khối Tetris
class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = cols // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
grid = [[BLACK for _ in range(cols)] for _ in range(rows)]

def check_collision(shape, offset_x, offset_y):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + offset_x
                new_y = y + offset_y
                if new_x < 0 or new_x >= cols or new_y >= rows:
                    return True
                if new_y >= 0 and grid[new_y][new_x] != BLACK:
                    return True
    return False

def merge_shape(shape, offset_x, offset_y, color):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell and 0 <= y + offset_y < rows and 0 <= x + offset_x < cols:
                grid[y + offset_y][x + offset_x] = color

def clear_lines():
    global grid
    grid = [row for row in grid if any(cell == BLACK for cell in row)]
    while len(grid) < rows:
        grid.insert(0, [BLACK for _ in range(cols)])

def draw_grid():
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def new_tetromino():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return Tetromino(shape, color)

# Game loop
running = True
fall_time = 0
current_piece = new_tetromino()

while running:
    screen.fill(BLACK)
    fall_speed = 0.5
    fall_time += clock.get_rawtime()
    clock.tick()

    if fall_time / 1000 >= fall_speed:
        if not check_collision(current_piece.shape, current_piece.x, current_piece.y + 1):
            current_piece.y += 1
        else:
            merge_shape(current_piece.shape, current_piece.x, current_piece.y, current_piece.color)
            clear_lines()
            current_piece = new_tetromino()
            if check_collision(current_piece.shape, current_piece.x, current_piece.y):
                print("Game Over!")
                running = False
        fall_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not check_collision(current_piece.shape, current_piece.x - 1, current_piece.y):
                    current_piece.x -= 1
            elif event.key == pygame.K_RIGHT:
                if not check_collision(current_piece.shape, current_piece.x + 1, current_piece.y):
                    current_piece.x += 1
            elif event.key == pygame.K_DOWN:
                if not check_collision(current_piece.shape, current_piece.x, current_piece.y + 1):
                    current_piece.y += 1
            elif event.key == pygame.K_UP:
                current_piece.rotate()
                if check_collision(current_piece.shape, current_piece.x, current_piece.y):
                    for _ in range(3):  # quay lại 3 lần để về vị trí cũ
                        current_piece.rotate()

    draw_grid()
    # Vẽ khối hiện tại
    for y, row in enumerate(current_piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, current_piece.color,
                                 ((current_piece.x + x) * BLOCK_SIZE, (current_piece.y + y) * BLOCK_SIZE,
                                  BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

pygame.quit()
