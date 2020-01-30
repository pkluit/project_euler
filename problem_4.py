########################################################################################################################
# Title:    problem_4.py                                                                                               #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  Find the largest palindrome made from the product of two 3-digit numbers.                                  #
# Last Modified; 1/29/2020                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

#=============================================Import Packages==========================================================#

from itertools import product

#=============================================Define Functions=========================================================#

def is_pdrome(num: int):
    num = str(num)
    for i in range(0,len(num)):
        if num[i] != num[-i-1]:
            return False
        else:
            pass
    return True

#=============================================Output Solution==========================================================#

mult_lst = [x*y for x,y in product(range(100,1000),range(100,1000))]

pdrome_lst = [x for x in mult_lst if is_pdrome(x)]
solution = max(pdrome_lst)