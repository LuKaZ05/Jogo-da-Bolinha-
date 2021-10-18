
from graphics import *
import random
#win2 (Tela inicial)
win2 = GraphWin('Jogo da Bolinha', 800, 600)
win2.setBackground('green')
titulo = Text(Point(390, 70), 'Soccer Ball')
titulo.setSize(18)
titulo.setStyle('bold')
titulo.setFace('courier')
titulo.draw(win2)

txtnome = Text(Point(400, 280), 'Nome do jogador')
txtnome.draw(win2)
input_box = Entry(Point(400, 300), 13)
input_box.draw(win2)
nome = input_box.getText()

linhaSuperior = Line(Point(0, 40), Point(800, 40))
linhaSuperior.setWidth(3)
linhaSuperior.setOutline("black")
linhaSuperior.setFill('white')
linhaSuperior.draw(win2)

linhaInferior = Line(Point(0, 550), Point(800, 550))
linhaInferior.setWidth(3)
linhaInferior.setOutline('black')
linhaInferior.setFill('white')
linhaInferior.draw(win2)

linhaMeio = Line(Point(0,300), Point(800,300))
linhaMeio.setWidth(3)
linhaMeio.setOutline('black')
linhaMeio.setFill('white')
linhaMeio.draw(win2)

circulo = Circle(Point(400,300), 50)
circulo.setWidth(3)
circulo.setOutline("white")
circulo.draw(win2)

linhaTrave1 = Line(Point(250,550), Point(250,530))
linhaTrave1.setWidth(3)
linhaTrave1.setOutline('white')
linhaTrave1.setFill('white')
linhaTrave1.draw(win2)

linhaTrave2 = Line(Point(540,550), Point(540,530))
linhaTrave2.setWidth(3)
linhaTrave2.setOutline('white')
linhaTrave2.setFill('white')
linhaTrave2.draw(win2)

linhaTrave3 = Line(Point(540,60), Point(540,40))
linhaTrave3.setWidth(3)
linhaTrave3.setOutline('white')
linhaTrave3.setFill('white')
linhaTrave3.draw(win2)

linhaTrave4 = Line(Point(250,60), Point(250,40))
linhaTrave4.setWidth(3)
linhaTrave4.setOutline('white')
linhaTrave4.setFill('white')
linhaTrave4.draw(win2)


retangulo1 = Rectangle(Point(80, 80), Point(116, 100))
retangulo1.setFill("black")
retangulo1.setOutline("black")
retangulo1.draw(win2)

retangulo2 = Rectangle(Point(600, 80), Point(636, 100))
retangulo2.setFill("black")
retangulo2.setOutline("black")
retangulo2.draw(win2)


retangulo3 = Rectangle(Point( 500, 200), Point(536, 220))
retangulo3.setFill("black")
retangulo3.setOutline("black")
retangulo3.draw(win2)

retangulo = Rectangle(Point(200, 200), Point(236, 220))
retangulo.setFill("black")
retangulo.setOutline("black")
retangulo.draw(win2)


win2.getMouse()
win2.close()


#win (tela do jogo)
win = GraphWin("Bolinha ...", 800, 600)
win.setBackground('green')

linhaSuperior = Line(Point(0, 40), Point(800, 40))
linhaSuperior.setWidth(3)
linhaSuperior.setOutline("black")
linhaSuperior.setFill('white')
linhaSuperior.draw(win)

linhaInferior = Line(Point(0, 550), Point(800, 550))
linhaInferior.setWidth(3)
linhaInferior.setOutline('black')
linhaInferior.setFill('white')
linhaInferior.draw(win)

linhaMeio = Line(Point(0,300), Point(800,300))
linhaMeio.setWidth(3)
linhaMeio.setOutline('black')
linhaMeio.setFill('white')
linhaMeio.draw(win)

circulo = Circle(Point(400,300), 50)
circulo.setWidth(3)
circulo.setOutline("white")
circulo.draw(win)


# Texto Vidas
txtv = Text(Point(730, 560), 'VIDAS:')
txtv.setFace('courier')
txtv.setStyle('bold')
txtv.draw(win)

