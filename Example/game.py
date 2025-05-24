import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Thiết lập kích thước cửa sổ game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game đầu tiên với Pygame!")

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tạo nhân vật là hình vuông
player_size = 50
player_x = width // 2
player_y = height // 2
player_speed = 5

# Vòng lặp game chính
running = True
while running:
    pygame.time.delay(15)  # độ trễ giữa các khung hình (FPS)
    if player_y ==550:
        running = False
    if player_y <550:
        player_y -= -2.5
    # Bắt sự kiện (thoát game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lấy các phím đang nhấn
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= (player_speed+20)
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Vẽ nền và nhân vật
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    pygame.display.update()

# Thoát khỏi pygame
pygame.quit()
sys.exit()
