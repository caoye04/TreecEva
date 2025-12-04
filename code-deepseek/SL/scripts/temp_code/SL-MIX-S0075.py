from collections import Counter

# Process customer transaction categories
transactions = ['retail', 'online', 'retail', 'wholesale', 'online', 'retail', 'service', 'online']
category_counts = Counter(transactions)

# Initial processing with some unnecessary intermediate steps
retail_count = category_counts['retail']
online_count = category_counts['online']
wholesale_count = category_counts.get('wholesale', 0)
service_count = category_counts.get('service', 0)

# Distractor calculations that don't affect final result
potential_revenue = retail_count * 150 + online_count * 200
discount_factor = 0.85 if retail_count > 2 else 0.90

# Core logic with moderate nesting
base_tally = retail_count * 3
if online_count > 1:
    base_tally += online_count * 2
    if wholesale_count > 0:
        base_tally += 5  # This condition is never met

# More distraction
intermediate_sum = sum(category_counts.values())
average_transactions = intermediate_sum / len(category_counts)

# Final processing
final_tally = base_tally + service_count
adjustment_factor = 2 if retail_count >= online_count else 3

# Target variable assignment
processed_result = final_tally * adjustment_factor

print(f"Target result: {processed_result}")