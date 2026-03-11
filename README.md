# Chess960 Position Generator

A Python utility that generates valid random Chess960 (Fischer Random Chess) starting positions.

## What is Chess960?

Chess960—also known as Fischer Random Chess—introduces variety by randomizing the back-rank piece placement while preserving the core mechanics of chess. Rather than memorizing opening theory, players must rely on understanding. There are exactly **960** legal starting positions that satisfy the rules.

## Rules Enforced

The generator ensures each position meets all Chess960 constraints:

- **Bishops on opposite colors** — One bishop on a light square, one on a dark square
- **King between the rooks** — Required for castling to work on both sides
- **Remaining pieces** — Two knights and one queen fill the three leftover squares

## Requirements

- Python 3.6+

No external dependencies—uses only the standard library.

## Usage

```bash
python chess960_pos_gen.py
```

Or import and use the `makeBoard()` function in your own code:

```python
from chess960_pos_gen import makeBoard

board = makeBoard()
for row in board:
    print(row)
```

## Output Format

Returns an 8×8 list representing the board:

- **Row 0 & 7** — Back ranks (`king`, `queen`, `rook`, `bishop`, `knight`)
- **Row 1 & 6** — Pawn ranks
- **Row 2–5** — Empty ranks

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

MIT License — see [LICENSE](LICENSE) for details.
