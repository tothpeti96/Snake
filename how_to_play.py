import menu_functions
import pygame
import main_menu

def main():

    pygame.time.set_timer(pygame.USEREVENT, 10)
    quit = False
    window = menu_functions.Window()
    how_to_image = pygame.image.load("how_to_play_resized.png")
    how_to_image_pos = how_to_image.get_rect(topleft = (10,20))
    mouse = menu_functions.Mouse(pygame.mouse.get_pos())

    back_button = menu_functions.Button(window, mouse, text = "Vissza", pos = (300, 550))

    while not quit:

        event = pygame.event.wait()
        mouse.pos = pygame.mouse.get_pos()

        if event.type == pygame.USEREVENT:
            window.window.blit(how_to_image, how_to_image_pos)

            back_button.on_button = False
            back_button.is_on_button(mouse)
            back_button.draw(window)

        if event.type == pygame.MOUSEBUTTONDOWN and back_button.on_button == True:
            return

        if event.type == pygame.QUIT:
            return

        pygame.display.update()

