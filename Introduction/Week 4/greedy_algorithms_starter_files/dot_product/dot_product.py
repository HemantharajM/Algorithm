#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    token = input().split()
    n = int(token[0])
    a = input().split()
    a = [int(i) for i in a]
    b = input().split()
    b = [int(i) for i in b]

    print(max_dot_product(a, b))
    
