import pygame
import random
import time
from pygame.examples import playmus

pingu_height = 40
pingu_width = 10

screen_width = 800
screen_height = 700

pink = (234, 137, 154)
white = (255, 255, 255)
blue = (37, 36, 64)
red = (200, 0, 0)
red_floji = (255, 0, 0)
green = (18, 230, 0)
green_floji = (206, 255, 42)
orange = (255, 131, 0)
orange_floji = (251, 232, 112)
blue_floji = (173, 216, 230)
pink_floji=(255,213,240)

screen = pygame.display.set_mode((screen_width, screen_height))
score = 0
clock = pygame.time.Clock()


def juego_init():
    pygame.init()
    pygame.mixer.music.load("nemo.mp3")
    pygame.mixer_music.play(3)
    pygame.display.set_caption('Saving Nemo')



def puntuacion(cont, x, y, message_format='Text: %d'):
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render(message_format % cont, True, white)
    screen.blit(text, (x, y))


def texto(text, font):
    texto_s = font.render(text, True, white)
    return texto_s, texto_s.get_rect()


def image_loaded(x, y, name_image):
    imagen = pygame.image.load(name_image)
    screen.blit(imagen, (x, y))


# DISPLAY TO SHOW MESSAGES
def screen_message(text):
    pygame.font.init()
    texto_grande = pygame.font.SysFont("Garamond", 100)
    text_surf, text_rect = texto(text, texto_grande)
    text_rect.center = ((screen_width / 2), (screen_height / 2))
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)
    dory_game()


#button(text, dimensions/location of the text, colors of the text, action(e.g. if you want to quit the game)
def boton(msg, x, y, wi, he, ic, act, action=None):

    mouse_cursor = pygame.mouse.get_pos()
    mouse_input = pygame.mouse.get_pressed()

    if x + wi > mouse_cursor[0] > x and y + he > mouse_cursor[1] > y:
        pygame.draw.ellipse(screen, act, (x, y, wi, he))
        if mouse_input[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, ic, (x, y, wi, he))
    pygame.font.init()
    text_peq = pygame.font.SysFont('Courier', 30)
    text_surf, text_rect = texto(msg, text_peq)
    text_rect.center = ((x + (wi / 2)), (y + (he / 2)))
    screen.blit(text_surf, text_rect)



