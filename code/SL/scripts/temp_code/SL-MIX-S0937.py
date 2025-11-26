from itertools import accumulate, chain

def process_inventory_data():
    # Initial inventory data with some outdated entries
    raw_inventory = [45, 23, 67, 89, 12, 56, 78]
    
    # Distractor processing - not used in final calculation
    temp_analysis = [x * 2 for x in raw_inventory if x > 30]
    intermediate_sum = sum(temp_analysis)
    
    # Main processing chain using itertools
    filtered_items = [item for item in raw_inventory if item > 25]
    cumulative_totals = list(accumulate(filtered_items))
    
    # Another distractor calculation
    weighted_avg = sum(cumulative_totals) / len(cumulative_totals) if cumulative_totals else 0
    
    # Key processing steps
    adjusted_values = [val - 10 for val in cumulative_totals]
    processed_data = [val * 2 for val in adjusted_values]
    
    # Final result extraction
    final_result = processed_data[-1]
    print(f"Target result: {final_result}")
    return final_result

process_inventory_data()