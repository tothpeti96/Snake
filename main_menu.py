import menu_functions
import pygame.font
import one_or_two
import leaderboards_one
import how_to_play
import Credits

def main():

    menu_window = menu_functions.Window()
    pos_init = pygame.mouse.get_pos()

    mouse = menu_functions.Mouse(pos_init)

    title_betutip = pygame.font.Font(None, 100)
    snake_text = title_betutip.render("Snake", True, (255,255,255))
    title_pos =  snake_text.get_rect(center = (312.495, 76.205))
   
    start_button = menu_functions.Button(menu_window, mouse, text="Start", pos = (312.495, 206.845), heigth = 108.87, width = 208.33, fontsize = 40)
    lb_button = menu_functions.Button(menu_window, mouse, text="Leaderboard", pos = (312.495, 337.485), heigth = 108.87, width = 208.33)
    credits_button = menu_functions.Button(menu_window, mouse, text="Credits", pos = (312.495, 468.125), heigth = 108.87, width = 208.33)
    exit_button = menu_functions.Button(menu_window, mouse, text="Exit", pos = (312.495, 598.75), heigth = 108.87, width = 208.33)
    how_to_button = menu_functions.Button(menu_window, mouse, text = "How to Play", pos = (60, 30), width = 100, heigth = 30, fontsize = 25)

    quit = False
    pygame.time.set_timer(pygame.USEREVENT, 10)
    
    while not quit:

        mouse.pos = pygame.mouse.get_pos()
        event = pygame.event.wait()

        if event.type == pygame.USEREVENT:

            menu_window.window.fill((0,0,0))

            menu_window.window.blit(snake_text, title_pos)

            start_button.on_button = False
            start_button.is_on_button(mouse)
            start_button.draw(menu_window)

            lb_button.on_button = False
            lb_button.is_on_button(mouse)
            lb_button.draw(menu_window)

            credits_button.on_button = False
            credits_button.is_on_button(mouse)
            credits_button.draw(menu_window)

            exit_button.on_button = False
            exit_button.is_on_button(mouse)
            exit_button.draw(menu_window)

            how_to_button.on_button = False
            how_to_button.is_on_button(mouse)
            how_to_button.draw(menu_window)

        if event.type == pygame.MOUSEBUTTONDOWN and start_button.on_button == True:
            one_or_two.main()
            
        if event.type == pygame.MOUSEBUTTONDOWN and lb_button.on_button == True:
            leaderboards_one.main()

        if event.type == pygame.MOUSEBUTTONDOWN and credits_button.on_button == True:
            Credits.main()
            
        if event.type == pygame.MOUSEBUTTONDOWN and how_to_button.on_button == True:
            how_to_play.main()
        
        if event.type == pygame.QUIT:
            quit = True

        if event.type == pygame.MOUSEBUTTONDOWN and exit_button.on_button == True:
            quit = True
        
        pygame.display.update()
    return