# Uses python3
import sys

def gcd_fast(a, b):
    val = [a,b]
    val.sort()

    a = val[1]
    b = val[0]

    if b == 0:
        return a
    else:
        return gcd_fast(a % b, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_fast(a, b))
