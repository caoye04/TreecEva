import math

# Simulated sensor data from a distributed environmental monitoring system
def generate_sensor_data():
    return [14, 17, 23, 42, 56, 77, 89, 90, 101, 112, 134, 145, 156, 167, 178]

# Irrelevant helper: converts numbers to binary strings (used nowhere)
def to_binary_string(n):
    return bin(n)[2:]

# Misleading transformation: applies bit rotation (not actually used in main logic)
def rotate_bits(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

# Dead function: calculates sum of squares but never called
def sum_of_squares(lst):
    return sum(x * x for x in lst)

# Unused checksum calculator for red herring
def checksum(data):
    chk = 0
    for d in data:
        chk = (chk + d) * 31 % 10007
    return chk

# Core processing: filters anomalies using set operations and thresholds
valid_range = set(range(20, 160))
anomaly_flags = {23, 42, 145, 178}  # Known problematic readings


def filter_anomalies(raw_readings):
    # Step 1: remove out-of-range values
    in_range = [r for r in raw_readings if r in valid_range]
    
    # Step 2: exclude known anomaly codes using set difference
    filtered_set = set(in_range) - anomaly_flags
    
    # Step 3: sort and convert back to list
    return sorted(list(filtered_set))

# Transform logs into frequency distribution (complex distractor)
def build_frequency_map(data):
    freq = {}
    for item in data:
        group = item // 10
        freq[group] = freq.get(group, 0) + 1
    return freq

# Unused string encoding function (red herring)
def encode_reading(r):
    if r < 50:
        return ''.join(reversed(f'low_{r}'))
    else:
        return f'high_{r//10}x'

# Real pipeline starts here
raw_logs = generate_sensor_data()
processed_logs = filter_anomalies(raw_logs)

# Extraneous accumulation: computes cumulative products (not used)
cumulative_product = 1
temp_products = []
for val in processed_logs:
    cumulative_product *= val
    temp_products.append(cumulative_product)

# Distractor: complex floating point computation with no impact
float_distractor = 0.0
for i in range(len(processed_logs)):
    float_distractor += math.sin(processed_logs[i]) * math.cos(i * 0.5)

# Real logic: count how many readings are above median threshold
median_threshold = 90
def analyze_readings(cleaned_data):
    total_above = 0
    running_sum = 0
    
    # Multiple nested conditions to assess compliance
    for reading in cleaned_data:
        running_sum += reading
        if reading > median_threshold:
            if reading % 2 == 0:  # Only even high readings count
                total_above += 1
    
    # Final diagnostic based on count and sum interaction
    adjustment = len(cleaned_data) - total_above
    final_score = running_sum // (total_above + 1)  # Avoid division by zero
    return final_score + adjustment

# Key statement
final_diagnostic = analyze_readings(processed_logs)

# Print result as required
print(f"Result: {final_diagnostic}")