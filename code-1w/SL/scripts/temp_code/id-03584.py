from collections import defaultdict
import math

def preprocess_records(raw_entries):
    # Irrelevant transformation: counts per category (not used in final logic)
    category_count = defaultdict(int)
    for entry in raw_entries:
        category_count[entry['category']] += 1

    # Relevant processing: extract and scale values
    scaled_values = []
    for entry in raw_entries:
        base_val = entry['value']
        if entry['active']:
            if base_val > 50:
                scaled_values.append(base_val * 0.8)
            else:
                scaled_values.append(base_val * 1.2)
    return scaled_values

def analyze_trends(scaled_data):
    # Misleading trend analysis with unused statistics
    avg = sum(scaled_data) / len(scaled_data) if scaled_data else 0
    variance = sum((x - avg) ** 2 for x in scaled_data) / len(scaled_data) if scaled_data else 0
    volatility_index = math.sqrt(variance) if variance > 10 else 0  # Unused beyond this

    # Actual relevant threshold flag
    high_volatility = variance > 50
    return avg, high_volatility

def calculate_final_score(data_chunk):
    total = 0
    bonus_applied = False

    # Real logic: sum filtered values and apply conditional bonus
    filtered = [x for x in data_chunk if x > 40]

    for val in filtered:
        if val > 70 and not bonus_applied:
            total += int(val * 0.1)  # Bonus: 10% of first large value
            bonus_applied = True
        total += int(val)

    # Dead code path - never reached due to logic above
    if len(filtered) > 100:
        total -= 999  # Red herring adjustment

    return total

# Main execution
raw_dataset = [
    {'value': 30, 'category': 'A', 'active': True},
    {'value': 60, 'category': 'B', 'active': True},
    {'value': 80, 'category': 'A', 'active': True},
    {'value': 25, 'category': 'C', 'active': False},  # Inactive, won't be processed
    {'value': 90, 'category': 'B', 'active': True},
    {'value': 45, 'category': 'A', 'active': True},
]

# Step 1: Preprocess the data
processed_data = preprocess_records(raw_dataset)

# Step 2: Analyze trends (some return values unused)
mean_val, is_high_vol = analyze_trends(processed_data)

# Step 3: Calculate final score — critical execution point
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")