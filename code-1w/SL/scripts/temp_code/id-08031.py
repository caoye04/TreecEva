import itertools

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant smoothing calculation (distractor)
    smoothed = [sequence[0]]
    for j in range(1, len(sequence)):
        smoothed_val = 0.5 * sequence[j] + 0.5 * smoothed[-1]
        smoothed.append(round(smoothed_val))
    
    # Actual logic: count rising edges
    rising_edges = 0
    for t in trend:
        if t == 1:
            rising_edges += 1
    
    return rising_edges

# Simulate sensor data acquisition
data_stream = [23, 21, 25, 25, 29, 27, 33, 35]
offset_correction = 5
adjusted_data = [x + offset_correction for x in data_stream]

# Filter out values above threshold (semi-relevant preprocessing)
threshold = 30
filtered_data = list(itertools.dropwhile(lambda x: x <= threshold, adjusted_data))

# Dead code path - never executed but looks important
if len(filtered_data) > 10:
    filtered_data = [x for x in filtered_data if x % 2 == 0]
elif len(filtered_data) == 0:
    filtered_data = [0, 0]

# Auxiliary diagnostic (irrelevant to final result)
diagnostic_flag = False
checksum = 0
for val in data_stream:
    checksum ^= val  # Bitwise XOR chain (distraction)
diagnostic_flag = (checksum > 50)

# Core processing function
def process_signals(seq):
    base = 10
    multiplier = len(seq) if seq else 1
    
    # Conditional expression used idiomatically
    adjustment = 2 if any(x % 4 == 0 for x in seq) else 1
    
    temp_result = base * multiplier + adjustment
    
    # Nested conditional with misleading intermediate steps
    if len(seq) >= 2:
        first_diff = seq[1] - seq[0]
        if first_diff > 0:
            temp_result -= first_diff  # Relevant subtraction
        else:
            temp_result += abs(first_diff)
    
    # Spurious complex-looking but unused calculation
    shadow_accum = 0
    for a, b in itertools.combinations(seq, 2):
        shadow_accum += (a ^ b) >> 1  # Bitwise distraction
    
    return temp_result

# Key statement
final_output = process_signals(filtered_data)

print(f"Result: {final_output}")