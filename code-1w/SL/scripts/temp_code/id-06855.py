def compute_aggregate():
    base_values = [3, 7, 2, 8, 2, 9]
    offset = 5
    adjusted = [x + offset for x in base_values]
    
    # Generate composite values using arithmetic and set deduplication
    composite_values = []
    for val in adjusted:
        if val % 2 == 0:
            composite_values.append(val ** 2)
        else:
            composite_values.append(val // 2)
    
    # Key statement
    filtered_sum = sum(sorted(set(composite_values)))
    
    # Irrelevant tracking variable (minimal distraction)
    count_tracker = len([x for x in composite_values if x > 10])
    
    print(f"Result: {filtered_sum}")

compute_aggregate()