#!/usr/bin/env python

lower_limit = int(input("Enter the lower limit"))
upper_limit = int(input("Enter the upper limit"))

for i in range(lower_limit, upper_limit):
    if (i % 2 != 0):
        # TODO: Make it user friendly, print odd numbers are: i
        print(i)

#other TODO: 1) Print statements if there is no numbers to print.
#            2) Test if user left the lower_limit or upper_limit empty.
