def process_inventory_data(items):
    # Distractor: string manipulation that doesn't affect final result
    temp_str = "INVENTORY_ANALYSIS_2024"
    encoded_header = temp_str.lower().replace('_', '-')[:15]
    
    # Distractor: unnecessary dictionary operations
    config_params = {'threshold': 50, 'max_items': 100, 'offset': 7}
    dummy_calc = config_params['threshold'] * config_params['offset'] // 3
    
    # Relevant: actual processing with bitwise operations
    checksum = 0
    processed_count = 0
    
    for item in items:
        # Distractor: misleading intermediate calculation
        weight_factor = (item['id'] & 0xF) + (len(item['name']) % 8)
        
        # Relevant: core checksum calculation
        if item['status'] == 'active':
            checksum ^= (item['quantity'] << 4) | (item['price'] & 0xFF)
            processed_count += 1
        
        # Distractor: dead code path
        if item['category'] == 'electronics':
            dummy_multiplier = weight_factor * 3
            
    # Distractor: unused string operation
    result_prefix = f"CS:{processed_count}-"
    
    # Final relevant operation
    checksum = (checksum + processed_count) & 0xFFFF
    return checksum

# Main execution
inventory_items = [
    {'id': 101, 'name': 'laptop', 'quantity': 15, 'price': 42, 'status': 'active', 'category': 'electronics'},
    {'id': 102, 'name': 'monitor', 'quantity': 8, 'price': 67, 'status': 'active', 'category': 'electronics'},
    {'id': 103, 'name': 'keyboard', 'quantity': 25, 'price': 23, 'status': 'inactive', 'category': 'accessories'},
    {'id': 104, 'name': 'mouse', 'quantity': 30, 'price': 18, 'status': 'active', 'category': 'accessories'}
]

# Distractor: unnecessary variable assignments
analysis_mode = True
verbose_logging = False
backup_data = inventory_items.copy()

final_checksum = process_inventory_data(inventory_items)
print(f"Result: {final_checksum}")