class Solution:
    BOARDSIZE = 9
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_rows = board
        board_columns = self.transposer(board) 
        # print(board_rows)
        # print(board_columns)
        for board_row in board_rows:
            if board_row.count('.'): break
            else: return None
        for i in range(self.BOARDSIZE): 
            if board[i].count('.') > 0: break
            else: return None
        ha = self.highest_appearance(board_rows) # getting value(s) with highest appearance
        if self.with_ha(ha):         # checking if value is worthy exploring
            for most_frequent in ha:    # getting that value
                for i in range(0, self.BOARDSIZE, 3):
                    for j in range(0, self.BOARDSIZE, 3):
                        thirds_ij = self.get_thirds(board_rows, i, j)
                        thirds_ji = self.get_thirds(board_columns, i, j)
                        thirds_end = j + 3
                        thirds_joined = []
                        for thirds_row in thirds_ij: thirds_joined += thirds_row
                        if most_frequent in thirds_joined:
                                continue
                        else:
                            row_free = self.free_indices(most_frequent, board_rows)
                            column_free = self.free_indices(most_frequent, board_columns)
                            thirds_available_col, thirds_available_row = []
                            for num in range(j, j+3):
                                if num in row_free: thirds_available_row.append(num)
                                if num in column_free: thirds_available_col.append(num)

                            available_boxes = list[tuple]
                            for available_row_index in thirds_available_row:
                                if thirds_ij[available_row_index].count('.') == 0: continue
                                for available_col_index in thirds_available_row:
                                    if thirds_ji[available_col_index].count('.') == 0: continue
                                    available_boxes.append((available_row_index, available_col_index))

                            if len(available_boxes) == 1: 
                                board[available_boxes[0]][available_boxes[1]]
                                self.solveSudoku(board)
                            else:
                                for box in available_boxes:
                                    if thirds_available_row == 1:
                                        if num_frees(board_columns[box[1]]) > (2/3)*(self.BOARDSIZE): continue
                                        else:
                                            board[box[0]][box[1]] = most_frequent
                                            self.solveSudoku(board)
                                    if thirds_available_col == 1:
                                        if num_frees(board_rows[box[1]]) > (2/3)*(self.BOARDSIZE): continue
                                        else:
                                            board[box[0]][box[1]] = most_frequent
                                            self.solveSudoku(board)
        else:
            all_nums = [i for i in range(1, self.BOARDSIZE+1)]
            for i in range(self.BOARDSIZE):
                if self.num_frees(board_rows[i]) <= (1/3)*self.BOARDSIZE:
                    for num in board_rows[i]: 
                        if num in all_nums: all_nums.remove(num)
                    for number in all_nums:
                        if len(all_nums) > 2:
                            strikes = 0
                            for x in range((i//3)*3, ((i//3)*3)+3, 3):
                                for y in range(0, self.BOARDSIZE, 3):
                                    thhirds = get_thirds(board_rows, x, y)
                                    thhirds_joined = []
                                    for k in range(3): thhirds_joined += thhirds[k]
                                    if num in thhirds_joined: 
                                        strikes += 1
                                        continue
                                    else: 
                                        affacted_col_index = board_rows[i].index('.', y, self.BOARDSIZE)
                                        if number in board_columns[affacted_col_index]:
                                            strikes += 1
                            if strikes == 2:
                                board[x][y] = number
                                self.solveSudoku(board)
                        else:
                            for x in range((i//3)*3, ((i//3)*3)+3, 3):
                                for y in range(0, self.BOARDSIZE, 3):
                                    thhirds = get_thirds(board_columns, x, y)
                                    thhirds_joined = []
                                    for k in range(3): thhirds_joined += thhirds[k]
                                    if num in thhirds_joined: continue
                                    else: 
                                        affacted_row_index = board_columns[i].index('.', y, self.BOARDSIZE)
                                        if number in board_rows[affacted_row_index]: continue
                                        else: 
                                            board[x][y] = number
                                            self.solveSudoku(board)
                if self.num_frees(board_columns[i]) <= (1/3)*self.BOARDSIZE:
                    for num in board_columns[i]: 
                        if num in all_nums: all_nums.remove(num)
                    for number in all_nums:
                        if len(all_nums) > 2:
                            strikes = 0
                            for x in range((i//3)*3, ((i//3)*3)+3, 3):
                                for y in range(0, self.BOARDSIZE, 3):
                                    thhirds = self.get_thirds(board_columns, x, y)
                                    thhirds_joined = []
                                    for k in range(3): thhirds_joined += thhirds[k]
                                    if num in thhirds_joined: 
                                        strikes += 1
                                        continue
                                    else: 
                                        affacted_row_index = board_columns[i].index('.', y, self.BOARDSIZE)
                                        if number in board_rows[affacted_row_index]:
                                            strikes += 1
                            if strikes == 2:
                                board[y][x] = number
                                self.solveSudoku(board)
                        else:
                            for x in range((i//3)*3, ((i//3)*3)+3, 3):
                                for y in range(0, self.BOARDSIZE, 3):
                                    thhirds = self.get_thirds(board_columns, x, y)
                                    thhirds_joined = []
                                    for k in range(3): thhirds_joined += thhirds[k]
                                    if num in thhirds_joined: continue
                                    else: 
                                        affacted_row_index = board_columns[i].index('.', y, self.BOARDSIZE)
                                        if number in board_rows[affacted_row_index]: continue
                                        else: 
                                            board[y][x] = number
                                            self.solveSudoku(board)

        


    def num_frees(self, board_row: list[str]):
        return board_row.count('.')

    def transposer(self, board: list[list[str]]) -> list[list[str]]:
        transposed = []
        column = []
        for i in range(self.BOARDSIZE):
            for row in board:
                column.append(row[i])
            transposed.append(column)
            column = []
        return transposed

    def free_indices(self, value: str, board: list[list[str]]) -> list[str]:
        return [i for i in rnage(self.BOARDSIZE) if not value in board[i]]

    def num_present(self, value: str, board: list[list[str]]) -> int:
        i = 0
        for row in board:
            if value in row:
                return i
            i += 1
        return 0

    def num_appearances(self, board: list[list[str]], value='.')  -> int:
        value_count = 0
        for row in board:
            if value in row: value_count += 1
        return value_count

    def highest_appearance(self, board: list[list[str]]) -> dict[str:int]:
        ha_dets = {}
        highest_appearance = self.num_appearances(board, 0)
        for i in range(1, self.BOARDSIZE):
            if self.num_appearances(board, i) > highest_appearance:
                highest_appearance = self.num_appearances(board, i)
                ha_dets[str(i)] = highest_appearance
        return ha_dets
        
    def with_ha(self, ha: dict[str:str]) -> bool:
        for value, appearance_count in ha.items():
            if appearance_count >= 5: return True
        return False

    def get_thirds(self, board: list[list[str]],x: int, y: int) -> list[list[str]]:
        thirds_row = []
        thirds = []
        for i in range(x, x+3):
            for j in range(y, y+3):
                thirds_row.append(board[i][j])
            thirds.append(thirds_row)
        return thirds
    

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
my_sol = Solution()
my_sol.solveSudoku(board)
        