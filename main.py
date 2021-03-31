import pygame
import os
import random

pygame.init()

HEIGHT, WIDTH = 600, 900 #Set screen dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Set WIN as the window
pygame.display.set_caption("Rock Paper Scissors")  #Set title

DavidFont = pygame.font.SysFont('David', 54) #Set font

FPS = 60 #Set veriable 'FPS' to 60


BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'wall.jpg')), (WIDTH, HEIGHT))  #Import image and scaling down 


ROCK = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'rock.jpg')), (150, 150))  #Import image and scaling down

SCISSORS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'scissors.jpg')), (150, 150))  #Import image and scaling down

PAPER = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'paper.jpg')), (150, 150))  #Import image and scaling down



BIG_ROCK = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'rock.jpg')), (300, 300))  #Import image and scaling down

BIG_SCISSORS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'scissors.jpg')), (300, 300))  #Import image and scaling down

BIG_PAPER = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'paper.jpg')), (300, 300))  #Import image and scaling down


def com(): #A function that choose randomally (for the computer)
    options = ['r', 'p',  's']
    return random.choice(options)


def draw_window(): # A function that draws the outline
    WIN.blit(BG, (0, 0)) #Set BG as background pic 
    WIN.blit(ROCK, (600, 20)) #Draw ROCK (image) in the screen
    WIN.blit(SCISSORS, (600, 190)) #Draw SCISSORS (image) in the screen
    WIN.blit(PAPER, (600, 360)) #Draw PAPER (image) in the screen
    pygame.display.update() #Actually update the screen with the new things we draw


def user(mouse): #Function that gets the sign the user chose
    player = ''
    if 600 < mouse[0] < 750: #Where we drew the pictures (horizantaly)
        if 20 < mouse[1] < 170: #Where we drew specificaly the rock image
            player = 'r'
        elif 190 < mouse[1] < 340: #Where we drew specificaly the scissors image
            player = 's'
        elif 360 < mouse[1] < 510: #Where we drew specificaly the paper image
            player = 'p'

    return player


def check(choice, computer): #Check how won
    side = ''
    if choice == 'r':
        if computer == 'r':
            side = 'draw'
        elif computer == 'p':
            side = 'com'
        else:
            side = 'plr'

    elif choice == 'p':
        if computer == 'r':
            side = 'plr'
        elif computer == 'p':
            side = 'draw'
        else:
            side = 'com'

    elif choice == 's':
        if computer == 'r':
            side = 'com'
        elif computer == 'p':
            side = 'plr'
        else:
            side = 'draw'
    
    return side


def main():
    clock = pygame.time.Clock()
    run = True
    player, computer = '', ''
    while run:
        click = False
        clock.tick(FPS) #Setting the window to update FPS (ver) times in a second (in this case - 60)
        for event in pygame.event.get(): #Checks for events that's happenning
            if event.type == pygame.QUIT: #In case the event is close the program, go out if the loop
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #If the event is a mouse click, click (ver) is True
                click = True
        mouse = pygame.mouse.get_pos() #Get the position of the mouse
        draw_window() #Drawing the outline
        if click == True:
            player = user(mouse) #Getting the player choice
            if player != '': #If he didn't click on the pictures, don't run the rest
                computer = com() #Getting the computer choice
                #Drawing the chice of the computer:
                if computer == 'r': 
                    WIN.blit(BIG_ROCK, (100, 150))
                elif computer == 'p':
                    WIN.blit(BIG_PAPER, (100, 150))
                elif computer == 's':
                    WIN.blit(BIG_SCISSORS, (100, 150))
                side = check(player, computer) #checking who won
                #Setting text of who won:
                if side == 'draw':
                    txt = DavidFont.render("DRAW!", 1, (0, 0, 0))
                elif side == 'com':
                    txt = DavidFont.render("COMPUTER WON!", 1, (0, 0, 0))
                elif side == 'plr':
                    txt = DavidFont.render("YOU WON!", 1, (0, 0, 0))
                WIN.blit(txt, (100, 50)) #Drawing txt (text)
                pygame.display.update() #Actually drawing

                pygame.time.wait(2000) #Waiting for 2 seconds


if __name__ == '__main__':
    main()
