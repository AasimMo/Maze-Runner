#MAZE RUNNER

import pygame
import time

pygame.init()

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]

width = 700
height = 700
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Maze Runner')
clock = pygame.time.Clock()

    
def obj_easy(x,y):
    pygame.draw.rect(screen, red, [x,y,14,14])
    
def obj_medium(x,y):
    pygame.draw.rect(screen, red, [x,y,10,10])
    
    
def obj_hard(x,y):
    pygame.draw.rect(screen, red, [x,y,8,8])
  
    
def grid_easy(x1,y1):
    gridimg = pygame.image.load('MAZE1.png')
    screen.blit(gridimg,(0,0))
 
def grid_medium(x1,y1):
    gridimg = pygame.image.load('MAZE2.png')
    screen.blit(gridimg,(0,0))
    
    
def grid_hard(x1,y1):
    gridimg = pygame.image.load('MAZE3.png')
    screen.blit(gridimg,(0,0))
   
 
def text_objects(text, font):
    textSurface = font.render(text, True, white, black)
    return textSurface, textSurface.get_rect()

    
def message_display(text):
    lText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, lText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(1)
    
      
def text_obj_intro(text,font):
    textSurface1 = font.render(text, True, white)
    return textSurface1, textSurface1.get_rect()

   
    
def crash():
    message_display('You Crashed!')
    
def oob():
    message_display('Out of Bounds')
    
def gamewin():
    message_display('You win!')
  
def timeout():
    message_display('Time Out!')
    
    
def win(winx, winy, winw, winh, color):
    pygame.draw.rect(screen, color, [winx, winy, winw, winh])    

def game_intro():
    
    intro = True
    
    while intro == True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
            
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RETURN:
                     game_difficulty()        
                 if event.key == pygame.K_ESCAPE:
                     pygame.quit()
                     quit()
                     
                     
        screen.fill(black)
        introtext = pygame.font.Font('freesansbold.ttf',85)
        subintrotext = pygame.font.Font('freesansbold.ttf',40)
        endintrotext = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects('MAZE RUNNER', introtext)
        TextSurf1, TextRect1 = text_objects('Press ENTER to continue',subintrotext)
        TextSurf2, TextRect2 = text_objects('ESC to quit', endintrotext)
        TextRect.center = ((width/2),(200))
        TextRect1.center = ((width/2),(340))
        TextRect2.center = ((width/2),(400))
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf1, TextRect1)
        screen.blit(TextSurf2, TextRect2)
        pygame.display.update()
       

        
def game_difficulty():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    game_intro()
                    
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    easy_game_loop()
                                
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    medium_game_loop()
                            
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    hard_game_loop()
                    
            
    
        screen.fill(black)
        difficultytext = pygame.font.Font('freesansbold.ttf',40)
        TextSurf1, TextRect1 = text_objects('Press 1 for EASY difficulty', difficultytext)
        TextSurf2, TextRect2 = text_objects('Press 2 for MEDIUM difficulty',difficultytext)
        TextSurf3, TextRect3 = text_objects('Press 3 for HARD difficulty', difficultytext)
        TextRect1.center = ((width/2),(250))
        TextRect2.center = ((width/2),(350))
        TextRect3.center = ((width/2),(450))
        screen.blit(TextSurf1, TextRect1)
        screen.blit(TextSurf2, TextRect2)
        screen.blit(TextSurf3, TextRect3)
        pygame.display.update()
                 

