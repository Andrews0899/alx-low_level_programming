#!/usr/bin/python3
""" Grid Mobule """


def island_perimeter(grid):
    """ looks for any islands inside grid and calculates it's perimeter """
    width = 0
    height = 0
    height_idx = 0
    for i in range(len(grid)):
        j = height_idx
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if grid[i][j+1] == 1:
                    width += 1
                    continue
                elif grid[i+1][j] == 1:
                    height += 1
                    height_idx = j
                    break
                else:
                    if width == 0 and grid[i][j-1] == 1:
                        j = 0
                        continue
                    width += 1
                    height += 1
                    break
    return (width + height) * 2
