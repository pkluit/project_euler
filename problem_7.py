########################################################################################################################
# Title:    problem_7.py                                                                                               #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  What is the 10 001st prime number?                                                                         #
# Last Modified; 1/30/2020                                                                                             #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

#=============================================Import Packages==========================================================#

from math import sqrt

#=============================================Define Functions=========================================================#

def is_prime(num: int):
    if any([True for x in range(2, int(1 + sqrt(num))) if num % x == 0]) == True:
        return False
    else:
        return True

def nth_prime(n: int):
    prime_cnt=0
    prime = 2
    while prime_cnt != n:
        if is_prime(prime):
            prime_cnt+=1
            if prime_cnt == n:
                break
            else:
                prime+=1
        else:
            prime+=1
    return prime

#=============================================Output Solution==========================================================#

solution = nth_prime(10001)