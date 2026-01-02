import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [
    (1.2, 'C'), (3.5, 'A'), (2.1, 'B'), (4.8, 'A'), (1.9, 'C'),
    (3.3, 'B'), (5.0, 'A'), (2.5, 'B'), (4.1, 'C'), (3.7, 'A')
]

# Irrelevant mapping table for unused mode translation
mode_map = {'A': 'ACTIVE', 'B': 'STANDBY', 'C': 'IDLE'}
status_weights = {'ACTIVE': 3, 'STANDBY': 2, 'IDLE': 1}  # Distractor: not used in logic

# Noisy preprocessing pipeline with dead functions
def filter_outliers(seq, limit=4.5):
    return [x for x in seq if x[0] <= limit]

# Unused function - red herring
def translate_modes(data):
    return [(val, mode_map[code]) for val, code in data]

# Function that looks important but is only partially used
def group_by_category(data):
    sorted_data = sorted(data, key=lambda x: x[1])
    grouped = {}
    for k, g in itertools.groupby(sorted_data, key=lambda x: x[1]):
        grouped[k] = [x[0] for x in g]
    return grouped

# Decoy aggregation function that computes something irrelevant
def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

# Real processing begins here — subtle signal in noise
cleaned_data = filter_outliers(data_stream)  # Remove outlier (5.0, 'A')
temp_dict = group_by_category(cleaned_data)

# Extract only category 'A' values for focus analysis
focus_values = temp_dict.get('A', [])

# Secondary filtering based on dynamic threshold (mean of focus group)
if focus_values:
    dynamic_ref = sum(focus_values) / len(focus_values)
else:
    dynamic_ref = 0

decision_flag = dynamic_ref > 3.0  # Triggers downstream path

# Complex conditional transformation chain
transformed = []
for val in focus_values:
    if val < 2.5:
        transformed.append(val * 1.1)
    elif val < 3.5:
        transformed.append(val * 0.95)
    else:
        transformed.append(val * 1.05)

# Aggregation using weighted rolling adjustment (only uses transformed)
aggregated_data = sum(
    (transformed[i] + transformed[i-1]) * 0.5 
    for i in range(1, len(transformed))
) if len(transformed) > 1 else (transformed[0] if transformed else 0)

# Threshold derived from length of original stream — subtle dependency
threshold = len(data_stream) * 0.6

# Core logic hidden among distractions
def process_results(data, limit):
    if data > limit:
        adjustment = 1.1
    elif data == limit:
        adjustment = 1.0
    else:
        adjustment = 0.9
    intermediate = data * adjustment
    
    # Extra steps to obscure final path
    temp_result = intermediate + 0.05 * abs(intermediate)
    normalized = round(temp_result, 4)
    score_shift = int(normalized) % 3
    
    # Final computation relying on prior state
    final_value = int(normalized) + (score_shift * 0.25)
    
    # Dead branch — never executed due to logic above
    if False and normalized < 0:
        fallback = 0
        for _ in range(5):
            fallback += 2
        return fallback
    
    return final_value

# Key assignment statement
final_score = process_results(aggregated_data, threshold)

# Debug printing of irrelevant variables
# print('Diagnostics:', compute_variance(focus_values), decision_flag)

# Output the target result
print(f"Target result: {final_score}")