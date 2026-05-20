class Solution:
    """ ht* - hash_table    sb* - sub-box"""
    BOARDSIZE = 9
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hash_table = self.get_ht(board)
        for row in hash_table:
            row_simplified = self.row_simplify(row)
            row_x, row_y = row_simplified
            for i in range(len(row)):   # duplicates in rows and columns
                if row_x.count(row_x[i]) > 1: return False
                if row_y.count(row_y[i]) > 1: return False
            for sb_min in range(0, self.BOARDSIZE, 3): # duplicates in sub-boxes
                sb_rows, sb_cols = self.sb_helper(row_simplified, len(row), sb_min)
                if len(sb_rows)>1 and len(sb_cols)>1: return False
        return True

    def sb_helper(self, ht_row: list[tuple], row_length: int, subbox_min: int) -> list[list[int]]:
        r_x, r_y = ht_row
        sb_r = [r_x[z] for z in range(row_length) if r_x[z] in range(subbox_min, subbox_min+3)]
        sb_c = []
        if len(sb_r) > 1:
            for sb_min in range(0, Solution.BOARDSIZE, 3):
                sb_c = [r_y[r_x.index(sb_r_val)] for sb_r_val in sb_r if r_y[r_x.index(sb_r_val)] in range(sb_min, sb_min+3)]
                if len(sb_c) > 1: break
        return [sb_r, sb_c]

    def hash_function(self, given_board: list[list[str]], x: int, y:int):
        xy_cell = given_board[x][y]
        return xy_cell if xy_cell != '.' else None

    def get_ht(self, given_board: list[list[str]]) -> list[list[str]]:
        hash_table = [[], [],[],[],[],[],[],[],[]]
        for row_idx in range(0, self.BOARDSIZE):
            for col_idx in range(0, self.BOARDSIZE):
                hash_code = self.hash_function(given_board, row_idx, col_idx)
                if hash_code: hash_table[int(hash_code)-1].append((row_idx, col_idx))
        return hash_table

    def row_simplify(self, ht_row: list[tuple]) -> list[list[int]]:
        ht_x = [coord[0] for coord in ht_row]
        ht_y = [coord[1] for coord in ht_row]
        row_simplified = [ht_x]
        row_simplified.append(ht_y)
        return row_simplified


board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
    ]

my_solution = Solution()
print(my_solution.isValidSudoku(board))

# [
#     [(1, 3), (4, 8), (7, 4)],                         1
#     [(5, 4), (6, 6)],                                 2
#     [(0, 1), (3, 8), (4, 5)],                         3
#     [(4, 0), (7, 3)],                                 4
#     [(0, 0), (1, 5), (7, 8)],                         5
#     [(1, 0), (2, 7), (3, 4), (5, 8), (6, 1)],         6
#     [(0, 4), (5, 0), (8, 7)],                         7
#     [(2, 2), (3, 0), (4, 3), (6, 7), (8, 4)],         8
#     [(1, 4), (2, 1), (7, 5), (8, 8)]                  9
# ]


# [
#     [(1, 3), (4, 8), (7, 4)],
#     [(5, 4), (6, 6)],
#     [(0, 1), (3, 8), (4, 5)],
#     [(4, 0), (7, 3)], [(1, 5), (7, 8)],
#     [(1, 0), (2, 7), (3, 4), (5, 8), (6, 1)],
#     [(0, 4), (5, 0), (8, 7)],
#     [(0, 0), (2, 2), (3, 0), (4, 3), (6, 7), (8, 4)],
#     [(1, 4), (2, 1), (7, 5), (8, 8)]
# ]


# [
#     [(1, 3), (4, 8), (7, 4)],
#     [(5, 4), (6, 6)],
#     [(0, 1), (3, 8), (4, 5)],
#     [(4, 0), (7, 3)],
#     [(1, 5), (7, 8)],
#     [(1, 0), (2, 7), (3, 4), (5, 8), (6, 1)],
#     [(0, 4), (5, 0), (8, 7)],
#     [(0, 0), (1, 1), (2, 2), (4, 3), (6, 7), (8, 4)],
#     [(1, 4), (2, 1), (7, 5), (8, 8)]
# ]

    # def row_col_helper(self, ht_row: list[tuple], row_length: int) -> list[list[int]]:
    #     for idx in range(row_length):
    #         for row in ht_row: False if row.count(row[idx]) > 1 else continue