import itertools

# Simulate sensor data with noise and valid readings
def generate_sensor_stream():
    raw_readings = [12, -999, 34, -999, 56, 78, -999, 91, 104, -999, 115]
    return [x for x in raw_readings if x != -999]

# Irrelevant function: computes checksum but not used in main logic
def compute_checksum(data):
    checksum = 0
    for x in data:
        checksum = (checksum + x * 3) % 256
    return checksum

# Misleading transformation chain
def apply_filtering(signal):
    filtered = []
    for i in range(len(signal)):
        if i == 0:
            filtered.append(signal[i])
        else:
            # Exponential smoothing with arbitrary coefficient
            smoothed = 0.3 * signal[i] + 0.7 * filtered[i-1]
            filtered.append(int(smoothed))
    return filtered

# Unused decoy function that looks important
def analyze_pattern(seq):
    trends = []
    for a, b in zip(seq, seq[1:]):
        trends.append(1 if b > a else 0)
    return trends

# Core processing: extract every third element after offset
def extract_critical_band(data):
    offset = len(data) % 4
    band = []
    for i in range(offset, len(data), 3):
        band.append(data[i])
    return band

# Bit manipulation red herring
def scramble_bits(value):
    return ((value << 3) & 255) | ((value >> 5) & 255)

# Real transformation: modular arithmetic and accumulation
def transform_band(band_data):
    acc = 7
    result = []
    for val in band_data:
        acc = (acc * 11 + val) % 89
        result.append(acc)
    return result

# Recursive reduction (not actually needed but looks complex)
def recursive_sum(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Main processing pipeline
sensor_data = generate_sensor_stream()  # [12, 34, 56, 78, 91, 104, 115]
filtered_data = apply_filtering(sensor_data)  # Smoothed version

# Dead code path: this is computed but unused
checksum_val = compute_checksum(sensor_data)
trend_analysis = analyze_pattern(sensor_data)

# Actual relevant path starts here
selected_band = extract_critical_band(filtered_data)  # Take every 3rd from offset

# Apply transformation using string method as distraction (convert to str and back)
str_temp = ''.join([str(x) for x in selected_band])
digit_shift = int(str_temp[-1]) if str_temp else 0  # Use last digit

# Transform band with modular math
transformed_data = transform_band(selected_band)

# Add irrelevant bit scrambling (no effect on output)
scrambled_values = [scramble_bits(x) for x in transformed_data]

# Final computation
final_output = process_sequence(transformed_data) if 'process_sequence' in globals() else -1

# But we define it now — deferred definition as distraction
def process_sequence(seq):
    base = 1
    for num in seq:
        base = (base + num) * 2 % 100000
    return base

# Recompute final output correctly
final_output = process_sequence(transformed_data)

print(f"Result: {final_output}")