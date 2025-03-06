from pygame.locals import (
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_ESCAPE,
    K_SPACE,
    K_UP,
    RLEACCEL,
    QUIT,
)
 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_SIZE = 500
PIECE_SIZE = 50
PZ = 50
SZ = 450
WL = 2
CIRCLE_RADIUS = 7
 
BLACK = (0, 0, 0)
ORANGE = (181, 101, 29)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (135, 206, 250)
RED = (255, 0, 0)
RED_B = (255, 102, 102)
RED_P = (255, 51, 51)
GRIS_BRIGHT = (192, 192, 192)
GRIS = (128, 128, 128)

B = {
        'king': pygame.image.load(os.path.join("img", "black_king.png")),
        'queen': pygame.image.load(os.path.join("img", "black_queen.png")),
        'rook': pygame.image.load(os.path.join("img", "black_rook.png")),
        'bishop': pygame.image.load(os.path.join("img", "black_bishop.png")),
        'knight': pygame.image.load(os.path.join("img", "black_knight.png")),
        'pawn': pygame.image.load(os.path.join("img", "black_pawn.png")),
    }
 
W = {
        'king': pygame.image.load(os.path.join("img", "white_king.png")),
        'queen': pygame.image.load(os.path.join("img", "white_queen.png")),
        'rook': pygame.image.load(os.path.join("img", "white_rook.png")),
        'bishop': pygame.image.load(os.path.join("img", "white_bishop.png")),
        'knight': pygame.image.load(os.path.join("img", "white_knight.png")),
        'pawn': pygame.image.load(os.path.join("img", "white_pawn.png")),
    }

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 35)
        self.font2 = pygame.font.SysFont("comicsansms", 72)
        pygame.quit()

def Menu(self):
        self.screen.fill(BLUE)
 
        txt = self.font2.render("-= Chess Game =-", True, RED)
        txt_center = (
            SCREEN_SIZE/2 - txt.get_width() // 2,
            SCREEN_SIZE/2 - txt.get_height() // 2
        )
 
        txt2 = self.font.render("Player 1 vs Player 2", True, GREEN)
        txt2_center = (
            SCREEN_SIZE/2 - txt2.get_width() // 2,
            SCREEN_SIZE/2 + 30
        )
        txt3 = self.font.render("Player 1 vs AI Computer", True, GREEN)
        txt3_center = (
            SCREEN_SIZE/2 - txt3.get_width() // 2,
            SCREEN_SIZE/2 + 60
        )
        option = -1
        running = True
        while running:
            self.screen.fill(BLUE)
            self.screen.blit(txt, txt_center)
            self.screen.blit(txt2, txt2_center)
            self.screen.blit(txt3, txt3_center)
            pygame.display.flip()
            return option

        cmate = -1
        option = self.Menu()
        if option == 1:
            cmate = self.Game_player_vs_player(board, pieces)
        elif option == 2:
            cmate = self.Game_player_vs_AI_Minimax(board, pieces)
        self.Game_Over(board, pieces, cmate)

class Board():
    def __init__(self, screen):
        self.screen = screen
        self.color = BLUE

def draw_board(self, C):
        pygame.draw.rect(self.screen, C, (0, 0, SCREEN_SIZE, PIECE_SIZE))
        pygame.draw.rect(self.screen, C, (0, 0, PIECE_SIZE, SCREEN_SIZE))
        pygame.draw.rect(self.screen, C, (SCREEN_SIZE-PIECE_SIZE, 0, PIECE_SIZE, SCREEN_SIZE))
        pygame.draw.rect(self.screen, C, (0, SCREEN_SIZE-PIECE_SIZE, SCREEN_SIZE-PIECE_SIZE, PIECE_SIZE))
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    self.color = WHITE
                else:
                    self.color = ORANGE
                pygame.draw.rect(
             
      self.screen, self.color,
                    (PIECE_SIZE*(x+1), PIECE_SIZE*(y+1), PIECE_SIZE, PIECE_SIZE))

board = Board(self.screen)
class Pieces():
    def __init__(self, screen):
        self.screen = screen
        self.prev_move = PrevMove()
        self.init_array_pieces()
        self.init_surf_pieces()
