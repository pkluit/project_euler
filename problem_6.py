########################################################################################################################
# Title:    problem_6.py                                                                                               #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  Find the difference between the sum of the squares of the first one hundred natural numbers                #
#           and the square of the sum.                                                                                 #
# Last Modified; 1/29/2020                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

#=============================================Import Packages==========================================================#
from itertools import product
#=============================================Define Functions=========================================================#

#=============================================Output Solution==========================================================#

A = B = list(range(1,101))
solution=sum([x*y for x,y in product(A,B) if x!=y])