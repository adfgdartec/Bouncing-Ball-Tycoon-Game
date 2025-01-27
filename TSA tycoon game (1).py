import pygame
import sys
import time
import math
import random
from colorama import Fore


# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 960, 720

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSA Tyccon game")
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)



#colors
bg = (78, 78, 228)
black = (0, 0, 0)
white = (235, 235, 235)
off_white = (240, 239, 235)
yellow = (213, 235, 20)
pipe_green = (0, 154, 20)
orange = (255, 199, 67)

#Fonts

font_size = 50

font = pygame.font.SysFont('Bauhaus 93', font_size)

#Images

Ball = pygame.image.load('C:/Users\sahar\Desktop\Saharsh\Coding\All my python codes\TSA 2024-2025\TSA Game\Assets\IMG_3014-removebg-preview.png')
Ball_scale_factor = 7
Ball_img_size_w = (496/Ball_scale_factor)
Ball_img_size_h = (503/Ball_scale_factor)
Ball_scale = pygame.transform.scale(Ball, ((Ball_img_size_w),(Ball_img_size_h)))



ball_x = (WIDTH/2) - (Ball_img_size_w/2)
ball_y = (HEIGHT/2) - (Ball_img_size_h/2)
ball_speed_x = 5
ball_speed_y = 5
ball_angle = 0


hole_w = 100
hole_h = 100
hole_x = 1000 #WIDTH/2-(hole_w/2)
hole_y = HEIGHT/2 - (hole_h/2)



timer = 0




start_button_width = 200
start_button_height = 50
start_button_x = (WIDTH/2) - (start_button_width/2)
start_button_y = (HEIGHT/2) - (start_button_height/2)


#Functions

def draw_text(text, font, text_col, text_x, text_y):
    img = font.render(text, True, text_col)
    screen.blit(img, (text_x, text_y))
money = 0


def ball_movement():
    
    global ball_x
    global ball_y
    global ball_speed_x
    global ball_speed_y
    global Ball_rotated
    global ball_angle


    ball_x += ball_speed_x
    ball_y += ball_speed_y


    if ball_x <0 or ball_x + Ball_img_size_w > WIDTH:
        ball_speed_x = -ball_speed_x



    if ball_y <0 or ball_y + Ball_img_size_h > HEIGHT:
        ball_speed_y = -ball_speed_y

    

    # ball rotation

    Ball_rotated = pygame.transform.rotate(Ball_scale, ball_angle)

    ball_angle += 1

    if ball_angle == 360:
        ball_angle = 0







#Clock

clock = pygame.time.Clock()


#while loop Stuff

all_game_run = True
begining_run = True
game_run = False


