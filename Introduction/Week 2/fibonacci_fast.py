n = int(input())

def fibonacci_fast(n):
	
    arr = [0,1]

    for i in range(2,n+1):
        arr.append(arr[i-1] + arr[i-2])

    return arr[n]


print(fibonacci_fast(n))
