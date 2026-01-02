def calculate_total(values, changes):
    base = sum(values)
    modifier = list(map(lambda x: x * 0.1, changes))
    adjustment = sum(modifier) if sum(modifier) > 5 else 10
    return int(base + adjustment)

# Irrelevant utility function (minor distraction)
def log_event(event):
    timestamp = "2023-01-01"
    level = "INFO"
    return f"[{timestamp}] {level}: {event}"

# Main data
prices = [15, 25, 35, 45]
adjustments = [20, 30]
dummy_dict = {"version": "1.0", "active": True}

# Key computation
final_score = calculate_total(prices, adjustments)

print(f"Result: {final_score}")