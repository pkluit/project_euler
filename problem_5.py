########################################################################################################################
# Title:    problem_5.py                                                                                               #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?          #
# Last Modified; 1/29/2020                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

#=============================================Import Packages==========================================================#

#=============================================Define Functions=========================================================#

def is_divisible(num: int, div_lst: list):
    return all([True if num%x == 0 else False for x in div_lst]) == True

#=============================================Output Solution==========================================================#

div_lst = list(range(1,21))
step = test_val = max(div_lst)
while True:
    if is_divisible(test_val,div_lst):
        break
    else:
        test_val += step

solution = test_val