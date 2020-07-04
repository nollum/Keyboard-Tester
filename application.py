import pygame
import sys

KEY_SIZE = 35
HOR_START = 32 
VERT_START = 95
OUTLINE_SIZE = 2
INTERVAL = 38 
SECTION_PADDING = 18 
CTRL_EXTRA = TAB_BACKSLASH_EXTRA = KEY_SIZE * 0.5
CAPSLOCK_RETURN_EXTRA = KEY_SIZE * 0.75
BACKSPACE_EXTRA = SHIFT_EXTRA = KEY_SIZE 

font = pygame.font.Font('freesansbold.ttf', 25)
text = font.render('reset', True, (0,0,0))
text_size = [font.size('reset')[0], font.size('reset')[1]]

class Application:
    def __init__(self):
        self.last_key = None
        self.curr_key = None
        self.key_rects = { pygame.K_BACKSPACE : [[HOR_START+INTERVAL*13, VERT_START+INTERVAL, KEY_SIZE*2, KEY_SIZE], False],  
                           pygame.K_TAB : [[HOR_START, VERT_START+INTERVAL*2, KEY_SIZE*1.5, KEY_SIZE], False], 
                          # pygame.K_CLEAR : False,
                           pygame.K_RETURN : [[HOR_START+INTERVAL*12+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE*2.335, KEY_SIZE], False],
                           pygame.K_PAUSE : [[HOR_START + INTERVAL*16+SECTION_PADDING*3,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_ESCAPE : [[HOR_START,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_SPACE : [[HOR_START+INTERVAL*3+CTRL_EXTRA*2, VERT_START+INTERVAL*5, KEY_SIZE*7.6, KEY_SIZE], False],
                          # pygame.K_EXCLAIM : False,
                          # pygame.K_QUOTEDBL : False,
                          # pygame.K_HASH : False,
                          # pygame.K_DOLLAR : False,
                          # pygame.K_AMPERSAND : False,
                           pygame.K_QUOTE : [[HOR_START+INTERVAL*11+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                          # pygame.K_LEFTPAREN : False,
                          # pygame.K_RIGHTPAREN : False,
                          # pygame.K_ASTERISK : False,
                           pygame.K_COMMA : [[HOR_START+INTERVAL*8+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_MINUS : [[HOR_START+INTERVAL*11, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_PERIOD : [[HOR_START+INTERVAL*9+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_SLASH : [[HOR_START+INTERVAL*10+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_0 : [[HOR_START+INTERVAL*10, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_1 : [[HOR_START+INTERVAL, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_2 : [[HOR_START+INTERVAL*2, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_3 : [[HOR_START+INTERVAL*3, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_4 : [[HOR_START+INTERVAL*4, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_5 : [[HOR_START+INTERVAL*5, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_6 : [[HOR_START+INTERVAL*6, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_7 : [[HOR_START+INTERVAL*7, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_8 : [[HOR_START+INTERVAL*8, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_9 : [[HOR_START+INTERVAL*9, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                          # pygame.K_COLON : False,
                           pygame.K_SEMICOLON : [[HOR_START+INTERVAL*10+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                          # pygame.K_LESS : False,
                           pygame.K_EQUALS : [[HOR_START+INTERVAL*12, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                          # pygame.K_GREATER : False,
                          # pygame.K_QUESTION : False,
                          # pygame.K_AT : False,
                           pygame.K_LEFTBRACKET : [[HOR_START+INTERVAL*11+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_BACKSLASH : [[HOR_START+INTERVAL*13+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE*1.5, KEY_SIZE], False],
                           pygame.K_RIGHTBRACKET : [[HOR_START+INTERVAL*12+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False],
                          # pygame.K_CARET : False,
                          # pygame.K_UNDERSCORE : False,
                           pygame.K_BACKQUOTE : [[HOR_START, VERT_START+INTERVAL, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_a : [[HOR_START+INTERVAL+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_b : [[HOR_START+INTERVAL*5+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_c : [[HOR_START+INTERVAL*3+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_d : [[HOR_START+INTERVAL*3+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_e : [[HOR_START+INTERVAL*3+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_f : [[HOR_START+INTERVAL*4+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_g : [[HOR_START+INTERVAL*5+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_h : [[HOR_START+INTERVAL*6+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_i : [[HOR_START+INTERVAL*8+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_j : [[HOR_START+INTERVAL*7+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_k : [[HOR_START+INTERVAL*8+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_l : [[HOR_START+INTERVAL*9+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_m : [[HOR_START+INTERVAL*7+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_n : [[HOR_START+INTERVAL*6+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_o : [[HOR_START+INTERVAL*9+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_p : [[HOR_START+INTERVAL*10+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_q : [[HOR_START+INTERVAL+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_r : [[HOR_START+INTERVAL*4+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_s : [[HOR_START+INTERVAL*2+CAPSLOCK_RETURN_EXTRA, VERT_START+INTERVAL*3, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_t : [[HOR_START+INTERVAL*5+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_u : [[HOR_START+INTERVAL*7+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_v : [[HOR_START+INTERVAL*4+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_w : [[HOR_START+INTERVAL*2+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_x : [[HOR_START+INTERVAL*2+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_y : [[HOR_START+INTERVAL*6+TAB_BACKSLASH_EXTRA, VERT_START+INTERVAL*2, KEY_SIZE, KEY_SIZE], False], 
                           pygame.K_z : [[HOR_START+INTERVAL+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_DELETE : [[HOR_START + INTERVAL*14+SECTION_PADDING*3,VERT_START+INTERVAL*2,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP0 : [[HOR_START + INTERVAL*17+SECTION_PADDING*4,VERT_START+INTERVAL*5,KEY_SIZE*2.1,KEY_SIZE], False],
                           pygame.K_KP1 : [[HOR_START + INTERVAL*17+SECTION_PADDING*4,VERT_START+INTERVAL*4,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP2 : [[HOR_START + INTERVAL*18+SECTION_PADDING*4,VERT_START+INTERVAL*4,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP3 : [[HOR_START + INTERVAL*19+SECTION_PADDING*4,VERT_START+INTERVAL*4,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP4 : [[HOR_START + INTERVAL*17+SECTION_PADDING*4,VERT_START+INTERVAL*3,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP5 : [[HOR_START + INTERVAL*18+SECTION_PADDING*4,VERT_START+INTERVAL*3,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP6 : [[HOR_START + INTERVAL*19+SECTION_PADDING*4,VERT_START+INTERVAL*3,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP7 : [[HOR_START + INTERVAL*17+SECTION_PADDING*4,VERT_START+INTERVAL*2,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP8 : [[HOR_START + INTERVAL*18+SECTION_PADDING*4,VERT_START+INTERVAL*2,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP9 : [[HOR_START + INTERVAL*19+SECTION_PADDING*4,VERT_START+INTERVAL*2,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP_PERIOD : [[HOR_START + INTERVAL*19+SECTION_PADDING*4,VERT_START+INTERVAL*5,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP_DIVIDE : [[HOR_START + INTERVAL*18+SECTION_PADDING*4,VERT_START+INTERVAL,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP_MULTIPLY : [[HOR_START + INTERVAL*19+SECTION_PADDING*4,VERT_START+INTERVAL,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP_MINUS :[[HOR_START + INTERVAL*20+SECTION_PADDING*4,VERT_START+INTERVAL,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_KP_PLUS : [[HOR_START + INTERVAL*20+SECTION_PADDING*4,VERT_START+INTERVAL*2,KEY_SIZE,KEY_SIZE*2.1], False],
                           pygame.K_KP_ENTER : [[HOR_START + INTERVAL*20+SECTION_PADDING*4,VERT_START+INTERVAL*4,KEY_SIZE,KEY_SIZE*2.1], False],
                          # pygame.K_KP_EQUALS : False,
                           pygame.K_UP : [[HOR_START + INTERVAL*15+SECTION_PADDING*3,VERT_START+INTERVAL*4,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_DOWN : [[HOR_START + INTERVAL*15+SECTION_PADDING*3,VERT_START+INTERVAL*5,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_RIGHT : [[HOR_START + INTERVAL*16+SECTION_PADDING*3,VERT_START+INTERVAL*5,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_LEFT : [[HOR_START + INTERVAL*14+SECTION_PADDING*3,VERT_START+INTERVAL*5,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_INSERT : [[HOR_START + INTERVAL*14+SECTION_PADDING*3,VERT_START+INTERVAL,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_HOME : [[HOR_START + INTERVAL*15+SECTION_PADDING*3,VERT_START+INTERVAL,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_END : [[HOR_START + INTERVAL*15+SECTION_PADDING*3,VERT_START+INTERVAL*2,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_PAGEUP : [[HOR_START + INTERVAL*16+SECTION_PADDING*3,VERT_START+INTERVAL,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_PAGEDOWN : [[HOR_START + INTERVAL*16+SECTION_PADDING*3,VERT_START+INTERVAL*2,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F1 : [[HOR_START + INTERVAL*2,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F2 : [[HOR_START + INTERVAL*3,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F3 : [[HOR_START + INTERVAL*4,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F4 : [[HOR_START + INTERVAL*5,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F5 : [[HOR_START + INTERVAL*6 + SECTION_PADDING,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F6 : [[HOR_START + INTERVAL*7 + SECTION_PADDING,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F7 : [[HOR_START + INTERVAL*8 + SECTION_PADDING,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F8 : [[HOR_START + INTERVAL*9 + SECTION_PADDING,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F9 : [[HOR_START + INTERVAL*10 + SECTION_PADDING*2,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F10 : [[HOR_START + INTERVAL*11 + SECTION_PADDING*2,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F11 : [[HOR_START + INTERVAL*12 + SECTION_PADDING*2,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_F12 : [[HOR_START + INTERVAL*13 + SECTION_PADDING*2,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_NUMLOCK : [[HOR_START + INTERVAL*17+SECTION_PADDING*4,VERT_START+INTERVAL,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_CAPSLOCK : [[HOR_START, VERT_START+INTERVAL*3, KEY_SIZE*1.75, KEY_SIZE], False],
                           pygame.K_SCROLLOCK : [[HOR_START + INTERVAL*15+SECTION_PADDING*3,VERT_START,KEY_SIZE,KEY_SIZE], False],
                           pygame.K_RSHIFT : [[HOR_START+INTERVAL*11+SHIFT_EXTRA, VERT_START+INTERVAL*4, KEY_SIZE*3.17, KEY_SIZE], False],
                           pygame.K_LSHIFT : [[HOR_START, VERT_START+INTERVAL*4, KEY_SIZE*2, KEY_SIZE], False],
                           pygame.K_RCTRL : [[HOR_START+INTERVAL*6+CTRL_EXTRA*3+KEY_SIZE*6.6, VERT_START+INTERVAL*5, KEY_SIZE*1.5, KEY_SIZE], False],
                           pygame.K_LCTRL : [[HOR_START, VERT_START+INTERVAL*5, KEY_SIZE*1.5, KEY_SIZE], False],
                           pygame.K_RALT : [[HOR_START+INTERVAL*4+CTRL_EXTRA*2+KEY_SIZE*6.6, VERT_START+INTERVAL*5, KEY_SIZE*1.5, KEY_SIZE], False],
                           pygame.K_LALT : [[HOR_START+INTERVAL*2+CTRL_EXTRA, VERT_START+INTERVAL*5, KEY_SIZE*1.5, KEY_SIZE], False],
                          # pygame.K_RMETA : False,
                          # pygame.K_LMETA : False,
                           pygame.K_LSUPER : [[HOR_START+INTERVAL+CTRL_EXTRA, VERT_START+INTERVAL*5, KEY_SIZE, KEY_SIZE], False],
                           pygame.K_RSUPER : [[HOR_START+INTERVAL*5+CTRL_EXTRA*3+KEY_SIZE*6.6, VERT_START+INTERVAL*5, KEY_SIZE, KEY_SIZE], False],
                          # pygame.K_MODE : False,
                          # pygame.K_HELP : False,
                           pygame.K_PRINT : [[HOR_START + INTERVAL*14+SECTION_PADDING*3,VERT_START,KEY_SIZE,KEY_SIZE], False],
                          # pygame.K_SYSREQ : False,
                          # pygame.K_BREAK : False,
                          # pygame.K_MENU : False,
                          # pygame.K_POWER : False
                           }  


    def resetKeys(self):
        for key in self.key_rects:
            self.key_rects[key][1] = False

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.key_rects[event.key][1] = True
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x,y = pygame.mouse.get_pos()
                if x >= 25 and x <= 25 + text_size[0] and y >= 25 and y <= 25 + text_size[1]:
                    self.resetKeys()

    def draw(self, screen):
        screen.fill((192,192,192))
        screen.blit(text, [25,25])
        for key in self.key_rects:
            pygame.draw.rect(screen, (0,0,0), self.key_rects[key][0], 2)
            if self.key_rects[key][1] == True:
                pygame.draw.rect(screen, (255,255,255), [self.key_rects[key][0][0] + 2, self.key_rects[key][0][1]+2, self.key_rects[key][0][2]-3, self.key_rects[key][0][3]-3])
        #x = 0
        #for i in range(22):
            #pygame.draw.rect(screen, (0,0,0), [32+x,VERT_START,35,35], 2)
            #pygame.draw.rect(screen, (255,255,255), [34+x,302,32,32])
            #x += 38


    def update(self, screen):
        pygame.display.flip()
