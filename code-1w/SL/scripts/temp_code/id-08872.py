import math

def analyze_phase_shift(frequency, amplitude, phase):
    # Irrelevant signal analysis function (dead end)
    if frequency <= 0:
        return 0
    angular_velocity = 2 * math.pi * frequency
    shifted = amplitude * math.sin(angular_velocity + phase)
    normalized = (shifted + 1) / 2
    return round(normalized * 100, 2)


def compute_entropy(data_stream):
    # Distractor: computes information entropy but not used in final result
    from collections import Counter
    counts = Counter(data_stream)
    total = len(data_stream)
    entropy = 0.0
    for k in counts:
        p = counts[k] / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)


def validate_timing_sequence(seq):
    # Misleading validation that looks important but is unused
    if not seq:
        return False
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            return False
    return True

# Simulated system telemetry
timing_log = [0.1, 0.3, 0.5, 0.9, 1.2, 1.7, 2.1]
sensor_data = [23.1, 24.5, 22.8, 25.0, 26.3, 27.1, 25.8]
error_flags = [False, False, True, False, False, True, False]

# Unused but plausible intermediate calculations
baseline_offset = sum(timing_log) / len(timing_log)
amplitude_profile = [math.sin(x * math.pi) for x in timing_log]
spike_count = len([x for x in sensor_data if x > 25.0])

# Core state variables
system_state = {
    'status': 'ACTIVE',
    'mode': 'DIAGNOSTIC',
    'cycle': 12,
    'flags': error_flags,
    'timestamp': 1729384756
}

# Decoy data structure
performance_matrix = [
    [i * j + 0.1 for j in range(4)] 
    for i in range(4)
]

# Auxiliary function with red herring logic
def generate_diagnostic_code(state, cycle):
    # Looks important but not called in critical path
    code = 0
    for c in state['mode']:
        code += ord(c)
    code ^= cycle
    return code % 999

# Key transformation pipeline
def extract_diagnostics(log, state):
    # Step 1: Filter intervals greater than 0.5 seconds
    long_intervals = [t for t in log if t > 0.5]
    
    # Step 2: Compute interval differences
    deltas = []
    for i in range(1, len(long_intervals)):
        deltas.append(long_intervals[i] - long_intervals[i-1])
    
    # Step 3: Apply exponential weighting
    weights = [math.exp(-0.5 * i) for i in range(len(deltas))]
    weighted_sum = 0.0
    for i in range(len(deltas)):
        weighted_sum += deltas[i] * weights[i]
    
    # Step 4: Adjust based on system cycle count
    adjusted = weighted_sum * (state['cycle'] / 10.0)
    
    # Step 5: Introduce conditional offset
    flag_count = sum(1 for f in state.get('flags', []) if f)
    if flag_count > 0:
        adjusted += 2.5
    else:
        adjusted -= 1.0
    
    # Step 6: Floor and convert to integer context
    return int(math.floor(adjusted * 10))

# Primary aggregation function
def aggregate_metrics(log, state):
    raw_diag = extract_diagnostics(log, state)
    
    # Fake enhancement layer (no effect)
    temp_buffer = [raw_diag + i for i in range(3)]
    processed = temp_buffer[0]  # Only first used
    
    # Conditional override check (not triggered)
    if state['mode'] == 'OPERATIONAL' and state['cycle'] > 20:
        processed = 999
    
    # Final adjustment based on status
    if state['status'] == 'ACTIVE':
        processed += 7
    
    # Additional irrelevant bit manipulation
    masked = processed ^ 0b1010
    shifted_back = masked >> 2
    
    # The real answer path ends here
    return shifted_back

# Trigger the actual computation
timing_subset = [t for t in timing_log if t >= 0.5]  # Used in extract_diagnostics indirectly
current_diagnostic = analyze_phase_shift(5.2, 1.0, math.pi/4)  # Red herring call
entropy_value = compute_entropy([1,1,2,2,3,3,4])  # Another distractor

final_diagnostic = aggregate_metrics(timing_log, system_state)
print(f"Result: {final_diagnostic}")