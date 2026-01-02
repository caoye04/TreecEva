from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data processing pipeline with decoy components
def load_calibration_data():
    # Irrelevant calibration loading (dead end)
    return {chr(i): i - 97 for i in range(97, 123)}

def generate_noise_profile(length):
    # Distractor: generates noise but never used in final computation
    return [i ^ 255 for i in range(length) if i % 7 != 0]

def accumulate_signal(raw_samples):
    # Real signal path: integrate valid pulses
    accumulator = 0
    pulse_count = 0
    for val in raw_samples:
        if val < 0:
            continue
        if val % 3 == 0 and val % 5 != 0:
            accumulator += val >> 1
            pulse_count += 1
    return accumulator, pulse_count

def filter_artifacts(data_stream):
    # Misleading preprocessing that appears important
    filtered = []
    for x in data_stream:
        if x in [17, 23, 42]:  # arbitrary magic numbers as red herring
            continue
        if x > 100:
            x = x // 3
        filtered.append(x ^ 1)
    return filtered

def temporal_shift(sequence, steps):
    # Unused transformation - looks relevant due to name
    cycled = cycle(sequence)
    shifted = list(islice(cycled, steps, steps + len(sequence)))
    return shifted

def analyze_harmonics(signal):
    # Dead-end analysis function (never called in execution path)
    harmonics = defaultdict(int)
    for i, s in enumerate(signal):
        harmonics[i % 4] += s
    return dict(harmonics)

# Main processing chain
raw_input = [24, -5, 18, 63, 45, 12, 99, 36, 72, 50, 81]

# Step 1: Accumulate valid signal segments
energy_total, detected_pulses = accumulate_signal(raw_input)

# Step 2: Apply masking via bitwise interaction (relevant)
dynamic_mask = (energy_total & 0xFF) ^ detected_pulses
modulated_energy = energy_total + (dynamic_mask << 2)

# Step 3: Buffer construction using slicing and filtering (partial relevance)
signal_slice = raw_input[1:8:2]  # Extract every other element starting at index 1
extended_buffer = signal_slice + [detected_pulses]
cleaned_buffer = [x for x in extended_buffer if x % 2 == 0]  # Only even values retained

# Step 4: Construct frequency-weighted sum (core logic)
frequency_weights = {
    0: 1.0,
    1: 0.85,
    2: 0.72,
    3: 0.6,
    4: 0.5
}

weighted_sum = 0
for idx, val in enumerate(cleaned_buffer):
    weight_key = idx % 5
    weighted_sum += val * frequency_weights[weight_key]

# Step 5: Final nonlinear transformation
intermediate_state = int(weighted_sum) ^ modulated_energy

# Step 6: Signal normalization through modular constraint
if intermediate_state > 10000:
    normalized_state = intermediate_state % 9763
else:
    normalized_state = intermediate_state % 4871  # Actual path taken

# Step 7: Phase output determination via conditional mapping
if normalized_state < 2000:
    phase_shift = 3
elif normalized_state < 4000:
    phase_shift = 5
else:
    phase_shift = 7

# Key statement
phase_output = (normalized_state << 1) | phase_shift

# Irrelevant counters and logs (distractors)
log_table = Counter(['A', 'B', 'B', 'C', 'D', 'D', 'D'])
diagnostic_trace = defaultdict(lambda: 'OK')
diagnostic_trace['SENSOR_1'] = 'NOISE_HIGH'
diagnostic_trace['SENSOR_2'] = 'CALIBRATING'

# Unused transformations
unused_buffer = temporal_shift(raw_input, 3)
noise_model = generate_noise_profile(50)

# Output target result
print(f"Result: {phase_output}")