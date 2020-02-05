########################################################################################################################
# Title:    problem_9.py                                                                                               #
# Purpose:  The purpose of this script is to solve the following problem                                               #
# Problem:  There exists exactly one Pythagorean triplet for which a + b + c = 1000.                                  #
#           Find the product abc.                                                                         #
# Last Modified; 2/4/2020                                                                                              #
# Property of: Paul Kluitenberg                                                                                        #
########################################################################################################################

#=============================================Import Packages==========================================================#



#=============================================Define Functions=========================================================#

def criteria_met(a: int,b: int, c: int, sum: int):
    if ((a+b+c)==sum) and (a < b < c) and ((a**2+b**2)==c**2):
        return True
    else:
        return False

#=============================================Output Solution==========================================================#

SUM = 1000
val_range = range(0,SUM+1)
lst=[[a,b,c,a*b*c] for a in val_range for b in val_range for c in val_range if criteria_met(a,b,c,SUM)]
solution = lst[3]