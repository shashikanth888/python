#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    ans = ''
    i=1
    length=1
    while(2**i<n):
        i+=1
        length+=1
        print(2**i, length)
    maxi=0
    res=0

    for j in range(length-1, -1, -1):
        # print(n//(2**j))
        if (n//(2**j))>0:
            n = n%(2**j)
            ans+='1'
            #print(ans)
            maxi+=1
            if(maxi>res):
                res=maxi
        else:
            maxi=0
            ans+='0'
            #print(ans)
    print(ans)
    print(res)