def easy_game_loop():
    x = 14
    y = 8
    
    x1 = 0
    y1 = 0
    
    stuffw = stuffh = 13
    
    gridimg = pygame.image.load('MAZE1.png')
     
    winx = 634
    winy = 665
    winw = 27
    winh = 15
    
    x_change = 0
    y_change = 0
    crashed = False
    
    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_difficulty()
                    
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x_change = -5
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x_change = 5
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y_change = -5
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y_change = 5
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x_change = 0
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x_change = 0
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y_change = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y_change = 0
            
            
        x += x_change
        y += y_change    
       
        
        screen.fill(black)
        grid_easy(x1,y1)
        win(winx, winy, winw, winh, green)
        obj_easy(x,y)
        
        if  y > winy-stuffh and x > winx-stuffw and y < winy+stuffh and x < winx+stuffw:
            gamewin()
            medium_game_loop()
            
        if x < 0 or y < 0 or y > height-10 or x > width-20:
            oob()
            easy_game_loop()
            
        #crash sequence
        if gridimg.get_at((x,y)).a != 0 or gridimg.get_at((x+stuffw,y+stuffh)).a != 0 or gridimg.get_at((x+stuffw,y)).a != 0 or gridimg.get_at((x,y+stuffh)).a != 0:
            crash()
            easy_game_loop()
            
        if gridimg.get_at((x+2,y)).a != 0 or gridimg.get_at((x+4,y)).a != 0 or gridimg.get_at((x+6,y)).a != 0 or gridimg.get_at((x+8,y)).a != 0 :  
            crash()
            easy_game_loop()
            
        if gridimg.get_at((x+2,y+2)).a != 0 or gridimg.get_at((x+4,y+4)).a != 0 or gridimg.get_at((x+6,y+6)).a != 0 or gridimg.get_at((x+8,y+8)).a != 0 or gridimg.get_at((x+10,y+10)).a != 0:  
            crash()
            easy_game_loop()
            
        if gridimg.get_at((x+2,y+stuffh)).a != 0 or gridimg.get_at((x+4,y+stuffh)).a != 0 or gridimg.get_at((x+6,y+stuffh)).a != 0 or gridimg.get_at((x+8,y+stuffh)).a != 0:  
            crash()
            easy_game_loop()
            
        if gridimg.get_at((x+stuffw,y+2)).a != 0 or gridimg.get_at((x+stuffw,y+4)).a != 0 or gridimg.get_at((x+stuffw,y+6)).a != 0 or gridimg.get_at((x+stuffw,y+8)).a != 0:  
            crash()
            easy_game_loop()
            
        if gridimg.get_at((x,y+2)).a != 0 or gridimg.get_at((x,y+4)).a != 0 or gridimg.get_at((x,y+6)).a != 0 or gridimg.get_at((x,y+8)).a != 0:  
            crash()
            easy_game_loop()
            
        pygame.display.update()
        clock.tick(30)



def medium_game_loop():
    x = 25
    y = 8
    
    x1 = 0
    y1 = 0
    
    stuffw = stuffh = 9
    
    gridimg = pygame.image.load('MAZE2.png')
     
    winx = 632
    winy = 670
    winw = 35
    winh = 15
    
    x_change = 0
    y_change = 0
    crashed = False
    
    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_difficulty()
                    
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x_change = -4
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x_change = 4
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y_change = -4
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y_change = 4
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x_change = 0
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x_change = 0
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y_change = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y_change = 0
            
            
        x += x_change
        y += y_change    
       
        
        screen.fill(black)
        grid_medium(x1,y1)
        win(winx, winy, winw, winh, green)
        obj_medium(x,y)
        
        if y > winy-stuffh and x > winx-stuffw and y < winy+stuffh and x < winx+stuffw :
            gamewin()
            hard_game_loop()
            
        if x < 0 or y < 0 or y > height-5 or x > width-30:
            oob()
            medium_game_loop()
            
        #crash sequence
        if gridimg.get_at((x,y)).a != 0 or gridimg.get_at((x+stuffw,y+stuffh)).a != 0 or gridimg.get_at((x+stuffw,y)).a != 0 or gridimg.get_at((x,y+stuffh)).a != 0:
            crash()
            medium_game_loop()
            
        if gridimg.get_at((x+2,y)).a != 0 or gridimg.get_at((x+4,y)).a != 0 or gridimg.get_at((x+6,y)).a != 0 or gridimg.get_at((x+8,y)).a != 0 :  
            crash()
            medium_game_loop()
            
        if gridimg.get_at((x+2,y+2)).a != 0 or gridimg.get_at((x+4,y+4)).a != 0 or gridimg.get_at((x+6,y+6)).a != 0 or gridimg.get_at((x+8,y+8)).a != 0:  
            crash()
            medium_game_loop()
            
        if gridimg.get_at((x+2,y+stuffh)).a != 0 or gridimg.get_at((x+4,y+stuffh)).a != 0 or gridimg.get_at((x+6,y+stuffh)).a != 0 or gridimg.get_at((x+8,y+stuffh)).a != 0:  
            crash()
            medium_game_loop()
            
        if gridimg.get_at((x+stuffw,y+2)).a != 0 or gridimg.get_at((x+stuffw,y+4)).a != 0 or gridimg.get_at((x+stuffw,y+6)).a != 0 or gridimg.get_at((x+stuffw,y+8)).a != 0:  
            crash()
            medium_game_loop()
            
        if gridimg.get_at((x,y+2)).a != 0 or gridimg.get_at((x,y+4)).a != 0 or gridimg.get_at((x,y+6)).a != 0 or gridimg.get_at((x,y+8)).a != 0:  
            crash()
            medium_game_loop()
            
        pygame.display.update()
        clock.tick(30)



