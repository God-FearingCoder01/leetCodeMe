class Solution:
    BOARDSIZE = 9
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_rows = board
        board_columns = transposer(board) 
        if with_ha(highest_appearance(board_rows)):
            

    def transposer(self, board: list[list[str]]) -> list[str]:
        transposed, column = [], column
        for i in range(BOARDSIZE):
            for row in board:
                column.append(row[i])
            transposed.append(column)
            column.clear()
        return transposed

    def num_appearances(self, value: str, board: list[list[str]])  -> int:
        value_count = 0
        for row in board:
            if value in row: value_count += 1
        return value_count

    def highest_appearance(self, board: list[list[str]]) -> dict[str:str]:
        ha_dets = {}
        highest_appearance = num(i, board)
        for i in range(1, BOARDSIZE):
            if self.num_appearance(i, board) > highest_appearance:
                highest_appearance = num_appearance
                ha_dets[i] = highest_appearance
        return ha_dets
        
    def with_ha(self, ha: dict[str:str]) -> bool:
        for value, appearance_count in ha:
            if appearance_count >= 5: return True
        return False

    def get_thirds(self, board: list[str],x: int, y: int) -> list[str]:
        thirds = []
        for i in range(x, x+3):
            for j in range(y, y+3):
                thirds.apppend(board[i][j])
        return thirds
    
        