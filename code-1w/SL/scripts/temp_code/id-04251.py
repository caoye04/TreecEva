import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(size):
    return [i * 0.5 + (i % 7) for i in range(size)]

def apply_filter(data):
    filtered = []
    for x in data:
        if x > 10:
            filtered.append(x * 0.9)
        elif x > 5:
            filtered.append(x * 0.95)
        else:
            filtered.append(x)
    return filtered

def shift_phase(signal, offset=3):
    # Irrelevant phase manipulation
    return [(math.sin(x) + offset) for x in signal]

def generate_checksum(sequence):
    # Unused checksum function - red herring
    return sum([hash(str(x)) % 100 for x in sequence]) % 97

def encode_metadata(key_values):
    # Distractor: encodes nothing relevant
    encoded = ''
    for k, v in key_values.items():
        encoded += f'{k[0]}{len(str(v))}'
    return encoded.upper().replace("0", "X")

def transform_readings(raw):
    # Applies non-linear transformation
    return [math.log(abs(x) + 1) * 2.5 for x in raw]

def count_outliers(data, limit=10.0):
    # Misleading: used to distract from main logic
    return len([x for x in data if abs(x) > limit])

def recursive_reduce(value, depth):
    if depth <= 0 or value < 1:
        return value
    return recursive_reduce(value / 2 + 1, depth - 1)

def analyze_signal(data, cutoff):
    total = 0
    for val in data:
        if val > cutoff:
            total += recursive_reduce(val, 3)
    return int(total)

# Main execution flow
sample_size = 50
data_log = {'sensor': 'SNSR-7A', 'version': '2.1.0', 'active': True}

raw_signal = collect_samples(sample_size)
filtered_signal = apply_filter(raw_signal)

# Irrelevant metadata encoding (distractor)
meta_tag = encode_metadata(data_log)

transformed_data = transform_readings(filtered_signal)

# Dead code path - never called
checksum = generate_checksum(transformed_data)

# Unused outlier count
spikes = count_outliers(transformed_data, 12)

# Apply meaningless phase shift (no impact on result)
phase_shifted = shift_phase(transformed_data)

# Key threshold based on transformed data characteristics
dynamic_base = sum(transformed_data[:5]) / 5
threshold = math.sqrt(dynamic_base) * 1.5

# Final diagnostic calculation
final_diagnostic = analyze_signal(transformed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")