def collision(x, y):
    pygame.mixer.music.stop()

    pygame.font.init()
    texto_grande = pygame.font.SysFont('Comic Sans', 70)
    text_surf, text_rect, = texto("GAME OVER", texto_grande)
    text_rect.center = ((screen_width / 2), (screen_height / 3))
    screen.blit(text_surf, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        boton("Play Again", 200, 500, 180, 180, pink, pink_floji, intro_game)
        boton("Exit", 450, 500, 180, 180, red, red_floji, exit_game)

        pygame.display.update()
        clock.tick(15)


def exit_game():
    pygame.quit()
    quit()


def intro_game():
    intro = True
    score = 0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(blue)
        mar = pygame.image.load('mar.jpg')
        screen.blit(mar, (0, 0))
        pygame.display.flip()
        texto_grande = pygame.font.SysFont("Garamond", 82)
        text_surf, text_rect = texto(" 'SAVING NEMO' ", texto_grande)
        text_rect.center = ((screen_width / 2), (screen_height / 2))
        screen.blit(text_surf, text_rect)

        boton("Level 1: Dory", 125, 500, 170, 170, green, green_floji, dory_game)
        boton("Level 2: Nemo", 300, 500, 170, 170, orange, orange_floji, nemo_game)
        boton("Exit", 475, 500, 170, 170, red, red_floji, exit_game)

        pygame.display.update()
        clock.tick(15)


def nemo_game():

    score = 0
    pygame.mixer_music.play(3)

    x = (screen_width * 0.45)
    y = (screen_height * 0.75)
    x_cge = 0
    pin_width = 70
    pin_height = 140
    pin_startx = random.randrange(100, screen_width - 200)
    pin_starty = -600
    pin_speed = 25
    ly = 0
    lh = 450
    l_speed = 100
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_cge = -10
                if event.key == pygame.K_RIGHT:
                    x_cge = 10
            if event.type == pygame.KEYUP:
                x_cge = 0

        x += x_cge
        screen.fill(blue)
        mar = pygame.image.load('mar.jpg')
        screen.blit(mar, (0, 0))
        pygame.display.flip()
        image_loaded(pin_startx, pin_starty, 'tiburon.png')
        image_loaded(x, y, 'nemo.png')
        pin_starty += pin_speed
        ly += pin_speed
        puntuacion(((pin_speed * 60) - 1020), 5, 45, "Speed: %d ")
        puntuacion(score, 5, 5, "Score: %d")

        # CRASH BOUNDARIES ON THE DISPLAY
        if x > screen_width - pingu_width - 70 or x < 0:
            collision(x, y)

        if pin_starty > screen_height:
            pin_starty = 0 - pin_height
            pin_startx = random.randrange(170, screen_width - pin_width - 150)
            score += 1  # INCREASE SCORE WHEN DODGING
            pin_speed += 1 / 20  # ACCELERATE

        if ly > screen_height:
            ly = 0 - lh
            pin_speed += 1 / 15

        # CHECK CRASHES
        if y < (pin_starty + pin_height) and y + pingu_height >= pin_starty + pin_height:
            if x > pin_startx and x < (pin_startx + pin_width) or x + pingu_width > pin_startx \
                    and x + pingu_width < pin_startx + pin_width:
                collision(x, y)
        pygame.display.update()
        clock.tick(20)

        if score == 26:
            congrats()


# GAME LOOP
def dory_game():
    # global score
    score = 0
    pygame.mixer_music.play(3)
    x = (screen_width * 0.45)
    y = (screen_height * 0.75)
    x_cge = 0

    dor_width = 70
    dor_height = 140
    dor_startx = random.randrange(100, screen_width - 200)
    dor_starty = -600
    dor_speed = 18
    ly = 0
    lh = 450
    dor_speed = 18
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_cge = -10
                if event.key == pygame.K_RIGHT:
                    x_cge = 10

            if event.type == pygame.KEYUP:
                x_cge = 0

        x += x_cge
        screen.fill(blue)
        mar = pygame.image.load('mar.jpg')

        screen.blit(mar, (0, 0))
        pygame.display.flip()
        image_loaded(dor_startx, dor_starty, 'tiburon.png')
        image_loaded(x, y, 'dory.png')

        dor_starty += dor_speed
        ly += dor_speed
        puntuacion(((dor_speed * 60) - 1020), 5, 45, "Speed: %d ")
        puntuacion(score, 5, 5, "Score: %d")

        # CRASH BOUNDARIES ON THE DISPLAY
        if x > screen_width - pingu_width - 70 or x < 0:
            collision(x, y)

        if dor_starty > screen_height:
            dor_starty = 0 - dor_height
            dor_startx = random.randrange(170, screen_width - dor_width - 150)
            score += 1  # INCREASE SCORE WHEN DODGING
            dor_speed += 1 / 20  # ACCELERATE

        if ly > screen_height:
            ly = 0 - lh
            dor_speed += 1 / 15

        # CHECK CRASHES
        if y < (dor_starty + dor_height) and y + pingu_height >= dor_starty + dor_height:
            if x > dor_startx and x < (dor_startx + dor_width) or x + pingu_width > dor_startx \
                    and x + pingu_width < dor_startx + dor_width:
                collision(x, y)

        pygame.display.update()
        clock.tick(60)


        if score == 26:
            congrats()


def congrats():
    pygame.mixer.music.stop()
    # game_over = pygame.mixer.Sound("bros.mp3")
    # game_over.play()
    pygame.font.init()
    texto_grande = pygame.font.SysFont('Comic Sans', 60)
    text_surf, text_rect, = texto("Congratulations, You have won!", texto_grande)
    text_rect.center = ((screen_width / 2), (screen_height / 3))
    screen.blit(text_surf, text_rect)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        boton("Play Again", 200, 500, 180, 180, pink, pink_floji, intro_game)
        boton("Exit", 450, 500, 180, 180, red, red_floji, exit_game)
        pygame.display.update()
        clock.tick(15)


def main():
    juego_init()
    intro_game()
    dory_game()
    nemo_game()
    congrats()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
