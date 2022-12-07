import pygame
import random
pygame.init()

# creating window
gameWindow=pygame.display.set_mode((500, 500))
pygame.display.set_caption("First_game")

# colours
white=(255,255,255)
red=(255,0,0)
green=(255,153,153)
black=(0,0,0)

clock=pygame.time.Clock()
font= pygame.font.SysFont(None, 30)

# print score on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

#snake length
def plot(gameWindow, color, snake_lsit, size):
    for x, y in snake_lsit:
        pygame.draw.rect(gameWindow, color, [x, y, size, size])

#welcome window
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((128,128,128))
        text_screen(" Wlcm to game", (255,0,127), 140, 200)
        text_screen("press Q to continue", (0,255,255), 100, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            # if key pressed again game has to start (only Enter key has to pressed)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_loop()

        pygame.display.update()
        clock.tick(60)

# creating game loop
def game_loop():

    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    size = 10
    fps = 30

    # increa speed of snake
    vel_x = 0
    vel_y = 0
    score = 0

    # list represent the snake
    snake_lsit = []
    snk_len = 1

    # snake food
    food_x = random.randint(50, 480)
    food_y = random.randint(50, 480)

    #reading the high score file
    with open("high.txt", "r") as f:
        high_s=f.read()

    while not exit_game:

        # game over display
        if game_over:
            with open("high.txt", "w") as f:
                f.write(str(high_s))
            gameWindow.fill(red)
            #print("high score:"+high)
            text_screen("Game over press enter to continue", white, 80, 200)
            text_screen("        High score:" + str(high_s), white, 120, 220)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                # if key pressed again game has to start (only Enter key has to pressed)
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
               # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        vel_x =5
                        vel_y=0
                    if event.key==pygame.K_LEFT:
                        vel_x =-5
                        vel_y=0
                    if event.key == pygame.K_UP:
                        vel_y = -5
                        vel_x=0
                    if event.key == pygame.K_DOWN:
                        vel_y=5
                        vel_x=0
            snake_x +=vel_x
            snake_y +=vel_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10
                #print("Score:",score)
                food_x = random.randint(50, 480)
                food_y = random.randint(50, 480)
                snk_len+=5 #increase the length of snake by 5
                if score>int(high_s):
                    high_s=score

            gameWindow.fill(green)
            text_screen("Score:" + str(score), black, 5, 5)
            pygame.draw.rect(gameWindow, black, [food_x, food_y, size, size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_lsit.append(head)

            if len(snake_lsit)>snk_len:
                del snake_lsit[0]

            if head in snake_lsit[:-1]:
                game_over=True

            if snake_x<0 or snake_x>500 or snake_y<0 or snake_y>500:
                game_over=True
                #print("Game over")

            #pygame.draw.rect(gameWindow, red, [snake_x,snake_y,size,size])
            plot(gameWindow, red, snake_lsit, size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()