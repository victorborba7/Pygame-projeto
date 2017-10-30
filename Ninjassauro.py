import pygame
import sys
import os
import random

#Variáveis iniciais

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
bright_red = (200,0,0)
green = (0,255,0)
bright_green = (0,200,0)
blue = (0,0,255)
bright_blue = (0,0,200)

clock = pygame.time.Clock()

screen_width = 800
screen_height = 600


game_Display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ninjassauro')
clock = pygame.time.Clock()

#Funções para definições de texto

def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Função para mensagens

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText, black)
    TextRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_intro()

#Função para Botões

def button(msg, pos_x, pos_y, width, high, initial_color, final_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if pos_x + width > mouse[0] > pos_x and pos_y + high > mouse[1] > pos_y:
        pygame.draw.rect(game_Display, final_color, (pos_x, pos_y, width, high))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(game_Display, initial_color, (pos_x, pos_y, width, high))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((pos_x + (width / 2)), (pos_y + (high / 2)))
    game_Display.blit(textSurf, textRect)

#Função para sair do jogo

def quitgame():
    pygame.quit()
    quit()

#Função do tutorial do jogo

def game_tutorial():
    tutorial = True
    scene = ("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg")
    scene_random = random.randint(0,(len(scene) - 1))
    scene = pygame.image.load(os.path.join("images", scene[scene_random]))
    while tutorial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        game_Display.blit(scene ,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects('Tutorial', largeText, black)
        TextRect.center = (90, 100)
        game_Display.blit(TextSurf, TextRect)

        largeTutorial = pygame.font.Font('freesansbold.ttf', 20)
        TutorialSurf, TutorialRect = text_objects('Spacebar/Up: Jump', largeText, black)
        TutorialRect.center = (175, 200)
        game_Display.blit(TutorialSurf, TutorialRect)

        largeTutorial1 = pygame.font.Font('freesansbold.ttf', 20)
        Tutorial1Surf, Tutorial1Rect = text_objects('Esc: Pause', largeText, black)
        Tutorial1Rect.center = (116, 300)
        game_Display.blit(Tutorial1Surf, Tutorial1Rect)

        button('Back', 30, 500, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(15)


#Menu do jogo

def game_intro():
    intro = True
    #Cenário
    
    scene = ("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg")
    scene_random = random.randint(0,(len(scene) - 1))
    scene = pygame.image.load(os.path.join("images", scene[scene_random]))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        game_Display.blit(scene, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Ninjassauro', largeText, black)
        TextRect.center = ((screen_width / 2), (150))
        game_Display.blit(TextSurf, TextRect)

        button('Play', 125, 350, 100, 50, green, bright_green, game_loop)
        button('Quit', 350, 450, 100, 50, red, bright_red,  quitgame)
        button('Tutorial', 575, 350, 100, 50, blue, bright_blue, game_tutorial)

        pygame.display.update()
        clock.tick(15)

#Tela de pontuação

def game_high_score():
    score = True
    while score:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        game_Display.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Highscores', largeText, black)
        TextRect.center = ((screen_width / 2), (150))
        game_Display.blit(TextSurf, TextRect)

        button('Menu', 125, 350, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(15)
    

#Jogo rodando

def game_loop():

    #Váriaveis dino

    y = 400
    jump = 0

    #Música
    pygame.mixer.music.load("songs/Naruto.ogg")
    pygame.mixer.music.play()
    
    #Cenário
    
    scene = ("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg")
    scene_count = 0
    scene = pygame.image.load(os.path.join("images", scene[scene_count]))

    #Personagem

    dino = ("raptor1.png", "raptor2.png", "raptor3.png", "raptor4.png", "raptor5.png", "raptor6.png", "raptor7.png", "raptor8.png")
    dino_count = 0
    dino = pygame.image.load(os.path.join("dino", dino[dino_count]))
    
    #Timer

    start_ticks = pygame.time.get_ticks()
        
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            #if event.type == pygame.KEYDOWN:

                #Pulo
                
                #if event.key == pygame.K_SPACE:
                    
                

        seconds = str(int((pygame.time.get_ticks()-start_ticks)/100))
        points = int(seconds)

        #Levels

        if points%100 == 0 and points > 0:
            scene = ("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg")
            scene_count += 1
            if scene_count > 5:
                scene_count = 0
            scene = pygame.image.load(os.path.join("images", scene[scene_count]))

        #Movimentos

        dino = ("raptor1.png", "raptor2.png", "raptor3.png", "raptor4.png", "raptor5.png", "raptor6.png", "raptor7.png", "raptor8.png")
        dino_count += 1
        if dino_count > 7:
            dino_count = 0
        dino = pygame.image.load(os.path.join("dino", dino[dino_count]))
        
        game_Display.blit(scene, (0, 0))
        game_Display.blit(dino, (0, y))
        if scene_count == 5:
            largeText = pygame.font.Font('freesansbold.ttf', 30)
            TextSurf, TextRect = text_objects(seconds, largeText, white)
            TextRect.center = (50, 30)
            game_Display.blit(TextSurf, TextRect)
        else:
            largeText = pygame.font.Font('freesansbold.ttf', 30)
            TextSurf, TextRect = text_objects(seconds, largeText, black)
            TextRect.center = (50, 30)
            game_Display.blit(TextSurf, TextRect)
        
        
        pygame.display.update()
        clock.tick(10)
        
                

game_intro()
