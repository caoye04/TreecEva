def calculate_weighted_score():
    items = ['A', 'B', 'C', 'D', 'E']
    points = [3, 7, 2, 8, 4]
    total_score = 0
    
    for index, item in enumerate(items):
        if item in ['B', 'D']:
            multiplier = 2
        else:
            multiplier = 1
            
        # Irrelevant string manipulation (minor distraction)
        item_description = f"Item: {item}"
        item_length = len(item_description)
        
        # Key computation step
        i = index % len(points)
        total_score += points[i] * (index + 1)
        
        # Extra operation with no effect on result
        temp_offset = item_length - 9
    
    # Output result as required
    print(f"Result: {total_score}")

# Execute function
calculate_weighted_score()