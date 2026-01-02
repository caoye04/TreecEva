import math

# Simulated sensor data and configuration
raw_readings = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
scaling_factor = 2.5
offset_correction = -1.2
sample_window = 4
dummy_flag = True
useless_counter = 0

# Irrelevant transformation (dead path)
def obsolete_normalization(data):
    global useless_counter
    result = []
    for x in data:
        if x > 10:
            result.append(x * 0.1)
        else:
            result.append(x + 1)
        useless_counter += 1
    return result

# Unused helper (distractor)
reduction_op = lambda seq: sum([x for x in seq if x % 2 == 1])

# Real signal preprocessing
def preprocess(signal, factor, offset):
    corrected = [int(x * factor + offset) for x in signal]
    filtered = [x for x in corrected if x > 0]  # Remove negative readings
    return list(set(filtered))  # Deduplicate

# Secondary data structure with red herring content
status_codes = {
    'INIT': 100,
    'ACTIVE': 200,
    'STANDBY': 150,
    'ERROR_X1': 301,
    'DEBUG_MASK': 0b111000
}

# Decoy function that looks important but isn't called
def trigger_calibration(seq):
    if len(seq) % 2 == 0:
        return [seq[i] ^ seq[-i-1] for i in range(len(seq)//2)]
    return seq

# Threshold logic based on prime characteristics
prime_flags = {x: all(x % i != 0 for i in range(2, int(math.sqrt(x))+1)) for x in range(2, 50)}

def classify_value(n):
    if n >= 20 and prime_flags.get(n, False):
        return 'CRITICAL'
    elif n % 3 == 0:
        return 'WARNING'
    else:
        return 'NORMAL'

# Mapping creation with intentional noise
threshold_map = {key: len(key) * 10 for key in ['CRITICAL', 'WARNING', 'NORMAL']}
threshold_map['IGNORED'] = 999  # Misleading entry

# Data transformation chain
temp_buffer = []
for val in raw_readings:
    temp_buffer.append(int((val + 2) ** 1.5))

transformed_data = preprocess(temp_buffer, scaling_factor, offset_correction)

# Redundant string processing (distractor)
log_header = "SENSOR_DIAG_01"
version_tag = log_header.lower().replace('_', '-')[6:]
if version_tag.startswith('d'):
    dummy_flag = False

# Another decoy list comprehension
shadow_copy = [math.ceil(z/10)*10 for z in transformed_data if z % 4 == 0]

# Core analysis function with conditional branching
def analyze_pattern(dataset, thresholds):
    counts = {'CRITICAL': 0, 'WARNING': 0, 'NORMAL': 0}
    
    for item in dataset:
        cat = classify_value(item)
        if cat in counts:
            counts[cat] += 1
    
    # Complex scoring with weighted logic
    score = 0
    score += counts['CRITICAL'] * thresholds['CRITICAL']
    score += counts['WARNING'] * thresholds['WARNING']
    score += counts['NORMAL'] * thresholds['NORMAL']
    
    # Inject irrelevant bit manipulation
    bit_state = 0b1010
    for _ in range(counts['CRITICAL']):
        bit_state = (bit_state << 1) | (bit_state >> 3)
        bit_state &= 0b1111
    
    # Final diagnostic derived from score and state
    final_score = score + (bit_state & 0b111)
    
    # Dead code branch (never executed due to logic)
    if len(dataset) < 5 and dummy_flag:
        return -999
        extra = [x for x in dataset if x > 100]
        final_score -= sum(extra)

    return final_score

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, threshold_map)
print(f"Result: {final_diagnostic}")