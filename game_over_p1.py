import menu_functions
import pygame
import main_menu
import one_or_two
import ranglista_one_txt

def main(pont, name):
    pygame.init()

    ranglista_one_txt.main(name, pont)

    window = menu_functions.Window()
    mouse = menu_functions.Mouse(pygame.mouse.get_pos())

    font = pygame.font.Font(None, 65)
    new_font = pygame.font.Font(None, 35)
    game_over_text = font.render("Vége a játéknak!", True, (255,255,255))
    game_over_text_pos = game_over_text.get_rect(center = (300,150))

    pont_text = new_font.render("Elért pontszámod", True, (255,255,255))
    pont_text_pos = pont_text.get_rect(center = (300,250))
    
    pont = new_font.render(str(pont), True, (255,255,255))
    pont_pos = pont.get_rect(center = (300, 300))

    new_game_text = new_font.render("Szeretnél új játékot játszani?", True, (255,255,255))
    new_game_text_pos = new_game_text.get_rect(center = (300,350))

    exit_button = menu_functions.Button(window, mouse, text = "Főmenü", pos = (200, 400), width = 150)
    new_game_button = menu_functions.Button(window, mouse, text = "Új játék", pos = (400, 400), width = 150)

    quit = False
    pygame.time.set_timer(pygame.USEREVENT, 10)

    while not quit:
        event = pygame.event.wait()
        mouse.pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and exit_button.on_button:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN and new_game_button.on_button:
            return True

        if event.type == pygame.USEREVENT:

            exit_button.on_button = False
            exit_button.is_on_button(mouse)
            exit_button.draw(window)

            new_game_button.on_button = False
            new_game_button.is_on_button(mouse)
            new_game_button.draw(window)

            window.window.blit(game_over_text, game_over_text_pos)
            window.window.blit(pont_text, pont_text_pos)
            window.window.blit(new_game_text, new_game_text_pos)
            window.window.blit(pont, pont_pos)

        if event.type == pygame.QUIT:
            quit = True

        pygame.display.update()
