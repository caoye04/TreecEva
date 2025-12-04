from collections import Counter

# Process customer order frequencies
customer_orders = [3, 7, 2, 5, 3, 8, 2, 7, 7, 4]
order_counter = Counter(customer_orders)

# Calculate some intermediate metrics (not all used in final result)
unique_orders = len(order_counter)
total_orders = sum(customer_orders)
average_orders = total_orders / len(customer_orders)

# Process data dictionary with various calculations
process_data = {}
for order_count in customer_orders:
    doubled = order_count * 2
    squared = order_count ** 2
    process_data[order_count] = doubled - (squared // 3)

# Additional unused calculations (distractor)
max_order = max(customer_orders)
min_order = min(customer_orders)
range_orders = max_order - min_order

# Sample keys for data access
sample_keys = [3, 7, 2, 5]

# Key operation - accessing specific processed data
final_result = process_data[sample_keys[2]]

print(f"Target result: {final_result}")