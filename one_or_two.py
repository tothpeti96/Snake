import pygame
import menu_functions
import pygame.font
import one_player
import two_players
import player_names
import two_names
import main_menu

def main():
    pygame.init()

    one_or_two_window = menu_functions.Window()
    pos_init = pygame.mouse.get_pos()

    mouse = menu_functions.Mouse(pos_init)

    title_betutip = pygame.font.Font(None, 40)
    one_or_two_text = title_betutip.render("Egy vagy két játékos üzemmód?", True, (255, 255, 255))
    title_pos = one_or_two_text.get_rect(center = (300, 122.828))

    one_button = menu_functions.Button(one_or_two_window, mouse, text = "Egy játékos", pos = (177.175, 300), heigth = 108.7, width = 200, fontsize = 40)
    two_button = menu_functions.Button(one_or_two_window, mouse, text = "Két játékos", pos = (422.825, 300), heigth = 108.7, width = 200, fontsize = 40)
    back_button = menu_functions.Button(one_or_two_window, mouse, text = "Vissza", pos = (300, 477.175), heigth = 108.7, width = 136.95, fontsize = 40)
    
    quit = False
    pygame.time.set_timer(pygame.USEREVENT, 10)

    while not quit:
        mouse.pos = pygame.mouse.get_pos()
        event = pygame.event.wait()

        if event.type == pygame.USEREVENT:

            one_or_two_window.window.fill((0,0,0))
            
            one_or_two_window.window.blit(one_or_two_text, title_pos)

            one_button.on_button = False
            one_button.is_on_button(mouse)
            one_button.draw(one_or_two_window)

            two_button.on_button = False
            two_button.is_on_button(mouse)
            two_button.draw(one_or_two_window)

            back_button.on_button = False
            back_button.is_on_button(mouse)
            back_button.draw(one_or_two_window)

        if event.type == pygame.MOUSEBUTTONDOWN and one_button.on_button:
            new_game = player_names.main()
            if new_game:
                pass
            else:
                return
            
        if event.type == pygame.MOUSEBUTTONDOWN and two_button.on_button:
            new_game = two_names.main()
            if new_game:
                pass
            else:
                return

        if event.type == pygame.MOUSEBUTTONDOWN and back_button.on_button:
            return

        if event.type == pygame.QUIT:
            quit = True

        pygame.display.update()


