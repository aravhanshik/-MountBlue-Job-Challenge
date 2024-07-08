#Sales by Match
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    d=dict()
    for i in ar:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    c=0
    for i in d:
        if d[i]==1:
            continue
        elif d[i]%2==0:
            c+=d[i]
        else:
            c=c+(d[i]-1)
    return int(c/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
