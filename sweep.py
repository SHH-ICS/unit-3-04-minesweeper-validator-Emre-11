# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invalid)
def validate( block_data ):
  # Check whether the centre block is a bomb, a number, or an invalid input
  # Skip bombs, send an error on invalid input, verify numbers

    if len(block_data) != 3 or any(len(row) != 3 for row in block_data):   
        return "invalid, grid is not 3x3"

    CenterBlock = block_data[1][1] 
    if CenterBlock == -1:
        return "invalid, the centre block is a BOMB"
    
    bombcount = 0
    for r in range (3):
        for c in range (3): 
            if block_data[r][c] == -1:
                bombcount = bombcount+1

    if bombcount != CenterBlock:
         return("invalid, Bomb count does not match centre block value")

    if CenterBlock == 0:  
        return "valid, no bombs insight"

    return "valid, centre block value matches bomb count"
grid = [
  [-1,1,0],
  [1,1,0],
  [0,0,0]
]
print (validate(grid))
