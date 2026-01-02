import itertools

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.0034
REFERENCE_VOLTAGE = 3.3
BASELINE_DRIFT = [0.01, -0.02, 0.005]

# Sensor metadata and decoy processing
sensor_ids = ['S1A', 'S2B', 'S3C', 'S4D']
sensor_status = {sid: True for sid in sensor_ids}
sensor_weights = {sid: (i + 1) * 0.25 for i, sid in enumerate(sensor_ids)}

# Irrelevant signal transformation chain
def apply_noise_filter(signal_data):
    return [x * 0.98 + CALIBRATION_OFFSET for x in signal_data]

def compute_envelope(signal_data):
    return max(signal_data) - min(signal_data)

# Fake diagnostic routine (dead code path)
def run_diagnostics():
    diagnostics = {}
    for i in range(4):
        diagnostics[f'test_{i}'] = (i ** 3) % 7
    return diagnostics  # never used

# Core data sequence (key input)
raw_readings = [12, 8, 15, 3, 9, 11, 6]

# Misleading preprocessing steps
temp_normalized = [x / sum(raw_readings) for x in raw_readings]
weighted_avg = sum(temp_normalized[i] * (i + 1) for i in range(len(temp_normalized)))

# Decoy function with bit manipulation red herring
def analyze_bits(x):
    if x <= 0:
        return 0
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count  # computed but not used in final logic

# Simulate phase shift detection from sensor patterns
monitor_sequence = []
for a, b in itertools.pairwise(raw_readings):
    if a > b:
        monitor_sequence.append(1)
    elif a < b:
        monitor_sequence.append(-1)
    else:
        monitor_sequence.append(0)

# Add dummy transitions using itertools cycle (distraction)
cycle_gen = itertools.cycle([0, 0, 1])
decoy_transitions = [next(cycle_gen) for _ in range(10)]

# Inject irrelevant list transformation
duplicated_pairs = list(itertools.chain.from_iterable(itertools.repeat(x, 2) for x in monitor_sequence[:4]))

# Key function: integrates actual logic buried under noise
def integrate_phase_shifts(phases):
    accumulator = 0
    adjustment_factor = 0.0

    # Real logic hidden in middle of distractions
    for i, p in enumerate(phases):
        if i % 2 == 0:
            accumulator += p * (i + 1)
        else:
            accumulator -= p

    # Secondary adjustment based on arithmetic pattern
    length = len(phases)
    if length > 5:
        adjustment_factor = (length // 2) * 0.5

    # Hidden rounding logic dependent on tuple unpacking
    config_flags = (True, False, True)
    enable_correction, _, scale_output = config_flags

    intermediate = accumulator

    if enable_correction:
        intermediate -= 2  # corrective offset

    if scale_output:
        intermediate *= 2

    # Final computation
    result = intermediate + int(adjustment_factor)

    # Dead assignment - misleading
    result = result if result != 0 else -999

    return result

# Unused complex structure (distractor)
data_cube = [[[i+j+k for k in range(2)] for j in range(2)] for i in range(3)]

# Another red herring: bitmask analysis over decoy_transitions (never called)
bit_analysis = [analyze_bits(x) for x in raw_readings]

# Critical execution point
final_flux = integrate_phase_shifts(monitor_sequence)

# Output result as required
print(f"Target result: {final_flux}")