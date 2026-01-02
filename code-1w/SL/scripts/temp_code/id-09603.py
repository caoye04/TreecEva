import math

# Simulated sensor data processing with red herrings and distractions
def analyze_pattern(sequence):
    if len(sequence) < 5:
        return 0
    count_peaks = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]:
            count_peaks += 1
    return count_peaks

# Distractor function: looks relevant but unused in final path
def compute_entropy(data):
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0.0
    total = len(data)
    for v in freq_map.values():
        p = v / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Another decoy: operates on strings but not used in critical path
def decode_sequence(token_list):
    decoded = []
    for token in token_list:
        if token.isdigit():
            decoded.append(str(int(token) % 10))
        else:
            cleaned = ''.join(sorted(set(token.lower())))
            decoded.append(cleaned[:3])
    return '_'.join(decoded)

# Core transformation pipeline (key logic buried among distractions)
def transform_signal(raw):
    stage_one = [x * 1.5 for x in raw if x > 0]
    stage_two = [int(y) for y in stage_one]
    normalized = [z / max(stage_two) * 100 for z in stage_two]
    filtered = [w for w in normalized if w >= 10]
    return sorted(filtered, reverse=True)

# Main processing function that actually gets called
def process_signal(data, limit):
    temp_result = 0
    adjustment_factor = 0.85
    
    # Real computation begins
    for val in data:
        if val > limit:
            temp_result += math.sqrt(val) * adjustment_factor
        elif val == limit:
            temp_result += val / 20
        else:
            continue
    
    # Red herring: modifies a local copy that isn't used
    shadow_copy = [v * 0.95 for v in data]
    fake_peak = analyze_pattern(shadow_copy)
    _ = fake_peak  # Unused
    
    # Another distraction: string manipulation unrelated to numeric output
    diagnostic_tag = "SIG_{}".format(len(data))
    diagnostic_tag = diagnostic_tag.replace('_', '').lower()
    tag_sum = sum(ord(c) for c in diagnostic_tag) % 100
    
    # Final adjustment using irrelevant tag_sum as decoy influence (but actually doesn't affect result)
    final_value = int(temp_result + 17)  # +17 is key, tag_sum is red herring
    return final_value

# Irrelevant global variables (distractors)
BASELINE_READINGS = [0.1, 0.4, 0.7, 1.3, 2.2]
CALIBRATION_MODE = True
MAX_BUFFER_SIZE = 512
active_filters = ['lowpass', 'notch']

# Seemingly important setup code (but mostly noise)
raw_sensor_stream = [-3, -1, 0, 4, 8, 12, 9, 15, 18, 7]
decoded_tokens = ['A12', 'B7', 'C15', 'X9']

# More distractions
encoded_ref = ''.join([t[0] for t in decoded_tokens]).lower()
if encoded_ref.startswith('a'):
    encoded_ref = encoded_ref[::-1]

# Actual execution begins here
transformed_data = transform_signal(raw_sensor_stream)
threshold = 50

# Key statement where answer is determined
final_output = process_signal(transformed_data, threshold)

# Print required output
print(f"Result: {final_output}")