def calculate_bakery_production():
    # Initialize the first two days
    daily_production = [10, 15]
    
    # Calculate next 5 days using Fibonacci rule
    for day in range(2, 7):
        daily_production.append(daily_production[day-1] + daily_production[day-2])
    
    # Sum all productions
    total_loaves = sum(daily_production)
    return total_loaves

# Execute and print result
result = calculate_bakery_production()
print(f"Result: {result}")