def init_array_pieces(self):
        self.ar = [['  ' for i in range(8)] for i in range(8)]
        for i in (0, 7):
            if i == 0:
                bw = 'b'
            else:
                bw = 'w'
            self.ar[i][0] = bw + 'r'
            self.ar[i][1] = bw + 'n'
            self.ar[i][2] = bw + 'b'
            self.ar[i][3] = bw + 'q'
            self.ar[i][4] = bw + 'k'
            self.ar[i][5] = bw + 'b'
            self.ar[i][6] = bw + 'n'
            self.ar[i][7] = bw + 'r'
        for i in range(8):
            self.ar[1][i] = 'bp'
            self.ar[6][i] = 'wp'
 
  	def draw_pieces_upgrade(self, pos):
        for i in range(8):
            for j in range(8):
                if pos != () and i == pos[0][0]-1 and j == pos[0][1]-1:
                    pygame.draw.rect(
                            self.screen, RED_B,
                            (PIECE_SIZE*(j+1), PIECE_SIZE*(i+1), PIECE_SIZE, PIECE_SIZE))
                if self.ar[i][j] != '  ':
                    if (i + j) % 2 == 0:
                        CLR = GRIS_BRIGHT
                    else:
                        CLR = GRIS
                    if self.ar[i][j] == '..' or self.ar[i][j] == '...':
                        pygame.draw.rect(
                                self.screen, CLR,
                                (PIECE_SIZE*(j+1), PIECE_SIZE*(i+1), PIECE_SIZE, PIECE_SIZE))
                    elif self.ar[i][j][0] == '.':
                        pygame.draw.rect(
                                self.screen, CLR,
                                (PIECE_SIZE*(j+1), PIECE_SIZE*(i+1), PIECE_SIZE, PIECE_SIZE))
                        self.P[self.ar[i][j][1:]].rect = cal_rect(1, i+1,j+1)
                        self.screen.blit(self.P[self.ar[i][j][1:]].surf, cal_rect(1, i+1,j+1))
                    else:
                        if pos != () and i == pos[1][0]-1 and j == pos[1][1]-1:
                            pygame.draw.rect(
                                    self.screen, RED_P,
                                    (PIECE_SIZE*(j+1), PIECE_SIZE*(i+1), PIECE_SIZE, PIECE_SIZE))
                        self.P[self.ar[i][j]].rect = cal_rect(1, i+1,j+1)
                        self.screen.blit(self.P[self.ar[i][j]].surf, cal_rect(1, i+1,j+1))

def Game_player_vs_player(self, board, pieces):
        # player 0 for white
        #        1 for black
        cplayer = ['w', 'b']
        C = [BLUE, BLACK]
        player, cl, st, cmate = 0, -1, [], -1
        last_pos = ()
        running = True
        while running:
        	board.draw_board(C[player])
        	pieces.draw_pieces_upgrade(last_pos)
            pygame.display.flip()
            return cmate
  	
def Game_player_vs_AI_Minimax(self, board, pieces):
 
        cplayer = ['w', 'b']
        C = [BLUE, BLACK]
        player, cl, st, cmate = 0, -1, [], -1
        last_pos = ()
        running = True
        while running:
            board.draw_board(C[player])
            pieces.draw_pieces_upgrade(last_pos)
            pygame.display.flip()
        return cmate

pieces = Pieces(self.screen)
def is_prevent_check(self, ar, a, b, c, d, m):
        type = ar[a][b][0]
        ar[c][d] = m
        self.prev_move.move(ar,a,b,c,d)
        return not self.prev_move.is_checked(ar, self.P, type)
 
def selecting(self, p):
        x, y = p[0]-1, p[1]-1
        type = self.ar[x][y][0]
 
        lst = self.available_moves(self.ar[x][y], p, type)
        if self.ar[x][y][-1] == 'k':
            res = self.precond_castling(self.ar, type)
            if res[0] == 1:
                lst.append((x,y-2))
            if res[1] == 1:
                lst.append((x,y+2))
        if self.ar[x][y][-1] == 'p':
            tmp = self.prev_move.precond_en_passant(self.ar, x, y, type)
            if tmp != []:
                for i in tmp:
                    if self.is_prevent_check(deepcopy(self.ar),x,y,i[0],i[1],'...'):
                        self.ar[i[0]][i[1]] = '...'
        if lst != []:
            for i in lst:
                if self.ar[i[0]][i[1]] != '  ':
                    if self.is_prevent_check(deepcopy(self.ar),x,y,i[0],i[1],'.' + deepcopy(self.ar[i[0]][i[1]])):
                        self.ar[i[0]][i[1]] = '.' + self.ar[i[0]][i[1]]
                else:
                    if self.is_prevent_check(deepcopy(self.ar),x,y,i[0],i[1],'..'):
                        self.ar[i[0]][i[1]] = '..'
 
