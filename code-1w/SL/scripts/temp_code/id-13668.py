from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor: not all fields are used)
sensor_feeds = {
    'temp': [23.4, 24.1, 22.9, 25.0, 23.8],
    'pressure': [101.3, 100.7, 102.1, 99.8, 100.5],
    'vibration': [0.05, 0.07, 0.04, 0.12, 0.09],
    'humidity': [45, 47, 44, 50, 46]
}

# Irrelevant preprocessing: dead code path (never called)
def analyze_trend(data_list):
    trend_score = 0
    for i in range(1, len(data_list)):
        if data_list[i] > data_list[i-1]:
            trend_score += 1
        elif data_list[i] < data_list[i-1]:
            trend_score -= 1
    return abs(trend_score)

# Decoy function with misleading name (not part of final calculation)
def compute_health_index_v1(readings):
    base = sum(readings) / len(readings)
    variance = sum((x - base) ** 2 for x in readings) / len(readings)
    return base - variance * 0.5

# Real processing begins here
baseline_ref = [0.04, 0.06, 0.03, 0.10, 0.08]

# Extract relevant signal (subset of distractor data)
vibration_signal = sensor_feeds['vibration']

# Apply windowed filtering (slicing operation)
window_size = 3
smoothed = [
    sum(vibration_signal[i:i+window_size]) / window_size
    for i in range(len(vibration_signal) - window_size + 1)
]

# Generate bit signature from smoothed peaks (bitwise operations)
peak_mask = []
for val in smoothed:
    if val > 0.07:
        peak_mask.append(1)
    else:
        peak_mask.append(0)

# Convert to integer via binary interpretation
bit_sequence = ''.join(map(str, peak_mask))
bit_interpretation = int(bit_sequence, 2) if bit_sequence else 0

# Create frequency profile (using Counter)
freq_profile = Counter(smoothed)
unique_values = len(freq_profile)

# Construct health signature using multiple concepts
health_signature = [
    len(smoothed),
    round(sum(smoothed), 2),
    unique_values,
    bit_interpretation
]

# Auxiliary lambda for dynamic thresholding (not directly used but looks important)
dynamic_threshold = lambda x, ref: x > (sum(ref) / len(ref)) * 1.1

# Actual core logic hidden among distractions
def process_metrics(metrics, reference):
    # metrics[0] = length of smoothed signal → 3
    # metrics[1] = sum of smoothed → 0.21 + 0.17 + 0.25 = 0.63 → rounded to 0.63
    # metrics[2] = unique values in smoothed → {0.21, 0.17, 0.25} → 3
    # metrics[3] = bit_interpretation → peak_mask = [0,1,1] → '011' → 3
    
    a = metrics[0]  # 3
    b = int(round(metrics[1] * 100))  # 63
    c = metrics[2]  # 3
    d = metrics[3]  # 3
    
    # Complex conditional expression with XOR obfuscation
    intermediate = (a + b) if a > 2 else (b - a)
    intermediate ^= c  # 66 ^ 3 = 65
    intermediate += d  # 68
    
    # Nested conditionals with red herring variables
    adjustment_factor = 0
    if intermediate % 2 == 0:
        adjustment_factor += 1
    if intermediate > 50:
        adjustment_factor += 2  # now 3
    if d == 3:
        adjustment_factor *= 2  # now 6
    
    # Final computation chain
    result = intermediate + adjustment_factor  # 68 + 6 = 74
    
    # Dead code branch (never reached due to prior logic)
    if False and len(reference) > 10:
        fallback = sum(reference) * 1000
        result = fallback if result < 0 else result // 2
    
    # Destructuring distraction (tuple unpacking with unused vars)
    p, q, r = (result, result*2, result//2)  # q and r unused
    
    # Final transformation using slicing on string representation
    str_result = str(result)  # '74'
    reversed_part = str_result[::-1]  # '47'
    final_numeric = int(reversed_part)  # 47
    
    # One last twist: XOR with length of original baseline_ref
    final_diagnostic = final_numeric ^ len(baseline_ref)  # 47 ^ 5 = 48
    
    return final_diagnostic

# Key execution point
final_diagnostic = process_metrics(health_signature, baseline_ref)
print(f"Target result: {final_diagnostic}")