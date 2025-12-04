from collections import Counter

# Process inventory data for warehouse optimization
def analyze_inventory(inventory_items):
    item_counts = Counter(inventory_items)
    
    # Calculate base metrics
    total_items = len(inventory_items)
    unique_items = len(item_counts)
    
    # Intermediate calculation (not directly used in final result)
    avg_per_type = total_items / unique_items if unique_items > 0 else 0
    
    # Calculate processing metrics
    high_demand_items = sum(1 for count in item_counts.values() if count >= 3)
    low_stock_items = sum(1 for count in item_counts.values() if count <= 1)
    
    # Distractor calculation (appears relevant but not used)
    excess_inventory = sum(count - 2 for count in item_counts.values() if count > 2)
    
    # Main processing logic
    base_score = high_demand_items * 15 + low_stock_items * 8
    processed_data = base_score - (unique_items * 2)
    
    # Adjustment calculations
    adjustment_factor = (total_items % 7) * 3
    temp_adjustment = (unique_items ^ high_demand_items) + 5  # Distractor
    
    # Final computation
    final_result = processed_data - adjustment_factor
    
    print(f"Target result: {final_result}")
    return final_result

# Sample inventory data
inventory = ["widget", "gadget", "widget", "tool", "gadget", "widget", "part", "tool"]
result = analyze_inventory(inventory)