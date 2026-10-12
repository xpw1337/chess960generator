import random


class Board:
    """A Chess960 (Fischer Random Chess) starting board."""

    EMPTY = "     "
    PAWN = "pawns"
    SIZE = 8

    def __init__(self, back_rank=None):
        # Use the given back rank if provided, otherwise generate a random one
        if back_rank is None:
            back_rank = self.generate_back_rank()
        elif not self.is_valid_back_rank(back_rank):
            raise ValueError(f"Invalid Chess960 back rank: {back_rank}")

        self.back_rank = list(back_rank)
        self.grid = self._build_grid()

    @staticmethod
    def generate_back_rank():
        row = [None] * Board.SIZE

        # Bishops on opposite colors
        row[random.choice(range(0, Board.SIZE, 2))] = "bishop"
        row[random.choice(range(1, Board.SIZE, 2))] = "bishop"

        # Queen and knights on any three remaining squares
        for piece in ("queen", "knight", "knight"):
            empty = [i for i, square in enumerate(row) if square is None]
            row[random.choice(empty)] = piece

        # The last three empty squares go rook, king, rook so the king is between the rooks
        empty = [i for i, square in enumerate(row) if square is None]
        for i, piece in zip(empty, ("rook", "king", "rook")):
            row[i] = piece

        return row

    @staticmethod
    def is_valid_back_rank(row):
        if len(row) != Board.SIZE:
            return False
        if sorted(row) != sorted(["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]):
            return False

        # Bishops on opposite colors
        bishops = [i for i, piece in enumerate(row) if piece == "bishop"]
        if bishops[0] % 2 == bishops[1] % 2:
            return False

        # King between the rooks
        rooks = [i for i, piece in enumerate(row) if piece == "rook"]
        return rooks[0] < row.index("king") < rooks[1]

    def _build_grid(self):
        pawns_row = [self.PAWN] * self.SIZE
        return (
            [list(self.back_rank), list(pawns_row)]
            + [[self.EMPTY] * self.SIZE for _ in range(4)]
            + [list(pawns_row), list(self.back_rank)]
        )

    def __iter__(self):
        return iter(self.grid)

    def __eq__(self, other):
        return isinstance(other, Board) and self.back_rank == other.back_rank

    def __repr__(self):
        return f"Board({self.back_rank!r})"

    def __str__(self):
        return "\n".join(str(row) for row in self.grid)


if __name__ == "__main__":
    board = Board()
    board2 = Board()
    print(board)
    print(board2)
