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
