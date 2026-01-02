def analyze_compatibility(items, constraints):
    compatible = set()
    for item in items:
        if item % 3 == 0 and item > constraints['min_size']:
            compatible.add(item)
    return compatible

items = [12, 15, 8, 9, 21, 14, 18, 25]
constraints = {'min_size': 10, 'max_weight': 100}

# Red herring: unused function
def calculate_efficiency(x):
    return (x * 2) // 3 + 5

# Distractor variables
temp_weights = [item * 2 for item in items if item < 20]
duplicate_filter = {x//2 for x in temp_weights if x > 10}

selected = analyze_compatibility(items, constraints)

# Simulate shifting storage bins
shelf_config = []
for i, val in enumerate(sorted(selected)):
    shifted = (val + i) % 7
    shelf_config.append(shifted * 2 if shifted % 2 == 0 else shifted)

# Buffer calculation with irrelevant rounding
raw_buffer = sum(shelf_config) / 4.0
truncated_buffer = int(raw_buffer)
overflow_buffer = round(truncated_buffer * 1.5)

# Core logic disguised among other operations
baseline = len(shelf_config) * 3
adjustment = 0
for idx in range(len(shelf_config)):
    if shelf_config[idx] > 5:
        adjustment += 2
    elif shelf_config[idx] == 4:
        adjustment -= 1

interim = baseline + adjustment

# Secondary red herring: dead computation on string
status_log = "System OK"
if len(status_log) > 5:
    status_log = status_log.replace("OK", "ACTIVE")

# Key state transformation
flagged_slots = set()
for i, v in enumerate(shelf_config):
    if v % 3 == 0:
        flagged_slots.add(i)

# Real computation path
def optimize_storage(config, buffer):
    total = sum(config)
    limit = total + buffer
    penalty = len([x for x in config if x > 6])
    return limit - penalty * 2

final_capacity = optimize_storage(shelf_config, overflow_buffer)

print(f"Result: {final_capacity}")