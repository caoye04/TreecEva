from collections import Counter, defaultdict

def calculate_item_score(item_properties):
    base_score = item_properties['rarity'] * 2.5
    bonus = item_properties['level'] * 0.75
    penalty = item_properties.get('condition_penalty', 0)
    return max(0, base_score + bonus - penalty)

# Item database with properties
items = {
    'ancient_amulet': {'weight': 3, 'rarity': 8, 'level': 12, 'condition_penalty': 2},
    'mystic_orb': {'weight': 2, 'rarity': 7, 'level': 9},
    'enchanted_blade': {'weight': 6, 'rarity': 5, 'level': 14, 'condition_penalty': 3},
    'crystal_flask': {'weight': 1, 'rarity': 6, 'level': 8},
    'dragon_scale': {'weight': 4, 'rarity': 9, 'level': 15, 'condition_penalty': 1}
}

# Expedition constraints
max_capacity = 10
min_items = 2

# Track item frequencies for analysis (not used in final calculation)
item_counter = Counter()
for item_name in items:
    rarity_class = 'common' if items[item_name]['rarity'] < 7 else 'rare'
    item_counter[rarity_class] += 1

# Calculate scores for all items
item_scores = {}
for item_name, properties in items.items():
    score = calculate_item_score(properties)
    item_scores[item_name] = score

# Sort items by score-to-weight ratio (efficiency)
efficiency = {}
for item_name, score in item_scores.items():
    weight = items[item_name]['weight']
    efficiency[item_name] = score / weight if weight > 0 else 0

# This is a distraction - not used in final selection
backup_items = defaultdict(list)
for item_name, props in items.items():
    tier = 'high' if props['level'] > 10 else 'low'
    backup_items[tier].append(item_name)

# Select items based on efficiency until capacity is reached
remaining_capacity = max_capacity
selected_items = []

# Sort items by efficiency (highest first)
sorted_items = sorted(efficiency.items(), key=lambda x: x[1], reverse=True)

for item_name, _ in sorted_items:
    if remaining_capacity >= items[item_name]['weight']:
        selected_items.append(item_name)
        remaining_capacity -= items[item_name]['weight']

# Check if we need to optimize for minimum items requirement
if len(selected_items) < min_items and len(selected_items) > 0:
    # Remove the least efficient item to make room
    removed_item = selected_items.pop()
    remaining_capacity += items[removed_item]['weight']
    
    # Try to add smaller items to meet minimum requirement
    for item_name, _ in sorted(items.items(), key=lambda x: x[1]['weight']):
        if item_name not in selected_items and remaining_capacity >= items[item_name]['weight']:
            selected_items.append(item_name)
            remaining_capacity -= items[item_name]['weight']
            if len(selected_items) >= min_items:
                break

# Convert selection to a weight map
final_selection = {item: items[item]['weight'] for item in selected_items}

# Calculate total weight of selected items
total_weight = sum(final_selection.values())

# Apply a weight adjustment based on a formula (distraction)
adjusted_weight = total_weight * (1 - 0.05 * (max_capacity - total_weight))

print(f"Result: {total_weight}")