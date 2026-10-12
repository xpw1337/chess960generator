# Chess960 Position Generator

A Python utility that generates valid random Chess960 (Fischer Random Chess) starting positions.

## What is Chess960?

Chess960 (also known as Fischer Random Chess) introduces variety by randomizing the back-rank piece placement while preserving the core mechanics of chess. Rather than memorizing opening theory, players must rely on understanding. There are exactly **960** legal starting positions that satisfy the rules.

## Rules Enforced

The generator ensures each position meets all Chess960 constraints:

- **Bishops on opposite colors**: One bishop on a light square, one on a dark square
- **King between the rooks**: Required for castling to work on both sides
- **Remaining pieces**: Two knights and one queen fill the three leftover squares

## Requirements

- Python 3.6+

No external dependencies; uses only the standard library.

## Usage

```bash
python chess960_pos_gen.py
```

This prints two random Chess960 boards.

Or import the `Board` class and create boards as objects:

```python
from chess960_pos_gen import Board

board = Board()            # random Chess960 position
print(board)

for row in board:          # boards are iterable, row by row
    print(row)

print(board.back_rank)     # just the back rank
print(board.grid)          # the full 8x8 list

# Build a board from a specific back rank (validated against Chess960 rules)
classic = Board(["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"])
```

Passing an invalid back rank raises a `ValueError`. You can also check a back rank yourself with `Board.is_valid_back_rank(row)`.

## Checking the Generator

`checker.py` verifies that the generator only produces valid boards:

```bash
python checker.py
```

This generates 1000 boards and checks each one, printing `All 1000 generated boards are valid.` on success. If a bad board turns up, it prints the board and what is wrong with it.

You can also use the checker in your own code:

```python
from chess960_pos_gen import Board
from checker import check_board, check_generator

problems = check_board(Board())   # list of problems, empty if the board is valid
check_generator(trials=5000)      # returns True if every generated board is valid
```

`check_board` checks the whole board, not just the back rank:

- The board is 8×8
- The back rank follows the Chess960 rules
- Rows 0 and 7 match
- Rows 1 and 6 are all pawns
- Rows 2 to 5 are empty

## Output Format

`board.grid` is an 8×8 list representing the board:

- **Row 0 & 7**: Back ranks (`king`, `queen`, `rook`, `bishop`, `knight`)
- **Row 1 & 6**: Pawn ranks
- **Row 2–5**: Empty ranks

Each back-rank square contains a piece type: `"king"`, `"queen"`, `"rook"`, `"bishop"`, or `"knight"`.

## Example Output

```
['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
['pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns']
['     ', '     ', '     ', '     ', '     ', '     ', '     ', '     ']
['     ', '     ', '     ', '     ', '     ', '     ', '     ', '     ']
['     ', '     ', '     ', '     ', '     ', '     ', '     ', '     ']
['     ', '     ', '     ', '     ', '     ', '     ', '     ', '     ']
['pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns', 'pawns']
['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
```

## License

MIT License. See [LICENSE](LICENSE) for details.
