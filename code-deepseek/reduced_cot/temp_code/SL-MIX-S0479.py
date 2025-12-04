def compute_final_result(inventory_data, processing_config):
    # Distractor operations that don't affect final result
    temp_sum = sum(item['count'] for item in inventory_data.values())
    processed_items = {k: v for k, v in inventory_data.items() if v['status'] == 'active'}
    
    # Actual computation path
    base_multiplier = processing_config.get('multiplier', 1)
    adjustment_factor = processing_config.get('adjustment', 0)
    
    # More distraction - intermediate calculations that aren't used
    max_count = max(item['count'] for item in inventory_data.values())
    min_count = min(item['count'] for item in inventory_data.values())
    count_difference = max_count - min_count
    
    # Key computation
    relevant_items = [item for item in inventory_data.values() 
                     if item['category'] == processing_config['target_category']]
    
    if not relevant_items:
        return adjustment_factor
    
    weighted_total = sum(item['count'] * item['weight'] for item in relevant_items)
    final_value = (weighted_total * base_multiplier) + adjustment_factor
    
    # Final distraction - unused transformation
    normalized_value = final_value / len(relevant_items) if len(relevant_items) > 0 else 0
    
    return final_value

# Main execution
inventory_data = {
    'item_A': {'count': 8, 'weight': 2, 'status': 'active', 'category': 'electronics'},
    'item_B': {'count': 5, 'weight': 3, 'status': 'inactive', 'category': 'electronics'},
    'item_C': {'count': 12, 'weight': 1, 'status': 'active', 'category': 'furniture'},
    'item_D': {'count': 3, 'weight': 4, 'status': 'active', 'category': 'electronics'}
}

processing_config = {
    'target_category': 'electronics',
    'multiplier': 2,
    'adjustment': 10
}

final_output = compute_final_result(inventory_data, processing_config)
print(f"Result: {final_output}")