def available_moves(self, pc, p, type):
        return self.P[pc].a_moves(self.ar, p, type)
 
def move(self, ar, r, rr):
        a, b, c, d = r[0]-1, r[1]-1, rr[0]-1, rr[1]-1
        type = ar[a][b][0]
 
        if ar[c][d][0] == '.':
            if ar[a][b][-1] == 'k' and (b-d==2 or d-b==2):
                if b - d == 2:
                    self.prev_move.update(ar[a][b], (a,b), (c,d-2))
                    self.castle_move(ar, (a,b),(c,d-2))
                elif d - b == 2:
                    self.prev_move.update(ar[a][b], (a,b), (c,d+1))
                    self.castle_move(ar, (a,b),(c,d+1))
            else:
                self.prev_move.update(ar[a][b], (a,b), (c,d))
                if ar[c][d] == '...':
                    if type == 'b':
                        ar[c-1][d] = '  '
                    if type == 'w':
                        ar[c+1][d] = '  '
                ar[c][d] = deepcopy(ar[a][b])
                ar[a][b] = '  '
                if ar[c][d][-1] == 'p':
                    if type == 'b' and c == 7:
                        ar[c][d] = deepcopy('bq')
                    elif type == 'w' and c == 0:
                        ar[c][d] = deepcopy('wq')
 
        else:
            return 0
        clean_selected(ar)
        return 1
    def is_checked(self, ar, type):
        p = king_position(ar, type)
        x, y = p[0], p[1]
        for i in range(8):
            for j in range(8):
                if ar[i][j] != '  ' and ar[i][j][0] != type:
                    for pos in self.available_moves(ar[i][j], (i+1,j+1), ar[i][j][0]):
                        if pos[0] == x and pos[1] == y:
                            return True
        return False
 
    def is_checkmate(self, ar, type):
        if self.is_checked(ar, type):
            for x in range(8):
                for y in range(8):
                    if ar[x][y][0] == type:
                        lst = self.available_moves(ar[x][y], (x+1,y+1), type)
                        if ar[x][y][-1] == 'p':
                            tmp = self.prev_move.precond_en_passant(ar, x, y, type)
                            if tmp != []:
                                for i in tmp:
                                    if self.is_prevent_check(deepcopy(ar),x,y,i[0],i[1],'...'):
                                        return False
                        if lst != []:
                            for i in lst:
                                if ar[i[0]][i[1]] != '  ':
                                    if self.is_prevent_check(deepcopy(ar),x,y,i[0],i[1],'.' + deepcopy(ar[i[0]][i[1]])):
                                        return False
                                else:
                                    if self.is_prevent_check(deepcopy(ar),x,y,i[0],i[1],'..'):
                                        return False
            return True
        return False
 
    def is_pos_not_checked(self, ar, p, type): #<--
        x, y = p[0], p[1]
        for i in range(8):
            for j in range(8):
                if ar[i][j] != '  ' and ar[i][j][0] != type:
                    for pos in self.available_moves(ar[i][j], (i+1,j+1), ar[i][j][0]):
                        if pos[0] == x and pos[1] == y:
                            return False
        return True
def switch_piece(self, a, b):
        x, y = a[0]-1, a[1]-1
        kx, ky = b[0]-1, b[1]-1
        if self.ar[x][y][0] == self.ar[kx][ky][0]:
            return True
        return False

class King():
 
    def __init__(self, surf, rect, type, p):
        self.surf = surf
        self.surf.set_colorkey(BLACK, RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (PIECE_SIZE, PIECE_SIZE))
        self.rect = rect
        self.type = type
 
    def a_moves(self, ar, p, type):
        x, y, lst = p[0]-1, p[1]-1, []
        index = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
        for i in index:

            nx, ny = x+i[0], y+i[1]
            if check_valid(nx, ny):
                if ar[nx][ny] == '  ' or ar[x][y][0] != ar[nx][ny][0]:
                    lst.append((nx, ny))
        return lst

