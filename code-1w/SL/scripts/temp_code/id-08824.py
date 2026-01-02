def main():
    data_points = [12, -7, 31, 8, -15, 26, 4, 9]
    offset = 10
    adjusted_values = [x + offset for x in data_points]
    
    # Irrelevant distraction: unused variable
    baseline_correction = 5
    
    is_valid = lambda x: x > 10 and (x % 2 == 0)
    processed_data = [val * 2 for val in adjusted_values if val != 0]
    filtered_sum = sum(filter(is_valid, processed_data))
    
    # Another irrelevant operation
    temp_result = len(processed_data) * 2
    
    print(f"Result: {filtered_sum}")

if __name__ == "__main__":
    main()