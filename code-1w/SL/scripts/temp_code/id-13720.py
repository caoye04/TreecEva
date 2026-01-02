def main():
    data = [3, 7, 12, 15, 18, 21, 25]
    
    # Mapping: apply square root approximation via lambda
    mapper = lambda x: int(x ** 0.5)
    mapped_values = list(map(mapper, data))
    
    # Define validity: odd numbers greater than 2
    is_valid = lambda x: x > 2 and x % 2 == 1
    
    # Filtering and summation
    filtered_sum = sum(filter(is_valid, mapped_values))
    
    # Irrelevant distraction: unused variable
    temp_debug_log = [f'val_{i}' for i in range(len(data))]
    
    print(f"Result: {filtered_sum}")

main()