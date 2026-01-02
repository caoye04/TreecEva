def main():
    data_stream = [17, 23, 31, 44, 52]
    offset = 3
    
    # Preprocess: apply modular arithmetic to normalize values
    processed_data = [(x % 13 + offset) for x in data_stream]
    
    # Irrelevant distraction: unused variable (minimal interference)
    backup_copy = processed_data.copy()
    
    # Define transformation function using lambda
    transform = lambda seq: sum(x * 2 if i % 2 == 0 else x - 1 for i, x in enumerate(seq))
    
    # Key computation step
    result = transform(processed_data)
    
    print(f"Result: {result}")

main()