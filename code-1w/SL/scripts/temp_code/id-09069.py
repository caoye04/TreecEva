from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic logic
def preprocess_stream(raw_readings):
    normalized = []
    scaling_factor = 1.78
    offset = 0.22
    for val in raw_readings:
        if val > 100:
            val = 100
        elif val < 0:
            val = 0
        corrected = (val * scaling_factor + offset) % 97
        normalized.append(int(corrected))
    return normalized

# Irrelevant helper - dead code path
def deprecated_filter(sequence):
    return [x for x in sequence if x % 3 != 0]

# Signal pattern analyzer
def generate_pattern_key(sequence):
    freq_map = defaultdict(int)
    for item in sequence:
        freq_map[item] += 1
    sorted_items = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))
    return [k for k, _ in sorted_items[:5]]

# Misleading intermediate computation - looks important but unused later
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

# Core transformation: bit manipulation and masking
def apply_convolution(signal, kernel):
    result = []
    kern_len = len(kernel)
    sig_len = len(signal)
    padded = [0] * (kern_len // 2) + signal + [0] * (kern_len // 2)
    
    for i in range(sig_len):
        weighted_sum = 0
        for j in range(kern_len):
            weighted_sum += padded[i + j] * kernel[j]
        result.append(weighted_sum % 101)
    return result

# Fault detection using XOR-based signature
def detect_anomalies(pattern, threshold=45):
    signature = 0
    for i, val in enumerate(pattern):
        if i % 2 == 0:
            signature ^= (val & 15)
        else:
            signature ^= ((val >> 2) & 7)
    return signature > threshold

# Main analysis function with multiple concerns
def analyze_signal(buffer, mask_flag):
    # Step 1: Filter and compress signal
    filtered = [x for x in buffer if x % 2 == 1]  # Keep only odd values
    
    # Step 2: Frequency counting with defaultdict
    count_log = defaultdict(int)
    for num in filtered:
        count_log[num] += 1
    
    # Step 3: Build frequency-weighted array
    weighted_vals = []
    for num in filtered:
        weight = count_log[num]
        transformed = (num * weight + 7) % 89
        weighted_vals.append(transformed)
    
    # Step 4: Apply cyclic shift based on mask
    if mask_flag:
        shift_amount = sum(weighted_vals[:3]) % len(weighted_vals)
        shifted = weighted_vals[shift_amount:] + weighted_vals[:shift_amount]
    else:
        shifted = weighted_vals[::-1]
    
    # Step 5: Compute diagnostic hash via bitwise reduction
    accumulator = 0
    for i, val in enumerate(shifted):
        if i % 3 == 0:
            accumulator += val ^ 23
        elif i % 3 == 1:
            accumulator -= (val & 17)
        else:
            accumulator += (val | 5)
    
    # Final adjustment
    final_score = abs(accumulator) % 10000
    
    # Decoy calculation that appears related but isn't used
    dummy_diagnostic = 0
    for x in shifted:
        dummy_diagnostic = (dummy_diagnostic * 31 + x) % 997
    
    # Critical red herring: function call that does nothing to final result
    _ = compute_entropy(buffer)
    
    return final_score

# Simulated input data
raw_sensor_data = [84, 23, 56, 71, 42, 67, 93, 15, 56, 29, 88, 71, 34, 23, 71]

# Preprocessing stage
processed_signal = preprocess_stream(raw_sensor_data)

# Generate auxiliary pattern key (unused red herring)
pattern_key = generate_pattern_key(processed_signal)

# Convolution kernel - irrelevant to final outcome
kernel_weights = [1, -1, 2, -2, 1]
convolved_output = apply_convolution(processed_signal, kernel_weights)

# Fault mask activation based on anomaly check (actually always True but obscured)
fault_trigger = detect_anomalies(processed_signal, threshold=40)

# Build pattern buffer using complex logic
pattern_buffer = []
for idx, val in enumerate(processed_signal):
    if idx % 4 == 0:
        pattern_buffer.append((val + idx) % 97)
    elif idx % 4 == 1 and val > 30:
        pattern_buffer.append(val - 10)
    elif idx % 4 == 2:
        pattern_buffer.append((val * 2) % 83)
    else:
        pattern_buffer.append(val)

# Additional distraction: unused statistical summary
stats_summary = {
    'mean': sum(pattern_buffer) / len(pattern_buffer),
    'mode': Counter(pattern_buffer).most_common(1)[0][0],
    'range': max(pattern_buffer) - min(pattern_buffer)
}

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, fault_mask=fault_trigger)

# Output result
print(f"Target result: {final_diagnostic}")