while all_game_run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #Begining Screen


    while begining_run == True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        #Ball movement/bouncing

        ball_movement()



        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] < WIDTH/2+(start_button_width/2) and mouse_pos[0] > WIDTH/2-(start_button_width/2) and mouse_pos[1] < HEIGHT/2+(start_button_height/2) and mouse_pos[1] > HEIGHT/2-(start_button_height/2) and event.type == pygame.MOUSEBUTTONDOWN:
            # Check which button was pressed
            if event.button == 1:  # Left mouse button
                print("Left mouse button clicked at:", mouse_pos)
                game_run = True
                begining_run = False







        #Background
        screen.fill(off_white)

        #Ball on screen
        screen.blit(Ball_rotated, (ball_x, ball_y))

        #Start Button
        pygame.draw.rect(screen, (black), (WIDTH/2-(start_button_width/2), HEIGHT/2-(start_button_height/2), start_button_width, start_button_height))




        pygame.display.flip()


        #Framerate
        clock.tick(60)





    #Pre Game adjustments and Loading Screen

    ball_x = (WIDTH/2) - (Ball_img_size_w/2)
    ball_y = (HEIGHT/2) - (Ball_img_size_h/2)
    ball_angle = 0


    load_wait_time = random.randrange(2,4)

    font_size = 100
    font = pygame.font.SysFont('Bauhaus 93', font_size)









    for i in range(load_wait_time):
        screen.fill(off_white)
        draw_text(("Loading."), font, black, (WIDTH/2-170), (HEIGHT/2-50))
        pygame.display.flip()


        time.sleep(0.5)

        screen.fill(off_white)
        draw_text(("Loading.."), font, black, (WIDTH/2-169), (HEIGHT/2-50))
        pygame.display.flip()


        time.sleep(0.7)

        screen.fill(off_white)
        draw_text(("Loading..."), font, black, (WIDTH/2-168), (HEIGHT/2-50))
        pygame.display.flip()


        time.sleep(0.5)



    font_size = 50
    font = pygame.font.SysFont('Bauhaus 93', font_size)



    round_of_game = 1

    #Actual Game

    while game_run == True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        #Round number of game chart: 1 - Selecting where hole is, 2 - The Ball moves and bounces around while trying to hit the hole, 3 - is the buying phase and money chilling phase

        while round_of_game == 1:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            #Find where to put the hole based on mouse click

            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check which button was pressed
                if event.button == 1:  # Left mouse button
                    print("Left mouse button clicked at:", mouse_pos)
                    hole_x = mouse_pos[0] - (hole_w/2)
                    hole_y = mouse_pos[1] - (hole_h/2)
                    round_of_game = 2




            #Background
            screen.fill(off_white)



            #Hole it needs to touch
            hole = (hole_x, hole_y, hole_w, hole_h)
            pygame.draw.rect(screen, (black), hole)



            #Instructions
            draw_text(("Click to set the Box's location"), font, black, (WIDTH/2 - 350), 20)


            #Update frame
            pygame.display.flip()

            clock.tick(60)





        while round_of_game == 2:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            ball_movement()

            #Checking if ball is touching the hole

            if ((ball_x + Ball_img_size_w) > hole_x) and ((ball_x) < (hole_x + hole_w)) and ((ball_y + Ball_img_size_h) > hole_y) and ((ball_y) < (hole_y + hole_h)):
                money += 1



            timer += 1

            if timer == 500:
                round_of_game = 3



            #Background
            screen.fill(off_white)


            #Hole it needs to touch

            hole = (hole_x, hole_y, hole_w, hole_h)
            pygame.draw.rect(screen, (black), hole)



            #Ball on screen
            screen.blit(Ball_rotated, (ball_x, ball_y))


            #Money Counter
            draw_text(("Money: $"+str(money)), font, black, 20, 20)


            #Update frame
            pygame.display.flip()

            clock.tick(60)



        print("done")


        timer = 0
        ball_x = (WIDTH/2)
        ball_y = (HEIGHT/2)

        while round_of_game == 3:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            #Checking if ball is touching the hole

            #if ((ball_x + Ball_img_size_w) > hole_x) and ((ball_x) < (hole_x + hole_w)) and ((ball_y + Ball_img_size_h) > hole_y) and ((ball_y) < (hole_y + hole_h)):
                #money += 1



            mouse_pos = pygame.mouse.get_pos()

            #Calc Ball_angle

            x_dist = mouse_pos[0] - ball_x
            y_dist = -(mouse_pos[1] - ball_y)
            ball_angle = (math.degrees(math.atan2(y_dist, x_dist))) -90
            ball_rect = Ball_rotated.get_rect(center = (ball_x, ball_y))


            # ball rotation
            Ball_rotated = pygame.transform.rotate(Ball_scale, ball_angle)



            #Check if they want to play another round
            if mouse_pos[0] < WIDTH/2+(start_button_width/2) and mouse_pos[0] > WIDTH/2-(start_button_width/2) and mouse_pos[1] < HEIGHT+(start_button_height + 20) and mouse_pos[1] > HEIGHT-(start_button_height + 20) and event.type == pygame.MOUSEBUTTONDOWN:
                # Check which button was pressed
                if event.button == 1:  # Left mouse button
                    print("Left mouse button clicked at:", mouse_pos)
                    round_of_game = 1
                    hole_x = 1000 #WIDTH/2-(hole_w/2)
                    hole_y = HEIGHT/2 - (hole_h/2)
                    time.sleep(0.3)


            #Menu and code for the upgrade section


            if mouse_pos[0] < (WIDTH - 20) and mouse_pos[0] > (WIDTH - (start_button_width + 20)) and mouse_pos[1] < (start_button_height + 20 )and mouse_pos[1] > 20 and event.type == pygame.MOUSEBUTTONDOWN:
                # Check which button was pressed
                if event.button == 1:  # Left mouse button
                    print("Left mouse button clicked at:", mouse_pos)















            #Background
            screen.fill(off_white)


            #Hole it needs to touch


            #Ball on screen
            screen.blit(Ball_rotated, ball_rect)


            #Money Counter
            draw_text(("Money: $"+str(money)), font, black, 20, 20)


            #Draw start button
            pygame.draw.rect(screen, (black), (WIDTH/2-(start_button_width/2), HEIGHT-(start_button_height + 20), start_button_width, start_button_height))


            #Draw Shop button
            pygame.draw.rect(screen, (black), (WIDTH - (start_button_width + 20), 20, start_button_width, start_button_height))


            #Update frame
            pygame.display.flip()

            clock.tick(60)







        #Background
        screen.fill(off_white)



        #Hole it needs to touch

        hole = (hole_x, hole_y, hole_w, hole_h)
        pygame.draw.rect(screen, (black), hole)



        #Ball on screen
        screen.blit(Ball_rotated, (ball_x, ball_y))


        #Money Counter
        draw_text(("Money: $"+str(money)), font, black, 20, 20)



        #Update frame
        pygame.display.flip()





        clock.tick(60)








#Quits pygame
pygame.quit()




