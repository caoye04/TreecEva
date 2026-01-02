import math

# Simulated sensor readings from a water purification plant
def generate_raw_readings():
    return [187, 203, 195, 211, 176, 200, 190, 183, 199, 205]

# Irrelevant auxiliary function - decoy
def calculate_efficiency(index, base):
    if index < 2:
        return base
    return calculate_efficiency(index-1, base) + calculate_efficiency(index-2, base)

# Misleading transformation chain
raw_data = generate_raw_readings()
adjusted_readings = [x + 5 for x in raw_data if x > 185]
decoy_sequence = [math.log(x) for x in adjusted_readings if x % 2 == 0]

# Dead code path with unused variables
buffer_cache = set()
for val in raw_data:
    if val % 4 == 0:
        buffer_cache.add(val * 3)

# Real processing begins here
baseline = sum(raw_data) / len(raw_data)
variance_pool = [abs(x - baseline)**2 for x in raw_data]
mean_variance = sum(variance_pool) / len(variance_pool)
std_deviation = math.sqrt(mean_variance)

# Conditional filtering based on statistical thresholds
target_elements = []
for x in raw_data:
    if (baseline - 1.5 * std_deviation) <= x <= (baseline + 1.5 * std_deviation):
        target_elements.append(x)

# Bit manipulation red herring
obfuscation_key = 0b110101
masked_values = [x ^ obfuscation_key for x in target_elements if x & 1 == 1]

# Tuple unpacking distraction
data_points = [(x, x+1) for x in masked_values[:2]]
if len(data_points) >= 1:
    first_val, second_val = data_points[0]
    shift_offset = first_val >> 2
else:
    shift_offset = 0

# Actual relevant logic hidden among noise
processed_elements = []
threshold = 195
for item in target_elements:
    if item > threshold:
        processed_elements.append(item * 0.95)
    elif item == threshold:
        processed_elements.append(item)
    else:
        processed_elements.append(item * 1.02)

# Decoy string processing block
log_entry = "Purification cycle complete: {} elements processed"
entry_formatted = log_entry.format(len(processed_elements))
checksum_chars = {c for c in entry_formatted if c.isdigit()}

# Core validation function - depends only on processed_elements
def validate_purity(elements):
    purity_factor = 1.75
    adjustment = 0.0
    if len(elements) > 4:
        adjustment += 12.5
    if sum(elements) > 800:
        adjustment += 18.3
    # Final score uses set cardinality as multiplier
    unique_count = len(set([round(e) for e in elements]))
    return (sum(elements) / len(elements)) + adjustment + (unique_count * 0.7)

# Key execution point
filtration_score = validate_purity(processed_elements)

# Output result
print(f"Result: {filtration_score}")