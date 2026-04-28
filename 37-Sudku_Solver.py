BOARD_SIZE = 9
board_at_the_start = [
    [5,3,'.', '.', 7, '.', '.', '.', '.'],
    [6,'.','.', 1, 9, 5, '.', '.', '.'],
    ['.',9, 8, '.', '.', '.', '.', 6, '.'],
    [8,'.','.', '.', 6, '.', '.', '.', 3],
    [4,'.','.', 8, '.', 3, '.', '.', 1],
    [7,'.','.', '.', 2, '.', '.', '.', 6],
    ['.',6,'.', '.', '.', '.', 2, 8, '.'],
    ['.','.','.', 4, 1, 9, '.', '.', 5],
    ['.','.','.', '.', 8, '.', '.', 7, 9],
]
print("Board before transposing\n")
print(board_at_the_start)

def transpose(board: list):
    new_row = []
    new_board = []
    
    for i in range(len(board)):
        for row in board:
            new_row.append(row[i])
        new_board.append(new_row)
        new_row = []
    return new_board

def most_filled(board, fill_value = '.'):
    lowest_row_board_count = len(board)
    row_board_count = len(board)
    for row_index in range(row_board_count):
        current_row_board_count = board[row_index].count(fill_value)
        # print(board_count)
        if current_row_board_count < lowest_row_board_count : 
            lowest_row_board_count = current_row_board_count
            most_filled_row_index = row_index
    return {most_filled_row_index: (row_board_count - lowest_row_board_count)}

def get_proposed_fill(most_filled_row, most_filled_column):
    if list(most_filled_row.items())[0][1] > list(most_filled_column.items())[0][1] : return most_filled_row
    elif list(most_filled_row.items())[0][1] < list(most_filled_column.items())[0][1] : return most_filled_column
    else: return None 

def qualifies(proposed_fill, board_size):
    if list(proposed_fill.items())[0][1] > (1/3 * board_size): return True
    else: False

print("After transposing")
transposed_board = transpose(board_at_the_start)
print(transposed_board)

print("row with the highest fillings")
most_filled_row = most_filled(board_at_the_start)
print(most_filled_row)

print("col with the highest fillings")
most_filled_column = most_filled(transposed_board)
print(most_filled_column)

print("proposed fill: ")
proposed_fill = get_proposed_fill(most_filled_row, most_filled_column)
print(proposed_fill)

print("proposed fill qualify ?")
proposed_fill_qualify = qualifies(proposed_fill, len(board_at_the_start))
print(proposed_fill_qualify)

def count_fillings(board, filling_value: int):
    num_fillings = 0
    for row in board:
        if row.count(filling_value): num_fillings += 1
    return num_fillings


most_appearing = [count_fillings(board_at_the_start, i) for i in range(1, BOARD_SIZE)]

for i in range(BOARD_SIZE):
    print(f"{i+1} appears {count_fillings(board_at_the_start, (i+1))} times in board rows")

print("================================================================================================")

for i in range(BOARD_SIZE):
    print(f"{i+1} appears {count_fillings(transposed_board, (i+1))} times in board columns")


rows = board_at_the_start
columns = transposed_board

def get_eights(x, y):
    eights = []
    for i in range(x, x+3):
        for j in range(y, y+3):
            eights.append(board_at_the_start[i][j])
    return eights



print(get_eights(3, 0))

if 2 in get_eights(3, 0):
    print("Ngikhonaaa!")
else:
    print("Angikhoooo")


print("most appearing is ")

print(most_appearing)

