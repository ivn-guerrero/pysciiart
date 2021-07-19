def unflatten(flattened, rows, col_size):
    unflattened = []
    for row in range(rows):
        row_start_idx = row * col_size
        row_end_idx = row * col_size + col_size
        flattened[row_start_idx: row_end_idx]
        unflattened.append(flattened[row_start_idx: row_end_idx])
    return unflattened
