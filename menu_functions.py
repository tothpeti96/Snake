import pygame
import pygame.font

"""
A menü felépítéséhez használt különböző atrribútumokat és funkciókat tartalmazó osztályok. 
"""

class Mouse:
    """
    Az egér pozícióját tartalmazó segédosztály melynek példányát egyéb osztályok fogják majd használni. 
    """
    def __init__(self, pos):
        self.pos = pos

class Window:
    """
    Az éppen aktuális menüablak attribútumait tartalmazó osztály. Tartalmazza az ablak méretét, színét és címét.
    """
    def __init__(self):
        self.window = pygame.display.set_mode((625, 675))
        self.caption = pygame.display.set_caption('Snake')
        self.color = (0,0,0)

class Button(Window, Mouse):

    """
    Az éppen aktuális menüablakon található gombok attribútumait tartalmazó osztály. Használja a Window() és a Mouse() osztályok egy-egy példányát is. 
    """

    def __init__(self, window, mouse, width = 100, heigth = 50, pos = (312.5, 337.5), color_unclicked = (255, 0, 0), color_click = (0, 255, 0), text = "Start", fontsize = 40):

        """
        A Button() osztály konstruktor függvénye.  Attribútuma a gomb szélessége és hossza, a gomb felülete amin majd a gomb megjelenik a képernyőn, a pozíciója,
        a gomb színét amikor nincs rajta illetve mikor rajta van a kurzor. A gomb feliratának betűtipusát, annak szövegét és a szöveg pozícióját (ami megegyezik a gomb felületének pozíciójával.)
        Bool változoként tárolja, hogy a kurzor éppen a gomb felett van-e. 
        """

        self.width = width
        self.heigth = heigth
        self.button = pygame.Surface((self.width, self.heigth))
        self.pos = self.button.get_rect(center = pos)
        self.color_unclicked = color_unclicked
        self.color_click = color_click
        self.on_button = False
        self.fontsize = fontsize
        self.betutip = pygame.font.Font(None, self.fontsize)
        self.text = self.betutip.render(text, True, (255,255,255))
        self.text_pos = self.text.get_rect(center = pos)

    def is_on_button(self, mouse):

        """
        A függvény megvizsgálja, hogy a kurzor a gomb felett van-e. 
        Ha a téglalap objektum határain belül van a kurzor, akkor a self.on_button értéket igazra változtatja.
        A függvény az egér pozíciójának megtalálása miatt használja a Mouse() osztály egy példányát. 

        """
        if mouse.pos[0] < self.pos.center[0] + self.width/2:
            if mouse.pos[0] > self.pos.center[0] - self.width/2:
                if mouse.pos[1] < self.pos.center[1] + self.heigth/2:
                    if mouse.pos[1] > self.pos.center[1] - self.heigth/2:
                        self.on_button = True

    def draw(self, window):
        """
        Kirajzolja a gombot a éppen aktuális menüablak felületére a megadott pozíciónak megfelelően.
        Amennyiben a kurzor rajta van a gombon, akkor a gomb színe zöldre változik, ellenkekező esetben a gomb színe piros.
        """
        if self.on_button:
            self.button.fill(self.color_click)
            window.window.blit(self.button, self.pos)
        else:
            self.button.fill(self.color_unclicked)
            window.window.blit(self.button, self.pos)
        window.window.blit(self.text, self.text_pos)

