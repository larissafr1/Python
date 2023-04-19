import pygame as pg #tela inicial
import math #cálculos especificos
import pandas as pd #informações específicas

#CORES
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
cinza = (150, 150, 150)

#SETUP TELA DO JOGO
window = pg.display.set.mode ((1000, 600))
window.fill(branco)

#INICIALIZAÇÃO DA FONTE
pg.font.init()
fonte = pg.font.SysFont("Comic Sans MS", 30)

board_array = [
    ['n', 'n', 'n'],
    ['n', 'n', 'n'],
    ['n', 'n', 'n']
]

click_last_status = 0
click_on_off = 0
click_position_x = -1
click_position_y = -1

X_or_O_turn = 'x'
end_game = 0

#DESENHO DO TABULEIRO
def grade_do_tabuleiro(window):
    pg.draw.line(window, preto, (205, 0), (205,600), 10)
    pg.draw.line(window, preto, (405, 0), (405,600), 10)
    pg.draw.line(window, preto, (0, 205), (600, 205), 10)
    pg.draw.line(window, preto, (0, 405), (600, 405), 10)


#CONFERE O CLICK ATUAL E O ULTIMO
def click_logic(click_on_off, click_last_status, x, y):
    if click[0] == 0 and click_last_status == 1:
        click_on_off = 1
        x = (math.ceil(mouse[0] / 200) -1)
        y = (math.ceil(mouse[1] / 200) -1)
    elif click[0] == 0 and click_last_status == 0:
        click_on_off = 0
        x = -1
        y = -1
    return click_on_off, click_last_status, x, y 

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()


    #DECLARANDO VARIÁVEL DA POSIÇÃO DO MOUSE
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse [0]
    mouse_position_y = mouse [1]
     

    #DECLARANDO VARIÁVEL NO CLICK DO MOUSE
    clickk = pg.mouse.get_pressed()
    print (click) #varia true e false


    #JOGO
    grade_do_tabuleiro(window)



    if click[0] == 1:
        click_last_status = 1
    else: 
        click_last_status = 0
    
    pg.display.update()



