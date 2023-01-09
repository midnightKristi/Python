import pygame
import threading
import time


pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
brown=(153,77,0)
light_green=(25,199,7)

FPS=25
fps=1

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Whack A Mole!')


smallfont=pygame.font.SysFont("comicsansms", 25,bold=True,italic=True)
medfont=pygame.font.SysFont("comicsansms", 50,bold=True,italic=True)
largefont=pygame.font.SysFont("comicsansms", 80,bold=True,italic=True)


bgimg=pygame.image.load('back.png')
gamebg=pygame.image.load('back.png')
moleimg=pygame.image.load('mole.png')
hammerimg=pygame.image.load('hammer.png')
lyinghammer=pygame.image.load('lyinghammer.png')

clock=pygame.time.Clock()
start_ticks=pygame.time.get_ticks()

def text_message(msg, color,size):
    if size=="small":
        textSurface=smallfont.render(msg, True, color)
    if size=="medium":
        textSurface=medfont.render(msg, True, color)
    if size=="large":
        textSurface=largefont.render(msg, True, color)
   
    return textSurface, textSurface.get_rect()

def message_display(msg,color,x_displace=0,y_displace=0,size="small"):
    textSurf, textRect=text_message(msg,color,size)
    textRect.center=(display_width//2-x_displace),(display_height//2+y_displace)
    gameDisplay.blit(textSurf, textRect)

    

def mole():
    import random
    Holes=[(30,250,62),(300,560,46),(0,100,240),(200,400,210),(400,690,236),(210,400,380)]
    molejump=random.choice(Holes)
    #gameDisplay.blit(moleimg,[(molejump[0]+molejump[1])//2,molejump[2]])
    return molejump
        

def game_intro():
    intro=True
   
    while intro:
        
        gameDisplay.blit(bgimg,[0,0])
        pygame.draw.circle(gameDisplay,green,[390,500],55)
        
        
        
        message_display('''WELCOME!''', white,0,-50,"large")

        message_display('''to ''', white,0,20,"medium")
        message_display('''Whack A Mole!''', white,0,70,"medium")

        mouse=pygame.mouse.get_pos()
        
        x,y=mouse
        if (int(x)-390)**2+(int(y)-500)**2<=55**2:
            pygame.draw.circle(gameDisplay,light_green,[390,500],50)
        else:
            
            pygame.draw.circle(gameDisplay,green,[390,500],55)
      
        
        message_display("START!",black,10,200,"small")
        

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if (int(x)-390)**2+(int(y)-500)**2<=55**2:
                    gamePage()
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
           
            pygame.display.update()






#############################################################MOLE & HAMMER###############################################################################
def molerocks():
    while start:
        molejump=mole()
        gameDisplay.blit(gamebg,[0,0])
        gameDisplay.blit(moleimg,[(molejump[0]+molejump[1])//2,molejump[2]])
        pygame.display.update() 
        clock.tick(0.5)

def hammeringbrains(score):
    while start:
         molejump=mole()
         mouse=pygame.mouse.get_pos()
         gameDisplay.blit(gamebg,[0,0])
         gameDisplay.blit(hammerimg,[(mouse[0]-display_width//2+20),(mouse[1]-display_height//2+20)])  
         clock.tick(FPS) 
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit()
                 quit()
             if event.type==pygame.MOUSEBUTTONDOWN:
                 if mouse[0]>=molejump[0] and mouse[0]<=molejump[1]and mouse[1]>=molejump[2] and mouse[1]<=molejump[2]+180:
                     pygame.transform.rotate(hammerimg,90)
                     pygame.display.update()
                     time.sleep(1/FPS)
                     score=score+1
             message_display('SCORE:'+str(score),black,200,200,'medium')
             pygame.display.update()       
#########################################################Threading Trial Begins!#########################################################################                
def threadsucks():
    
    t1=threading.Thread(target=molerocks)
    t1.start()
   # t3=threading.Thread(target=timer)
    #t3.start()
    t2=threading.Thread(target=hammeringbrains(score))
    t2.start()
    
    
    
####################################################COOOOOL###############################################################################################            
  
      


    
def gamePage():
    global score
    score=0                   
    game=True
    global hammer
    hammer=False
    global start
    start=False
    while game:
        gameDisplay.blit(gamebg,[0,0])
        while not start:
            while not hammer:
                mouse=pygame.mouse.get_pos()
                
                gameDisplay.blit(gamebg,[0,0])
            
                gameDisplay.blit(lyinghammer,[0,300])
                message_display("CLICK THE HAMMER TO START!",black,10,200,'small')  
                pygame.display.update()
                if mouse[0] in range(0,200):
                        if mouse[1] in range(300,600):
                            hammer=True
                for event in pygame.event.get():        
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                    
    
            while hammer:
                mouse=pygame.mouse.get_pos()
                if mouse[0] in range(0,200):
                        if mouse[1] in range(300,600):
                            gameDisplay.blit(gamebg,[0,0])
                            gameDisplay.blit(lyinghammer,[30,290])
                else:
                    hammer=False
                pygame.display.update()                
                for event in pygame.event.get():        
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                        
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if mouse[0] in range(0,200):
                            if mouse[1] in range(300,600):
                                start=True

        if start:
            threadsucks()
        
            
                

       
    
def gameLoop():
    
    
    
    gameExit=False
    gameOver=False

    while not gameExit:
        game_intro()
        
        while gameOver==True:
            message_display("Game Over.",red,-50,"large")
            message_display("Press C to continue or Q to Quit.",black,50,"medium")
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                    gameOver=False

                
                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    
                    elif event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True


        clock.tick(FPS)
           
    pygame.quit()
    quit()

gameLoop()
