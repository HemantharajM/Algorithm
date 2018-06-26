n = int(input())

def fibonacci_slow(n):

	if n <= 1:
		return n
	else :
		return fibonacci_slow(n-1) + fibonacci_slow(n-2)


print(fibonacci_slow(n))