class Textbox(Window):
    """
    Az éppen aktuális menüablakon található szövegdoboz adatait tartalmazó osztály. Használja a Window() osztály egyik példányát is. 

    """

    def __init__(self, window, width, heigth, pos, text, max = 15, min = 3):
        """
        A Textbox(Window) osztály konstruktor függvénye. Tartalmazza a szövegdobozba írható karakterek minimális és maximális hosszát, a karakterszám túllépése során keletkező hibaüzenetek betűtípusát,
        szövegét, a szövegdoboz magasságát és szélességét, illetve szövegdobozként szolgáló téglalap típusú objektum pozícióját. Emellett tartalmazza a szövegdoboz szövegének betűtípusát és magát a kiirandó szöveget.
        Bool változóként tárolja azt, hogy a szövegdobozba éppen belekattintott a felhasználó vagy sem. Egy bool változóban tárolja, hogy a szöveg tartalmaz-e space karaktert, illetve az ehhez tartozó hibaüzenet szövegét.
        Tartalmazza a szöveg létrehozásakkor létrejövő felület pozícióját, ami megegyezik a szövegdoboz keretének pozíciójával.
        
        """
        self.max = max
        self.min = min
        self.width = width
        self.heigth = heigth
        self.pos = pos
        self.font = pygame.font.Font(None, self.heigth)
        self.text = text
        self.textbox_surface = self.font.render(self.text, True, pygame.Color('white'))
        self.rect = pygame.Rect(pos[0] - self.width/2, pos[1] - self.heigth/2, self.width, self.heigth)
        self.clicked = False
        self.error = "{} karakter maximum!".format(max)
        self.error_surface = self.font.render(self.error, True, pygame.Color('red'))
        self.error_min = "{} karakter minimum".format(min)
        self.error_min_surface = self.font.render(self.error_min, True, pygame.Color('red'))
        self.space = False
        self.error_space_surface = self.font.render("Space nem lehet!", True, pygame.Color('red'))


    def event_handler(self, event):
        """

        Egérgomb vagy billentyűzet lenyomása esetén, esetleg felhaszálói esemény kezeléséről gonodoskodó függvény. 
        Abban az esetben ha az egérgomb lenyomásakor az egér pozíciója megegyezik a szövegdoboz téglatest objektumaként szolgáló pozícióval, 
        akkor a gombhoz tartozó self.clicked értéket negálja.

        Abban az esetben ha a lenyomott billentyűzet a backspace volt, akkor törli a szövegdobozban lévő utolsó karaktert.
        Bármilyen más billentyűzet lenyomása esetén az annak megfelelő unicode karaktert fűzi hozzá a szövegdoboz objektum szövegéhez

        Felhasználói esemény hatására leellenőrzi, hogy a szövegdoboz tartalmaz-e szóköz karaktert.
        
        """
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked

        if event.type == pygame.KEYDOWN:
            if self.clicked:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                if self.textbox_surface.get_width() > 150:
                    self.rect.w = self.textbox_surface.get_width() + self.heigth
        
        if event.type == pygame.USEREVENT:
            self.space = False
            for i in range(len(self.text)):
                if self.text[i] == " ":
                    self.space = True
                    break

    def draw(self, window):
        """
        Kirajzolja a szövegdobozt alá pedig az esetlegesen hozzá tartozó hibaüzeneteket. 3 karakternél kisebb vagy 15 karakternél nagyobb, 
        esetleg szóközt tartalmazó karakter esetén figyelmezteti a felhasználót, hogy javítson. Hibás bemenet esetén a szövegdoboz színe piros. 
        Abban az esetben ha a szövegdobozra a felhasználó rákattintott és az érték helyes a szövegdoboz kék. Ha a szövegdobozban szereplő string értéke helyes
        és a felhasználó nem kattintott bele a szövegdobozba, akkor annak színe fehér.

        """
        
        if len(self.text) > self.max:
            self.textbox_surface = self.font.render(self.text, False, pygame.Color('white'))
            window.window.blit(self.textbox_surface, self.textbox_surface.get_rect(midleft = ((self.pos[0]-self.width/2),(self.pos[1]))))
            pygame.draw.rect(window.window, pygame.Color('red'), self.rect, 2)
            window.window.blit(self.error_surface, ((self.rect.x), self.rect.y + self.rect.h))
        elif len(self.text) < self.min:
            self.textbox_surface = self.font.render(self.text, False, pygame.Color('white'))
            window.window.blit(self.textbox_surface, self.textbox_surface.get_rect(midleft = ((self.pos[0]-self.width/2),(self.pos[1]))))
            pygame.draw.rect(window.window, pygame.Color('red'), self.rect, 2)
            window.window.blit(self.error_min_surface, ((self.rect.x), self.rect.y + self.rect.h))            
        elif self.space == True:
            self.textbox_surface = self.font.render(self.text, False, pygame.Color('white'))
            window.window.blit(self.textbox_surface, self.textbox_surface.get_rect(midleft = ((self.pos[0]-self.width/2),(self.pos[1]))))
            pygame.draw.rect(window.window, pygame.Color('red'), self.rect, 2)
            window.window.blit(self.error_space_surface, ((self.rect.x), self.rect.y + self.rect.h))
        elif self.clicked == True:
            self.textbox_surface = self.font.render(self.text, False, pygame.Color('white'))
            window.window.blit(self.textbox_surface, self.textbox_surface.get_rect(midleft = ((self.pos[0]-self.width/2),(self.pos[1]))))
            pygame.draw.rect(window.window, pygame.Color('blue'), self.rect, 2)
        else:
            self.textbox_surface = self.font.render(self.text, False, pygame.Color('white'))
            window.window.blit(self.textbox_surface, self.textbox_surface.get_rect(midleft = ((self.pos[0]-self.width/2),(self.pos[1]))))
            pygame.draw.rect(window.window, pygame.Color('white'), self.rect, 2)