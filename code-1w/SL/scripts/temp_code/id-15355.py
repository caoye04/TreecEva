def main():
    data_stream = [12, 18, 24, 30]
    threshold = 20

    # Filter and preprocess data above threshold
    filtered = list(filter(lambda x: x > threshold, data_stream))
    
    # Apply transformation using bitwise and arithmetic operations
    processed_data = [(val ^ 3) + (val >> 2) for val in filtered]

    # Conditional computation based on sum
    total = sum(processed_data)
    result = None
    
    if total % 2 == 0:
        result = total * 1.5
    else:
        result = total + 100

    # Irrelevant distraction: unused variable
    backup_copy = data_stream.copy()

    # Final output
    print(f"Result: {result}")

main()