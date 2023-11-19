# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invalid)
def validate(block_data):
    # Check whether the center block is a bomb, a number, or an invalid input
    # Skip bombs, send an error on invalid input, verify numbers

    if len(block_data) != 3 or any(len(row) != 3 for row in block_data):
        return "invalid, grid is not 3x3"

    center_block = block_data[1][1]
    bomb_count = 0

    for r in range(3):
        for c in range(3):
            if block_data[r][c] == -1:
                bomb_count += 1

    if center_block == -1:
        return "invalid, the center block is a BOMB"
    elif center_block == 0:
        return "valid, no bombs in sight"
    elif center_block == 1:
        if bomb_count == 1:
            return "valid, 1 bomb in the area"
        else:
            return "invalid, bomb count does not match the center block"
    else:
        return "invalid, center block is neither 0 nor 1"


grid = [
    [-1, 1, 0],
    [1,1, 0],
    [0, 0, 0]
]

print(validate(grid))
