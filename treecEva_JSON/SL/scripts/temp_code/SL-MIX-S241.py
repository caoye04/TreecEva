def log_sales(func):
    weekly_log = {}
    def wrapper(day, sales):
        result = func(day, sales)
        updated_log = {day: result}
        weekly_log.update(updated_log)
        return weekly_log
    return wrapper

@log_sales
def record_daily_sales(day, sales):
    return sales

# Fibonacci sequence for the week (Monday to Sunday)
fib_sequence = [1, 1]
for i in range(2, 7):
    fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

# Record sales for each day
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i, day in enumerate(days_of_week):
    log = record_daily_sales(day, fib_sequence[i])

# Calculate total sales
total_pies_sold = sum(log.values())
print(f"Result: {total_pies_sold}")