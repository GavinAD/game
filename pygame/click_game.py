figure = Actor("character")
figure.pos = 0, 0

WIDTH = 500
HEIGHT = 300
BACKGROUND_COLOR = (174, 174, 174)

def draw():
    screen.fill(BACKGROUND_COLOR)
    figure.draw()

def update():
    figure.left = figure.left + 2
    if figure.left > WIDTH:
        figure.right = 0
    figure.bottom = figure.bottom + 1
    if figure.bottom > HEIGHT:
        figure.top = 0
