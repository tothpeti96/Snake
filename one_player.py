"""

Az alábbi fájl a kígyó játék logikai felépítését tartalmazza egy játékos esetén.

"""

import Snake_functions as game
import random
import pygame
import main_menu
import one_or_two
import game_over_p1
import menu_functions

def main(PlayerName):
   
    colors = game.Color() # Létrehozza a Color() osztály egy példányát.

    pygame.init() # Inicizializálja a pygame könyvtárat. Használatban marad egészen a pygame.quit() parancsig.
    grid = game.Grid() # Létrehozza a Grid() osztály egy példányát.
    grid.draw_grid_p1 

    snake = game.Snake(grid, colors) # Létrehozza a Snake() osztály egy példányát. 
    apple = game.Apple(grid, colors) # Létrehozza a Apple() osztály egy példányát.
    apple.draw_food(grid)
    pygame.time.set_timer(pygame.USEREVENT, 75) # A játék beépített órája. pygame.time.set_timer(pygame.USEREVENT, KÉPERNYŐFRISSÍTÉS MS-ban) 
                                                #FRAMERATE = 1000/KÉPRNYŐFRISSÍTÉS MS-ban

    name_surface = grid.betutip.render(PlayerName, True, pygame.Color('white'))
    name_pos = name_surface.get_rect(midleft = ((0), (grid.cella_meret)))

    """

    Játék logikája:
    Ameddig a "quit" változó értéke nem változik igazra, addig a játékciklus fut.

    1. Előző kígyó törlése
    2. Kígyó pozíciójának frissítése
        - Ha a kígyó 'grow' változója az előző cilusból igaz maradt, akkor a kígyó hossza eggyel nő.
        - Amennyiben valamelyik nyíl billenytűzet lenyomásra került, akkor a fej pozícióját annak megfelelően mozdítja el a program a cellákon. 
    3. Kígyó mozgatása egy pozícióval (abban az esetben ha valamelyik billentyűzet már lenyomsára került, illetve a kígyó még nem halt meg.)
    4. A kígyó 'grow' értékét Hamis-ra állítja.
    5. Pálya kirajzolása, az aktuális pontszámmal.
    6. Program leellenőrzni, hogy a kígyó nem ütközött-e fallal vagy esetleg saját magával. Ha nem akkor a cilus tovább fut, ellenkező esetben a a program futása kilép a ciklusból. 
    7. A program leellenőrzi, hogy a fej pozíciója megegyezik-e az alma pozíciójával, ha igen akkor belép az alábbi ciklusba:
        a. Hozzáad a játékos pontszámához egyet.
        b. Véletéenszám generátor segítségével meghatározza az alma cella_x és cella_y pozíciójának új értékét. Abban az esetben ha ez az érték egybe esik a kígyó aktuális helyével,
            új pozíció generálódik, egészen addig amíg egy olyan pozícició generálódik, ami nem esik egybe a kígyó pozíciójával. 
        c. A program a 'grow' értéket Igazra állítja át.
        d. Kirajzolja a pályát az új almapozícióval. 
    8. Abban az esetben ha a játékos megnyomná az ablak jobb felső sarkában található 'X' (kilépés) gombot, a játék bezáródik. 
    9. A program frissíti a képernyőt, hogy a ciklusban lejátszódó változások a felhasználó számára is megjelenjenek. 

    """

    quit = False
    while not quit:
        
        event = pygame.event.wait()
        snake.event_handler(event, snake)

        if event.type == pygame.USEREVENT:
            
            snake.clear_snake(grid, colors)
            snake.rearrange()
            snake.move(grid)
            snake.grow = False
            grid.draw_grid_p1(colors)
            grid.window.blit(name_surface, name_pos)
            snake.is_dead(grid)

            if snake.death == True:
                quit = True

            if snake.head == apple.pos:
                grid.pont_p1 += 1

                not_snake = False
                while not_snake != True:
                    not_snake = True
                    x_rand = random.randint(1, grid.cella_szam)
                    y_rand = random.randint(3, grid.cella_szam + 2)
                    apple.pos = (x_rand, y_rand)

                    for i in range(len(snake.pos)):
                        if apple.pos == snake.pos[i]:
                            not_snake = False
                            break
  
                snake.grow = True
                apple.draw_food(grid)
                
        if event.type == pygame.QUIT:
            quit = True

        pygame.display.update()
    return game_over_p1.main(grid.pont_p1, PlayerName)