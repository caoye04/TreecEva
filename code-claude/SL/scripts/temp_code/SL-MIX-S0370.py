def transform_string(text, operation_type='uppercase'):
    transform_map = {
        'uppercase': lambda s: s.upper(),
        'lowercase': lambda s: s.lower(),
        'capitalize': lambda s: s.capitalize(),
        'reverse': lambda s: s[::-1]
    }
    
    if operation_type in transform_map:
        return transform_map[operation_type](text)
    return text

def calculate_priority(data_points):
    if not data_points:
        return 0
        
    # Sort by importance first, then by name
    sorted_data = sorted(data_points, key=lambda x: (-x['importance'], x['name']))
    
    # Calculate weighted sum for top 3 items
    top_items = sorted_data[:3]
    
    # Initialize weight factors
    weight_base = 10
    decay_factor = 0.8
    
    total = 0
    weight = weight_base
    
    for item in top_items:
        # Apply transformations to item name (but this doesn't affect priority)
        transformed_name = transform_string(item['name'], 'capitalize')
        item['display_name'] = transformed_name
        
        # Calculate contribution to priority
        contribution = item['importance'] * weight
        total += contribution
        weight *= decay_factor
    
    # Adjust for data size (doesn't affect result for our specific data)
    size_factor = min(1.0, len(data_points) / 10)
    potential_adjustment = total * (1 - size_factor)
    
    # Round to nearest integer
    return round(total)

# Sample data collection
all_data = [
    {'name': 'alpha', 'importance': 7, 'category': 'primary'},
    {'name': 'beta', 'importance': 9, 'category': 'secondary'},
    {'name': 'gamma', 'importance': 3, 'category': 'primary'},
    {'name': 'delta', 'importance': 5, 'category': 'tertiary'},
    {'name': 'epsilon', 'importance': 8, 'category': 'primary'}
]

# Filter data by various criteria
filter_category = 'primary'
discard_threshold = 4

# Apply filters
filtered_by_category = [item for item in all_data if item['category'] == filter_category]
filtered_data = [item for item in all_data if item['importance'] > discard_threshold]

# Calculate alternative metrics (not used for final result)
max_importance = max(item['importance'] for item in all_data)
min_importance = min(item['importance'] for item in all_data)
importance_range = max_importance - min_importance

# Calculate the priority value
priority_value = calculate_priority(filtered_data)

# Display some information
print(f"Filtered data count: {len(filtered_data)}")
print(f"Importance range: {importance_range}")
print(f"Result: {priority_value}")