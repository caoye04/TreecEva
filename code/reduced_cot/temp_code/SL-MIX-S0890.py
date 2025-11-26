from collections import Counter

def process_inventory_data(data_stream):
    processed = []
    for item in data_stream:
        processed.append((item * 3) % 17 + 2)
    return processed

def analyze_sales_pattern(sales_data):
    temp_sum = 0
    temp_product = 1
    for val in sales_data:
        temp_sum += val
        temp_product *= (val % 7 + 1)
    return temp_sum, temp_product

def calculate_profit_margin(base_cost, selling_price):
    margin_data = []
    for i in range(len(base_cost)):
        margin = selling_price[i] - base_cost[i]
        margin_data.append(margin * 0.85)
    return margin_data

def process_analysis_data(raw_data):
    # Distractor: Unused computation path
    irrelevant_calc = sum([x * 2 for x in raw_data[:3]]) - 15
    
    # Main logic path
    counter_data = Counter(raw_data)
    filtered_items = [k for k, v in counter_data.items() if v >= 2]
    
    # Misleading intermediate result
    intermediate_val = len(filtered_items) * 7 - 3
    
    # Key computation
    if filtered_items:
        core_result = sum(filtered_items) // len(filtered_items)
        adjusted_result = (core_result * 11) % 23
    else:
        adjusted_result = 8
    
    # More distractions
    dead_code_path = [x for x in raw_data if x > 20]
    unused_computation = sum(dead_code_path) if dead_code_path else 0
    
    return adjusted_result

# Main execution
inventory_stream = [4, 12, 4, 8, 15, 12, 7, 4, 9, 15]
cost_data = [25, 40, 35, 30, 45]
price_data = [32, 50, 42, 38, 55]

# Irrelevant computations
processed_inventory = process_inventory_data(inventory_stream)
sales_analysis = analyze_sales_pattern(processed_inventory)
profit_margins = calculate_profit_margin(cost_data, price_data)

# Critical execution point
analysis_data = [item % 10 for item in inventory_stream]
result = process_analysis_data(analysis_data)

# Final output with some manipulation
final_output = (result * 3 + 7) // 2
print(f"Result: {final_output}")