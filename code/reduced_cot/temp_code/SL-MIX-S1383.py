import re
from functools import reduce
from collections import defaultdict

def process_updates(updates):
    # Initialize counters
    status_counts = defaultdict(int)
    
    # Process each update
    for update in updates:
        if 'status' in update and update['status'] == 'DELIVERED':
            status_counts[update['zone']] += 1
    
    # Merge with base counts using dictionary comprehension
    base_counts = {f'ZONE_{i}': i*2 for i in range(1, 4)}
    merged_counts = {k: base_counts.get(k, 0) + status_counts[k] for k in set(base_counts) | set(status_counts)}
    
    # Apply transformation using map and filter
    valid_zones = dict(filter(lambda item: item[1] > 3, merged_counts.items()))
    transformed_values = list(map(lambda x: x * 2 if x % 2 == 0 else x + 1, valid_zones.values()))
    
    # Calculate final count with short-circuit evaluation
    total = reduce(lambda a, b: a + b, transformed_values, 0)
    threshold = 15
    final_delivered_count = total if total >= threshold and len(transformed_values) > 0 else 0
    
    return final_delivered_count

# Simulate package updates
package_updates = [
    {'tracking': 'DL-1001-XYZ', 'status': 'IN_TRANSIT', 'zone': 'ZONE_1'},
    {'tracking': 'DL-1002-XYZ', 'status': 'DELIVERED', 'zone': 'ZONE_2'},
    {'tracking': 'DL-1003-XYZ', 'status': 'DELIVERED', 'zone': 'ZONE_2'},
    {'tracking': 'DL-1004-XYZ', 'status': 'DELIVERED', 'zone': 'ZONE_3'},
    {'tracking': 'DL-1005-XYZ', 'status': 'DELIVERED', 'zone': 'ZONE_3'},
    {'tracking': 'DL-1006-XYZ', 'status': 'DELIVERED', 'zone': 'ZONE_3'}
]

# Extract tracking numbers matching pattern
pattern = r'DL-\d{4}-XYZ'
matching_trackings = [p['tracking'] for p in package_updates if re.match(pattern, p['tracking'])]

# Process updates and get final count
final_delivered_count = process_updates(package_updates)

print(f'Result: {final_delivered_count}')