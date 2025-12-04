import itertools

def process_inventory(items, limit):
    # This function processes inventory data with some irrelevant calculations
    processed = list(itertools.filterfalse(lambda x: x <= limit, items))
    
    # Distractor operations that don't affect final result
    temp_sum = sum(items)
    avg_value = temp_sum / len(items) if items else 0
    
    # Actual relevant calculations
    combined = list(itertools.chain(processed, [limit * 2]))
    result = sum(combined) - (limit * 3)
    
    # More distractor operations
    squared_values = [x**2 for x in items if x > 0]
    max_squared = max(squared_values) if squared_values else 0
    
    return result

# Main execution
inventory_data = [45, 28, 67, 19, 82, 33]
threshold = 25

# Irrelevant intermediate calculations
sorted_data = sorted(inventory_data)
data_product = 1
for num in inventory_data:
    data_product *= num

final_calculation = process_inventory(inventory_data, threshold)
print(f"Target result: {final_calculation}")