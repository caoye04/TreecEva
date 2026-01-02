import math

# Simulated sensor data processing with embedded logic traps
def collect_readings():
    raw = [i * 0.5 for i in range(20)]
    filtered = [x for x in raw if x > 2.0]
    smoothed = [round(x + 0.1, 1) for x in filtered]
    return smoothed

# Irrelevant preprocessing: signal harmonics (dead path)
def compute_harmonics(data):
    return [math.sin(x) * math.cos(x) for x in data[::2]]

# Misleading transformation chain
def transform_sequence(seq):
    temp_a = [x * 1.5 for x in seq]
    temp_b = [x for x in temp_a if x < 8.0]
    shifted = [x - 1.0 for x in temp_b]
    return shifted[::-1]  # Reversed order - distractor

# Decoy function: looks important but unused in final calculation
def validate_coherence(pattern):
    total = sum(pattern)
    return total % 7 == 0

# Auxiliary checker with partial relevance
def assess_stability(values):
    diffs = [abs(values[i+1] - values[i]) for i in range(len(values)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return avg_diff < 1.2

# Core logic buried in multiple layers
def extract_segments(chain):
    segment_1 = chain[3:10]  # Actual relevant slice
    segment_2 = chain[12:15]  # Unused red herring
    meta_info = (len(segment_1), sum(segment_1))
    return meta_info

# Complex conditional routing with short-circuiting distraction
def route_processing(data, mode_flag=True):
    if mode_flag and len(data) > 5:
        processed = transform_sequence(data)
        if assess_stability(processed) or False:  # Short-circuit trap
            return processed[:8]
    else:
        return [0.0] * 5
    return data  # Dead return path

# Bit manipulation decoy - appears computational but irrelevant
def flag_analysis(n):
    return (n & (n - 1)) == 0  # Power of two check - unused

# Main analysis with intertwined valid and invalid paths
def analyze_pattern(sequence, limits):
    # Real computation begins here
    base_tuple = extract_segments(sequence)
    length_key, sum_value = base_tuple
    
    # Spurious bitwise operation (distractor)
    masked = sum_value ^ 256  # XOR with constant - not used later
    
    # Conditional layering with embedded truth evaluation
    threshold_met = any([sum_value > t for t in limits])
    adjustment = -5 if not threshold_met else 7
    
    # Critical arithmetic chain
    interim = (length_key * 33) + adjustment
    scaling_factor = 1.0
    
    # Fake branching with misleading comments
    if interim % 2 == 0:
        scaling_factor = 1.1  # Never taken due to logic
    else:
        scaling_factor = 1.0  # Always taken
    
    # Final computation buried under distractions
    result = interim * scaling_factor
    
    # Multiple variable assignments - obfuscation
    temp_result, final_diagnostic = 999, int(result)
    
    # Unused complex structure - tuple and slicing decoy
    audit_log = (sequence, limits, temp_result)
    snapshot = audit_log[0][::3]  # Slicing used as distractor
    
    return final_diagnostic

# Orchestration with irrelevant setup
readings = collect_readings()
harmonics = compute_harmonics(readings)  # Computed but unused
processed_flow = route_processing(readings, mode_flag=True)
thresholds = [40, 45.5, 48]  # Used in decision logic

# Key execution point
final_diagnostic = analyze_pattern(processed_flow, thresholds)
print(f"Result: {final_diagnostic}")