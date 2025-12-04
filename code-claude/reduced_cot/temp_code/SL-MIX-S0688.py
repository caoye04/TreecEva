import itertools

def calculate_priority(items):
    # Priority calculation based on item characteristics
    result = 0
    for item in items:
        item_value = item['value'] if item['active'] else 0
        category_multiplier = 1.5 if item['category'] == 'critical' else 1.0
        unused_factor = item.get('urgency', 5) / 10  # This factor isn't used
        
        # Calculate priority score with some complexity
        priority = item_value * category_multiplier
        result += priority
    
    return result

# Database of inventory items with various properties
inventory = [
    {'id': 101, 'name': 'Server Backup', 'value': 75, 'active': True, 'category': 'critical'},
    {'id': 102, 'name': 'Data Encryption', 'value': 60, 'active': True, 'category': 'standard'},
    {'id': 103, 'name': 'Network Monitor', 'value': 80, 'active': False, 'category': 'critical'},
    {'id': 104, 'name': 'Firewall Config', 'value': 90, 'active': True, 'category': 'critical'},
    {'id': 105, 'name': 'Password Manager', 'value': 45, 'active': True, 'category': 'standard'}
]

# Process inventory data
active_items = [item for item in inventory if item['active']]
standard_items = [item for item in inventory if item['category'] == 'standard']

# Create some combinations for analysis (not directly used in final calculation)
combinations = list(itertools.combinations([item['id'] for item in inventory], 2))
combination_count = len(combinations)

# Filter data based on conditions
filter_condition = lambda x: x['value'] > 50
filtered_data = [item for item in active_items if filter_condition(item)]

# Calculate a secondary metric (not used in final result)
secondary_metric = sum(item['value'] for item in standard_items)

# Calculate the priority value we're interested in
total_priority = calculate_priority(filtered_data)

# Convert some items to uppercase for a report (not affecting calculation)
item_names = {item['id']: item['name'].upper() for item in inventory}

print(f"Result: {total_priority}")