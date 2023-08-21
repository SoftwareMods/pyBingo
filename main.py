import pygame, sys
from settings import *
from button import Button

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Bingo!")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("arialblack", 40)


def play():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill((52, 78, 91))

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((52, 78, 91))

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def setup():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill((200, 200, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main_menu(screen):
    while True:
        button_width = screen.get_size()[0] // 5
        screen.fill((52, 78, 91))
        mouse_pos = pygame.mouse.get_pos()
        font = pygame.font.Font(None, int(screen.get_size()[1] / 5))
        text = font.render("BINGO", True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(screen.get_size()[0] / 2, screen.get_size()[1] / 5)
        )
        screen.blit(text, text_rect)
        items = ["Play", "Setup", "Options","Quit"]
        for index, item in enumerate(items):
            full_width = screen.get_size()[0]
            increment = full_width // len(items)
            left = (index * increment) + (increment - button_width) // 2
            top = screen.get_size()[1] * 0.7
            h = screen.get_size()[0] // 10
            w = screen.get_size()[0] // 5
            if item == "Play":
                PLAY_BUTTON = Button(
                    text_input="PLAY",
                    base_color="White",
                    hovering_color="Black",
                    left=left,
                    top=top,
                    w=w,
                    h=h
                )
            elif item == "Options":
                OPTIONS_BUTTON = Button(
                    text_input="OPTIONS",
                    base_color="White",
                    hovering_color="Black",
                    left=left,
                    top=top,
                    w=w,
                    h=h
                )
            elif item == "Setup":
                SETUP_BUTTON = Button(
                    text_input="SETUP",
                    base_color="White",
                    hovering_color="Black",
                    left=left,
                    top=top,
                    w=w,
                    h=h
                )
            elif item == "Quit":
                QUIT_BUTTON = Button(
                    text_input="QUIT",
                    base_color="DarkRed",
                    hovering_color="Black",
                    left=left,
                    top=top,
                    w=w,
                    h=h
                )

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, SETUP_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WIDTH = event.w
                HEIGHT = event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play()
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    options()
                if SETUP_BUTTON.checkForInput(mouse_pos):
                    setup()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()


main_menu(screen)
