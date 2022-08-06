import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
#Todas as amusicas comentadas
    #pygame.mixer.music.set_volume(0.2)
    #somDeFundo = pygame.mixer.music.load('pygame/Fundo.mp3')
    #pygame.mixer.music.play(-1)
    #colisão = pygame.mixer.Sound('pygame/smw_coin.wav')

width = 640
height = 480
xCobra = int(width/2)
yCobra = int(height/2)

Velocidade = 5

xControle = 5
yControle = 0

morreu = False
listaCobra = []
xComida = randint(40, 600)
yComida = randint(50, 430)
pontos = 0
comprimentoI = 5
tamanhoBorda = 30

fonte = pygame.font.SysFont('arial', 30, True, True)

# tela
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
# frames do jogo
clock = pygame.time.Clock()


def aumentarCobra(listaCobra):
    for XeY in listaCobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def reiniciar():
    global morreu, listaCabeça, listaCobra, xCobra, yCobra, xComida, yComida, pontos, comprimentoI, Velocidade, xControle, yControle
    morreu = False
    listaCobra = []
    listaCabeça = []
    xCobra = int(width//2)
    yCobra = int(height//2)
    xComida = randint(40, 600)
    yComida = randint(50, 430)
    pontos = 0
    comprimentoI = 5
    Velocidade = 5
    xControle = 5
    yControle = 0

while True:
    clock.tick(30)
    # Cor da tela ao atualizar
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_fomatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # mover
        if event.type == KEYDOWN:
            if event.key == K_a:
                if xControle == Velocidade:
                    pass
                else:
                    xControle = -Velocidade
                    yControle = 0
            if event.key == K_d:
                if xControle == -Velocidade:
                    pass
                else:
                    xControle = Velocidade
                    yControle = 0
            if event.key == K_w:
                if yControle == Velocidade:
                    pass
                else:
                    xControle = 0
                    yControle = -Velocidade
            if event.key == K_s:
                if yControle == -Velocidade:
                    pass
                else:
                    xControle = 0
                    yControle = Velocidade

    xCobra += xControle
    yCobra += yControle
    # bordas
    borda = pygame.draw.line(tela, (92, 64, 51),
                             (0, 0), (640, 0), tamanhoBorda)
    borda2 = pygame.draw.line(tela, (92, 64, 51),
                              (0, 0), (0, 640), tamanhoBorda)
    borda3 = pygame.draw.line(tela, (92, 64, 51),
                              (0, 480), (640, 480), tamanhoBorda)
    borda4 = pygame.draw.line(tela, (92, 64, 51),
                              (640, 480), (640, 0), tamanhoBorda)

    # desenhar retangulo
    cobra = pygame.draw.rect(tela, (0, 255, 0), (xCobra, yCobra, 20, 20))
    comida = pygame.draw.rect(tela, (255, 0, 0), (xComida, yComida, 20, 20))
    # colisões
    if comida.colliderect(cobra):
        xComida = randint(40, 600)
        yComida = randint(50, 430)
        #colisão.play()
        pontos += 1
        comprimentoI += 1
        Velocidade += 1
    if cobra.colliderect(borda) or cobra.colliderect(borda2) or cobra.colliderect(borda3) or cobra.colliderect(borda4):
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Pressione R para jogar novamente'
        formatado = fonte2.render(mensagem, False, (255, 255, 255))
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            tela.blit(formatado, (width//4, height//4))
            pygame.display.update()

    listaCabeça = []
    listaCabeça.append(xCobra)
    listaCabeça.append(yCobra)
    listaCobra.append(listaCabeça)

    if listaCobra.count(listaCabeça) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Pressione R para jogar novamente'
        formatado = fonte2.render(mensagem, True, (255, 255, 255))
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            tela.blit(formatado, (width//4, height//4))
            pygame.display.update()

    if len(listaCobra) > comprimentoI:
        del(listaCobra[0])

    aumentarCobra(listaCobra)

    tela.blit(texto_fomatado, (420, 40))
    # mantem a tela do jogo atualizando
    pygame.display.update()