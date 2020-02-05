########################################################################################################################
# Title:    problem_10.py                                                                                              #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  Find the sum of all the primes below two million.                                                          #
# Last Modified; 2/4/2020                                                                                              #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

#=============================================Import Packages==========================================================#

from problem_3 import is_prime

#=============================================Define Functions=========================================================#



#=============================================Output Solution==========================================================#

limit = 2000000
prime_lst = [2]
val_range = range(3,limit,2)
[prime_lst.append(x) for x in val_range if is_prime(x)]
solution = sum(prime_lst)
print(solution)