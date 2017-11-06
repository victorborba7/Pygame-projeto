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

#Tela de pontuação/game over

def game_high_score(points):
    score = True
    while score:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        game_Display.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Game Over', largeText, black)
        TextRect.center = ((screen_width / 2), (150))
        game_Display.blit(TextSurf, TextRect)

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(points, largeText, black)
        TextRect.center = ((screen_width / 2), (450))
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
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("songs/Naruto.ogg"))
    
    #Cenário
    
    scene = ("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg")
    scene_count = 0
    scene = pygame.image.load(os.path.join("images", scene[scene_count]))

    floor = ("floor1.jpg","floor2.jpg","floor3.jpg","floor4.jpg","floor5.jpg","floor6.jpg")
    floor_count = 0
    floor = pygame.image.load(os.path.join("floor", floor[floor_count]))
    x_floor = 0
    y_floor = 473
    floor_speed = 10

    #Personagem

    dino = ("raptor1.png", "raptor2.png", "raptor3.png", "raptor4.png", "raptor5.png", "raptor6.png", "raptor7.png", "raptor8.png")
    dino_count = 0
    dino = pygame.image.load(os.path.join("dino", dino[dino_count]))

    #Inimigos
    
    enemy_x = 500
    
    #Triceratops

    triceratops = ("triceratops1.png","triceratops2.png","triceratops3.png","triceratops4.png","triceratops5.png","triceratops6.png","triceratops7.png","triceratops8.png","triceratops9.png","triceratops10.png","triceratops11.png","triceratops12.png")
    triceratops_count = 0
    triceratops = pygame.image.load(os.path.join("enemies/Triceratops", triceratops[triceratops_count]))

    #Ptero

    ptero = ("ptero1.png","ptero2.png","ptero3.png","ptero4.png","ptero5.png","ptero6.png","ptero7.png","ptero8.png","ptero9.png")
    ptero_count = 0
    ptero = pygame.image.load(os.path.join("enemies/Ptero", ptero[ptero_count]))
        
    #Timer

    timer = 10
    start_ticks = pygame.time.get_ticks()
        
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:

                #Pulo
                
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds\jump.ogg'))
                    jump = 10
                    game_high_score(seconds)

        seconds = str(int((pygame.time.get_ticks()-start_ticks)/100))
        points = int(seconds)

        #Levels

        if points%100 == 0 and points > 0:
            scene = ("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg")
            scene_count += 1
            if scene_count > 5:
                scene_count = 0
            scene = pygame.image.load(os.path.join("images", scene[scene_count]))
            
            floor = ("floor1.jpg","floor2.jpg","floor3.jpg","floor4.jpg","floor5.jpg","floor6.jpg")
            floor_count += 1
            if floor_count > 5:
                floor_count = 0
            if floor_count == 5:
                y_floor = 458
            else:
                y_floor = 473
            floor = pygame.image.load(os.path.join("floor", floor[floor_count]))

        #Movimentos do dino

        dino = ("raptor1.png", "raptor2.png", "raptor3.png", "raptor4.png", "raptor5.png", "raptor6.png", "raptor7.png", "raptor8.png")
        dino_count += 1
        if dino_count > 7:
            dino_count = 0
        dino = pygame.image.load(os.path.join("dino", dino[dino_count]))

        y -= jump

        #Movimentos do triceratops

        triceratops = ("triceratops1.png","triceratops2.png","triceratops3.png","triceratops4.png","triceratops5.png","triceratops6.png","triceratops7.png","triceratops8.png","triceratops9.png","triceratops10.png","triceratops11.png","triceratops12.png",)
        triceratops_count += 1
        if triceratops_count > 11:
            triceratops_count = 0
        triceratops = pygame.image.load(os.path.join("enemies/Triceratops", triceratops[triceratops_count]))

        #Movimentos do Ptero

        ptero = ("ptero1.png","ptero2.png","ptero3.png","ptero4.png","ptero5.png","ptero6.png","ptero7.png","ptero8.png","ptero9.png")
        ptero_count += 1
        if ptero_count > 8:
            ptero_count = 0
        ptero = pygame.image.load(os.path.join("enemies/Ptero", ptero[ptero_count]))
        
        #Movimentos do cenário
        
        game_Display.blit(scene, (0, 0))
        
        rel_x_floor = x_floor % floor.get_rect().width
        game_Display.blit(floor, (rel_x_floor - floor.get_rect().width, y_floor))
        if (rel_x_floor < 800):
            game_Display.blit(floor, (rel_x_floor, y_floor))
        x_floor -= floor_speed
        
        game_Display.blit(dino, (0, y))

        game_Display.blit(triceratops, (enemy_x, 360))

        game_Display.blit(ptero, (enemy_x, 160))
        
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
        clock.tick(timer)
        
                

game_intro()
