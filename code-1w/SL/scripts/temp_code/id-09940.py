def compute_filtered_sum():
    numbers = list(range(1, 21))
    squares = [x ** 2 for x in numbers]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    filtered_sum = sum(even_squares)
    temp_result = [x for x in squares if x > 100]  # minor distraction
    extra_var = len(temp_result)  # irrelevant variable
    return filtered_sum

result = compute_filtered_sum()
print(f"Result: {result}")