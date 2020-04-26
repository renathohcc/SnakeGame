#Primeiro game

import pygame
import pygame.locals
from random import randint
import random

#CORES
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

try:
    pygame.init()
except:
    print("O jogo não iniciou corretamente")

largura = 600
alturaplacar = 40
altura = 400 + alturaplacar
tamanhox = 10
tamanhoy = 10
tempo = pygame.time.Clock()
tamanhoobj_x = 30
tamanhoobj_y = 10
tamanhoobj2_x = 10
tamanhoobj2_y = 30


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

def snake(SnakeXY):
    for XY in SnakeXY:
        pygame.draw.rect(tela, preto, [XY[0], XY[1], tamanhox, tamanhoy])

def snakevilain(SnakeVilainXY):
    for XY in SnakeVilainXY:
        pygame.draw.rect(tela, verde, [XY[0], XY[1], tamanhox, tamanhoy])

def apple(pos_x, pos_y):
    pygame.draw.rect(tela, vermelho, [pos_x, pos_y, tamanhox, tamanhoy])

def texto(msg, cor, size, x, y):
    fonte = pygame.font.SysFont(None, size)
    texto1 = fonte.render(msg, True, cor)
    tela.blit(texto1, [x,y])

def obstaculo(obs_x, obs_y, tamobjx, tamobjy):
    pygame.draw.rect(tela, azul, [obs_x, obs_y, tamobjx, tamobjy])
