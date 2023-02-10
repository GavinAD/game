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

def on_mouse_down(pos):
    if figure.collidepoint(pos):
        set_figure_hurt()
        print("EEK!")

def set_figure_hurt():
    figure.image = "character_clicked"
    sounds.oof.play()
    clock.schedule_unique(set_figure_normal, 1.0)

def set_figure_normal():
    figure.image = "character"
