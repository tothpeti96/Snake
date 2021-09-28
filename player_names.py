import menu_functions
import pygame
import one_player
import one_or_two

def main():
    pygame.init()

    init_pos = pygame.mouse.get_pos()
    mouse = menu_functions.Mouse(init_pos)
    screen = menu_functions.Window()
    Font = pygame.font.Font(None, 45)
    text_surface = Font.render("Játékos neve:", True, (255,255,255))
    textbox = menu_functions.Textbox(screen, 150, 45, (170 + (text_surface.get_width()),250), 'Player_1')
    back_button = menu_functions.Button(screen, mouse, text = "Vissza", pos = (200, 400))
    game_button = menu_functions.Button(screen, mouse, text = "Mehet!", pos = (400, 400))

    pygame.time.set_timer(pygame.USEREVENT, 10)
    quit = False

    while not quit:

        mouse.pos = pygame.mouse.get_pos()
        event = pygame.event.wait()
        textbox.event_handler(event)
        
        if event.type == pygame.USEREVENT:

            screen.window.fill((0,0,0))

            back_button.on_button = False
            back_button.is_on_button(mouse)
            back_button.draw(screen)

            game_button.on_button = False
            game_button.is_on_button(mouse)
            game_button.draw(screen)

            textbox.draw(screen)
            screen.window.blit(text_surface, text_surface.get_rect(center = (170, 250)))

        if event.type == pygame.MOUSEBUTTONDOWN and back_button.on_button == True:
            return True

        if event.type == pygame.MOUSEBUTTONDOWN and game_button.on_button == True and len(textbox.text) >= textbox.min and len(textbox.text) <= textbox.max and textbox.space == False:
            return one_player.main(textbox.text)

        if event.type == pygame.QUIT:
            quit = True
        
        pygame.display.update()

