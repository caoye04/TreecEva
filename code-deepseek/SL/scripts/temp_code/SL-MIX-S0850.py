from collections import Counter

def process_inventory_data():
    initial_stock = [45, 78, 32, 91, 67, 23]
    incoming_shipments = [15, 22, 8, 30, 18, 5]
    
    # Calculate total inventory (distractor - not used in final result)
    total_inventory = sum(initial_stock) + sum(incoming_shipments)
    
    # Process inventory adjustments
    processed_data = []
    for i, stock in enumerate(initial_stock):
        adjusted = stock + incoming_shipments[i]
        if adjusted > 60:
            processed_data.append(adjusted - 10)
        else:
            processed_data.append(adjusted + 5)
    
    # Calculate adjustment factor using Counter (distractor - not directly relevant)
    stock_counter = Counter(initial_stock)
    adjustment_factor = stock_counter.most_common(1)[0][1] * 3
    
    # Final calculation - this is what matters
    final_result = processed_data[2] - adjustment_factor
    
    print(f"Result: {final_result}")
    return final_result

# Execute the function
if __name__ == "__main__":
    process_inventory_data()