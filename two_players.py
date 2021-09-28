"""

Az alábbi fájl a kígyó játék logikai felépítését tartalmazza két játékos esetén.

"""

import Snake_functions as game
import pygame
import random
import two_player_end_scene

def main(Name1, Name2):

    colors = game.Color() # Létrehozza a Color() osztály egy példányát.

    pygame.init() # Inicizializálja a pygame könyvtárat. Használatban marad egészen a pygame.quit() parancsig.
    grid = game.Grid() # Létrehozza a Grid() osztály egy példányát.
    grid.draw_grid_p2

    snake1 = game.Snake(grid, colors) # Létrehozza a Snake() osztály első példányát. 
    snake1.color = colors.green  # Beállítja az első játékos kígyójának a színét.

    snake2 = game.Snake(grid, colors) # Létrehozza a Snake() osztály második példányát.
    snake2.color = colors.yellow # Beállítja a második játékos kígyójának a színét.

    snake2.pos = [(9, 16), (8, 16), (7, 16), (6, 16)]   # Megváltoztatja a második játékos kígyójának pozícióját. 
                                                        #(Kígyók között ne legyen átfedés már a játék kezdete elején.)

    apple = game.Apple(grid, colors) # Létrehozza a Apple() osztály egy példányát.
    apple.pos = (15, 13) # Megváltoztatja az étek pozíciójának alapbeállítását, 
                         #hogy a két kígyó kiindulási pozíciójától egyenlő távolságban legyen.

    apple.draw_food(grid)
    pygame.time.set_timer(pygame.USEREVENT, 75) # A játék beépített órája. pygame.time.set_timer(pygame.USEREVENT, KÉPERNYŐFRISSÍTÉS MS-ban) 
                                                #FRAMERATE = 1000/KÉPRNYŐFRISSÍTÉS MS-ban

    name_1_surface = grid.betutip.render(Name1, True, pygame.Color('white'))
    name_1_pos = name_1_surface.get_rect(midleft = ((0), (grid.cella_meret)))

    name_2_surface = grid.betutip.render(Name2, True, pygame.Color('white'))
    name_2_pos = name_2_surface.get_rect(midleft = ((grid.cella_szam/2)*grid.cella_meret, (grid.cella_meret)))

    """

    Játék logikája:
    Ameddig a "quit" változó értéke nem változik igazra, addig a játékciklus fut.

    1. Első és második kígyó törlése
    2. Első és második kígyó pozíciójának frissítése
        - Ha a bármelyik kígyó 'grow' változója az előző cilusból igaz maradt, akkor annak a kígyónak a hossza eggyel nő.
        - Amennyiben valamelyik nyíl billenytűzet lenyomásra került, akkor a billentyűzetnek megfelelő kígyó fej pozícióját annak megfelelően mozdítja el a program a cellákon. 
    3. A megfelelő kígyó mozgatása egy pozícióval (abban az esetben ha valamelyik billentyűzet már lenyomásra került, illetve a kígyó még nem halt meg.)
    4. A kígyók 'grow' értékét Hamis-ra állítja.
    5. Pálya kirajzolása, az aktuális pontszámokkal.
    6. Program leellenőrzni, hogy a kígyók nem ütközötek-e fallal, saját magával vagy esetleg a másik kígyó testével. Ha  mind a két kígyó meghalt akkor a program kilép a ciklusból. 
       Ha csak az egyik kígyó halt meg (pl. falnak ütközik vagy a kígyó testének), akkor annak pozíciója nem változik tovább (megfagy a pályán), azonban a még életben maradó kígyó bele tud ütközni.
       A még életben maradó kígyó addig játszat, ameddig az falnak vagy a másik kígyó testébe bele nem ütközik.
       Ha mind a kettő kígyó él, akkor a fej-fej ütközések esetén mind a két játékos kígyója meghal. 
    7. A program leellenőrzi, hogy a valamelyik fej pozíciója megegyezik-e az alma pozíciójával, ha igen akkor belép az alábbi ciklusba:
        a. Hozzáad az almával ütköző játékos pontszámához egyet.
        b. Véletéenszám generátor segítségével meghatározza az alma cella_x és cella_y pozíciójának új értékét. Abban az esetben ha ez az érték egybe esik a  valamelyik kígyó aktuális helyével,
            új pozíció generálódik, egészen addig amíg egy olyan pozícició generálódik, ami nem esik egybe valamelyik kígyó pozíciójával. 
        c. A program a megfelelő kígyó 'grow' értéket Igazra állítja át.
        d. Kirajzolja a pályát az új almapozícióval. 
    8. Abban az esetben ha valamelyik játékos megnyomná az ablak jobb felső sarkában található 'X' (kilépés) gombot, a játék bezáródik. 
    9. A program frissíti a képernyőt, hogy a ciklusban lejátszódó változások a felhasználók számára is megjelenjenek. 

    """

    quit = False
    while not quit:

        event = pygame.event.wait()
        snake1.event_handler(event, snake1)
        snake2.event_handler_snake2(event, snake2)
        
        if event.type == pygame.USEREVENT:
            snake1.clear_snake(grid, colors)
            snake2.clear_snake(grid, colors)
            if not snake1.death:
                snake1.rearrange()
            if not snake2.death:
                snake2.rearrange()
            snake1.move(grid)
            snake2.move(grid)
            snake1.grow = False
            snake2.grow = False
            grid.draw_grid_p2(colors)
            snake1.is_dead(grid)
            snake2.is_dead(grid)

            grid.window.blit(name_1_surface, name_1_pos)
            grid.window.blit(name_2_surface, name_2_pos)

            if snake1.head == snake2.head:
                quit = True

            #Második kígyó ütközik az első testével?
            if not snake1.death:
                for i in range(1, len(snake1.pos)):
                    if snake2.head == snake1.pos[i]:
                        snake2.death = True
            elif snake1.death:
                for i in range(len(snake1.pos)):
                    if snake2.head == snake1.pos[i]:
                        snake2.death = True

            #Első kígyó feje ütközik a második testével?
            if not snake2.death:
                for i in range(1, len(snake2.pos)):
                    if snake1.head == snake2.pos[i]:
                        snake1.death = True
            elif snake2.death:
                for i in range(len(snake2.pos)):
                    if snake1.head == snake2.pos[i]:
                        snake1.death = True

            if snake1.death == True and snake2.death == True:
                quit = True


            if snake1.head == apple.pos:
                grid.pont_p1 += 1

                not_snake = False
                while not_snake != True:
                    not_snake = True
                    x_rand = random.randint(1, grid.cella_szam)
                    y_rand = random.randint(3, grid.cella_szam + 2)
                    apple.pos = (x_rand, y_rand)

                    for i in range(len(snake1.pos)):
                        if apple.pos == snake1.pos[i]:
                            not_snake = False
                            break
                    for i in range(len(snake2.pos)):
                        if apple.pos == snake2.pos[i]:
                            not_snake = False
                            break

                    snake1.grow = True
                    apple.draw_food(grid)

            if snake2.head == apple.pos:
                grid.pont_p2 += 1

                not_snake = False
                while not_snake != True:
                    not_snake = True
                    x_rand = random.randint(1, grid.cella_szam)
                    y_rand = random.randint(3, grid.cella_szam + 2)
                    apple.pos = (x_rand, y_rand)

                    for i in range(len(snake1.pos)):
                        if apple.pos == snake1.pos[i]:
                            not_snake = False
                            break
                    for i in range(len(snake2.pos)):
                        if apple.pos == snake2.pos[i]:
                            not_snake = False
                            break

                    snake2.grow = True
                    apple.draw_food(grid)

        if event.type == pygame.QUIT:
            quit = True

        pygame.display.update()
    return two_player_end_scene.main(Name1, Name2, grid.pont_p1, grid.pont_p2)
