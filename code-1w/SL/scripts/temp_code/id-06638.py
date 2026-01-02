import math

# Irrelevant thermodynamics constants (distractors)
BOLTZMANN_CONSTANT = 1.380649e-23
PLANCK_CONSTANT = 6.62607015e-34
SPEED_OF_LIGHT = 299792458
GRAVITATIONAL_CONSTANT = 6.67430e-11

# System configuration parameters (some irrelevant)
SYSTEM_SCALE = 1024
RESOLUTION_FACTOR = 4
DEBUG_MODE = False
LOGGING_INTERVAL = 15
MAX_ITERATIONS = 1000

# Core data structures
energy_levels = [i ** 2 for i in range(1, 17)]
spin_states = [(-1) ** i for i in range(16)]
phase_flags = [False, True, True, False] * 4

# Misleading auxiliary functions (dead code path)
def calculate_entropy(data):
    return sum(math.log(x) if x > 0 else 0 for x in data)

def update_lattice(spins):
    return [s * -1 for s in spins]

# Decoy transformation chain
def transform_momentum(energy_list):
    shifted = [e + 5 for e in energy_list]
    scaled = [e * 1.5 for e in shifted]
    return [int(s) for s in scaled]

# Data slicing with red herring purpose
raw_segments = energy_levels[4:12:2]  # [36, 64, 100, 144]
filtered_data = [x for x in raw_segments if x % 12 == 0]
synchronized_buffer = filtered_data.copy()

# Irrelevant bit manipulation sequence
def scramble_index(idx):
    idx = idx ^ 0b1010
    idx = (idx << 2) & 0b1111
    idx = idx ^ 0b1100
    return idx | 0b0010

# Hidden calculation path (relevant only in part)
intermediate_cache = {}
for i, val in enumerate(energy_levels[:8]):
    temp_key = scramble_index(i)
    temp_val = val // (i + 1) if i % 3 != 0 else val - 10
    intermediate_cache[temp_key] = temp_val

# Actual signal within noise: extract key features
signal_peaks = []
for i in range(len(energy_levels)):
    if spin_states[i] == 1 and phase_flags[i]:
        signal_peaks.append(energy_levels[i])

# Secondary filtering using slicing and thresholds
trimmed_signal = signal_peaks[1:-1]  # Remove first and last
amplification_factor = len(trimmed_signal) * 2.5

# Distractor: complex unused expression
quantum_correction = (BOLTZMANN_CONSTANT * SYSTEM_SCALE) / (PLANCK_CONSTANT + 1e-50)
relativistic_shift = SPEED_OF_LIGHT / (SYSTEM_SCALE ** 2)

# Core processing function with embedded logic
# This function appears complex but relies on deterministic steps
def process_phase_transition(energy_source):
    # Step 1: Extract every third element starting from index 1
    sampled = energy_source[1::3]  # [4, 25, 64, 121, 196]
    
    # Step 2: Apply conditional scaling based on parity of index
    adjusted = []
    for j, v in enumerate(sampled):
        if j % 2 == 0:
            adjusted.append(v * 1.1)
        else:
            adjusted.append(v * 0.9)
    
    # Step 3: Compute moving average over window of size 2
    averaged = []
    for k in range(len(adjusted) - 1):
        avg_val = (adjusted[k] + adjusted[k+1]) / 2
        averaged.append(avg_val)
    
    # Step 4: Apply logarithmic compression
    compressed = [math.log(x) if x > 1 else 0 for x in averaged]
    
    # Step 5: Aggregate final statistic
    aggregate = sum(compressed) * amplification_factor  # Depends on trimmed_signal length
    
    # Step 6: Mask with decoy constant (no effect)
    masked_result = aggregate  # No actual masking; decoy line
    
    return masked_result

# Simulate diagnostic trace (irrelevant)
def run_diagnostics():
    status = 0
    for _ in range(LOGGING_INTERVAL):
        status ^= RESOLUTION_FACTOR
    return status

# Unused recursive function (red herring)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Trigger diagnostic (never used)
diag_result = run_diagnostics()

# Main execution flow
baseline_reference = calculate_entropy(energy_levels)  # Computed but unused
scrambled_energy = transform_momentum(energy_levels)     # Dead end

# Critical execution point
final_output = process_phase_transition(energy_states)

# The real answer depends on correct tracking through process_phase_transition
# But note: 'energy_states' is undefined above — must be defined before this!
# Let's fix the flow by redefining critical state just before call:
energy_states = [x * spin_states[i] for i, x in enumerate(energy_levels)]
final_output = process_phase_transition(energy_states)

# The key variable to evaluate
thermodynamic_potential = int(final_output * 1000) / 1000.0  # Rounded to 3 decimals

print(f"Result: {thermodynamic_potential}")