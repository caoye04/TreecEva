def fibonacci_like(n):
    if n <= 2:
        return n
    return fibonacci_like(n-1) + fibonacci_like(n-2)

# Record flower counts using list comprehension for first 10 days
flower_counts = [fibonacci_like(day) for day in range(1, 11)]

# Calculate cumulative sum up to day 7
cumulative_flowers_by_day_7 = sum(flower_counts[:7])

print(f'Result: {cumulative_flowers_by_day_7}')