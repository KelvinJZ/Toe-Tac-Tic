import turtle as t

t.speed(99)
s = t.getscreen()

def draw_board():
    # draw tic tac toe board
    for i in range(1, 3):
        t.penup()
        t.goto(0, i * 50)
        t.pendown()
        t.forward(150)
    t.left(90)
    for j in range(1, 3):
        t.penup()
        t.goto(j * 50, 0)
        t.pendown()
        t.forward(150)


def draw_o(x, y):
    # drawing a circle at the destinated x, y position
    t.width(3)
    t.color('deepskyblue')
    t.seth(0)
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.circle(20)


def draw_x(x, y):
    t.width(3)
    t.color('red1')
    t.seth(0)
    t.penup()
    # top right corner --> (x+20, y+20)
    t.goto(x + 20, y + 20)

    t.pendown()
    # lower left corner --> (x-20, y-20)
    t.goto(x - 20, y - 20)
    # top left corner
    t.penup()
    t.goto(x - 20, y + 20)
    t.pendown()
    # lower right corner
    t.goto(x + 20, y - 20)

w, h = 3, 3
board = [['-' for x in range(w)] for y in range(h)]
state = {'player': False}  # Keep track of the current player
players = [draw_x, draw_o]  # player x is false/0, player o is true/1
isPlaying = True

def click(x, y):
    global isPlaying
    draw = players[int(state['player'])]
    draw(x, y)
    user_click(x, y)
    state['player'] = not state['player']
    win()


def user_click(x, y):
    if x < 100 and x > 50 and y < 100 and y > 50:
        board[1][1] = state['player']
    elif x < 50 and x > 0 and y < 100 and y > 50:
        board[1][0] = state['player']
    elif x < 150 and x > 100 and y < 100 and y > 50:
        board[1][2] = state['player']
    elif x < 50 and x > 0 and y < 150 and y > 100:
        board[0][0] = state['player']
    elif x < 100 and x > 50 and y < 150 and y > 100:
        board[0][1] = state['player']
    elif x < 150 and x > 100 and y < 150 and y > 100:
        board[0][2] = state['player']
    elif x < 50 and x > 0 and y < 50 and y > 0:
        board[2][0] = state['player']
    elif x < 100 and x > 50 and y < 50 and y > 0:
        board[2][1] = state['player']
    elif x < 150 and x > 100 and y < 50 and y > 0:
        board[2][2] = state['player']
    else:
        print("Out of Bound")


def win():
    global isPlaying
    if check_row() or check_col() or check_diagonal():
        state['player'] = not state['player']
        print(int(state['player']), "Win")
        print("End Game")
        isPlaying = False
    check_tie()


def check_row():
    # check if row are the same
    for r in range(w):
        if '-' not in board[r]:
            if board[r][0] == board[r][1] and board[r][1] == board[r][2]:
                return True


def check_col():
    # check if col are the same
    for c in range(h):
        new_board = list(map(list, zip(*board)))
        if '-' not in new_board[c]:
            if board[0][c] == board[1][c] and board[1][c] == board[2][c]:
                return True


def check_diagonal():
    # check if diagonal are the same
    if board[1][1] != '-':
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True
        if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            return True


def check_tie():
    global isPlaying
    if '-' not in board[0] and '-' not in board[1] and '-' not in board[2]:
        print("TIE")
        isPlaying = False

if __name__ == '__main__':
    draw_board()
    print(board)
    while isPlaying:
        s.onclick(click)
        s.update()