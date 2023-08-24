#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    
    Args:
    grid (list[list[int]]): The grid representing the island.
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:  # If it's land
                perimeter += 4  # Add the base perimeter
                
                # Check adjacent cells and subtract if they are land
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    
    return perimeter
