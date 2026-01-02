import math

# Simulated biomedical signal processing system with red herrings
def analyze_waveform(signal):
    if len(signal) == 0:
        return 0
    peak = max(signal)
    trough = min(signal)
    amplitude = (peak - trough) / 2
    # Irrelevant transformation
    normalized = [x / (amplitude + 1e-9) for x in signal]
    power = sum(x**2 for x in normalized)
    return power

# Unused function - decoy
def compute_envelope(data):
    envelope = []
    for i in range(len(data)):
        envelope.append(abs(data[i]) * math.sin(i + 0.1))
    return [x for x in envelope if x > 0.5]

# Core logic disguised among distractions
def generate_baseline(length, seed=42):
    result = []
    value = seed
    for i in range(length):
        value = (value * 97 + 13) % 1000
        result.append(value / 100.0)
    return result

# Distractor: complex but unused data structure
class SignalBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
    
    def push(self, x):
        self.buffer.append(x % 100)
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)

    def stats(self):
        if not self.buffer:
            return 0, 0
        return sum(self.buffer), len(self.buffer)

# High-interference function with multiple concepts
baseline_readings = generate_baseline(12)
raw_signals = [[math.sin(j * 0.5 + i) for j in range(8)] for i in range(6)]

# Irrelevant aggregation
aggregated_power = sum(analyze_waveform(sig) for sig in raw_signals)
buffer = SignalBuffer(10)
for val in baseline_readings:
    buffer.push(val * 10)

# Real computation path begins here — obscured by prior noise
reference_set = {round(x, 1) for x in baseline_readings}
test_entries = [round(x * 1.05, 1) for x in baseline_readings]

# Use of set operations (required feature)
divergence_set = {x for x in test_entries} - reference_set
overlap_count = len({x for x in test_entries} & reference_set)

scaling_factor = 1.75 if len(divergence_set) > 4 else 2.25
adjusted_overlap = overlap_count * scaling_factor

# Lambda usage (required feature): filters and transforms test entries
filter_func = lambda x: x > 0.5 * scaling_factor
filtered_differences = list(filter(filter_func, [abs(a - b) for a, b in zip(test_entries, [x for x in reference_set])] + [scaling_factor]))

# Hidden critical variable construction
shift_register = 0b1101
for i in range(int(adjusted_overlap)):
    shift_register = ((shift_register << 1) | (shift_register >> 3)) & 0b1111

# Dictionary-based mapping - suggested paradigm
status_map = {
    0: 'critical',
    1: 'stable',
    2: 'active',
    3: 'monitoring',
    4: 'normal'
}

mode_key = len(divergence_set) % 5
operational_mode = status_map.get(mode_key, 'unknown')

# Composite diagnostic signature
health_signature = []
for i, base in enumerate(baseline_readings):
    temp_val = base * (i + 1)
    if i % 3 == 0:
        temp_val = math.cos(temp_val)
    elif i % 3 == 1:
        temp_val = abs(math.tanh(temp_val))
    else:
        temp_val = math.log(temp_val + 2)
    health_signature.append(round(temp_val, 3))

# Main processing function with nested logic
def process_metrics(signature, baseline):
    n = len(signature)
    cumulative = 0.0
    
    # Nested loops and conditionals (3-level nesting)
    for i in range(n):
        chunk_sum = 0
        for j in range(i + 1):
            if j < len(baseline):
                raw_contribution = signature[i] * baseline[j]
                if raw_contribution > 0.5:
                    # Bitwise distraction
                    masked = int(raw_contribution * 100) & 0xFF
                    chunk_sum += math.sqrt(masked) if masked > 0 else 0
                else:
                    chunk_sum += raw_contribution ** 2
        
        # Conditional expression (suggested paradigm)
        adjustment = chunk_sum / (i + 1) if i % 4 != 3 else chunk_sum * 0.75
        
        # Integer division and rounding
        bucket = int(adjustment) // 2
        rounded_adj = round(adjustment - bucket, 2)
        
        cumulative += rounded_adj * (i + 1)
    
    # Final transformation
    final_score = cumulative * 1000
    return int(final_score)  # Deterministic integer answer

# Key execution point
final_diagnostic = process_metrics(health_signature, baseline_readings)

# Print result as required
print(f"Target result: {final_diagnostic}")