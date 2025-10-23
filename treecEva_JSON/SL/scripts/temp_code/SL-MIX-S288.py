def modified_tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b, c = 0, 1, 1
        for i in range(3, n+1):
            next_val = a + b + c + (i-3 ^ i-2 ^ i-1)
            a, b, c = b, c, next_val
        return c

from functools import reduce
import operator

def calculate_efficiency_score(n):
    tribonacci_values = [modified_tribonacci(i) for i in range(n+1)]
    even_index_values = [tribonacci_values[i] for i in range(0, n+1, 2)]
    product = reduce(operator.mul, even_index_values, 1)
    return product % 997

# Main execution
n = 11
efficiency_score = calculate_efficiency_score(n)
print(f"Result: {efficiency_score}")