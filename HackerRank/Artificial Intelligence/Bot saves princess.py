def displayPathtoPrincess(n, grid):
    # print all the moves here
    p_pos = []
    b_pos = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] == "p":
                p_pos = [row, col]
            if grid[row][col] == "m":
                b_pos = [row, col]
    print_steps(p_pos, b_pos)


def print_steps(p_pos, b_pos):
    steps = []
    col_steps = p_pos[0] - b_pos[0]
    row_steps = p_pos[1] - b_pos[1]
    col_dir, row_dir = get_direction(col_steps, row_steps)
    for col in range(col_steps):
        print(col_dir)
    for row in range(row_steps):
        print(row_dir)


def get_direction(col_steps, row_steps):
    if row_steps < 0:
        row_dir = "LEFT"
    else:
        row_dir = "RIGHT"

    if col_steps < 0:
        col_dir = "UP"
    else:
        col_dir = "DOWN"
    return col_dir, row_dir


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)