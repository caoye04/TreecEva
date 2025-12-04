def analyze_text_patterns(text_samples):
    pattern_checks = [len(sample) % 7 for sample in text_samples]
    validation_mask = [check > 2 for check in pattern_checks]
    return sum(validation_mask)

def calculate_inventory_shifts(base_items, adjustments):
    temp_shift = base_items * 3 - adjustments
    intermediate_result = temp_shift // 2 + 5
    # Dead code path - misleading calculation
    unused_computation = (base_items << 2) ^ adjustments
    return intermediate_result

def process_inventory(item_records):
    # Irrelevant preprocessing
    item_lengths = [len(record) for record in item_records]
    max_length = max(item_lengths) if item_lengths else 0
    
    # Main computation with distractions
    base_count = sum(1 for record in item_records if 'active' in record.lower())
    
    # Misleading intermediate variable
    misleading_total = base_count * 2 + len(item_records)
    
    # Conditional expression with slicing
    processed_count = base_count + 3 if len(item_records) > 2 else base_count - 1
    
    # Set operations for distraction
    item_set = set(item_records)
    unique_processing = len(item_set) % 4
    
    # Actual relevant calculation
    adjusted_count = processed_count - unique_processing
    
    # More distractions
    fake_calculation = calculate_inventory_shifts(base_count, len(item_records))
    
    # Final result
    final_count = adjusted_count + (max_length // 3)
    
    # Print the target variable
    print(f"Target result: {final_count}")
    return final_count

# Main execution
item_records = ['Active Widget A', 'Inactive Component', 'ACTIVE Module X', 'Pending Item', 'active unit']
processed_items = process_inventory(item_records)