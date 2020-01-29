########################################################################################################################
# Title:    problem_1.py                                                                                                  #
# Purpose:  The purpose of this script is to solve the following problem                                                #
# Problem:  Find the sum of all the multiples of 3 or 5 below 1000.                                                     #
# Last Modified; 1/28/2020                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################


# Define functions
def sum_multiples(range_lst,val_lst):
    multiples = []
    [multiples.append(r) for r in range_lst for v in val_lst if r%v==0 and r not in multiples]
    return sum(multiples)

# output solution
solution = sum_multiples(list(range(1,1000)),[3,5])