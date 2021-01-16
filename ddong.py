import pygame
from random import *

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("똥 피하기")
#FPS 설정 안함
clock = pygame.time.Clock()
background = pygame.image.load("C:/Users/rla02/OneDrive/바탕 화면/용진/파이썬/PythonWorkSpace/pygame_basic/background.png")
#캐릭터 설정 안함
character = pygame.image.load("C:/Users/rla02/OneDrive/바탕 화면/용진/파이썬/PythonWorkSpace/pygame.ddong/character.jpg")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장아래에 해당하는 곳에 위치
#이동 좌표
to_x = 0
#이동 속도
character_speed = 0.45
#적 캐릭터
enemy = pygame.image.load("C:/Users/rla02/OneDrive/바탕 화면/용진/파이썬/PythonWorkSpace/pygame.ddong/ddong.jpg")
enemy_size = character.get_rect().size #이미지 크기를 구해옴
enemy_width = character_size[0] #적의 가로 크기
enemy_height = character_size[1] #적의 세로 크기
enemy_x_pos = randrange(0,480-enemy_width)
enemy_y_pos = 0 - enemy_height
enemy_speed = 10


#폰트정의
#총 시간
#시작 시간정보

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP: #키가 떼짐
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0    
    character_x_pos += to_x * dt 
    enemy_y_pos += enemy_speed

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0 - enemy_height
        enemy_x_pos = randrange(0,480-enemy_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("똥맞았당")
        running = False

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    pygame.display.update()
    #그리기

pygame.quit()