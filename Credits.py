import menu_functions
import pygame
import main_menu

def main():

    pygame.time.set_timer(pygame.USEREVENT, 10)
    quit = False
    window = menu_functions.Window()
    credits = pygame.image.load("credits.png")
    credits_pos = credits.get_rect(topleft = (10,120))
    mouse = menu_functions.Mouse(pygame.mouse.get_pos())

    back_button = menu_functions.Button(window, mouse, text = "Vissza", pos = (300, 550))

    while not quit:

        event = pygame.event.wait()
        mouse.pos = pygame.mouse.get_pos()

        if event.type == pygame.USEREVENT:
            window.window.blit(credits, credits_pos)

            back_button.on_button = False
            back_button.is_on_button(mouse)
            back_button.draw(window)

        if event.type == pygame.MOUSEBUTTONDOWN and back_button.on_button == True:
            return

        if event.type == pygame.QUIT:
            return

        pygame.display.update()

