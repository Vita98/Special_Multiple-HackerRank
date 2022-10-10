#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    # Write your code here
    queue = [9]
    
    while True:
        x = queue.pop(0)
        
        if x % n == 0:
            return str(x)
        
        queue.append(x*10)
        queue.append(x*10+9)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
