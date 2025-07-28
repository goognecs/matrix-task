# import numpy as np
import copy

def read_matrix(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip().split(','))) for line in f.readlines()]

def min_path_sum(grid):
    rlen=len(grid)
    clen=len(grid[0])
    original_grid = copy.deepcopy(grid)

    for i in range(1, clen):
        grid[0][i]+=grid[0][i - 1]

    for j in range(1, rlen):
        grid[j][0]+=grid[j - 1][0]

    for j in range(1, rlen):
        for i in range(1, clen):
            grid[j][i]+=min(grid[j - 1][i], grid[j][i - 1])
    # return = grid[rlen - 1][clen - 1]

# Get the path
    path_coords=[]
    r, c=rlen - 1, clen - 1
    while r > 0 or c > 0:
        path_coords.append((r, c))
        if r == 0:
            c-=1
        elif c == 0:
            r-=1
        else:
            if grid[r - 1][c] < grid[r][c - 1]:
                r-=1
            else:
                c-=1

    path_coords.append((0, 0))
    path_coords.reverse()

    # value pf minimum path
    path_values=[original_grid[r][c] for r, c in path_coords]

    return grid[rlen - 1][clen - 1], path_values


if __name__ == "__main__":
    matrix=read_matrix("matrix.txt")
    min_sum, path_vals=min_path_sum(matrix)
    print("Minimum Path Sum:", min_sum)
    print("Path of Minimum Sum:\n " + " -> ".join(map(str, path_vals)))
