"""

 Törzsfájl. Ez a fájl tartalmazza azokat az osztályokat, amelyből a játék egy-, illetve kétjátékos üzemmódban felépül. 
 A játék három fő osztályból épül fel, ezek a pályatulajdonságokat összefoglaló osztály (Grid), a kígyó testének tulajdonságait 
 összefoglaló osztály (Snake), illetve a kígyónak étkül szolgáló alma tulajdonságait magában foglaló osztály (Apple).
 Ezeken felül található még egy kiegészítő osztály is, ami a három fő osztály által használt RGB színkódokat tartalmazza.

"""

import pygame
import pygame.font

class Color:

    """

    Színkódokat tartalmazó mellékosztály.

    """
    def __init__(self):
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.background = (0, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)

class Grid(Color):

    """

    A pálya tulajdonságait tartalmazó egyik főosztály.
    A Color() osztály egy példányát is használja. 

    """

    def __init__(self):

        """

        A Grid(Color) osztály konstruktor függvénye. Tartalmazza a cellák számát és méretét (amiből a játékablak fog felépülni), illetve fejléc és a betűtípus adatait.
        Ennek az osztálynak szintén attribútuma az első és második játékos pontszáma, ami a megadott betűtípusban fog kiíródni a fejlécre. 

        """
        self.cella_szam = 25
        self.cella_meret = 25
        self.betutip = pygame.font.Font(None, self.cella_meret)
        self.window_size = self.cella_szam * self.cella_meret 
        self.window = pygame.display.set_mode((self.cella_szam*self.cella_meret, (self.cella_szam + 2)*self.cella_meret))
        self.caption = pygame.display.set_caption('Snake')
        self.fejlec = pygame.Surface((self.cella_meret * self.cella_szam, 2 * self.cella_meret))
        self.fejlec_pos = self.fejlec.get_rect(topleft = ((0, 0)))
        self.pont_p1 = 0
        self.pont_p2 = 0
        
    def draw_grid_p1(self, color):
        """

        Egy játékos esetén a függvény meghívásával a program kirajzolja a pályát és a fejlécet az éppen aktuális pontszámmal.
        
        """
        self.fejlec.fill((0, 0, 255))
        self.window.blit(self.fejlec, self.fejlec_pos)
        pontszam = self.betutip.render(str(self.pont_p1), True, color.white)
        self.window.blit(pontszam, pontszam.get_rect(center = (self.cella_szam/2.5 * self.cella_meret, self.cella_meret)))

    def draw_grid_p2(self, color):
        """

        Két játékos esetén a függvény meghívásával a program kirajzolja a pályát és a fejlécet az éppen aktuális pontszámokkal. 

        """

        self.fejlec.fill((0, 0, 255))
        self.window.blit(self.fejlec, self.fejlec_pos)
        pontszam1 = self.betutip.render(str(self.pont_p1), True, color.white)
        self.window.blit(pontszam1, pontszam1.get_rect(center = (self.cella_szam/5 * self.cella_meret, self.cella_meret)))
        pontszam2 = self.betutip.render(str(self.pont_p2), True, color.white)
        self.window.blit(pontszam2, pontszam1.get_rect(center = (self.cella_szam/2.5*2 * self.cella_meret, self.cella_meret)))


