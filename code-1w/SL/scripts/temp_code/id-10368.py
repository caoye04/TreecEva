import itertools

# System diagnostics simulation with decoy and actual logic paths
def initialize_quantum_registers():
    # Real initialization data
    return [7, 2, 5, 1, 9, 4, 8]

# Irrelevant helper - looks important but unused in final path
def deprecated_checksum(seq):
    return sum(x ** 2 for x in seq if x % 2 == 0) % 11

# Decoy transformation function (never called)
def transform_legacy_mode(data):
    shifted = [(x << 2) & 15 for x in data]
    return [y ^ 5 for y in shifted]

# Auxiliary diagnostic (used only partially)
def compute_entropy(signal):
    freq_map = {}
    for val in signal:
        freq_map[val] = freq_map.get(val, 0) + 1
    entropy = 0
    total = len(signal)
    for count in freq_map.values():
        p = count / total
        entropy -= p * p  # Simplified measure
    return round(entropy, 6)

# Signal alignment via itertools (actual usage)
def align_phase_signals(registers):
    paired = list(itertools.pairwise(registers))
    adjusted = []
    for a, b in paired:
        if a > b:
            adjusted.append(a - b)
        else:
            adjusted.append(b - a)
    return adjusted

# Filtering mechanism with red herring condition
def filter_anomalies(sequence):
    # This filtering seems sophisticated but only length matters in reality
    valid = []
    threshold = sum(sequence) // len(sequence)
    for item in sequence:
        # Complex-looking condition, but all pass due to domain
        if (item + 3) % 7 != 0 or item in {2, 4, 8}:  # Mostly true
            valid.append(item * 2)
        else:
            valid.append(item)
    # Truth: only the length of `valid` is later used
    return valid

# Core analysis with distractor variables
def analyze_system_state(qregs):
    # Step 1: real preprocessing
    phase_aligned = align_phase_signals(qregs)  # [5,3,4,8,5,4]
    
    # Distractor variables - look like they contribute
    noise_floor = sum(x ** 0.5 for x in qregs if x % 3 == 0)  # ~ irrelevant
    coherence_score = compute_entropy(qregs)  # computed but unused
    
    # Step 2: actual dependency
    amplified_signal = [x * 3 for x in phase_aligned]  # [15,9,12,24,15,12]
    
    # Step 3: filtering with side effect
    filtered = filter_anomalies(amplified_signal)
    
    # Step 4: extract control metric
    sample_window = filtered[:len(qregs)-1]  # same length as phase_aligned
    
    # Step 5: statistical moment calculation (real contribution)
    mean_val = sum(sample_window) / len(sample_window)
    variance_proxy = sum((x - mean_val) ** 2 for x in sample_window) / len(sample_window)
    
    # Step 6: modular checksum (only this matters)
    raw_sum = sum(amplified_signal)  # 15+9+12+24+15+12 = 87
    mod_key = len(qregs)  # 7
    diagnostic_base = raw_sum % mod_key  # 87 % 7 = 3
    
    # Step 7: secondary adjustment based on set uniqueness
    unique_phases = set(qregs)
    bonus_shift = len(unique_phases.intersection({1, 3, 7}))  # {1,7} -> 2
    
    # Final computation
    final_diagnostic = (diagnostic_base * 100) + (bonus_shift * 10)  # 3*100 + 2*10 = 320
    
    # Dead code - misleading print
    # print(f'Debug: noise={noise_floor}, coherence={coherence_score}')
    
    return final_diagnostic

# --- Execution ---
quantum_registers = initialize_quantum_registers()

# Simulated intermediate checks (distractors)
current_mode = "STANDBY"
if len(quantum_registers) > 5:
    current_mode = "ACTIVE"

legacy_buffer = [x ^ 15 for x in quantum_registers]  # computed but unused

final_diagnostic = analyze_system_state(quantum_registers)
print(f"Result: {final_diagnostic}")