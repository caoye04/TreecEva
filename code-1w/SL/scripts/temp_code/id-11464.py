import math

# Simulated sensor array data from environmental monitoring station
def acquire_sensor_data():
    raw_values = [127, 255, 192, 64, 224, 32, 160, 96]
    timestamps = [1623456780 + i*30 for i in range(len(raw_values))]
    return list(zip(timestamps, raw_values))

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_compatibility_mode(data):
    conversion_map = {i: val * 0.01 for i, val in enumerate([50, 100, 200, 400])}
    adjusted = []
    for item in data:
        ts, val = item
        if val > 200:
            adjusted.append((ts, val * conversion_map[2]))
        else:
            adjusted.append((ts, val * conversion_map[0]))
    return adjusted

# Signal normalization with bit manipulation (relevant)
def normalize_signal(value):
    if value == 0:
        return 0
    normalized = (value & 255) ^ 128  # XOR flip middle bits
    normalized = abs(normalized - 64)
    return max(1, min(normalized, 100))  # clamp to 1-100

# Apply exponential smoothing (relevant)
def smooth_sequence(seq):
    alpha = 0.3
    smoothed = []
    for i, val in enumerate(seq):
        if i == 0:
            smoothed.append(val)
        else:
            smoothed.append(alpha * val + (1 - alpha) * smoothed[i-1])
    return [round(x, 2) for x in smoothed]

# Redundant transformation – looks important but unused later (distractor)
def generate_frequency_bands(signal_list):
    bands = {'low': [], 'mid': [], 'high': []}
    for val in signal_list:
        if val < 30:
            bands['low'].append(val ** 0.5)
        elif val < 70:
            bands['mid'].append(math.log(val + 1))
        else:
            bands['high'].append(math.sin(val))
    return bands

# Core processing pipeline
processed_signals = []
def process_sensor_array():
    global processed_signals
    data_pairs = acquire_sensor_data()
    
    # Extract and normalize values using bitwise logic
    extracted = [pair[1] for pair in data_pairs]
    normalized = [normalize_signal(val) for val in extracted]
    
    # Apply smoothing filter
    filtered = smooth_sequence(normalized)
    
    # Additional irrelevant scaling (distractor)
    scaled_distractor = [x * 1.75 for x in filtered if x > 50]
    temp_offset = sum(scaled_distractor) / 100 if scaled_distractor else 0.0
    
    # Final relevant assignment
    processed_signals = [int(round(x)) for x in filtered]

# Recursive diagnostic analyzer (relevant)
def analyze_readings(readings):
    def recursive_score(lst, index=0, acc=0):
        if index >= len(lst):
            return acc
        current = lst[index]
        if current % 2 == 0:
            acc += current // 4
        else:
            acc -= current % 7
        return recursive_score(lst, index + 1, acc)
    
    # Decoy branch that doesn't execute (short-circuit distractor)
    score_modifier = 0
    if len(readings) > 20 and (sum(readings) / len(readings)) > 150:
        score_modifier = 100  # never reached
    
    base_score = recursive_score(readings)
    return base_score + 10  # fixed offset

# Unused data structure – creates confusion (distractor)
class DiagnosticBuffer:
    def __init__(self, size):
        self.data = [None] * size
        self.ptr = 0
    
    def push(self, val):
        self.data[self.ptr] = val
        self.ptr = (self.ptr + 1) % len(self.data)

# Misleading intermediate calculation (distractor)
shadow_analysis = 0
def compute_shadow_diagnostic(signal_list):
    global shadow_analysis
    total_bits = 0
    for val in signal_list:
        temp = val
        while temp:
            total_bits += temp & 1
            temp >>= 1
    shadow_analysis = total_bits * 2 - 5

# Main execution flow
if __name__ == "__main__":
    process_sensor_array()
    
    # Call to irrelevant function (distractor)
    dummy_data = [(1000, 50), (1030, 75)]
    legacy_output = legacy_compatibility_mode(dummy_data)
    
    # Another red herring
    freq_components = generate_frequency_bands(processed_signals)
    
    # Compute misleading shadow result
    compute_shadow_diagnostic(processed_signals)
    
    # Key statement: this determines the actual answer
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print required output
    print(f"Result: {final_diagnostic}")