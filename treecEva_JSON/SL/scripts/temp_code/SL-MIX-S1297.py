from collections import deque

# Pie prices: apple=5, cherry=7, blueberry=6, pumpkin=8
pie_prices = {'apple': 5, 'cherry': 7, 'blueberry': 6, 'pumpkin': 8}

# Daily pie sales (in order of sale)
daily_sales_stack = ['apple', 'cherry', 'blueberry', 'pumpkin', 'apple']
daily_sales_queue = deque(['pumpkin', 'apple', 'cherry', 'blueberry', 'pumpkin'])

# Calculate revenue from most recent 3 sales (stack)
recent_revenue = sum(pie_prices[daily_sales_stack.pop()] for _ in range(3))

# Calculate revenue from earliest 3 sales (queue)
earliest_revenue = sum(pie_prices[daily_sales_queue.popleft()] for _ in range(3))

# Total revenue calculation
total_revenue = recent_revenue + earliest_revenue

print(f'Result: {total_revenue}')