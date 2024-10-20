from collections import deque                           # To avoid namespace cramming, imported just deque

print("Enter number of rows and columns for the grid")	# Input from user
M, N = map(int, input().split())                        # "map" iteration object 

print("\nEnter boolean integers for grid")              # Takes N input for each line within M lines
grid = [list(map(int, input().split())) for _ in range(M)]

print("\nEnter source cell coordinates")
src = list(map(int, input().split()))                   # Source cell

print("\nEnter destination cell coordinates")
dest = list(map(int, input().split()))

print("\nEnter move_rule")                              # Destination cell
move_rule = list(map(int, input().split()))

def min_move(M, N, grid, src, dest, move_rule):         # Row, Column, 2D Array, Source, Destination, Move Rule
    dir_x = move_rule[0]                                # Direction of x based on the move rule
    dir_y = move_rule[1]                                # Direction of y based on the move rule
    
    direction = [
        (dir_x, dir_y),                                 # Forward
        (dir_y, -dir_x),                                # Right (90 Clockwise)
        (-dir_y, dir_x),                                # Left (90 Anticlockwise)
        (-dir_x, -dir_y)                                # Backward
    ]
    
    queue = deque()                                     # BFS initialization
    queue.append((src[0], src[1], 0))                   # "Visited" function avoids redundancy
    visited = set()
    visited.add((src[0], src[1]))
    
    while queue:                                        # BFS loop until "queue" is completed
        x, y, moves = queue.popleft()
        
        if (x, y) == (dest[0], dest[1]):                # Terminates if destination is reached, else continues
            return moves
        
        for dir_x, dir_y in direction:                  # Trial and error of every direction to find shortest path
            new_x = x + dir_x                           
            new_y = y + dir_y

                            # Validity of new position using "if" condition                                         
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))             
                queue.append((new_x, new_y, moves + 1))
    
    print("\nDestination Unreachable")                  # Display error to show destination is unreachable
    return -1                                           # If queue exhausts before reaching destination
                
result = min_move(M, N, grid, src, dest, move_rule)     # Calculate minimum moves
print("\nNumber of minimum moves:")                     # "\n" newline character for formatting
print(result)