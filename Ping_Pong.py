import os
import pygame
from pygame.constants import QUIT

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

######################################################################

current_path = os.path.dirname(__file__)     
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "Ping_Pong_background.png"))

stage = pygame.image.load(os.path.join(image_path, "Ping_Pong_stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]
stage_x_pos = (screen_width - stage_width) / 2
stage_y_pos = (screen_height - stage_height) / 2

plate1 = pygame.image.load(os.path.join(image_path, "Ping_Pong_plate1.png"))
plate1_size = plate1.get_rect().size
plate1_width = plate1_size[0]
plate1_height = plate1_size[1]
plate1_x_pos = stage_x_pos + plate1_width * 2
plate1_y_pos = (screen_height / 2) - (plate1_height / 2)
plate1_to_up = 0
plate1_to_down = 0
plate1_speed = 10

plate2 = pygame.image.load(os.path.join(image_path, "Ping_Pong_plate2.png"))
plate2_size = plate2.get_rect().size
plate2_width = plate2_size[0]
plate2_height = plate2_size[1]
plate2_x_pos = screen_width - stage_x_pos - plate2_width * 3
plate2_y_pos = (screen_height / 2) - (plate2_height / 2)
plate2_to_up = 0
plate2_to_down = 0
plate2_speed = 10

ball = pygame.image.load(os.path.join(image_path, "Ping_Pong_ball.png"))
ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_x_pos = (screen_width / 2) - (ball_width / 2)
ball_y_pos = (screen_height / 2) - (ball_height / 2)
ball_to_x = 5
ball_to_y = 5
ball_speed = 1
score = 0

start_ticks = pygame.time.get_ticks()

game_font = pygame.font.Font(None, 100)
game_font_min = pygame.font.Font(None, 50)


running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                plate1_to_up -= plate1_speed
            elif event.key == pygame.K_s:
                plate1_to_down += plate1_speed
            elif event.key == pygame.K_UP:
                plate2_to_up -= plate2_speed
            elif event.key == pygame.K_DOWN:
                plate2_to_down += plate2_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                plate1_to_up = 0
            elif event.key == pygame.K_s:
                plate1_to_down = 0
            elif event.key == pygame.K_UP:
                plate2_to_up = 0
            elif event.key == pygame.K_DOWN:
                plate2_to_down = 0

    plate1_y_pos += plate1_to_up + plate1_to_down
    if plate1_y_pos < stage_y_pos:
        plate1_y_pos = stage_y_pos
    elif plate1_y_pos > screen_height - stage_y_pos - plate1_height:
        plate1_y_pos = screen_height - stage_y_pos - plate1_height
    
    plate2_y_pos += plate2_to_up + plate2_to_down
    if plate2_y_pos < stage_y_pos:
        plate2_y_pos = stage_y_pos
    elif plate2_y_pos > screen_height - stage_y_pos - plate2_height:
        plate2_y_pos = screen_height - stage_y_pos - plate2_height

    ball_x_pos += ball_to_x
    ball_y_pos += ball_to_y
    if ball_y_pos < stage_y_pos:
        ball_to_y *= -1
    elif ball_y_pos > screen_height - stage_x_pos - ball_height:
        ball_to_y *= -1
    
    if ball_x_pos <= stage_x_pos:
        running = False
    elif ball_x_pos >= screen_width - stage_x_pos - ball_width:
        running = False
    

    plate1_rect = plate1.get_rect()
    plate1_rect.left = plate1_x_pos
    plate1_rect.top = plate1_y_pos

    plate2_rect = plate2.get_rect()
    plate2_rect.left = plate2_x_pos
    plate2_rect.top = plate2_y_pos

    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    if ball_rect.colliderect(plate1_rect):
        ball_to_x *= -1.01
        ball_to_y *= 1.01
        ball_speed *= 1.01
        score += 1      
    elif ball_rect.colliderect(plate2_rect):
        ball_to_x *= -1.01
        ball_to_y *= 1.01
        ball_speed *= 1.01 
        score += 1
        

    screen.blit(background, (0, 0))
    screen.blit(stage, (stage_x_pos, stage_y_pos))
    screen.blit(plate1, (plate1_x_pos, plate1_y_pos))
    screen.blit(plate2, (plate2_x_pos, plate2_y_pos))
    screen.blit(ball, (ball_x_pos, ball_y_pos))
    # msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
    # screen.blit(msg, msg_rect)
    ball_speed_record = game_font_min.render("Ball Speed : {}x".format(round(ball_speed, 2)), True, (255, 255, 255))
    screen.blit(ball_speed_record, (10, 10))
    score_record = game_font_min.render("Score : {}".format(score), True, (255, 255, 255))
    screen.blit(score_record, (450, 10))

    pygame.display.update()


pygame.time.delay(500)

pygame.quit()



