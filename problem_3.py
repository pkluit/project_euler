########################################################################################################################
# Title:    problem_3.py                                                                                               #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  What is the largest prime factor of the number 600851475143 ?                                              #
# Last Modified; 1/28/2020                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

# Import Packages
from math import sqrt

# Define Functions

# outputs list of factors of a number
def lst_factors(num: int):
    lst = list(range(1,int(sqrt(num))))
    return [x for x in lst if num%x==0]


# determines the primality of a number
def is_prime(num: int):
    if any([True for x in range(2, int(1 + sqrt(num))) if num % x == 0]) == True:
        return False
    else:
        return True

limit = 600851475143
primes = [x for x in lst_factors(limit) if is_prime(x)==True]
solution = max(primes)