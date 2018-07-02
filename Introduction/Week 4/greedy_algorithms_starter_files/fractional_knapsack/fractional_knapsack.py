# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    n = len(weights)
    fraction = [values[i] / weights[i] for i in range(n)]
    
    indices = sorted(range(len(fraction)), key = fraction.__getitem__, reverse = True)

    for i in indices:
        if capacity > weights[i]:
            value = value + values[i]
            capacity = capacity - weights[i]
        else :
            value = value + (capacity * fraction[i])
            capacity = capacity - capacity
    return value


if __name__ == "__main__":
    token = input().split()
    n = int(token[0])
    capacity = int(token[1])
    values = [0 for i in range(n)] 
    weights = [0 for i in range(n)]

    for i in range(n):
        token = input().split()
        values[i] = int(token[0])
        weights[i] = int(token[1])

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
