import math


def get_box_num(row_ind: int, col_ind: int) -> int:
    box_col = col_ind // 3
    box_row = row_ind // 3

    box_num = (box_row * 3) + box_col + 1

    return box_num


def get_board_states(
    incomplete: list,
) -> tuple[dict, dict, dict, list] | tuple[None, None, None, None]:
    row_state = {}
    col_state = {}
    box_state = {}
    zero_indices = []

    for i, row in enumerate(incomplete):
        row_num = i + 1
        if row_num not in row_state:
            row_state[row_num] = set()

        for j, col in enumerate(row):
            col_num = j + 1
            box_num = get_box_num(i, j)

            if col_num not in col_state:
                col_state[col_num] = set()
            if box_num not in box_state:
                box_state[box_num] = set()

            found_num = incomplete[i][j]

            if found_num != 0:
                if (
                    found_num in row_state[row_num]
                    or found_num in col_state[col_num]
                    or found_num in box_state[box_num]
                ):
                    return (None, None, None, None)

                row_state[row_num].add(found_num)
                col_state[col_num].add(found_num)
                box_state[box_num].add(found_num)
            else:
                zero_indices.append((i, j))
    return (row_state, col_state, box_state, zero_indices)


def search_for_possibilities(
    row_possibilities: set, col_possibilities: set, box_possibilities: set
):
    pass


def solve_sudoku(
    incomplete: list,
    row_state: dict | None = None,
    col_state: dict | None = None,
    box_state: dict | None = None,
    zero_indices: list | None = None,
) -> list | None:
    # Initial Scan
    # Set up dicts of col, row, and box nums
    # Base Case:
    if zero_indices is not None and len(zero_indices) == 0:
        return incomplete

    row_state, col_state, box_state, zero_indices = get_board_states(incomplete)

    if not row_state or not col_state or not box_state or not zero_indices:
        return None

    full_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for i, inds in enumerate(zero_indices):
        row_ind, col_ind = inds
        row_num = row_ind + 1
        col_num = col_ind + 1
        box_num = get_box_num(row_ind, col_ind)

        row_possibilities = full_set - row_state[row_num]
        col_possibilities = full_set - col_state[col_num]
        box_possibilities = full_set - box_state[box_num]

        intersection = row_possibilities.intersection(
            col_possibilities, box_possibilities
        )
        if len(intersection) == 1:
            print(f"Intersection Found: {row_ind},{col_ind} -> {intersection}")
            valid_num = list(intersection)[0]
            incomplete[row_ind][col_ind] = valid_num

            row_state[row_num].add(valid_num)
            col_state[col_num].add(valid_num)
            box_state[box_num].add(valid_num)
            zero_indices.pop(i)
    # Then annotate each empty cell based on what it could contain
    # Identify cases where columns, rows, or boxes only have one solution for a number
    # Fill that number, update dicts
    print(f"Zero Indices Left: {len(zero_indices)}")
    return solve_sudoku(incomplete, row_state, col_state, box_state, zero_indices)


def main():
    sudoku_1 = [
        [2, 8, 6, 0, 5, 0, 0, 0, 0],
        [0, 9, 4, 1, 0, 0, 5, 8, 0],
        [3, 5, 0, 9, 7, 8, 2, 0, 4],
        [0, 0, 9, 7, 8, 3, 1, 0, 2],
        [0, 3, 2, 0, 9, 1, 4, 7, 6],
        [1, 7, 0, 0, 0, 6, 0, 0, 0],
        [6, 0, 8, 2, 0, 7, 9, 0, 0],
        [9, 0, 0, 0, 4, 5, 8, 2, 7],
        [5, 0, 7, 8, 3, 9, 6, 0, 1],
    ]

    sudoku_1_solved = [
        [2, 8, 6, 3, 5, 4, 7, 1, 9],
        [7, 9, 4, 1, 6, 2, 5, 8, 3],
        [3, 5, 1, 9, 7, 8, 2, 6, 4],
        [4, 6, 9, 7, 8, 3, 1, 5, 2],
        [8, 3, 2, 5, 9, 1, 4, 7, 6],
        [1, 7, 5, 4, 2, 6, 3, 9, 8],
        [6, 4, 8, 2, 1, 7, 9, 3, 5],
        [9, 1, 3, 6, 4, 5, 8, 2, 7],
        [5, 2, 7, 8, 3, 9, 6, 4, 1],
    ]

    solved = solve_sudoku(sudoku_1)
    if not solved:
        print("Sudoku solution was found to be null")
        return False

    for i, row in enumerate(solved):
        for j, col in enumerate(row):
            if solved[i][j] != sudoku_1_solved[i][j]:
                print(f"Found inconsistency at: ({i},{j})")
                return False

    print("Success, Correct Sudoku Found!")
    return True


if __name__ == "__main__":
    main()
