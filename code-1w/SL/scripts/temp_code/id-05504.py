import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Decoy transformation with misleading intermediate result
def decoy_transform(seq):
    temp = [int(math.sin(x) * 100) for x in seq]
    offset = sum(temp) % 7
    return [t + offset for t in temp]

# Real transformation function used in logic
transform_fn = lambda arr: [((x << 1) ^ 0xA) & 0xF for x in arr]

# Simulated sensor data sequence (base input)
sensor_readings = [12, 8, 3, 15, 6, 1, 10]

# Irrelevant derived sequence (distractor)
stale_readings = [r // 2 for r in sensor_readings if r > 5]

# Key control parameter computed via bit logic
activation_mask = sum([(r & (r - 1)) == 0 for r in sensor_readings])  # count powers of two

# Initial data transformation (relevant)
encoded_signal = transform_fn(sensor_readings)

# Secondary transformation using logical shifts and XOR
modulated_signal = [(x >> 1) ^ 5 for x in encoded_signal]

# Construct key_sequence based on conditional pattern matching
key_sequence = []
for val in modulated_signal:
    if val < 7:
        key_sequence.append(val * 3)
    elif val == 7:
        key_sequence.append(42)  # red herring value
    else:
        key_sequence.append(val - 4)

# Unused alternate sequence (misleading path)
alternate_seq = [val for val in key_sequence if val != 42]

# Apply filtering mask based on activation level
filtered_sequence = []
mask_enabled = (activation_mask > 2)
if mask_enabled:
    filter_threshold = 6
    for i, v in enumerate(key_sequence):
        if i % 2 == 0 or v > filter_threshold:
            filtered_sequence.append(v)
else:
    filtered_sequence = key_sequence[:3]

# Transform into frequency domain analog (irrelevant complex computation)
def fake_fourier_magnitude(signal):
    magnitude = 0
    for k in range(len(signal)):
        real = sum([signal[n] * math.cos(2 * math.pi * k * n / len(signal)) for n in range(len(signal))])
        magnitude += abs(real)
    return round(magnitude, 3)

# Distractor variable with plausible but unused result
phantom_diagnostic = fake_fourier_magnitude(filtered_sequence)

# Actual core analysis function
def analyze_pattern(data, reference):
    accumulator = 0
    ref_set = set(reference)
    for idx, d in enumerate(data):
        if d in ref_set:
            accumulator += idx * d
        else:
            accumulator -= (d ^ idx)
    
    # Additional logic layer: check parity chain
    parity_chain = all((data[i] + data[i+1]) % 2 == 1 for i in range(len(data)-1))
    if parity_chain:
        accumulator *= 2
    
    # Final adjustment using bitwise reduction
    final_bit = 0
    for d in data:
        final_bit ^= (d & 7)
    accumulator += final_bit

    return accumulator

# Transform sensor data into working form
transformed_data = [((x + 3) | 5) & 0xF for x in sensor_readings]  # apply bit mask pipeline

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, key_sequence)

print(f"Result: {final_diagnostic}")