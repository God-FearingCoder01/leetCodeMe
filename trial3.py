class Solution:
    BOARDSIZE = 9
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, just change thhe board in-place.
        """

        uncomplete_rows = 0
        for row in board: 
            if row.count('.'): uncomplete_rows += 1 
        if uncomplete_rows == 0: return None

        self.board_horizontal = board
        self.board_vertical = self.transposed(board)

        for highest_appearing in self.most_appearing(self.board_horizontal):
            for x in range(0, self.BOARDSIZE, 3): 
                for y in range(0+(x), self.BOARDSIZE, 3):
                    free_rows, free_cols = [], []
                    if x == y:
                        if highest_appearing in self.sub_grid(self.sub_board(self.board_horizontal, x, y)): continue
                        else:
                            free_rows = self.not_present(highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, x, y), x)
                            free_cols = self.not_present(highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, y, x), y)
                            if len(free_rows) == 1 and len(free_cols) == 1: 
                                board[free_rows[0]][free_cols[0]] = highest_appearing
                                # print(board)
                    else:
                        if not highest_appearing in self.sub_grid(self.sub_board(self.board_horizontal, x, y)):
                            free_rows = self.not_present(highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, x, y), x)
                            free_cols = self.not_present(highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, y, x), y)
                            if len(free_rows) == 1 and len(free_cols) == 1: 
                                board[free_rows[0]][free_cols[0]] = highest_appearing
                                # print(board)
                        if highest_appearing in self.sub_grid(self.sub_board(self.board_vertical, x, y)): continue
                        else:
                            free_rows = self.not_present(highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, y, x), y)
                            free_cols = self.not_present(highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, x, y), x)
                            if len(free_rows) == 1 and len(free_cols) == 1: 
                                board[free_rows[0]][free_cols[0]] = highest_appearing
                                # print(board)

        for i in range(self.BOARDSIZE):
            row_available = self.missing_values(self.board_horizontal[i])
            for j in range(self.BOARDSIZE):
                possible_cv = []
                current_cell = self.board_horizontal[i][j]
                if current_cell != '.': continue
                row_idx = i - (i % 3) if i % 3 else i 
                col_idx = j - (j % 3) if j % 3 else j
                for value in row_available:
                    if value in self.sub_grid(self.sub_board(self.board_horizontal, row_idx, col_idx)): continue
                    if value in self.board_vertical[j]: continue
                    possible_cv += value
                if len(possible_cv) != 1: continue
                board[i][j] = possible_cv[0]
                # print(board)
        self.solveSudoku(board)


    def missing_values(self, given_row: list[str]) -> list[str]:
        return [str(i) for i in range(1, self.BOARDSIZE+1) if not str(i) in given_row]


    def transposed(self, given_board: list[list[str]]) -> list[list[str]]:
        col = []
        transposed_board = []
        for i in range(self.BOARDSIZE):
            for row in given_board: col.append(row[i])
            transposed_board.append(col)
            col = []
        return transposed_board

    def most_appearing(self, given_board: list[list[str]]) -> list[str]:
        i_count, ma_list = 0, []
        for i in range(1, (self.BOARDSIZE+1)):
            for row in given_board:
                if row.count(str(i)): i_count += 1
            if i_count >= 5: ma_list.append(str(str(i)))
            i_count = 0
        return ma_list

    def sub_board(self, given_board: list[list[str]], row_idx: int, col_idx: int) -> list[list[str]]:
        sb_row = []
        sb = []
        for x in range(row_idx, row_idx+3):
            for y in range(col_idx, col_idx+3): sb_row.append(given_board[x][y])
            sb.append(sb_row)
            sb_row = []
        return sb

    def sub_grid(self, given_board: list[list[str]]) -> list[str]:
        sg_list = []
        for row in given_board:
            sg_list += row
        return sg_list
    
    def not_present(self, value: str, given_board: list[list[str]], given_sb: list[list[str]], idx: int) -> list[str]:
        vacant_rows, sb_index = [], 0
        for i in range(idx, idx+3):
            if value in given_board[i]: 
                sb_index += 1
                continue
            else:
                if given_sb[sb_index].count('.'): vacant_rows.append(i)
                sb_index += 1
        return vacant_rows

# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
my_sol = Solution()
my_sol.solveSudoku(board)