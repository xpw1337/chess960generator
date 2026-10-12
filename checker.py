from chess960_pos_gen import Board


def check_board(board):
    """Return a list of problems with the board (empty if the board is valid)."""
    problems = []
    grid = board.grid

    if len(grid) != Board.SIZE or any(len(row) != Board.SIZE for row in grid):
        return ["board is not 8x8"]

    back_rank = grid[0]
    if not Board.is_valid_back_rank(back_rank):
        problems.append(f"invalid back rank: {back_rank}")
    if grid[7] != back_rank:
        problems.append("rows 0 and 7 do not match")

    # Pawn ranks
    for i in (1, 6):
        if grid[i] != [Board.PAWN] * Board.SIZE:
            problems.append(f"row {i} is not all pawns")

    # Empty ranks
    for i in range(2, 6):
        if grid[i] != [Board.EMPTY] * Board.SIZE:
            problems.append(f"row {i} is not empty")

    return problems


def check_generator(trials=1000):
    """Generate boards and check each one. Return True if every board is valid."""
    for _ in range(trials):
        board = Board()
        problems = check_board(board)
        if problems:
            print(f"Invalid board: {board!r}")
            for problem in problems:
                print(f"  - {problem}")
            return False

    print(f"All {trials} generated boards are valid.")
    return True


if __name__ == "__main__":
    check_generator()
