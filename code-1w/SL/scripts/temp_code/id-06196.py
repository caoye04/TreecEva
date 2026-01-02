def main():
    raw_input = '8,12,5,19,3'
    threshold = 10

    # Split and convert to integers
    data = list(map(int, raw_input.split(',')))

    # Filter values above threshold using lambda
    filtered = list(filter(lambda x: x > threshold, data))

    # Compute derived values: square root of sum of squares
    import math
    sum_of_squares = sum(map(lambda x: x**2, filtered))
    processed_data = math.sqrt(sum_of_squares)

    # Final transformation
    result = int(processed_data * 2)  # Truncate to integer after scaling

    print(f"Result: {result}")

main()