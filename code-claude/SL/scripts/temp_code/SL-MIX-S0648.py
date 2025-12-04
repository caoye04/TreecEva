# Stock trading profit analysis
# Analyzing a week of daily profits to find the highest profit in a specific time window

daily_profits = [12, -5, 8, 14, -3, 7, 10, -2, 6]

# Initialize variables for analysis
start = 2
end = 7
lowest_profit = min(daily_profits)
period_length = end - start

# Calculate total profit across all days
total_profit = sum(daily_profits)
average_profit = total_profit / len(daily_profits)

# Find the highest profit in our target window
highest_profit = max(daily_profits[start:end])

# Calculate ratio of highest to average (not used in final result)
if average_profit > 0:
    ratio = highest_profit / average_profit
else:
    ratio = 0

print(f"Result: {highest_profit}")