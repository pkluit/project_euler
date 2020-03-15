########################################################################################################################
# Title:    problem_10.py                                                                                              #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  What is the greatest product of four adjacent numbers in the same direction (up, down, left, right,        #
#           or diagonally) in the 20×20 grid?                                                                          #
# Last Modified; 2/4/2020                                                                                              #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

#=============================================Import Packages==========================================================#

import numpy as np

#=============================================Define Functions=========================================================#



#=============================================Output Solution==========================================================#

grid = np.loadtxt(open("/repos/project_euler/problem_11_grid.csv", "rb"), delimiter=",", skiprows=0)
search_len = 4
max_prod = [0]
for i in range(0,len(grid)):
    for j in range(0,len(grid[0])):
        # right
        r = [grid[i][x] for x in range(j, j + search_len)]
        print(r)
        max_prod.append(r)

        # down right
        dr = [grid[y][x] for x in range(j, j + search_len) for y in range(i, i + search_len)]
        print(dr)
        max_prod.append(dr)

        # down
        d = [grid[x][j] for x in range(i, i + search_len)]
        print(d)
        max_prod.append(d)

        # down left
        dl = [grid[y][x] for x in range(j - search_len + 1, j + 1) for y in range(i, i + search_len)]
        print(dl)
        max_prod.append(dl)

        # left
        l = [grid[i][x] for x in range(j - search_len+1,j + 1)]
        print(l)
        max_prod.append(l)

        # up left
        ul = [grid[y][x] for x in range(j - search_len+1,j + 1) for y in range(i - search_len +1,i + 1)]
        print(ul)
        max_prod.append(ul)

        # up
        u = [grid[x][j] for x in range(i - search_len +1,i + 1)]
        print(u)
        u = max_prod.append(u)

        # up right
        ur = [grid[y][x] for x in range(j, j + search_len) for y in range(i - search_len +1,i + 1) ]
        print(ur)
        max_prod.append(ur)

        # find max product
        max_prod = [max(max_prod)]