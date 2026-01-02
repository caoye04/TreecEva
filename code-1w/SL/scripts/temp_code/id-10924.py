import itertools

def analyze_cycle_efficiency(cycle_data):
    """Irrelevant analysis function - decoy."""
    total = 0
    for x in cycle_data:
        if x > 50:
            total += x * 0.3
    return total // 2 if total > 100 else total

def normalize_sequence(seq):
    """Another distraction - performs irrelevant normalization."""
    mean_val = sum(seq) / len(seq)
    return [round((x - mean_val) * 1.5, 2) for x in seq]

def shift_phase_signal(signal, offset=3):
    """Bit manipulation red herring."""
    shifted = []
    for val in signal:
        # Bitwise operations that look important but aren't used in final result
        masked = (val & 255) ^ offset
        rotated = ((masked << 3) | (masked >> 5)) & 255
        shifted.append(rotated)
    return shifted

def calculate_entropy(stream):
    """Unused entropy calculation to mislead."""
    from math import log2
    freq = {}
    for s in stream:
        freq[s] = freq.get(s, 0) + 1
    return -sum(f * log2(f / len(stream)) for f in freq.values())

def extract_diagnostic_codes(log_str):
    """String processing decoy - looks critical but unused."""
    parts = log_str.split('|')
    codes = []
    for part in parts:
        cleaned = part.strip().upper()
        if cleaned.startswith('ERR'):
            codes.append(int(cleaned[3:]) if cleaned[3:].isdigit() else 0)
    return sorted(set(codes))

def adjust_thermal_rating(flux, cycles):
    """Core relevant function: computes adjusted thermal output."""
    base = flux * 1.75
    if cycles < 10:
        adjustment = 0.8
    elif cycles < 50:
        adjustment = 1.1
    else:
        adjustment = 1.35
    
    # Real computation path
    intermediate = base * adjustment
    
    # Distractor: string transformation that mimics data relevance
    tag = f"THERM-{int(intermediate)}-X"
    if 'X' in tag:
        tag = tag.replace('X', 'FINAL')
    
    # Actual logic continues
    safety_margin = 0.93
    if 'FINAL' in tag:
        intermediate *= 1.02
    
    return int(intermediate * safety_margin)

# Simulated sensor input (irrelevant structure)
cycle_readings = [45, 89, 23, 67, 12, 91, 44, 77]
normalized_readings = normalize_sequence(cycle_readings)
efficiency_score = analyze_cycle_efficiency(normalized_readings)

# Fake diagnostic log with string methods
diag_log = "| INIT:OK | ERR001 | ERR005 | STATUS:RUNNING | ERR001 |"
diag_codes = extract_diagnostic_codes(diag_log)

# Irrelevant bit signal transformation
phase_signal = [120, 200, 75, 90]
processed_signal = shift_phase_signal(phase_signal)

# Unused entropy on string characters
char_stream = [c for c in diag_log if c.isalnum()]
entropy = calculate_entropy(char_stream)

# Real parameters entering the critical path
base_flux = 420  # Core input

# Misleading list comprehension using itertools
time_windows = list(itertools.combinations([10, 20, 30, 40], 2))
window_sums = [sum(w) for w in time_windows if sum(w) > 50]  # Dead-end computation

# Critical execution path begins
cycle_count = len(cycle_readings)

# Key statement
thermal_output = adjust_thermal_rating(base_flux, cycle_count)

# Output the target result
print(f"Target result: {thermal_output}")