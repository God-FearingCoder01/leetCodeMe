class Solution:
    BOARDSIZE = 9
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, just change thhe board in-place.
        """
        self.row_count_unfilled_spots = 0
        for row in board: 
            if row.count('.'): self.row_count_unfilled_spots += 1 
        if self.row_count_unfilled_spots == 0: return None

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
                    self.free_rows = []
                    self.free_cols = []
                    if self.x == self.y:
                        if self.highest_appearing in self.sub_grid(self.sub_board(self.board_horizontal, self.x, self.y)): continue
                        else:
                            self.free_rows = self.not_present(self.highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, self.x, self.y), self.x)
                            self.free_cols = self.not_present(self.highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, self.y, self.x), self.y)
                            # self.solveSudoku(board)
                            if len(self.free_rows) == 1 and len(self.free_cols) == 1: 
                                board[self.free_rows[0]][self.free_cols[0]] = self.highest_appearing
                                print(board)
                                
                            # else:
                            #     if self.free_rows > 1:
                            #         board[self.free_rows[0]][self.free_cols[0]] = self.highest_appearing
                            #         print(board)
                            #     has_more = self.free_rows if len(self.free_rows) > 1 else self.free_cols


                    else:
                        if not self.highest_appearing in self.sub_grid(self.sub_board(self.board_horizontal, self.x, self.y)):
                            self.free_rows = self.not_present(self.highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, self.x, self.y), self.x)
                            self.free_cols = self.not_present(self.highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, self.y, self.x), self.y)
                            if len(self.free_rows) == 1 and len(self.free_cols) == 1: 
                                board[self.free_rows[0]][self.free_cols[0]] = self.highest_appearing
                                print(board)
                            # self.solveSudoku(board)
                        if self.highest_appearing in self.sub_grid(self.sub_board(self.board_vertical, self.x, self.y)): continue
                        else:
                            self.free_rows = self.not_present(self.highest_appearing, self.board_horizontal, self.sub_board(self.board_horizontal, self.y, self.x), self.y)
                            self.free_cols = self.not_present(self.highest_appearing, self.board_vertical, self.sub_board(self.board_vertical, self.x, self.y), self.x)
                            if len(self.free_rows) == 1 and len(self.free_cols) == 1: 
                                print("Here here...")
                                board[self.free_rows[0]][self.free_cols[0]] = self.highest_appearing
                                print(board)
                            # self.solveSudoku(board)
        print("LAPHA!!!!!!!!!!!!!!!!1111")
        for self.i in range(self.BOARDSIZE):
            # print("u 'self.i' yena = ",self.i)
            # print(f"u 'given_row' ka {self.i} ngu {self.board_horizontal[self.i]}")
            self.row_available = self.missing_values(self.board_horizontal[self.i])
            # print(f"u self.row_available waka {self.i} ngu {self.row_available}")
            for self.j in range(self.BOARDSIZE):
                self.possible_cv = []
                self.current_cell = self.board_horizontal[self.i][self.j]
                if self.current_cell != '.': continue
                self.row_idx = self.i - (self.i % 3) if self.i % 3 else self.i 
                self.col_idx = self.j - (self.j % 3) if self.j % 3 else self.j
                # print("row_idx = ", self.row_idx)
                # print("col_idx = ", self.col_idx)
                for self.value in self.row_available:
                    # print(self.value in self.sub_grid(self.sub_board(self.board_horizontal,self.row_idx,self.col_idx))) 
                    if self.value in self.sub_grid(self.sub_board(self.board_horizontal,self.row_idx,self.col_idx)): continue
                    if self.value in self.board_vertical[self.j]: continue
                    self.possible_cv += self.value
                print(f"for cell [{self.i}][{self.j}], possible values are: {self.possible_cv}")
                if len(self.possible_cv) != 1: continue
                board[self.i][self.j] = self.possible_cv[0]
                print("~~~~~~~~~~~~Technique 1~~~~~~~~~~~~~~~~~~")
                print(board)
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

    # def most_populated(self, given_board: list[list[str]]) -> dict[str:int]:
    #     most_populated_row, row_index = 0, 0
    #     value_most_populated = given_board[most_populated_row].count('.')
    #     for row in given_board:
    #         if row.count('.') > value_most_populated : 
    #             value_most_populated = row.count('.')
    #             most_populated_row = row_index
    #         row_index += 1


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
my_sol = Solution()
my_sol.solveSudoku(board)