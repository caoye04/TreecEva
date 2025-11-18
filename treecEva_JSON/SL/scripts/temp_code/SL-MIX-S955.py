def fibonacci_bakery_production():
    # Day 1 and Day 2 production
    day_1 = 10
    day_2 = 15
    
    # Initialize total with first two days
    total_loaves = day_1 + day_2
    
    # Calculate production for days 3 through 7
    prev_prev = day_1
    prev = day_2
    
    for day in range(3, 8):
        current = prev + prev_prev
        total_loaves += current
        prev_prev = prev
        prev = current
    
    return total_loaves

# Calculate total bread production
production_result = fibonacci_bakery_production()
print(f"Result: {production_result}")