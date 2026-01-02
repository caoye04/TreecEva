from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data processing with red herrings and complex flow
def preprocess_sensors(raw_readings):
    processed = []
    noise_floor = 0.003
    scaling_factor = 2.718
    temp_buffer = []

    for reading in raw_readings:
        if reading < 0:
            adjusted = abs(reading) * scaling_factor
        else:
            adjusted = reading + noise_floor

        temp_buffer.append(adjusted)

    filtered = [x for x in temp_buffer if x > 0.01]
    normalized = [round(x / sum(filtered), 6) for x in filtered]

    # Distractor: unused smoothing path
    smoothed = []
    for i in range(len(normalized)):
        if i == 0 or i == len(normalized) - 1:
            smoothed.append(normalized[i])
        else:
            smoothed.append((normalized[i-1] + normalized[i] + normalized[i+1]) / 3)

    return normalized  # Actual return; smoothed is a red herring


def transform_sequence(seq, key_offset):
    # Bit manipulation mixed with arithmetic
    shifted = [(x << 2) ^ key_offset for x in seq]
    wrapped = [x % 100 for x in shifted]
    inverted = [99 - x for x in wrapped]
    return inverted

# Irrelevant auxiliary function (decoy)
def calculate_entropy(data_list):
    freqs = Counter(data_list)
    total = len(data_list)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 4)

# Another decoy: dead code path
unused_states = ['idle', 'calibrating', 'error']
current_state_index = 0
temporary_cache = defaultdict(list)

for idx in range(3):
    temporary_cache[unused_states[current_state_index]].append(idx * 100)
    current_state_index = (current_state_index + 1) % 3

# Core analysis logic
def analyze_pattern(data, config):
    base_value = 0
    mode_toggles = 0
    history = []

    for i, val in enumerate(data):
        if i % 5 == 0:
            base_value += val * (i + 1)
        elif i % 3 == 0:
            base_value -= val
        else:
            base_value ^= val  # Bitwise XOR as part of computation

        if val > config['limit']:
            mode_toggles += 1
            if mode_toggles > config['max_toggles']:
                break

        history.append(base_value)

    # Introduce linear search in history (real use)
    found = False
    position = 0
    for j, h_val in enumerate(history):
        if h_val > config['threshold'] and h_val % 2 == 0:
            position = j
            found = True
            break

    if not found:
        position = -1

    # Final transformation using multiple concepts
    adjustment = len(history) // (position + 1) if position != -1 else 1
    final_score = base_value + adjustment * mode_toggles

    # Red herring: unused complex structure
    diagnostics_log = {
        'raw_length': len(data),
        'toggles_recorded': mode_toggles,
        'history_peak': max(history) if history else 0,
        'computed_at': 'simulated_timestamp',
        'debug_matrix': [[i * j for j in range(3)] for i in range(3)]
    }

    return int(final_score)

# Main execution flow
if __name__ == '__main__':
    # Initial sensor input (real data source)
    raw_input_stream = [0.1, -0.05, 0.3, 0.02, -0.01, 0.4, 0.03, 0.2, -0.005, 0.5]
    
    # Step 1: Preprocess sensor readings
    cleaned_data = preprocess_sensors(raw_input_stream)
    indexed_stream = [int(x * 1000) for x in cleaned_data]  # Convert to integers for bit ops

    # Step 2: Transform with key offset
    transformed_data = transform_sequence(indexed_stream, key_offset=13)

    # Step 3: Configuration setup
    thresholds = {
        'limit': 85,
        'max_toggles': 3,
        'threshold': 200
    }

    # Step 4: Analyze pattern (key statement)
    final_diagnostic = analyze_pattern(transformed_data, thresholds)

    # Print result as required
    print(f"Target result: {final_diagnostic}")