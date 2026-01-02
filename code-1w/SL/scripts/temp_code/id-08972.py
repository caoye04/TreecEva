from itertools import combinations

# Simulate inventory analysis with anomaly detection
items = ['sensor', 'actuator', 'valve', 'sensor', 'controller', 'valve', 'sensor', 'actuator']
readings = [104, 205, 180, 110, 220, 175, 108, 208]

# Step 1: Count occurrences of each item (relevant)
item_counts = {}
for item in items:
    item_counts[item] = item_counts.get(item, 0) + 1

base_count = item_counts['sensor'] * 10  # Each sensor contributes 10 units

# Step 2: Identify anomalous readings (over 200 or under 105)
anomalies = [r for r in readings if r > 200 or r < 105]
duplicate_anomalies = [x for x in anomalies if anomalies.count(x) > 1]  # Red herring: not used later

# Step 3: Compute moving average (distractor computation)
moving_avg = []
for i in range(len(readings) - 2):
    avg_val = sum(readings[i:i+3]) / 3
    moving_avg.append(round(avg_val, 1))

# Step 4: Generate all 2-combinations of high-value items (semi-relevant)
high_value_indices = [i for i, r in enumerate(readings) if r > 170]
high_pairs = list(combinations(high_value_indices, 2))
pair_distance_sum = sum(abs(p[1] - p[0]) for p in high_pairs)  # Used indirectly

# Step 5: Flag duplicate item positions (distraction)
duplicate_positions = []
seen = {}
for idx, item in enumerate(items):
    if item in seen:
        duplicate_positions.append((seen[item], idx))
    seen[item] = idx

# Step 6: Calculate adjustment based on specific pattern
adjustment = 0
for i in range(1, len(items)):
    if items[i] == 'valve' and readings[i] < 180:
        adjustment += 3

# Step 7: Use set operations to find unique configurations (relevant)
unique_item_set = set(items)
control_components = {'controller', 'actuator'}
peripheral_count = len(unique_item_set - control_components)  # sensors and valves

# Step 8: Final adjustment sum with dummy logic
adjustment_sum = adjustment
if len(peripheral_count.__str__()) == 1:  # Always true, obfuscated check
    adjustment_sum += pair_distance_sum % 5

# Key statement
final_tally = base_count - adjustment_sum

# Output result
print(f"Result: {final_tally}")