def hard_game_loop():
    x = 40
    y = 8
    
    x1 = 0
    y1 = 0
    
    stuffw = stuffh = 7
    
    gridimg = pygame.image.load('MAZE3.png')
     
    winx = 644
    winy = 677
    winw = 28
    winh = 15
    
    x_change = 0
    y_change = 0
    crashed = False
    
    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_difficulty()
                    
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x_change = -4
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x_change = 4
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y_change = -4
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y_change = 4
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x_change = 0
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x_change = 0
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y_change = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y_change = 0
            
            
        x += x_change
        y += y_change    
       
        
        screen.fill(black)
        grid_hard(x1,y1)
        win(winx, winy, winw, winh, green)
        obj_hard(x,y)
        
        if  y > winy-stuffh and x > winx-stuffw:
            gamewin()
            game_difficulty()
            
            
        if x < 0 or y < 0 or y > height-5 or x > width-30:
            oob()
            hard_game_loop()
       
        #crash sequence
        if gridimg.get_at((x,y)).r == 255 or gridimg.get_at((x+stuffw,y+stuffh)).r == 255 or gridimg.get_at((x+stuffw,y)).r == 255 or gridimg.get_at((x,y+stuffh)).r == 255:
            crash()
            hard_game_loop()
        
        if gridimg.get_at((x+2,y)).r == 255 or gridimg.get_at((x+4,y)).r == 255 or gridimg.get_at((x+6,y)).r == 255:  
            crash()
            hard_game_loop()
            
        if gridimg.get_at((x+2,y+2)).r == 255 or gridimg.get_at((x+4,y+4)).r == 255 or gridimg.get_at((x+6,y+6)).r == 255:  
            crash()
            hard_game_loop()
            
        if gridimg.get_at((x+2,y+stuffh)).r == 255 or gridimg.get_at((x+4,y+stuffh)).r == 255 or gridimg.get_at((x+6,y+stuffh)).r == 255:  
            crash()
            hard_game_loop()
            
        if gridimg.get_at((x+stuffw,y+2)).r == 255 or gridimg.get_at((x+stuffw,y+4)).r == 255 or gridimg.get_at((x+stuffw,y+6)).r == 255:  
            crash()
            hard_game_loop()
        
        if gridimg.get_at((x,y+2)).r == 255 or gridimg.get_at((x,y+4)).r == 255 or gridimg.get_at((x,y+6)).r == 255:  
            crash()
            hard_game_loop()
        
        pygame.display.update()
        clock.tick(30)


game_intro()
pygame.quit()
quit()    

        
    
       

    






