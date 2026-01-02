import math

# System diagnostics simulation for satellite telemetry processing
base_frequency = 57.3
signal_buffer = [12, 8, 15, 3, 9, 6]
diagnostic_log = set()
redundant_checksum = 0

def generate_harmonics(freq, harmonics=4):
    """Generate harmonic frequencies (distraction: not used in final result)"""
    return [round(freq * (i + 1), 2) for i in range(harmonics)]

def compute_entropy(data):
    """Calculate Shannon entropy of a dataset (red herring function)"""
    total = sum(data)
    probabilities = [x / total for x in data if x > 0]
    return round(-sum(p * math.log2(p) for p in probabilities), 4)

def detect_outliers(values, threshold=1.5):
    """Identify outliers using IQR method (dead code path)"""
    sorted_vals = sorted(values)
    q1, q3 = sorted_vals[len(sorted_vals)//4], sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [v for v in values if v < lower or v > upper]

def phase_shift_correction(signal_list, shift=1):
    """Apply circular shift to signal (distractor transformation)"""
    corrected = [((x << shift) & 15) ^ ((x >> (4 - shift)) & 15) for x in signal_list]
    return corrected

# Irrelevant preprocessing chain
entropy_metric = compute_entropy(signal_buffer)
harmonic_profile = generate_harmonics(base_frequency)
shifted_signal = phase_shift_correction(signal_buffer, 2)

diagnostic_log.add('INIT_PHASE_COMPLETE')
baseline_offset = sum(signal_buffer) // len(signal_buffer)
adjusted_readings = [x - baseline_offset for x in signal_buffer]

# Simulated fault signature detection (core relevant logic begins)
fault_signatures = set()
for reading in adjusted_readings:
    if reading % 3 == 0:
        fault_signatures.add(abs(reading))

# Generate secondary signal indicators (mixed relevance)
secondary_indicators = []
counter = 0
while counter < len(signal_buffer):
    temp_val = signal_buffer[counter]
    if temp_val > 8:
        # Complex bit manipulation with partial relevance
        transformed = ((temp_val ^ 5) + 2) & 12
        secondary_indicators.append(transformed)
        if transformed > 8:
            diagnostic_log.add(f'TRANSIENT_ALERT_{counter}')
    counter += 1

# Recurring signal extraction (key intermediate step)
recurring_signals = set()
for i, val in enumerate(signal_buffer):
    if val in fault_signatures and i % 2 == 1:
        recurring_signals.add(val * 2)
    elif val in secondary_indicators:
        recurring_signals.add(val // 2)

# Decoy statistical analysis
outlier_flags = detect_outliers(signal_buffer)
if outlier_flags:
    redundant_checksum += sum(outlier_flags)

# Core diagnostic engine (uses set operations as required)
def analyze_fault_pattern(patterns):
    known_anomalies = {6, 12, 18, 24}
    potential_matches = patterns.intersection(known_anomalies)
    suppression_mask = {x for x in patterns if bin(x).count('1') % 2 == 0}  # even parity filter
    
    # Actual answer computation buried in distractions
    base_score = sum(potential_matches) * 17
    penalty = len(suppression_mask) * 3
    adjustment = len(diagnostic_log) * 2  # always at least 1 for INIT_PHASE_COMPLETE
    
    # Dead computation branch (misleading)
    if base_score > 100:
        hypothetical = base_score / (penalty + 1)
        scaled = hypothetical * 0.85
    
    final_score = base_score - penalty + adjustment
    
    # Final transformation using modular arithmetic and sorting side effect
    sorted_patterns = sorted(list(patterns))
    pivot = sorted_patterns[len(sorted_patterns)//2] if patterns else 0
    final_score = (final_score + pivot) % 97
    
    return final_score

# Execute main analysis
diagnostic_log.add('ANALYSIS_STARTED')
final_diagnostic = analyze_fault_pattern(recurring_signals)
print(f"Target result: {final_diagnostic}")