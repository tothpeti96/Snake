import menu_functions
import pygame
import two_players
import one_or_two


def main():
    pygame.init()

    init_pos = pygame.mouse.get_pos()
    mouse = menu_functions.Mouse(init_pos)
    screen = menu_functions.Window()
    Font = pygame.font.Font(None, 45)
    text_surface_1 = Font.render("1. játékos neve:", True, (255,255,255))
    text_surface_2 = Font.render("2. játékos neve:", True, (255,255,255))
    textbox_1 = menu_functions.Textbox(screen, 150, 30, (170 + (text_surface_1.get_width()),200), "Player_1")
    textbox_2 = menu_functions.Textbox(screen, 150, 30, (170 + (text_surface_1.get_width()),300), "Player_2")
    back_button = menu_functions.Button(screen, mouse, text = "Vissza", pos = (200, 400))
    game_button = menu_functions.Button(screen, mouse, text = "Mehet!", pos = (400, 400))


    pygame.time.set_timer(pygame.USEREVENT, 10)
    quit = False

    while not quit:

        mouse.pos = pygame.mouse.get_pos()
        event = pygame.event.wait()
        textbox_1.event_handler(event)
        textbox_2.event_handler(event)

        if event.type == pygame.USEREVENT:
            screen.window.fill((0,0,0))

            if textbox_2.clicked:
                textbox_1.clicked = False

                if textbox_1.clicked:
                    textbox_2.clicked = False

            back_button.on_button = False
            back_button.is_on_button(mouse)
            back_button.draw(screen)

            game_button.on_button = False
            game_button.is_on_button(mouse)
            game_button.draw(screen)

            textbox_1.draw(screen)
            textbox_2.draw(screen)

            screen.window.blit(text_surface_1, text_surface_1.get_rect(center = (200, 200)))
            screen.window.blit(text_surface_2, text_surface_1.get_rect(center = (200, 300)))

        if event.type == pygame.MOUSEBUTTONDOWN and back_button.on_button == True:
            return True

        if event.type == pygame.MOUSEBUTTONDOWN and game_button.on_button == True and len(textbox_1.text) >= textbox_1.min and len(textbox_1.text) <= textbox_1.max and len(textbox_2.text) >= textbox_2.min and len(textbox_2.text) <= textbox_2.max :
            return two_players.main(textbox_1.text, textbox_2.text)
           

        if event.type == pygame.QUIT:
            quit = True

        pygame.display.update()

