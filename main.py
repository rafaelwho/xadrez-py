
board = {
    'a8': [], 'b8': [], 'c8': [], 'd8': [], 'e8': [], 'f8': [], 'g8': [], 'h8': [],
    'a7': [], 'b7': [], 'c7': [], 'd7': [], 'e7': [], 'f7': [], 'g7': [], 'h7': [],
    'a6': [], 'b6': [], 'c6': [], 'd6': [], 'e6': [], 'f6': [], 'g6': [], 'h6': [],
    'a5': [], 'b5': [], 'c5': [], 'd5': [], 'e5': [], 'f5': [], 'g5': [], 'h5': [],
    'a4': [], 'b4': [], 'c4': [], 'd4': [], 'e4': [], 'f4': [], 'g4': [], 'h4': [],
    'a3': [], 'b3': [], 'c3': [], 'd3': [], 'e3': [], 'f3': [], 'g3': [], 'h3': [],
    'a2': [], 'b2': [], 'c2': [], 'd2': [], 'e2': [], 'f2': [], 'g2': [], 'h2': [],
    'a1': [], 'b1': [], 'c1': [], 'd1': [], 'e1': [], 'f1': [], 'g1': [], 'h1': []
}

def setBoard():
    # white
    board['a1'] = 'T'
    board['b1'] = 'B'
    board['c1'] = 'N'
    board['d1'] = 'Q'
    board['e1'] = 'K'
    board['f1'] = 'N'
    board['g1'] = 'B'
    board['h1'] = 'T'
    board['a2'] = 'P'
    board['b2'] = 'P'
    board['c2'] = 'P'
    board['d2'] = 'P'
    board['e2'] = 'P'
    board['f2'] = 'P'
    board['g2'] = 'P'
    board['h2'] = 'P'
    # black
    board['a8'] = 'T'
    board['b8'] = 'B'
    board['c8'] = 'N'
    board['d8'] = 'K'
    board['e8'] = 'Q'
    board['f8'] = 'N'
    board['g8'] = 'B'
    board['h8'] = 'T'
    board['a7'] = 'P'
    board['b7'] = 'P'
    board['c7'] = 'P'
    board['d7'] = 'P'
    board['e7'] = 'P'
    board['f7'] = 'P'
    board['g7'] = 'P'
    board['h7'] = 'P'



def play(piece, positionFrom, positionTo):
    board[positionFrom].clear()
    board[positionTo] = piece


def start():
    setBoard()
    print(board)

start()