class Solution:
    BOARDSIZE = 9
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, just change thhe board in-place.
        """
        self.board_horizontal = board
        # print(self.board_horizontal)
        self.board_vertical = self.transposed(board)
        # print(self.board_vertical)
        # print(self.most_appearing(self.board_horizontal))
        for self.highest_appearing in self.most_appearing(self.board_horizontal):
            print(self.highest_appearing)
            for self.x in range(0, self.BOARDSIZE, 3): 
                for self.y in range(0+(self.x), self.BOARDSIZE, 3):
                    print(f"self.x = {self.x} and self.y = {self.y}")
                    print("'self.x == self.y' is ", self.x == self.y)
                    if self.x == self.y:
                        if self.highest_appearing in self.sub_grid(self.sub_board(self.board_horizontal, self.x, self.y)): continue
                        else:
                            self.free_rows = self.not_present(self.highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, self.x, self.y), self.x)
                            self.free_cols = self.not_present(self.highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, self.y, self.x), self.y)
                            if len(self.free_rows) == 1 and len(self.free_cols) == 1: 
                                board[self.free_rows[0]][self.free_cols[0]] = self.highest_appearing
                                print(board)
                    else:
                        if not self.highest_appearing in self.sub_grid(self.sub_board(self.board_horizontal, self.x, self.y)):
                            self.free_rows = self.not_present(self.highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, self.x, self.y), self.x)
                            self.free_cols = self.not_present(self.highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, self.y, self.x), self.y)
                            if len(self.free_rows) == 1 and len(self.free_cols) == 1: 
                                board[self.free_rows[0]][self.free_cols[0]] = self.highest_appearing
                                print(board)
                        if self.highest_appearing in self.sub_grid(self.sub_board(self.board_vertical, self.x, self.y)): continue
                        else:
                            self.free_rows = self.not_present(self.highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, self.y, self.x), self.y)
                            self.free_cols = self.not_present(self.highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, self.x, self.y), self.x)
                            if len(self.free_rows) == 1 and len(self.free_cols) == 1: 
                                board[self.free_rows[0]][self.free_cols[0]] = self.highest_appearing
                                print(board)


    def transposed(self, given_board: list[list[str]]) -> list[list[str]]:
        col = []
        transposed_board = []
        for i in range(self.BOARDSIZE):
            for row in given_board: col.append(row[i])
            transposed_board.append(col)
            col = []
        return transposed_board

    def most_appearing(self, given_board: list[list[str]]) -> list[str]:
        i_count = 0
        ma_list = []
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
        vacant_rows = []
        # for row in given_board:
        #     if value in row: continue
        #     else: break
        print("Your current thirds is: ")
        print(given_sb)
        print(f"value for 'value' is {value}")
        sb_index = 0
        for i in range(idx, idx+3):
            print(f"i value= {i}")
            if value in given_board[i]: 
                sb_index += 1
                continue
            else:
                if given_sb[sb_index].count('.'): vacant_rows.append(i)
                sb_index += 1
        print(f"Num vacant rows is {len(vacant_rows)}, where those vacant rows are:")
        print(vacant_rows)
        return vacant_rows

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
my_sol = Solution()
my_sol.solveSudoku(board)