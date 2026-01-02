import math

def preprocess_records(raw_entries):
    # Irrelevant transformation (not used in final calculation)
    normalized = [math.log(x + 1) for x in raw_entries if x > 0]
    filtered = [x for x in raw_entries if x % 2 == 1]  # Unused path
    return [x for x in raw_entries if x > 10]

def calculate_stability(values):
    if len(values) == 0:
        return 0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return round(math.sqrt(variance), 4)

def calculate_efficiency(data, limit):
    clipped = [min(x, limit) for x in data]
    adjustments = list(map(lambda x: x * 0.9 if x > 50 else x * 1.1, clipped))
    total_gain = sum(adjustments)
    penalty = 0
    for val in adjustments:
        if val > 45:
            penalty += 5
    # Dead code branch (never executed due to logic above)
    redundant_check = False
    if redundant_check:
        penalty += sum(1 for x in adjustments if x < 0)  # Unreachable
    base_effort = sum(data)
    efficiency = (total_gain - penalty * 2) / (base_effort + 1)
    return round(efficiency, 4)

# Main execution flow
raw_input_data = [12, 15, 22, 58, 63, 44, 31, 77, 81, 50]
config_settings = {'threshold': 60, 'mode': 'strict'}

# Step 1: Preprocess the input records
processed_data = preprocess_records(raw_input_data)

# Step 2: Compute auxiliary metric (not used in final result)
stability_metric = calculate_stability(processed_data)
backup_copy = processed_data[::-1]  # Slicing - irrelevant
offset = len(backup_copy) // 2
offset_correction = sum(backup_copy[:offset]) * 0.01  # Computed but unused

# Step 3: Determine threshold from config
threshold = config_settings['threshold']

# Step 4: Calculate the main efficiency score
# Key statement
efficiency_score = calculate_efficiency(processed_data, threshold)

# Print final target result
print(f"Target result: {efficiency_score}")