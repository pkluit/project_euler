########################################################################################################################
# Title:    problem_2.py                                                                                               #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  By considering the terms in the Fibonacci sequence whose values do not exceed four million,                #
#           find the sum of the even-valued terms.                                                                     #
# Last Modified; 1/28/2020                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

# Define functions

# Returns even valeus from list
def even_vals(lst):
    return [x for x in lst if x%2==0]

# Builds fibonnaci sequence from [1,2] to  a specific limit
def fib_lst(limit):
    fib = [1,2]
    [fib.append(x+fib[ind-1]) for ind,x in enumerate(fib) if ind > 0 and x+fib[ind-1]<=limit]
    return fib

# Output solution
solution = sum(even_vals(fib_lst(4000000)))