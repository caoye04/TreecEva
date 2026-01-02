import math

# Simulated sensor readings (irrelevant preprocessing)
raw_readings = [127, 63, 255, 91, 182, 44, 133, 77]
scaled_values = [x * 0.01 for x in raw_readings if x > 50]  # Distractor: not used later
temp_buffer = list(map(lambda x: (x + 10) ** 0.5, raw_readings))  # Dead path

# Core signal processing chain
binary_frames = [f'{x:08b}' for x in raw_readings]
bit_inverted = []
for frame in binary_frames:
    inverted = ''.join('1' if b == '0' else '0' for b in frame)
    bit_inverted.append(int(inverted, 2))

# Noise thresholding (distractor block)
mean_val = sum(raw_readings) / len(raw_readings)
std_dev = (sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)) ** 0.5
outlier_mask = [abs(x - mean_val) > 1.5 * std_dev for x in raw_readings]  # Unused mask

# Relevant data transformation starts here
parity_check = [bin(x).count('1') % 2 == 0 for x in bit_inverted]
corrected_signals = [bit_inverted[i] ^ 0xFF if not parity_check[i] else bit_inverted[i] for i in range(len(bit_inverted))]

# Signal filtering based on dynamic condition
threshold = 128
filtered_data = [x for x in corrected_signals if x > threshold]

# Decoy function - looks important but unused
def analyze_entropy(data):
    hist = {}
    for d in data:
        hist[d] = hist.get(d, 0) + 1
    return -sum((freq / len(data)) * math.log2(freq / len(data)) for freq in hist.values())

# Auxiliary calculation with misleading intermediate result
aggregate_metric = sum(math.sin(x * 0.1) for x in raw_readings)  # Looks analytical, not used

# Critical processing function
def process_signals(signals):
    if not signals:
        return -1
    
    # Accumulation with alternating weights
    weighted_sum = 0
    for idx, val in enumerate(signals):
        weight = 1.5 if idx % 2 == 0 else 0.5
        weighted_sum += val * weight
    
    # Secondary adjustment using modulo chaining
    adjusted = weighted_sum % 1000
    
    # Final nonlinear transformation
    result = int((adjusted ** 0.5) * 3) if adjusted > 250 else int(adjusted / 2)
    
    # Red herring: complex bit mixing (unused)
    decoy_result = 0
    for s in signals:
        decoy_result ^= (s << 1) ^ (s >> 2)
    decoy_result = decoy_result & 0xFFFF
    
    return result

# Key execution point
final_output = process_signals(filtered_data)

# Output the target result
print(f"Result: {final_output}")