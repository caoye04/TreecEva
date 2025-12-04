def count_combinations(n, r):
    # Calculate factorial using iterative approach
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    
    # Simple combination formula: nCr = n! / (r! * (n-r)!)
    if r < 0 or r > n:
        return 0
    
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    combinations = numerator // denominator
    
    # Additional check for valid combination count
    validation_check = combinations > 0
    
    return combinations

# Main execution
final_count = count_combinations(3, 2)
print(f"Result: {final_count}")