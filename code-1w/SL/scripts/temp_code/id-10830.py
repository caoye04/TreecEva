def main():
    data_stream = [3, 7, 12, 15, 18, 21, 25]

    # Transformation: map each value using a lambda to compute (x * 2 - 5)
    transform = lambda x: x * 2 - 5
    mapped_values = list(map(transform, data_stream))

    # Define validity condition: divisible by 3 and positive
    is_valid = lambda x: x > 0 and x % 3 == 0

    # Filtering and summation
    filtered_sum = sum(filter(is_valid, mapped_values))

    # Irrelevant distraction: unused variable (minimal interference)
    max_value = max(mapped_values)

    print(f"Result: {filtered_sum}")

main()