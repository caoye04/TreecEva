import itertools

# Simulate sensor data with noise and redundant channels
def generate_sensor_stream():
    base_signal = [i * 0.5 + 2.0 for i in range(20)]
    noise_floor = [0.1 * (-1)**i for i in range(20)]
    redundant_copy = [x + 0.01 for x in base_signal]
    return list(zip(base_signal, noise_floor, redundant_copy))

# Irrelevant transformation: spectral analysis stub (dead-end)
def compute_spectral_power(signal):
    """Dummy function - never actually used in main logic"""
    return sum(x**2 for x in signal) / len(signal)

# Misleading pre-processing step with decoy output
def apply_noise_filter(data_stream):
    filtered = []
    temp_accum = 0.0
    for entry in data_stream:
        clean_val = entry[0] + entry[1]  # Attempt to cancel noise
        temp_accum += abs(entry[1])
        if temp_accum > 5.0:  # Impossible condition due to small noise values
            break
        filtered.append(clean_val)
    normalization_factor = max(filtered) if filtered else 1.0
    return [x / normalization_factor for x in filtered]

# Key transformation: extract and align relevant dimensions
def extract_primary_channel(data_stream):
    raw_values = [entry[0] for entry in data_stream]  # Only first channel matters
    offset_compensation = sum(raw_values[:5]) / 5 - 2.0  # Baseline drift correction
    return [x - offset_compensation for x in raw_values]

# Decoy state tracker (unused but plausible)
class StateMonitor:
    def __init__(self):
        self.events = []
        self.threshold_triggers = 0
    
    def check_anomaly(self, value):
        if value < 0 or value > 100:
            self.events.append('OUT_OF_RANGE')
            self.threshold_triggers += 1

# Unused recursive validator (red herring)
def validate_monotonicity(seq, idx=0):
    if idx >= len(seq) - 1:
        return True
    if seq[idx] > seq[idx + 1]:
        return False
    return validate_monotonicity(seq, idx + 1)

# Real processing chain begins here
def transform_sequence(primary_channel):
    # Apply moving average filter
    window_size = 3
    smoothed = []
    for i in range(len(primary_channel)):
        start = max(0, i - window_size + 1)
        segment = primary_channel[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    
    # Amplify every third element using bit manipulation
    amplified = []
    for i, val in enumerate(smoothed):
        if (i + 1) % 3 == 0:  # Every third index
            # Multiply by 8 using left bit shift
            amplified.append(val * (1 << 3))
        else:
            amplified.append(val)
    
    return amplified

# Core aggregation logic with early termination condition
def process_sequence(seq):
    running_total = 0.0
    magnitude_tracker = []  # Distractor: collected but unused
    
    for i, value in enumerate(seq):
        abs_val = abs(value)
        magnitude_tracker.append(abs_val)
        
        # Early exit logic based on threshold
        if abs_val > 50.0:
            running_total += value * 0.9
            break
        
        # Accumulate with conditional sign flip
        if i % 4 == 0 and i > 0:
            running_total -= value
        else:
            running_total += value
        
        # Spurious logical check (never triggers)
        if value < 0 and not (value > -10 and i < 5):
            pass  # Dead code branch
    
    # Final adjustment using logical flags
    high_magnitude_observed = any(m > 20 for m in magnitude_tracker)
    final_correction = -5.0 if (high_magnitude_observed and len(magnitude_tracker) > 10) else 3.0
    
    return running_total + final_correction

# Generate raw input
data_feed = generate_sensor_stream()

# Apply irrelevant filtering (result discarded)
discarded_intermediate = apply_noise_filter(data_feed)

# Begin actual computation path
primary_data = extract_primary_channel(data_feed)

temp_state = StateMonitor()  # Created but not utilized
for x in primary_data:
    temp_state.check_anomaly(x)  # No effect on output

# Transform data using key operations
decision_flag = len(primary_data) >= 15 and all(x >= 1.0 for x in primary_data[:10])
if decision_flag:
    transformed_data = transform_sequence(primary_data)
else:
    transformed_data = primary_data

# Introduce itertools distraction
grouped = [list(g) for k, g in itertools.groupby(transformed_data, key=lambda x: x > 0)]
flattened_groups = list(itertools.chain.from_iterable(grouped))  # Same as original order

# Final computation step
final_output = process_sequence(transformed_data)

# Output result
print(f"Result: {final_output}")