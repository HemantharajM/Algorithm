# Uses python3
import sys

def get_change(m):
    #write your code here
    coin = [10, 5,1]
    count = 0

    for i in coin:
        if m > i:
            count = count + (m // i)
            m = m - (m // i) * i

    return count 

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
