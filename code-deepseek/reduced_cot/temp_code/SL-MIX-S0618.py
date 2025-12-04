def calculate_even_squares(n):
    # Calculate squares of even numbers up to n
    even_numbers = [x for x in range(n) if x % 2 == 0]
    squares = [num**2 for num in even_numbers]
    total_sum = sum(squares)
    print(f"Result: {total_sum}")
    return total_sum

# Main execution
limit = 8
result = calculate_even_squares(limit)
print(f"Target result: {result}")