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








    # Initial Approach which scores a 6ms Runtime and 19.4MB in memory
    
    # def isValidSudoku(self, board: list[list[str]]) -> bool:
        # self.board_horizontal = board
        # self.board_vertical = self.transpose(board)
        # self.sub_boxes = self.get_sb(board)
        # return self.check_validity(self.board_horizontal) and self.check_validity(self.board_vertical) and self.check_validity(self.sub_boxes)  

    # def transpose(self, given_board: list[list[str]]) -> list[list[str]]:
    #     transposed_row = []
    #     transposed_board = []
    #     for i in range(Solution.BOARDSIZE):
    #         for row in given_board:
    #             transposed_row.append(row[i])
    #         transposed_board.append(transposed_row)
    #         transposed_row = []
    #     return transposed_board
        
    # def get_sb(self, given_board: list[list[str]]) -> list[list[str]]:
    #     sb_row = []
    #     sb = []
    #     for sb_row_idx in range(0, Solution.BOARDSIZE, 3):
    #         for sb_col_idx in range(0, Solution.BOARDSIZE, 3):
    #             for row_idx in range(sb_row_idx, (sb_row_idx+3)):
    #                 for col_idx in range(sb_col_idx, (sb_col_idx+3)):
    #                     sb_row.append(given_board[row_idx][col_idx])
    #             sb.append(sb_row)
    #             sb_row = []
    #     return sb

    # def check_validity(self, given_board: list[list[str]]) -> bool:
    #     for row in given_board:
    #         for cell_idx in range(Solution.BOARDSIZE):
    #             if row[cell_idx] != '.':
    #                 if row.count(row[cell_idx]) > 1: return False
    #     return True

"""
Corrections
- there are two things that are currently tempering with the space and time complexity of this solution
    1. Code is doing a double job (which could be avoided), when first building the arrays for columns and sub-boxes, and then going through them to after, to check for any duplicates. 
    2. Code for creating the sub-boxes array, is using too many loops (which can reduced and still be able to achieve the same result)
"""

"""
New Approach
 - Create a way to validate the board in a single pass without having to create separate transpoed or sub-box arrays
 - Learn about Hash Table (as your current approach is saying Array, Simulation and Enumeration)
"""

"""
hash_table = board ==> [rows]       len(hash_table) = 9     index_value = row_count-1
buckets := container values in a hash table
0 - 18
[0][0] = 5

[2][3] [3][2]
def hash_functio(row) -> hash_code:
    
"""