def Game_player_vs_player(self, board, pieces):
        # player 0 for white
        #        1 for black
        cplayer = ['w', 'b']
        C = [BLUE, BLACK]
        player, cl, st, cmate = 0, -1, [], -1
        last_pos = ()
        running = True
        while running:
            pos_clicked = ()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos_clicked = rev_rect(pygame.mouse.get_pos())
                        cl += 1
                        if not pieces.precond(pos_clicked, player) and cl == 0:
                            cl -= 1
                            continue
            if pos_clicked != () and not check_valid(pos_clicked[0]-1, pos_clicked[1]-1):
                cl -= 1
                continue
            if pos_clicked != () and cl == 0:
                pieces.selecting(pos_clicked)
                st.append(pos_clicked)
                print_ar(pieces.ar)
            if pos_clicked != () and cl == 1:
                if eq(st[0], pos_clicked):
                    cl -= 1
                    continue
                if pieces.switch_piece(st[0], pos_clicked):
                    cl, st = -1, []
                    clean_selected(pieces.ar)
                    continue
                if not pieces.move(pieces.ar, st[0], pos_clicked):
                    cl -= 1
                    continue
                last_pos = (st[0], pos_clicked)
                player, cl, st = 1 - player, -1, []
                print_ar(pieces.ar)
                if pieces.is_checked(pieces.ar, cplayer[player]):
                    if pieces.is_checkmate(pieces.ar, cplayer[player]):
                        cmate = 1-player
                        running = False
 
            board.draw_board(C[player])
            pieces.draw_pieces_upgrade(last_pos)
 
            pygame.display.flip()
        return cmate
                        if pieces.is_checkmate(pieces.ar, cplayer[player]):
                            cmate = 1-player
                            running = False
            board.draw_board(C[player])
            pieces.draw_pieces_upgrade(last_pos)
            pygame.display.flip()
        return cmate

piece_eval = { 'p': 100, 'n': 280, 'b': 320, 'r': 479, 'q': 929, 'k': 60000 }
Score_init_WPsf = [  [ 0,   0,   0,   0,   0,   0,   0,   0],
            [78,  83,  86,  73, 102,  82,  85,  90],
            [ 7,  29,  21,  44,  40,  31,  44,   7],
           [-17,  16,  -2,  15,  14,   0,  15, -13],
           [-26,   3,  10,   9,   6,   1,   0, -23],
           [-22,   9,   5, -11, -10,  -2,   3, -19],
           [-31,   8,  -7, -37, -36, -14,   3, -31],
            [ 0,   0,   0,   0,   0,   0,   0,   0]]
Score_init_WNsf = [ [-66, -53, -75, -75, -10, -55, -58, -70],
            [-3,  -6, 100, -36,   4,  62,  -4, -14],
            [10,  67,   1,  74,  73,  27,  62,  -2],
           [ 24,  24,  45,  37,  33,  41,  25,  17],
           [ -1,   5,  31,  21,  22,  35,   2,   0],
           [-18,  10,  13,  22,  18,  15,  11, -14],
           [-23, -15,   2,   0,   2,   0, -23, -20],
           [-74, -23, -26, -24, -19, -35, -22, -69]]
Score_init_WBsf = [ [-59, -78, -82, -76, -23,-107, -37, -50],
           [-11,  20,  35, -42, -39,  31,   2, -22],
            [-9,  39, -32,  41,  52, -10,  28, -14],
            [25,  17,  20,  34,  26,  25,  15,  10],
            [13,  10,  17,  23,  17,  16,   0,   7],
            [14,  25,  24,  15,   8,  25,  20,  15],
            [19,  20,  11,   6,   7,   6,  20,  16],
            [-7,   2, -15, -12, -14, -15, -10, -10]]
Score_init_WRsf = [  [35,  29,  33,   4,  37,  33,  56,  50],
            [55,  29,  56,  67,  55,  62,  34,  60],
            [19,  35,  28,  33,  45,  27,  25,  15],
             [0,   5,  16,  13,  18,  -4,  -9,  -6],
           [-28, -35, -16, -21, -13, -29, -46, -30],
           [-42, -28, -42, -25, -25, -35, -26, -46],
           [-53, -38, -31, -26, -29, -43, -44, -53],
           [-30, -24, -18,   5,  -2, -18, -31, -32]]
Score_init_WQsf =  [  [ 6,   1,  -8,-104,  69,  24,  88,  26],
            [14,  32,  60, -10,  20,  76,  57,  24],
            [-2,  43,  32,  60,  72,  63,  43,   2],
             [1, -16,  22,  17,  25,  20, -13,  -6],
           [-14, -15,  -2,  -5,  -1, -10, -20, -22],
           [-30,  -6, -13, -11, -16, -11, -16, -27],
           [-36, -18,   0, -19, -15, -15, -21, -38],
           [-39, -30, -31, -13, -31, -36, -34, -42]]
