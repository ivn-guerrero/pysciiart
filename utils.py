from math import floor

# unflattens an array into an m x n matrix 
def unflatten(flattened, m, n):
    unflattened = []
    for row in range(m):
        col_start_idx = row * n
        col_end_idx = row * n + n
        flattened[col_start_idx: col_end_idx]
        unflattened.append(flattened[col_start_idx: col_end_idx])
    return unflattened


# maps a matrix of pixel data into a matrix
# of brightness data (using the R, G, B pixel
# average)
def map_to_brightness_avg(pixels):
    brightness_matrix = []
    for row in pixels:
        brightness_row = []
        for col in row:
            brightness_row.append(sum(col) / 3)
        
        brightness_matrix.append(brightness_row)

    return brightness_matrix


# maps a value X in range [A, B] to a number Y
# in range [C, D]
def map_to_range(a, b, c, d, x):
    y = (x - a) / (b - a) * (d - c) + c
    return y


# maps a matrix of brightness values into a matrix
# of printable characters
def map_to_chars(
        brightnesses,
        char_map,
        min_from,
        max_from,
        min_to,
        max_to):
    char_matrix = []
    for row in brightnesses:
        char_row = []
        for col in row:
            char = char_map[
                floor(
                    map_to_range(
                        min_from, max_from, min_to, max_to, col
                    )
                )
            ]
            char_row.append(char)
        
        char_matrix.append(char_row)
    
    return char_matrix


# prints a matrix into the console
def print_ascii_art(matrix):
    for row in matrix:
        for col in row:
            print(col * 3, end='')
        print()
