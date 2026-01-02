import math

# Simulated spacecraft thermal regulation system diagnostics
def analyze_thermal_node(temp_seq, threshold):
    cumulative_stress = 0
    peak_moment = -1
    for i, temp in enumerate(temp_seq):
        if temp > threshold + 50:
            cumulative_stress += (temp - threshold) ** 1.5
            if i % 2 == 0:
                peak_moment = i * 1.5
        elif temp < threshold - 30:
            cumulative_stress -= abs(temp - threshold) * 0.5  # cooling credit
    return int(cumulative_stress) + (10 if peak_moment > 0 else 0)


def bit_rotate(value, shift, width=8):
    # Irrelevant bit manipulation for obfuscation
    shift %= width
    return ((value << shift) | (value >> (width - shift))) & ((1 << width) - 1)


def evaluate_harmonic_stability(readings):
    # Distractor function – never called in execution path
    total = 0
    for r in readings:
        total += math.sin(r / 10) * math.cos(r / 20)
    return round(total, 4)


def recursive_checksum(seq, depth=0):
    # Decoy recursive function with misleading name
    if depth >= 3 or len(seq) == 0:
        return 77  # red herring result
    return recursive_checksum(seq[1:], depth + 1) ^ seq[0]


def validate_phase_coupling(matrix):
    # Unused validation logic – dead code path
    for row in matrix:
        if sum(row) % 2 != 0:
            return False
    return True


def compute_integrity_score(matrix, flags):
    base_score = 0
    adjustments = []
    
    # Real computation begins here — nested and mixed with distractors
    for idx, row in enumerate(matrix):
        if flags[idx] == 1:
            # Only active nodes contribute
            node_analysis = []
            for j, val in enumerate(row):
                shifted = val >> 1
                if j % 3 == 0:
                    adjusted_val = shifted + (val & 7)
                else:
                    adjusted_val = shifted ^ (j & 5)
                node_analysis.append(adjusted_val)
            
            # Use enumerate and zip as required
            paired = list(zip(node_analysis[:-1], node_analysis[1:]))
            differential = 0
            for i, (a, b) in enumerate(paired):
                if a > b:
                    differential += (a - b) * (i + 1)
                else:
                    differential -= (b - a) // (i + 2)
            
            # Key contribution to final score
            base_score += differential
        else:
            # Inactive branch — computes but does not affect outcome
            dummy = [x ** 0.5 for x in row if x > 0]
            adjustments.append(sum(dummy))
    
    # Core answer logic — depends only on specific paths
    multiplier = 3 if flags.count(1) >= 2 else 1
    
    # Introduce conditional expression
    offset = 15 if any(len(row) > 4 for row in matrix) else 5
    
    # Final computation
    raw_result = base_score * multiplier + offset
    
    # Apply bit rotation decoy operation that doesn't change anything
    # But looks important
    raw_result = bit_rotate(raw_result % 256, 3) + (raw_result & ~255)
    
    # Normalize to prevent overflow
    final_diagnostic = max(-1000000, min(1000000, raw_result))
    
    return final_diagnostic

# --- Simulation Data ---

# Real input data driving the computation
thermal_matrix = [
    [98, 45, 110, 60, 88],
    [30, 90, 105, 65, 70],
    [50, 40, 80, 75, 60]
]

system_flags = [1, 1, 0]  # Third node inactive

# --- Irrelevant Variables (Distractors) ---
diagnostic_log = {"node_1": "stable", "node_2": "fluctuating", "node_3": "inactive"}
timestamp_utc = 1712345678
baseline_reference = [evaluate_harmonic_stability([88, 92, 90]), 0.0, 0.0]  # unused

# --- Critical Execution Point ---
final_diagnostic = compute_integrity_score(thermal_matrix, system_flags)

# --- Output ---
print(f"Result: {final_diagnostic}")