Score_init_WKsf = [ [  4,  54,  47, -99, -99,  60,  83, -62],
           [-32,  10,  55,  56,  56,  55,  10,   3],
           [-62,  12, -57,  44, -67,  28,  37, -31],
           [-55,  50,  11,  -4, -19,  13,   0, -49],
           [-55, -43, -52, -28, -51, -47,  -8, -50],
           [-47, -42, -43, -79, -64, -32, -29, -32],
            [-4,   3, -14, -50, -57, -18,  13,   4],
            [17,  30,  -3, -14,   6,  -1,  40,  18]]

Score_init_BKsf = [i[::-1] for i in Score_init_WKsf]
Score_init_BQsf = [i[::-1] for i in Score_init_WQsf]
Score_init_BRsf = [i[::-1] for i in Score_init_WRsf]
Score_init_BBsf = [i[::-1] for i in Score_init_WBsf]
Score_init_BNsf = [i[::-1] for i in Score_init_WNsf]
Score_init_BPsf = [i[::-1] for i in Score_init_WPsf]

Score_init_BKsf.reverse()
Score_init_BQsf.reverse()
Score_init_BRsf.reverse()
Score_init_BBsf.reverse()
Score_init_BNsf.reverse()
Score_init_BPsf.reverse()

def eval_board(self, ar):
        score = 0
        for i in range(8):
            for j in range(8):
                if ar[i][j][0] == 'b':
                    score += piece_eval[ar[i][j][-1]]
                elif ar[i][j][0] == 'w':
                    score -= piece_eval[ar[i][j][-1]]
        return score

def minimax(self,ar,pieces,type,alpha,beta,depth, last_move,prev_move):
        if depth == 0:
            return [self.eval_board(ar),last_move[0],last_move[1]]        
        if type == 'b': # Maximal Player
            max_s = [-1000000000, None, None]
            ps = self.lst_pieces_available(ar, type)
            random.shuffle(ps)
            for piece in ps:
                x, y = piece[1], piece[2]
                lst_ai = self.selecting_AI_Move(ar, (x+1, y+1),prev_move)
                if lst_ai == []:
                    continue
                for pos in lst_ai:
                    img = deepcopy(ar[x][y])
                    cp_ar = deepcopy(ar)
                    cp_prev_move = deepcopy(prev_move)
                    self.move_AI_Minimax(cp_ar, (x+1,y+1),pos, cp_prev_move)
                    if self.is_checkmate_AI_Move(cp_ar, 'w',prev_move):
                        score = [10000000000000,(x+1,y+1),pos]
                    else:
                        score = self.minimax(cp_ar,pieces,'w',alpha,beta,depth-1, ((x+1,y+1),pos),cp_prev_move)
                        score[0] += Score_initsf[img][pos[0]-1][pos[1]-1]
                    if score[0] >= max_s[0]:
                        max_s = [score[0],(x+1,y+1),pos]
                    if alpha < max_s[0]:
                        alpha = max_s[0]
                    if alpha >= beta:
                        break
            return max_s
        else: # Minimal Player
            min_s = [1000000000, None, None]
            ps = self.lst_pieces_available(ar, type)
            random.shuffle(ps)
            for piece in ps:
                x, y = piece[1], piece[2]
                lst_ai = self.selecting_AI_Move(ar, (x+1, y+1),prev_move)
                if lst_ai == []:
                    continue
                for pos in lst_ai:
                    img = deepcopy(ar[x][y])
                    cp_ar = deepcopy(ar)
                    cp_prev_move = deepcopy(prev_move)
                    self.move_AI_Minimax(cp_ar, (x+1,y+1),pos,cp_prev_move)
                    if self.is_checkmate_AI_Move(cp_ar, 'b', prev_move):
                        score = [-10000000000000,(x+1,y+1),pos]
                    else:
                        score = self.minimax(cp_ar,pieces,'b',alpha,beta,depth-1, ((x+1,y+1),pos),cp_prev_move)
                        score[0] += Score_initsf[img][pos[0]-1][pos[1]-1]
                    if score[0] <= min_s[0]:
                        min_s = [score[0],(x+1,y+1),pos]
                    if beta > min_s[0]:
                        beta = min_s[0]
                    if alpha >= beta:
                        break
            return min_s
