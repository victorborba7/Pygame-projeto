import pygame

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

screen_width = 800
screen_height = 600


game_Display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ninjassauro')
clock = pygame.time.Clock()

#Funções para definições de texto

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Função para mensagens

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
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
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((pos_x + (width / 2)), (pos_y + (high / 2)))
    game_Display.blit(textSurf, textRect)

#Função para sair do jogo

def quitgame():
    pygame.quit()
    quit()

#Função do tutorial do jogo

def game_tutorial():
    tutorial = True
    while tutorial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        game_Display.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects('Tutorial', largeText)
        TextRect.center = (90, 100)
        game_Display.blit(TextSurf, TextRect)

        largeTutorial = pygame.font.Font('freesansbold.ttf', 20)
        TutorialSurf, TutorialRect = text_objects('Spacebar: Jump', largeText)
        TutorialRect.center = (153, 200)
        game_Display.blit(TutorialSurf, TutorialRect)

        largeTutorial1 = pygame.font.Font('freesansbold.ttf', 20)
        Tutorial1Surf, Tutorial1Rect = text_objects('Esc: Pause', largeText)
        Tutorial1Rect.center = (116, 300)
        game_Display.blit(Tutorial1Surf, Tutorial1Rect)

        button('Back', 30, 500, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(15)

#Menu do jogo

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        game_Display.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Ninjassauro', largeText)
        TextRect.center = ((screen_width / 2), (150))
        game_Display.blit(TextSurf, TextRect)

        button('Play', 125, 350, 100, 50, green, bright_green, quitgame)
        button('Quit', 350, 450, 100, 50, red, bright_red,  quitgame)
        button('Tutorial', 575, 350, 100, 50, blue, bright_blue, game_tutorial)

        pygame.display.update()
        clock.tick(15)

game_intro()