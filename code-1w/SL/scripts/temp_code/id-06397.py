from collections import defaultdict

# Simulate sensor data aggregation and weighted scoring
raw_readings = [12, 15, 10, 8, 23, 14, 7, 19]
weights = {'temp': 0.3, 'pressure': 0.25, 'flow': 0.15, 'humidity': 0.3}

# Misleading auxiliary data
aux_data = [x ** 2 for x in raw_readings if x % 2 == 0]
dummy_counter = defaultdict(int)
for val in aux_data:
    dummy_counter[val] += 1

# Real processing begins
filtered_data = [x for x in raw_readings if x > 10]
normalized = [(x - min(filtered_data)) / (max(filtered_data) - min(filtered_data)) if max(filtered_data) != min(filtered_data) else 0 for x in filtered_data]

# Bitwise checksum (unused red herring)
checksum = 0
for i, val in enumerate(raw_readings):
    checksum ^= (val << 1) | (i & 1)

# State tracker with partial relevance
state_log = []
current_state = 'INIT'
for val in normalized:
    if val > 0.5:
        current_state = 'HIGH'
    elif val < 0.3:
        current_state = 'LOW'
    else:
        current_state = 'MID'
    state_log.append(current_state)

# Core calculation function
def calculate_final_score(data, weight_dict):
    base_scores = {}
    base_scores['temp'] = sum(data[:3]) if len(data) >= 3 else 0
    base_scores['pressure'] = sum(d * 0.1 for d in data) // 1  # Floor average effect
    base_scores['flow'] = data[-1] * 2 if len(data) > 0 else 0
    base_scores['humidity'] = sum(1 for d in data if d > 0.5)

    # Irrelevant internal scaling
    scaled_internal = {k: v * 1.1 for k, v in base_scores.items()}
    for k in scaled_internal:
        scaled_internal[k] = round(scaled_internal[k], 2)

    # Actual weighted score uses original base_scores
    weighted_sum = 0.0
    for key, weight in weight_dict.items():
        weighted_sum += base_scores.get(key, 0) * weight
    
    return int(weighted_sum + 0.5)  # Round to nearest integer

# Final computation
data = normalized
duplicate_check = [x for x in data if data.count(x) > 1]  # Dead-end analysis
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")