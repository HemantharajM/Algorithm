# Uses python3
import sys

def get_fibonacci_huge_fast(n, m):
    
    token = 0
    fib_arr = [0,1]
    arr = [0, 1]

    count = 2
    while token == 0:

        val = fib_arr[count -1] + fib_arr[count -2]
        fib_arr.append(val)
        arr.append(val % m)

        l = len(arr)
        mid = l // 2
        count = count + 1
        if l % 2 != 0:
            continue

        for i in range(mid):
            if arr[i] == arr[mid+i]:
                pass
            else :
                break

        if i == mid -1:
            token = 1

    val = n % (len(arr) // 2) 

    return arr[val]




if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_fast(n, m))
