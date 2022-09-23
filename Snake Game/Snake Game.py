import pygame #importa lyb
from pygame.locals import * #importa todos com da lyb
from sys import exit
from random import randint

pygame.init()

#son de fundo
pygame.mixer.music.set_volume(0.05)
son_de_fundo= pygame.mixer.music.load('sons/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1) #-1 toca em loop
#son_colisao
son_colisao= pygame.mixer.Sound('sons/smw_coin.wav') #wav extensão necessario para tds sons sem ser o de fundo

largura = 640
altura = 480

#posição cobra
x_cobra= 400
y_cobra= 200

x_maca = randint(40,600)
y_maca = randint(40,430)

deslocamento = 10
x_controle = deslocamento
y_controle = 0

tela = pygame.display.set_mode((largura, altura)) #tamanho da tela
pygame.display.set_caption('My PyGame')

clock= pygame.time.Clock()

#painel de pontos#
fonte= pygame.font.SysFont('arial', 30, True, True) #fonte, tamanho, bold, italico
pontos = 0

#lista_cobra
lista_cobra = []
comp_inicio = 5

morreu = False

#def = define uma função
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y] -> XeY[0], XeY[1]
        pygame.draw.rect(tela, (0,153,0),(XeY[0], XeY[1], 40,40))

#função reiniciar
def reiniciar_jogo():
    global pontos, comp_inicio, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, morreu, frames
    pontos = 0
    comp_inicio = 5
    #posição cobra
    x_cobra= 400
    y_cobra= 200
    lista_cabeca =[]
    lista_cobra=[]
    x_maca = randint(40,600)
    y_maca = randint(40,430)
    morreu = False
    frames = 10


frames = 10

while True:
    clock.tick(frames)#fps
    tela.fill((0,0,0)) #preenchimento do backgroud
    #Painel de pontos
    msg= f'Pontos: {pontos}'
    txt_formatado= fonte.render(msg, False, (255, 255, 255)) #Texto, serrilhamento(pixels), cor

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

##movimentos com as teclas
    if event.type == KEYDOWN:
            if event.key == K_a or event.key ==K_LEFT:
                if x_controle == deslocamento:
                    pass
                else:
                    x_controle = -deslocamento
                    y_controle = 0
            if event.key == K_d or event.key ==K_RIGHT:
                if x_controle == -deslocamento:
                    pass
                else:
                    x_controle = +deslocamento
                    y_controle = 0
            if event.key == K_w or event.key ==K_UP:
                if y_controle == deslocamento:
                    pass
                else:
                    x_controle = 0
                    y_controle = -deslocamento
            if event.key == K_s or event.key ==K_DOWN:
                if y_controle == -deslocamento:
                    pass
                else:
                    x_controle = 0
                    y_controle = +deslocamento

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    
    cobra = pygame.draw.rect(tela, (0,153,0), (x_cobra,y_cobra,30,30)) #tela, cor, coordenadas e tamanho

    maca = pygame.draw.rect(tela, (204,0,0), (x_maca,y_maca,20,20)) #tela, cor, coordenadas e tamanho

    if cobra.colliderect(maca):
        pontos= pontos+1
        x_maca = randint(40,600)
        y_maca = randint(40,430)
        son_colisao.play()
        comp_inicio = comp_inicio+1
        frames = frames+0.5
         

    #lista das posições onde a cobra anda
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)


    if lista_cobra.count(lista_cabeca)>1 or x_cobra > largura or x_cobra < 0 or y_cobra < 0 or y_cobra > altura: 
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()


     ## 
    """if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0"""
    ##


    if (len(lista_cobra) > comp_inicio):
        del lista_cobra[0]

    #chama função
    aumenta_cobra(lista_cobra)

    #texto dos pontos    
    tela.blit(txt_formatado, (450,40)) #string, posição

    pygame.display.update()