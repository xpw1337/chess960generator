import random

import random

def makeBoard():
    # row variable contains row 1
    row = ["e"] * 8
    bishop1_posi, bishop2_posi = None, None
    king_posi = None
    rook1_posi, rook2_posi = None, None
    knight1_posi, knight2_posi, queen_posi = None, None, None

    # Bishops on opposite colors
    while bishop1_posi is None or bishop1_posi % 2 != 0:
        bishop1_posi = random.randint(0, len(row) - 1)
    while bishop2_posi is None or bishop2_posi % 2 == 0:
        bishop2_posi = random.randint(0, len(row) - 1)

    row[bishop1_posi] = row[bishop2_posi] = "bishop"

    # King: must be on an empty square AND have at least one empty on both sides
    while (
        king_posi is None
        or row[king_posi] != "e"
        or row[:king_posi].count("e") == 0
        or row[king_posi + 1 :].count("e") == 0
    ):
        king_posi = random.randint(0, 7)
    row[king_posi] = "king"

    # Rook to the left of the king on an empty square
    while rook1_posi is None or rook1_posi >= king_posi or row[rook1_posi] != "e":
        rook1_posi = random.randint(0, king_posi - 1)

    # Rook to the right of the king on an empty square
    while rook2_posi is None or rook2_posi <= king_posi or row[rook2_posi] != "e":
        rook2_posi = random.randint(king_posi + 1, len(row) - 1)

    # Correct assignment: place BOTH rooks on the board
    row[rook1_posi] = row[rook2_posi] = "rook"

    # Knights on empty squares
    while knight1_posi is None or row[knight1_posi] != "e":
        knight1_posi = random.randint(0, len(row) - 1)
    row[knight1_posi] = "knight"

    while knight2_posi is None or row[knight2_posi] != "e":
        knight2_posi = random.randint(0, len(row) - 1)
    row[knight2_posi] = "knight"

    # Queen on an empty square
    while queen_posi is None or row[queen_posi] != "e":
        queen_posi = random.randint(0, len(row) - 1)
    row[queen_posi] = "queen"

    # Build full board
    pawns_row = ["pawns"] * 8
    empty_row = ["     "] * 8
    return [row, pawns_row, empty_row, empty_row, empty_row, empty_row, pawns_row, row]


for i in makeBoard():
    print(i)