class Snake(Grid, Color):

    """

    A játékos kígyójának attribútumait tartalmazó osztály. A Grid() és a Color() osztályok egy-egy példányát használja.

    """

    def __init__(self, grid, color):
        """

        A Snake(Grid, Color) osztály konstruktor függvénye. Listaként tartalmazza a kígyó testelemeinek koordinátáit (cella_x, cella_y) formában, a kígyó színét (alapértelmezett szín a zöld),
        a kígyó fejének a pozícióját és a kígyó éppen aktuális haladási irányát. Szintén attribútomként tartalmazza a kígyó testének elemét. Emellett attribútuma hogy a kígyó éppen növekszik-e (bool, akkor válik igazzá ha a fej és az étek pozíciója megegyezik),
        illetve, hogy a kígyó még él és mozog, vagy falnak, testnek, két játékos esetén másik kígyótesttel történő ütközés következtében meghalt-e. 

        """

        self.pos = [(9, 10), (8, 10), (7, 10), (6, 10)]
        self.body_unit = pygame.Surface((grid.cella_meret, grid.cella_meret))
        self.color = color.green
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.grow = False
        self.death = False
        self.head = self.pos[0]

    def event_handler(self, event, snake):

        """
        A billentyűzet lenyomása során keletkező esemény kezeléséről gondoskodó függvény. 
        A megfelelő billentyűzetek lenyomásakor frissíti a kígyó haladási irányát a lenyomott
        gombnak megfelelően.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.head[0]+1 != snake.pos[1][0]:
                snake.right = True
                snake.left = False
                snake.up = False
                snake.down = False
            elif event.key == pygame.K_LEFT and snake.head[0]-1 != snake.pos[1][0]:
                snake.right = False
                snake.left = True
                snake.up = False
                snake.down = False
            elif event.key == pygame.K_UP and snake.head[1]-1 != snake.pos[1][1]:
                snake.right = False
                snake.left = False
                snake.up = True
                snake.down = False
            elif event.key == pygame.K_DOWN and snake.head[1]+1 != snake.pos[1][1]:
                snake.right = False
                snake.left = False
                snake.up = False
                snake.down = True

    def event_handler_snake2(self, event, snake2):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and snake2.head[0]+1 != snake2.pos[1][0]:
                snake2.right = True
                snake2.left = False
                snake2.up = False
                snake2.down = False
            elif event.key == pygame.K_a and snake2.head[0]-1 != snake2.pos[1][0]:
                snake2.right = False
                snake2.left = True
                snake2.up = False
                snake2.down = False
            elif event.key == pygame.K_w and snake2.head[1]-1 != snake2.pos[1][1]:
                snake2.right = False
                snake2.left = False
                snake2.up = True
                snake2.down = False
            elif event.key == pygame.K_s and snake2.head[1]+1 != snake2.pos[1][1]:
                snake2.right = False
                snake2.left = False
                snake2.up = False
                snake2.down = True

    def clear_snake(self, grid, color):
        """

        A függvény meghívásának hatására törli a kígyó előző pozícióját képernyőről.

        """

        for i in range(len(self.pos)):
            self.body_unit.fill(color.background)
            x_current = (self.pos[i][0] - 0.5) * grid.cella_meret
            y_current = (self.pos[i][1] - 0.5) * grid.cella_meret
            unit_pos = self.body_unit.get_rect(center = ((x_current, y_current)))
            grid.window.blit(self.body_unit, unit_pos)

    def is_dead(self, grid):

        """
        Leellenőrzi, hogy a kígyó feje a pályán belül található, illetve, hogy a kígyó fejének a pozíciója nem egyezik meg a kígyó bármely saját testelemének a pozíciójával. 

        """

        self.head = self.pos[0]
        if self.head[0] < 1 or self.head[0] > grid.cella_szam or self.head[1] <= 2 or self.head[1] > grid.cella_szam + 2:
            self.death = True
        for i in range(1,len(self.pos)):
            if self.head == self.pos[i]:
                self.death = True

    def rearrange(self):

        """
        Újrarendezi a kígyó testelemeinek a pozícióját. A haladási iránynak megfelelően eggyel nagyobb (x vagy y koordinátákon való pozítív haladási irány esetében) 
        vagy eggyel kisebb (x vagy y koordinátákon való pozítív haladási irány esetében) pozíciót vesz fel a kígyó feje, amit a pozíció lista elejére beszúr a program a függvény meghívásakor.
        Abban az esetben ha a kígyó nem találkozik étekkel, a lista utolsó elemét törli a program (így érhető el az a látszat, hogy a kígyó vonszolja maga után a testét), ellenkező esetben egy
        újrarrendezés idejéig nem törli a pozíciólista utolsó elemét, ekkor egy elemmel nő a kígyó testének hossza.

        """

        if self.right == True:
            self.pos.insert(0, (self.pos[0][0] + 1, self.pos[0][1]))
            if self.grow == False:
                self.pos.pop(len(self.pos)-1)

        if self.left == True:
            self.pos.insert(0, (self.pos[0][0] - 1, self.pos[0][1]))
            if self.grow == False:
                self.pos.pop(len(self.pos)-1)

        if self.down == True:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1] + 1)) 
            if self.grow == False:
                self.pos.pop(len(self.pos)-1)

        if self.up == True:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1] - 1))
            if self.grow == False:
                self.pos.pop(len(self.pos)-1)
        
    def move(self, grid):

        """
        Az újrarendezett pozíciólista elemeinek megfelelően kirajzolja a kígyó testének elemeit a játékablakra.

        """
               
        for i in range(0, len(self.pos)):
            self.body_unit.fill(self.color)
            cella = self.pos[i][0]
            x_current = (self.pos[i][0] - 0.5) * grid.cella_meret
            y_current = (self.pos[i][1] - 0.5) * grid.cella_meret
            unit_pos = self.body_unit.get_rect(center = ((x_current, y_current)))
            grid.window.blit(self.body_unit, unit_pos)
     
class Apple(Grid, Color):
    """

    A játékmezőn megjelenő étek (alma) attribútumait tartalmazó osztály. A Grid() és a Color() osztályok egy-egy példányát használja. 

    """

    def __init__(self, grid, color):

        """
        Az Apple(Grid, Color) osztály konstruktor függvénye. Tartalmazza az alma aktuális pozícióját, illetve az alma 
        grafikus megjelenítésének elemét. Az alma alapértelemzett színe piros.

        """
        self.pos = (15, 10)
        self.apple = pygame.Surface((grid.cella_meret, grid.cella_meret))
        self.color = color.red

    def draw_food(self, grid):

        """
        A függvény hívásának hatására megjelenik a játékmezőn az alma az éppen aktuális pozícióban. 
        """

        self.apple.fill(self.color)
        apple_pos = self.apple.get_rect(center = (((self.pos[0] - 0.5) * grid.cella_meret, (self.pos[1] - 0.5) * grid.cella_meret)))
        grid.window.blit(self.apple, apple_pos)