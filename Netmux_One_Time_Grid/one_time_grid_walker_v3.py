#!/usr/bin/env python3

# Including this to print error message if python < 3.0 is used
from __future__ import print_function
import sys
# Check for python3 and error out if not
if sys.version_info[0] < 3:
    print("This program requires Python 3.x", file=sys.stderr)
    sys.exit(1)


# The length of the one time grid
GRID_LEN = 7

# Max lengt of a run
MAX_RUN_LEN = 14

# Minimum length of a run
MIN_RUN_LEN = 1
        
## Sets up the grid to generate walks from        
def setup_grid():

    # generate the blank array
    one_time_grid = []
    
    # the plaintext values to add in the grid
    #
    # yes, I know I could make this more general, but *shrug*
    row1="IA9GVwc"
    row2="8oyIL$L"
    row3=")M.!q03"
    row4="WKHG8o+"
    row5="e+p+P?*"
    row6="+p{.$Tx"
    row7="Jz3hb.u"
    
    one_time_grid.append(list(row1))
    one_time_grid.append(list(row2))
    one_time_grid.append(list(row3))
    one_time_grid.append(list(row4))
    one_time_grid.append(list(row5))
    one_time_grid.append(list(row6))
    one_time_grid.append(list(row7))
    
    return one_time_grid
 
 
# Doing it recursively 
def walk_grid(one_time_grid, walk, heading = None, bend = None):

    ## Uncomment the line below to remove the requirement that there can only below
    #  one bend in a walk for the gird
    #bend = None
    x = walk[-1][0]
    y = walk[-1][1]
    #if it is a valid walk to the end, print results
    if len(walk) >= MIN_RUN_LEN:
        if x == 0 or x == GRID_LEN-1 or y == 0 or y == GRID_LEN-1:
            guess = ""
            for step in walk:
                guess += one_time_grid[step[0]][step[1]]
                print(one_time_grid[step[0]][step[1]], end='')
            print()
    
    # Make sure the run is not too long
    if len(walk) <  MAX_RUN_LEN:   
        # Check up
        if heading in [None,"up"] or bend == None:
            if x != 0 and (x-1,y) not in walk:
                walk.append((x-1,y))
                if heading and heading != "up":
                    bend = True
                walk_grid(one_time_grid, walk, heading= "up", bend = bend)
                del walk[-1]

        # Check up/right
        if heading in [None,"up/right"] or bend == None:
            if x != 0 and y != GRID_LEN-1 and (x-1,y+1) not in walk:
                walk.append((x-1,y+1))
                if heading and heading != "up/right":
                    bend = True
                walk_grid(one_time_grid, walk, heading= "up/right", bend = bend)
                del walk[-1]
            
        # Check right
        if heading in [None,"right"] or bend == None:
            if y != GRID_LEN-1 and (x,y+1) not in walk:
                walk.append((x,y+1))
                if heading and heading != "right":
                    bend = True
                walk_grid(one_time_grid, walk,heading= "right", bend = bend)
                del walk[-1]
            
        # Check down/right
        if heading in [None,"down/right"] or bend == None:
            if x != GRID_LEN-1 and y != GRID_LEN-1 and (x+1,y+1) not in walk:
                walk.append((x+1,y+1))
                if heading and heading != "down/right":
                    bend = True
                walk_grid(one_time_grid, walk,heading= "down/right", bend = bend)
                del walk[-1]
            
        # Check down
        if heading in [None,"down"] or bend == None:
            if x != GRID_LEN-1 and (x+1,y) not in walk:
                walk.append((x+1,y))
                if heading and heading != "down":
                    bend = True
                walk_grid(one_time_grid, walk, heading= "down", bend = bend)
                del walk[-1]
            
        # Check down/left
        if heading in [None,"down/left"] or bend == None:
            if x != GRID_LEN-1 and y != 0 and (x+1,y-1) not in walk:
                walk.append((x+1,y-1))
                if heading and heading != "down/left":
                    bend = True
                walk_grid(one_time_grid, walk, heading= "down/left", bend = bend)
                del walk[-1] 

        # Check left
        if heading in [None,"left"] or bend == None:
            if y != 0 and (x,y-1) not in walk:
                walk.append((x,y-1))
                if heading and heading != "left":
                    bend = True
                walk_grid(one_time_grid, walk, heading= "left", bend = bend)
                del walk[-1]
            
        # Check up/left
        if heading in [None,"up/left"] or bend == None:
            if x != 0 and y != 0 and (x-1,y-1) not in walk:
                walk.append((x-1,y-1))
                if heading and heading != "up/left":
                    bend = True
                walk_grid(one_time_grid, walk, heading= "up/left", bend = bend)
                del walk[-1]
 
## Start walks on the edge of a grid 
def start_point(one_time_grid):

    # Walks start on edge, try top
    for x in range(0,GRID_LEN):
        walk = [(0,x)]
        walk_grid(one_time_grid,walk)
        
    # Walks start on edge, try bottom
    for x in range(0,GRID_LEN):
        walk = [(GRID_LEN-1, x)]
        walk_grid(one_time_grid,walk)    
   
    # Walks start on edge, try left
    for x in range(1,GRID_LEN-1):
        walk = [(x,0)]
        walk_grid(one_time_grid,walk)
        
    # Walks start on edge, try right
    for x in range(1,GRID_LEN-1):
        walk = [(x,GRID_LEN-1)]
        walk_grid(one_time_grid,walk)
 
 
def main():
    one_time_grid = setup_grid()
    start_point(one_time_grid)
    
     
if __name__ == "__main__":
    main()