# Bolinhas da vida
b1 = Circle(Point(705, 580), 10)
b1.setOutline('black')
b1.setFill('white')
b1.draw(win)

b2 = Circle(Point(728, 580), 10)
b2.setOutline('black')
b2.setFill('white')
b2.draw(win)

b3 = Circle(Point(751, 580), 10)
b3.setOutline('black')
b3.setFill('white')
b3.draw(win)

vidas = 3

col = 390
lin = 80
raio = 15
circulo = Circle(Point(col, lin), raio)
circulo.setFill(color_rgb(250, 10, 200))
circulo.draw(win)

initial_speed = 5
velocity_increment = 1

ptsstring = 0
pontos = Text(Point(400, 575), " " + str(ptsstring))
pontos.setSize(14)
pontos.draw(win)

pts = 0

colIni = 10
tamanho = 100
barra = Line(Point(colIni, 530), Point(colIni + tamanho, 530))
barra.setOutline('black')
barra.setFill('black')
barra.setWidth(10)
barra.draw(win)

velocidade = 5
bateu = True
continuar = True
while continuar:

    if bateu:
        passo = random.randrange(1, 10)
        if random.random() < 0.5:
            passo = -passo
        bateu = False

    if (col + raio + passo) > 800:
        passo = -passo

    if (col - raio + passo) < 0:
        passo = -passo

    if lin < 65:
        velocidade = -velocidade

    if 515 <= lin <= 530 and colIni < col < (colIni + tamanho):
        pts += 1

        velocidade = initial_speed + (pts * velocity_increment)

        velocidade = -velocidade
        pontos.setText(pts)


    # Nova posição do círculo
    circulo.undraw()
    col += passo
    lin += velocidade
    circulo = Circle(Point(col, lin), 15)
    circulo.setFill(color_rgb(250, 10, 200))
    circulo.draw(win)

    # MECANISMO DE VIDAS
    if lin >= 550:
        circulo.undraw()
        vidas = vidas - 1

        if vidas > 0:
            col = 390
            lin = 80
            raio = 15
            circulo = Circle(Point(col, lin), raio)
            circulo.setFill(color_rgb(250, 10, 200))
            circulo.draw(win)
            circulo.undraw()
            col += passo
            lin += velocidade
            circulo = Circle(Point(col, lin), 15)
            circulo.setFill(color_rgb(250, 10, 200))
            circulo.draw(win)

            if vidas >= 2:
                b1.undraw()
            else:
                b2.undraw()

        # GAMEOVER A PARTIR DAQUI
        else:   # elif vidas == 0:
            win.close()
            win3 = GraphWin('FIM DE JOGO', 600, 600)
            win3.setBackground('black')
            gameovertxt = Text(Point(300, 100), 'FIM DE JOGO')
            gameovertxt.setFace('courier')
            gameovertxt.setSize(20)
            gameovertxt.setTextColor('red')
            placar = Text(Point(300, 250), pts)
            placar.setFace('courier')
            placar.setSize(18)
            placar.setTextColor('Red')
            pontos = Text(Point(310,300),'defesas')
            pontos.setFace('courier')
            pontos.setSize(18)
            pontos.setTextColor('red')
            nome1 = Text(Point(300, 200), input_box.getText())
            nome1.setFace('courier')
            nome1.setSize(18)
            nome1.setTextColor('red')
            nome1.draw(win3)
            placar.draw(win3)
            pontos.draw(win3)
            gameovertxt.draw(win3)
            win3.getMouse()
            win3.close()

    # Movimento horizontal da barra pelas setas direita/esquerda
    tecla = win.checkKey()

    # Sair do joguinho
    if tecla == "Escape":
        continuar = False
        continue

    if tecla == "Right":
        if (colIni + 20) < 701:
            colIni = colIni + 20

        barra.undraw()
        barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
        barra.setOutline('black')
        barra.setFill('black')
        barra.setWidth(10)
        barra.draw(win)

    if tecla == "Left":
        if (colIni - 20) > -1:
            colIni = colIni - 20

        barra.undraw()
        barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
        barra.setOutline('black')
        barra.setFill('black')
        barra.setWidth(10)
        barra.draw(win)

    # Esperar o ser humano reagir
    time.sleep(.05)

win.close()
