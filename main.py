import pygame
import random

pygame.init()

gamewindow=pygame.display.set_mode((1200,600))

pygame.display.set_caption("Dice Simulator")
pygame.display.update()
font=pygame.font.SysFont(None, 45)
# random dice_number 
dice_number=random.randint(1,6)
print(dice_number)


# variable
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue=(0,0,255)
rect_height=200
rect_width=200
rect_x=45
rect_y=30
circle_radius=20

centers=[(145,130),(175,180),(105,130),(145,90),(180,130),(145,170)]




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # next dice_number on click 
        if event.type == pygame.MOUSEBUTTONDOWN:
           dice_number=random.randint(1,6)
           print(dice_number)
    pygame.draw.rect(gamewindow, blue, [rect_x, rect_y, rect_width, rect_height])
    # loop for making circle 
    for i, center in enumerate(centers):
     if i>=dice_number:
        break
     pygame.draw.circle(gamewindow, white, center, circle_radius)
    #  long method
    # if (dice_number==1):
    #     pygame.draw.circle(gamewindow, white,(145,130),20)
    # elif(dice_number==2):
    #     pygame.draw.circle(gamewindow, white,(100,120),20)
    #     pygame.draw.circle(gamewindow, white,(145,130),20)
    # elif(dice_number==3):
    #     pygame.draw.circle(gamewindow, white,(145,130),20)
    #     pygame.draw.circle(gamewindow, white,(105,100),20)
    #     pygame.draw.circle(gamewindow, white,(145,130),20)
    # elif(dice_number==4):
    #     pygame.draw.circle(gamewindow, white,(145,130),20)
    #     pygame.draw.circle(gamewindow, white,(175,180),20)
    #     pygame.draw.circle(gamewindow, white,(105,130),20)
    #     pygame.draw.circle(gamewindow, white,(145,90),20)
    # elif(dice_number==5):
    #     pygame.draw.circle(gamewindow, white,(145,130),20)
    #     pygame.draw.circle(gamewindow, white,(175,180),20)
    #     pygame.draw.circle(gamewindow, white,(105,130),20)
    #     pygame.draw.circle(gamewindow, white,(145,90),20)
    #     pygame.draw.circle(gamewindow, white,(180,130),20)
    # elif(dice_number==6):
    #     pygame.draw.circle(gamewindow, white,(145,130),20)
    #     pygame.draw.circle(gamewindow, white,(175,180),20)
    #     pygame.draw.circle(gamewindow, white,(105,130),20)
    #     pygame.draw.circle(gamewindow, white,(145,90),20)
    #     pygame.draw.circle(gamewindow, white,(180,130),20)
    #     pygame.draw.circle(gamewindow, white,(145,170),20)
    pygame.display.update()
pygame.quit()
quit()
