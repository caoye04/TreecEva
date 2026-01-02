import math

# Simulated sensor data with noise and metadata
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9]
humidity_readings = [45, 48, 50, 55, 60, 53, 49]
pressure_readings = [1013, 1012, 1015, 1016, 1018, 1017, 1014]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 0.78
scaling_factor = 1.02
buffer_cache = {'temp': [], 'humid': []}
redundant_flag = True
debug_mode = False

# Misleading preprocessing function (dead path)
def legacy_normalize(data):
    return [x * 0.98 + 1.2 for x in data]

# Unused transformation chain
def transform_v1(x):
    return x ** 0.5

def transform_v2(x):
    return x * x

def transform_v3(x):
    return abs(x - 10) // 2

# Core processing components
def clean_data(stream):
    # Remove outliers using IQR method (simplified)
    sorted_vals = sorted(stream)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    filtered = [x for x in stream if lower_bound <= x <= upper_bound]
    return [round(x, 2) for x in filtered]

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 6)

def shift_cipher(text, shift):
    # Unused string method distractor
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Data mapping and categorization
category_map = {
    'stable': [],
    'fluctuating': [],
    'critical': []
}

status_flags = {i: 'OK' for i in range(len(temperature_readings))}

# Simulated data stream with metadata
data_stream = [
    {'id': f'D{i}', 't': temperature_readings[i], 'h': humidity_readings[i], 'p': pressure_readings[i]}
    for i in range(len(temperature_readings))
]

# Auxiliary dictionary operations (some irrelevant)
meta_tags = {}
for entry in data_stream:
    tag = entry['id']
    meta_tags[tag] = {
        'processed': False,
        'version': 'v2.1',
        'checksum': len(tag) + int(entry['t'])
    }

# Decoy loop with string manipulation
transformed_names = []
for i in range(3):
    name = f"SensorGroup_{chr(65+i)}"
    shifted = shift_cipher(name, 3)
    transformed_names.append(shifted.lower().replace('_', '-'))

# Real pipeline function with key logic buried among distractions
def process_pipeline(raw_data):
    cleaned_temps = clean_data([entry['t'] for entry in raw_data])
    cleaned_humid = clean_data([entry['h'] for entry in raw_data])
    
    # Derive composite index
    composite_scores = []
    for i in range(min(len(cleaned_temps), len(cleaned_humid))):
        score = (cleaned_temps[i] * 0.7) + (cleaned_humid[i] * 0.3)
        composite_scores.append(score)
    
    # Compute statistical entropy as system stability measure
    entropy_value = compute_entropy(composite_scores)
    
    # Apply hidden correction factor based on pressure median
    median_pressure = sorted([entry['p'] for entry in raw_data])[len(raw_data)//2]
    correction = (median_pressure - 1000) * 0.01
    
    # Key calculation path
    intermediate_result = entropy_value * 100 + correction
    
    # Distracting bit manipulation (unused)
    masked = int(intermediate_result) & 0xFF
    flipped = masked ^ 0b11110000
    
    # Final output derived from corrected entropy
    final_normalized = round(intermediate_result, 6)
    
    # Update metadata (side effect, not result)
    for tag in meta_tags:
        meta_tags[tag]['processed'] = True
        meta_tags[tag]['checksum'] = (meta_tags[tag]['checksum'] + 7) % 100
    
    # Red herring conditional
    if len(transformed_names) > 5:
        final_normalized -= 1000  # Never executed
    
    return final_normalized

# Execute main logic
final_output = process_pipeline(data_stream)

# Print result for evaluation
print(f"Result: {final_output}")