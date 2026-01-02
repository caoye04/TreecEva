from collections import defaultdict, Counter
import math

# Sensor simulation setup
def generate_signal(base_freq, sample_rate, duration):
    return [math.sin(2 * math.pi * base_freq * (i / sample_rate)) for i in range(int(duration * sample_rate))]

# Irrelevant helper function - dead code path
def deprecated_normalization(x):
    mean_val = sum(x) / len(x)
    std_val = (sum((i - mean_val) ** 2 for i in x) / len(x)) ** 0.5
    return [(i - mean_val) / std_val for i in x]

# Unused signal processing chain
def legacy_filter_chain(signal):
    filtered = [x * 0.9 for x in signal]
    return [abs(y) for y in filtered if y > 0.1]

# Core diagnostic engine
def preprocess_sensor_array(raw_readings):
    temp_store = []
    magnitude_sum = 0.0
    
    for idx, val in enumerate(raw_readings):
        if idx % 3 == 0:
            adjusted = abs(val) ** 1.5
        elif idx % 4 == 0:
            adjusted = val ** 2
        else:
            adjusted = abs(val) + 0.1
        
        magnitude_sum += adjusted
        temp_store.append(adjusted)
    
    avg_magnitude = magnitude_sum / len(temp_store)
    return [x / avg_magnitude for x in temp_store]

# Red herring: unused statistical analysis
def compute_entropy(values):
    counter = Counter([round(v, 1) for v in values])
    total = sum(counter.values())
    return -sum((count / total) * math.log2(count / total) for count in counter.values())

# Distractor data structure
class DiagnosticCache:
    def __init__(self):
        self.history = defaultdict(list)
        self.flags = set()
    
    def add_entry(self, tag, value):
        self.history[tag].append(value)
    
    def get_stats(self):
        return {k: len(v) for k, v in self.history.items()}

# Unused anomaly detector
def detect_spike_pattern(sequence, window=5):
    spikes = 0
    for i in range(len(sequence) - window):
        window_vals = sequence[i:i+window]
        if max(window_vals) > 2 * (sum(window_vals) / len(window_vals)):
            spikes += 1
    return spikes > 3

# Main processing pipeline
def analyze_readings(normalized_data, thresholds):
    result_map = defaultdict(int)
    phase_accumulator = 0.0
    event_counter = 0
    
    # Complex conditional logic with nested dependencies
    for i, reading in enumerate(normalized_data):
        if i == 0:
            continue
        
        diff = abs(reading - normalized_data[i-1])
        if diff > thresholds['delta']:
            phase_accumulator += diff * 1.7
            if i % 2 == 0:
                phase_accumulator = math.sqrt(abs(phase_accumulator))
            
            if phase_accumulator > thresholds['phase_cap']:
                event_counter += 1
                phase_accumulator *= 0.6
        
        # Secondary condition chain with bit manipulation red herring
        binary_tag = int(reading * 100) & 0xFF
        parity_check = bin(binary_tag).count('1') % 2
        
        if parity_check == 1 and reading > thresholds['parity_floor']:
            result_map['flagged'] += 1
        else:
            result_map['normal'] += 1
    
    # Tertiary integration step
    base_score = event_counter * 13
    adjustment = 0
    
    if result_map['flagged'] > 0:
        adjustment = int(math.log(result_map['flagged'] + 1) * 5)
    
    final_diagnostic = base_score + adjustment + int(phase_accumulator)
    
    # Dead assignment - irrelevant to final result
    debug_snapshot = {
        'last_diff': diff if 'diff' in locals() else 0,
        'final_map': dict(result_map)
    }
    
    return final_diagnostic

# Misleading auxiliary computation
unused_aggregate = []
for i in range(8):
    unused_aggregate.append((i * 1.5) ** 2.1)

# Threshold configuration (some values are decoys)
threshold_config = {
    'delta': 0.45,
    'phase_cap': 2.1,
    'parity_floor': 0.33,
    'deprecated_limit': 0.8  # Unused
}

# Simulate raw sensor input
raw_sensor_data = generate_signal(0.7, 25, 4)

# Process through relevant pipeline
processed_data = preprocess_sensor_array(raw_sensor_data)

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_config)

# Print target result
print(f"Result: {final_diagnostic}")