def jogo ():
#VARIAVEIS
    #Musica de Fundo
    pygame.mixer.music.load("background.wav")
    pygame.mixer.music.play(-1)
    gameover = False
    pos_x = randint(0,(largura-tamanhox)/10)*10
    pos_y = randint(0,(altura-tamanhoy-alturaplacar)/10)*10
    posv_x = randint(0, (largura - tamanhox) / 10) * 10
    posv_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
    apple_x = randint(0,(largura-tamanhox)/10)*10
    apple_y = randint(0,(altura-tamanhoy-alturaplacar)/10)*10
    vel_x = 0
    vel_y = 0
    fechar = True
    SnakeXY = []
    SnakeVilainXY = []
    CompSnake = 1
    CompSnakeVilain = 1
    pontos = 0
    velocidade = 15
    obs_x = randint(0, (largura-tamanhoobj_x)/10)*10
    obs_y = randint(0, (altura-tamanhoobj_y-alturaplacar)/10)*10
    obs2_x = randint(0, (largura - tamanhoobj_x) / 10) * 10
    obs2_y = randint(0, (altura - tamanhoobj_y - alturaplacar) / 10) * 10
    obs3_x = randint(0, (largura - tamanhoobj2_x) / 10) * 10
    obs3_y = randint(0, (altura - tamanhoobj2_y - alturaplacar) / 10) * 10
    obs4_x = randint(0, (largura - tamanhoobj2_x) / 10) * 10
    obs4_y = randint(0, (altura - tamanhoobj2_y - alturaplacar) / 10) * 10
    var_ale=random.randint(0,3)
    i=random.randint(0,10)
    while fechar:
        while gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fechar = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        # Musica de Fundo
                        pygame.mixer.music.load("background.wav")
                        pygame.mixer.music.play(-1)
                        gameover = False
                        pos_x = randint(0, (largura - tamanhox) / 10) * 10
                        pos_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
                        posv_x = randint(0, (largura - tamanhox) / 10) * 10
                        posv_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
                        apple_x = randint(0, (largura - tamanhox) / 10) * 10
                        apple_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
                        vel_x = 0
                        vel_y = 0
                        fechar = True
                        SnakeXY = []
                        SnakeVilainXY = []
                        CompSnake = 1
                        CompSnakeVilain = 1
                        pontos = 0
                        velocidade = 15
                        obs_x = randint(0, (largura - tamanhoobj_x) / 10) * 10
                        obs_y = randint(0, (altura - tamanhoobj_y - alturaplacar) / 10) * 10
                        obs2_x = randint(0, (largura - tamanhoobj_x) / 10) * 10
                        obs2_y = randint(0, (altura - tamanhoobj_y - alturaplacar) / 10) * 10
                        obs3_x = randint(0, (largura - tamanhoobj2_x) / 10) * 10
                        obs3_y = randint(0, (altura - tamanhoobj2_y - alturaplacar) / 10) * 10
                        obs4_x = randint(0, (largura - tamanhoobj2_x) / 10) * 10
                        obs4_y = randint(0, (altura - tamanhoobj2_y - alturaplacar) / 10) * 10
                        var_ale = random.randint(0, 3)
                        i = random.randint(0, 10)
                    if event.key == pygame.K_s:
                        fechar = False
                        gameover = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 180 and y > 120 and x < 330 and y < 147:
                        # Musica de Fundo
                        pygame.mixer.music.load("background.wav")
                        pygame.mixer.music.play(-1)
                        gameover = False
                        pos_x = randint(0, (largura - tamanhox) / 10) * 10
                        pos_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
                        posv_x = randint(0, (largura - tamanhox) / 10) * 10
                        posv_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
                        apple_x = randint(0, (largura - tamanhox) / 10) * 10
                        apple_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
                        vel_x = 0
                        vel_y = 0
                        fechar = True
                        SnakeXY = []
                        SnakeVilainXY = []
                        CompSnakeVilain = 1
                        CompSnake = 1
                        pontos = 0
                        velocidade = 15
                        obs_x = randint(0, (largura - tamanhoobj_x) / 10) * 10
                        obs_y = randint(0, (altura - tamanhoobj_y - alturaplacar) / 10) * 10
                        obs2_x = randint(0, (largura - tamanhoobj_x) / 10) * 10
                        obs2_y = randint(0, (altura - tamanhoobj_y - alturaplacar) / 10) * 10
                        obs3_x = randint(0, (largura - tamanhoobj2_x) / 10) * 10
                        obs3_y = randint(0, (altura - tamanhoobj2_y - alturaplacar) / 10) * 10
                        obs4_x = randint(0, (largura - tamanhoobj2_x) / 10) * 10
                        obs4_y = randint(0, (altura - tamanhoobj2_y - alturaplacar) / 10) * 10
                        var_ale = random.randint(0, 3)
                        i = random.randint(0, 10)
                    elif x > 340 and y > 120 and x < 410 and y < 147:
                        fechar = False
                        gameover = False
            tela.fill(branco)
            texto("Game Over!", vermelho, 50, 200, 30)
            texto("Score Final:" + str(pontos), preto, 30, 230, 80)
            pygame.draw.rect(tela, preto, [180, 120, 150, 27])
            texto("Jogar Novamente (N)", branco, 20, 190, 125)
            pygame.draw.rect(tela, preto, [340, 120, 70, 27])
            texto("Sair (S)", branco, 20, 350, 125)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and vel_x != tamanhox:
                    vel_y = 0
                    vel_x = -tamanhox
                if event.key == pygame.K_RIGHT and vel_x != -tamanhox:
                    vel_y = 0
                    vel_x = tamanhox
                if event.key == pygame.K_UP and vel_y != tamanhoy:
                    vel_x = 0
                    vel_y = -tamanhoy
                if event.key == pygame.K_DOWN and vel_y != -tamanhox:
                    vel_x = 0
                    vel_y = tamanhoy

        if fechar:
            tela.fill(branco)
            pos_x += vel_x
            pos_y += vel_y

    #Movimentação da cobra vilã
            if(var_ale==0):
                posv_x = posv_x+tamanhox
                if(i<10):
                    i=i+1
                else:
                    var_ale=random.randint(0,3)
                    i=random.randint(0,10)
                    while var_ale == 2:
                        var_ale = random.randint(0, 3)
                        i = random.randint(0, 10)
                        pass
            elif(var_ale==1):
                posv_y = posv_y+tamanhoy
                if(i<10):
                    i=i+1
                else:
                    var_ale=random.randint(0,3)
                    i=random.randint(0,10)
                    while var_ale == 3:
                        var_ale=random.randint(0,3)
                        i=random.randint(0,10)
                        pass
            elif(var_ale==2):
                posv_x = posv_x-tamanhox
                if(i<10):
                    i=i+1
                else:
                    var_ale=random.randint(0,3)
                    i=random.randint(0,10)
                    while var_ale == 0:
                        var_ale = random.randint(0, 3)
                        i = random.randint(0, 10)
                        pass
            elif(var_ale==3):
                posv_y = posv_y-tamanhoy
                if(i<10):
                    i=i+1
                else:
                    var_ale=random.randint(0,3)
                    i=random.randint(0,10)
                    while var_ale == 1:
                        var_ale = random.randint(0, 3)
                        i = random.randint(0, 10)
                        pass

    # Para comer a maçã e a cobrinha crescer
            if pos_x == apple_x and pos_y == apple_y:
                apple_x = randint(0, (largura - tamanhox) / 10) * 10
                apple_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
                CompSnake += 1
                CompSnakeVilain += 1
                pontos += 1
                velocidade += 0.5
                impacto_sound = pygame.mixer.Sound("impacto.wav")
                impacto_sound.play()

    #REGRA PARA AS BORDAS DO DISPLAY
            if pos_x + tamanhox > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x = largura - tamanhox
            if pos_y + tamanhoy > altura - alturaplacar:
                pos_y = 0
            if pos_y < 0:
                pos_y = altura - tamanhoy - alturaplacar
            if posv_x + tamanhox > largura:
                posv_x = 0
            if posv_x < 0:
                posv_x = largura - tamanhox
            if posv_y + tamanhoy > altura - alturaplacar:
                posv_y = 0
            if posv_y < 0:
                posv_y = altura - tamanhoy - alturaplacar

            SnakeStart = []
            SnakeStart.append(pos_x)
            SnakeStart.append(pos_y)
            SnakeXY.append(SnakeStart)
            snake(SnakeXY)

            SnakeVilainStart = []
            SnakeVilainStart.append(posv_x)
            SnakeVilainStart.append(posv_y)
            SnakeVilainXY.append(SnakeVilainStart)
            snakevilain(SnakeVilainXY)

            Obstaculo_x = range(obs_x,obs_x+tamanhoobj_x,1)
            Obstaculo_y = range(obs_y, obs_y+tamanhoobj_y, 1)
            Obstaculo2_x = range(obs2_x,obs2_x+tamanhoobj_x,1)
            Obstaculo2_y = range(obs2_y, obs2_y+tamanhoobj_y, 1)
            Obstaculo3_x = range(obs3_x,obs3_x+tamanhoobj2_x,1)
            Obstaculo3_y = range(obs3_y, obs3_y+tamanhoobj2_y, 1)
            Obstaculo4_x = range(obs4_x,obs4_x+tamanhoobj2_x,1)
            Obstaculo4_y = range(obs4_y, obs4_y+tamanhoobj2_y, 1)

    #Maçã não nascer dentro de um obstaculo
            if apple_x in Obstaculo_x and apple_y in Obstaculo_y:
                apple_x = randint(0, (largura - tamanhox) / 10) * 10
                apple_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
            if apple_x in Obstaculo2_x and apple_y in Obstaculo2_y:
                apple_x = randint(0, (largura - tamanhox) / 10) * 10
                apple_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
            if apple_x in Obstaculo3_x and apple_y in Obstaculo3_y:
                apple_x = randint(0, (largura - tamanhox) / 10) * 10
                apple_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10
            if apple_x in Obstaculo4_x and apple_y in Obstaculo4_y:
                apple_x = randint(0, (largura - tamanhox) / 10) * 10
                apple_y = randint(0, (altura - tamanhoy - alturaplacar) / 10) * 10

    #Para a cobra não crescer infinitamente
            if len(SnakeXY) > CompSnake:
                del SnakeXY[0]

    # Para a cobra vilã não crescer infinitamente
            if len(SnakeVilainXY) > CompSnakeVilain:
                del SnakeVilainXY[0]

    #Para detectar uma colisão com a propria cobra e dar gameover:
            if any(Bloco == SnakeStart for Bloco in SnakeXY[:-1]):
                gameover_sound = pygame.mixer.Sound("gameover.wav")
                gameover_sound.play()
                gameover = True
                pygame.mixer.music.pause()

    #Para dar gameover em uma colisão com a cobra vilã
            if any(Bloco == SnakeStart for Bloco in SnakeVilainXY):
                gameover_sound = pygame.mixer.Sound("gameover.wav")
                gameover_sound.play()
                gameover = True
                pygame.mixer.music.pause()
            if any(Bloco == SnakeVilainStart for Bloco in SnakeXY):
                gameover_sound = pygame.mixer.Sound("gameover.wav")
                gameover_sound.play()
                gameover = True
                pygame.mixer.music.pause()
    #Para dar gameover no obstaculo
            if pos_x in Obstaculo_x and pos_y in Obstaculo_y:
                gameover_sound = pygame.mixer.Sound("gameover.wav")
                gameover_sound.play()
                gameover = True
                pygame.mixer.music.pause()
            if pos_x in Obstaculo2_x and pos_y in Obstaculo2_y:
                gameover_sound = pygame.mixer.Sound("gameover.wav")
                gameover_sound.play()
                gameover = True
                pygame.mixer.music.pause()
            if pos_x in Obstaculo3_x and pos_y in Obstaculo3_y:
                gameover_sound = pygame.mixer.Sound("gameover.wav")
                gameover_sound.play()
                gameover = True
                pygame.mixer.music.pause()
            if pos_x in Obstaculo4_x and pos_y in Obstaculo4_y:
                gameover_sound = pygame.mixer.Sound("gameover.wav")
                gameover_sound.play()
                gameover = True
                pygame.mixer.music.pause()

            apple(apple_x, apple_y)
            tempo.tick(velocidade)
            pygame.draw.rect(tela, preto, [0, altura-alturaplacar, largura, alturaplacar])
            texto("Score:"+str(pontos), branco, 20, 10, altura-alturaplacar/2)
            obstaculo(obs_x, obs_y, tamanhoobj_x, tamanhoobj_y)
            obstaculo(obs2_x, obs2_y, tamanhoobj_x, tamanhoobj_y)
            obstaculo(obs3_x, obs3_y, tamanhoobj2_x, tamanhoobj2_y)
            obstaculo(obs4_x, obs4_y, tamanhoobj2_x, tamanhoobj2_y)
            pygame.display.update()


jogo()
pygame.quit()

