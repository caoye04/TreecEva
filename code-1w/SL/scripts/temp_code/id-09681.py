from collections import defaultdict
import itertools

# Simulate sensor signal processing with noise filtering and pattern detection
raw_data = [12, 15, 12, 18, 12, 21, 12, 15, 12, 18, 12]
noise_threshold = 3
base_reference = 12

def filter_noise(signal, base, threshold):
    return [x for x in signal if abs(x - base) <= threshold]

def count_transitions(data):
    transitions = 0
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            transitions += 1
    return transitions

def group_by_value(data):
    groups = defaultdict(list)
    for item in data:
        groups[item].append(item)
    return {k: len(v) for k, v in groups.items()}

def calculate_entropy(counts):
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return round(entropy, 4)

def detect_cycle_pattern(seq):
    # Detect if sequence has repeating sub-pattern
    for length in range(2, len(seq)//2 + 1):
        if len(seq) % length == 0:
            pattern = seq[:length]
            if all(seq[i:i+length] == pattern for i in range(0, len(seq), length)):
                return True, length
    return False, -1

def analyze_stability(ring_buffer):
    # Dummy analysis to add interference
    max_val = max(ring_buffer)
    min_val = min(ring_buffer)
    variance = sum((x - sum(ring_buffer)/len(ring_buffer))**2 for x in ring_buffer) / len(ring_buffer)
    return variance < 5

def generate_checksum(sequence):
    # Irrelevant checksum computation (distractor)
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val << (i % 4))
    return checksum % 1000

# Step 1: Filter out noise from raw sensor readings
filtered_signal = filter_noise(raw_data, base_reference, noise_threshold)

# Step 2: Count state transitions (important for stability metric)
transition_count = count_transitions(filtered_signal)

# Step 3: Group values to analyze distribution (used later)
value_distribution = group_by_value(filtered_signal)

dummy_list = [x * 2 for x in filtered_signal if x > 13]  # Dead-end list comprehension (distractor)

# Step 4: Detect repetition pattern in signal
has_cycle, cycle_length = detect_cycle_pattern(filtered_signal)

# Step 5: Compute auxiliary metrics (some irrelevant)
stability_flag = analyze_stability(filtered_signal)
irrelevant_checksum = generate_checksum(filtered_signal)

# Step 6: Calculate weighted balance score
balance_weights = []
for val, count in value_distribution.items():
    deviation = abs(val - base_reference)
    weight = count * (1 / (deviation + 1))
    balance_weights.append(weight)

weighted_sum = sum(balance_weights)
signal_length_factor = len(filtered_signal) / (cycle_length if has_cycle else 1)

# Step 7: Final equilibrium calculation
if transition_count < 5 and stability_flag:
    adjustment_factor = 1.2
else:
    adjustment_factor = 0.85

intermediate_metric = weighted_sum * signal_length_factor

# Introduce red herring conditional (never triggers due to data)
if len(dummy_list) > 10:
    intermediate_metric *= 1.5  # Dead code path

# Critical execution point
processed_signals = list(itertools.chain.from_iterable([filtered_signal]))
equilibrium_score = detect_equilibrium(processed_signals)

# Final function using filtered data
def detect_equilibrium(signal_sequence):
    raw_sum = sum(signal_sequence)
    norm_factor = len(signal_sequence) + 1e-8
    base_shift = base_reference * 0.5
    return int((raw_sum / norm_factor) - base_shift + adjustment_factor * 10)

print(f"Result: {equilibrium_score}")