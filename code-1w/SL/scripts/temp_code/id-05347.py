def analyze_distribution(items):
    frequencies = {}
    for item in items:
        frequencies[item] = frequencies.get(item, 0) + 1
    return frequencies


def validate_item_codes(codes):
    valid_count = 0
    for code in codes:
        if len(code) == 5 and code.isalnum() and code[0].isalpha():
            valid_count += 1
    return valid_count


def calculate_remaining_capacity(stock_levels, customer_orders):
    # Misleading intermediate: total_items appears relevant but isn't used in final logic
    total_items = sum(stock_levels.values())
    fulfilled_orders = 0
    
    # Track order processing with state
    order_status = {}
    capacity_used = 0
    
    for i, (product, qty) in enumerate(zip(customer_orders.keys(), customer_orders.values())):
        if product in stock_levels and stock_levels[product] >= qty:
            order_status[i] = 'fulfilled'
            stock_levels[product] -= qty
            capacity_used += qty
            fulfilled_orders += 1
        else:
            order_status[i] = 'backordered'
    
    # Red herring computation: unused efficiency metric
    efficiency_ratio = fulfilled_orders / len(customer_orders) if customer_orders else 0
    
    remaining_stock_value = sum(stock_levels.values())
    
    # Key distraction: complex string analysis unrelated to capacity
    code_list = [f"P{key.upper()}" for key in stock_levels.keys()]
    filtered_codes = [c for c in code_list if c.endswith('A') or c.endswith('E')]
    special_count = len(filtered_codes)
    
    # Final result based on actual inventory usage
    final_capacity = remaining_stock_value - special_count
    
    # Additional irrelevant set operation
    unique_products = set(stock_levels.keys())
    redundant_check = len(unique_products) > len(stock_levels) // 2
    
    return final_capacity

# Main execution context
inventory = {
    'alpha': 50,
    'beta': 30,
    'gamma': 25,
    'delta': 40,
    'epsilon': 10
}

orders = {
    'alpha': 15,
    'gamma': 30,
    'delta': 10,
    'zeta': 5
}

# Irrelevant preprocessing step
item_names = list(inventory.keys())
dispatch_priorities = {name: idx for idx, name in enumerate(item_names)}

# Unused combinatorics: count possible order pairings
from itertools import combinations
possible_pairs = list(combinations(orders.keys(), 2))
pair_count = len(possible_pairs)

# Misleading frequency analysis
all_requested = []
for prod, quantity in orders.items():
    all_requested.extend([prod] * quantity)
freq_analysis = analyze_distribution(all_requested)

# Validate codes (no effect on result)
candidate_codes = ['A1234', 'B5678', 'C9012', 'D3456']
valid_codes = validate_item_codes(candidate_codes)

# Core calculation
final_capacity = calculate_remaining_capacity(inventory, orders)

Result: {final_capacity}