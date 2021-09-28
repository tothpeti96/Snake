import pygame
import menu_functions
import main_menu
import leaderboards_two

def main():
    pygame.init()

    ranklist = []

    with open("ranglista_one_player.txt", "rt", encoding="utf-8") as f:
        for sor in f:
            hely_nev_pont = sor.split()
            if len(hely_nev_pont) == 3:
                ranklist.append(((hely_nev_pont[0]),(hely_nev_pont[1]),int((hely_nev_pont[2].rstrip("\n")))))
            else:
                break

    font = pygame.font.Font(None, 60)
    font_table = pygame.font.Font(None, 45)
    leaderboards_text = font.render("Leaderboards", True, pygame.Color('white'))
    text_pos = leaderboards_text.get_rect(center = (300,55))
    window = menu_functions.Window()
    mouse = menu_functions.Mouse(pygame.mouse.get_pos())
    frame = pygame.Rect(50, 100, 500, 450)
    button_up = menu_functions.Button(window, mouse, width = 45, heigth = 45, pos = (595, 122.5), text = "UP", fontsize = 20)
    button_down = menu_functions.Button(window, mouse, width = 45, heigth = 45, pos = (595, 527.5), text = "DOWN", fontsize = 20)
    button_one_player = menu_functions.Button(window, mouse, width = 100, heigth = 50, pos = (100, 600), text = "Egy játékos", fontsize = 25, color_click = (153,153,0), color_unclicked = (153,153,0))
    button_two_player = menu_functions.Button(window, mouse, width = 100, heigth = 50, pos = (300, 600), text = "Két játékos", fontsize = 25)
    button_back = menu_functions.Button(window, mouse, width = 100, heigth = 50, pos = (500, 600), text = "Vissza", fontsize = 25)
    
    min = 0
    if len(ranklist) < 10:
        max = len(ranklist)
    else:
        max = 10

    listahossz = max - min

    quit = False
    pygame.time.set_timer(pygame.USEREVENT, 10)

    while not quit:

        event = pygame.event.wait()
        mouse.pos = pygame.mouse.get_pos()
        last_min = min
        last_max = max

        if event.type == pygame.MOUSEBUTTONDOWN and button_two_player.on_button:
            stay_here = leaderboards_two.main()
            if stay_here:
                pass
            else:
                return

        if event.type == pygame.MOUSEBUTTONDOWN and button_back.on_button:
            return

        if event.type == pygame.MOUSEBUTTONDOWN and button_up.on_button:
            min -= 1
            max = min + listahossz
            
        if event.type == pygame.MOUSEBUTTONDOWN and button_down.on_button:
            min += 1
            max = min + listahossz

        if min < 0 or max > len(ranklist):
            min = last_min
            max = last_max
            
        if event.type == pygame.USEREVENT:

            window.window.fill((0,0,0))
            window.window.blit(leaderboards_text, text_pos)
            pygame.draw.rect(window.window, pygame.Color('white'), frame, 2)

            button_up.on_button = False
            button_up.is_on_button(mouse)
            button_up.draw(window)

            button_down.on_button = False
            button_down.is_on_button(mouse)
            button_down.draw(window)

            button_one_player.on_button = False
            button_one_player.is_on_button(mouse)
            button_one_player.draw(window)

            button_two_player.on_button = False
            button_two_player.is_on_button(mouse)
            button_two_player.draw(window)

            button_back.on_button = False
            button_back.is_on_button(mouse)
            button_back.draw(window)

            listahely = 0
            for i in range(min, max):
                try:
                    rank_i = font_table.render(ranklist[i][0], True, pygame.Color('white'))
                    rank_i_pos = rank_i.get_rect(center = (72.5, 122.5 + (listahely) * 45))
                    window.window.blit(rank_i, rank_i_pos)

                    name_i = font_table.render(ranklist[i][1], True, pygame.Color('white'))
                    name_i_pos = name_i.get_rect(center = (300, 122.5 + (listahely) *45))
                    window.window.blit(name_i, name_i_pos)

                    point_i = font_table.render(str(ranklist[i][2]), True, pygame.Color('white'))
                    point_i_pos = point_i.get_rect(center = (527.5, 122.5 + (listahely) *45))
                    window.window.blit(point_i, point_i_pos)

                    listahely += 1
                except IndexError:
                    min = last_min
                    max = last_max

            

        if event.type == pygame.QUIT:
            quit = True

        pygame.display.update()
    return

