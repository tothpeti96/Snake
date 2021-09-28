import menu_functions
import pygame
import main_menu
import one_or_two
import ranglista_two_txt

def main(pont1, pont2, name1, name2):
    pygame.init()

    ranglista_two_txt.main(pont1, name1)
    ranglista_two_txt.main(pont2, name2)

    window = menu_functions.Window()
    mouse = menu_functions.Mouse(pygame.mouse.get_pos())

    font = pygame.font.Font(None, 65)
    new_font = pygame.font.Font(None, 35)
    game_over_text = font.render("Vége a játéknak!", True, (255,255,255))
    game_over_text_pos = game_over_text.get_rect(center = (300,150))

    pont_text = new_font.render("Elért pontszámaitok", True, (255,255,255))
    pont_text_pos = pont_text.get_rect(center = (300,250))

    name1 = new_font.render(str(name1), True, (255,255,255))
    name1_pos = name1.get_rect(midright = (250, 300)) 

    name2 = new_font.render(str(name2), True, (255,255,255))
    name2_pos = name2.get_rect(midleft = (350, 300)) 
    
    pont1 = new_font.render(str(pont1), True, (255,255,255))
    pont1_pos = pont1.get_rect(midright = (250, 350))

    pont2 = new_font.render(str(pont2), True, (255,255,255))
    pont2_pos = pont2.get_rect(midleft = (350, 350))

    new_game_text = new_font.render("Szeretnél új játékot játszani?", True, (255,255,255))
    new_game_text_pos = new_game_text.get_rect(center = (300,400))

    exit_button = menu_functions.Button(window, mouse, text = "Főmenü", pos = (200, 450), width = 150)
    new_game_button = menu_functions.Button(window, mouse, text = "Új játék", pos = (400, 450), width = 150)

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
            window.window.blit(name1, name1_pos)
            window.window.blit(name2, name2_pos)
            window.window.blit(pont1, pont1_pos)
            window.window.blit(pont2, pont2_pos)
            window.window.blit(new_game_text, new_game_text_pos)

        if event.type == pygame.QUIT:
            quit = True

        pygame.display.update()
