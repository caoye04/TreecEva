from collections import defaultdict
import itertools

def analyze_distribution(items):
    # Irrelevant helper function that is called but doesn't affect final result
    freq = defaultdict(int)
    for item in items:
        freq[item] += 1
    return dict(freq)

def filter_expired(stocks, cutoff_week):
    # Another distraction: simulates filtering but not used in core logic
    valid_stocks = []
    for stock in stocks:
        if stock[1] >= cutoff_week:
            valid_stocks.append(stock[0])
    return valid_stocks

def calculate_remaining_capacity(changes, limit):
    balance = limit * 0.5  # Start at half capacity
    surge_buffer = 0

    # Simulate weekly restocking and returns
    for week, delta in enumerate(changes):
        temp_adj = 0
        if week % 4 == 0:
            surge_buffer += 15  # Quarterly surge adjustment (distractor)

        if delta > 20:
            audit_flag = True
            temp_adj = 5  # Extra check-in overhead
        else:
            audit_flag = False

        # Core logic: only this affects final answer
        if balance + delta <= limit:
            balance += delta + temp_adj
        else:
            balance = limit  # Max out at capacity

        # Dead computation: uses variables but no impact
        debug_snapshot = f"Week {week}: bal={balance}, surge={surge_buffer}"

    # Final adjustment based on unused buffer
    if surge_buffer > 30:
        balance -= 10  # Penalty for over-planning (never triggered)

    return int(balance)

# Main execution flow
inventory_log = ['A', 'B', 'C', 'A', 'D', 'B', 'A']
stock_movements = [(100, 3), (150, 5), (200, 8), (90, 10)]  # (item_id, week)

# Distractor data structures
item_frequencies = analyze_distribution(inventory_log)
active_items = filter_expired(stock_movements, 6)

# Real input for main calculation
inventory_changes = [25, -10, 35, 50, -20, 15]
warehouse_limit = 100

# Key statement
final_capacity = calculate_remaining_capacity(inventory_changes, warehouse_limit)

print(f"Result: {final_capacity}")