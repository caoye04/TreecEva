import math

# System health monitoring simulation with red herrings and complex logic paths
def analyze_subsystem_1(data):
    if not data:
        return 0
    temp_score = sum([x ** 2 for x in data if x > 0])
    normalization = max(data) if data else 1
    return int(temp_score / normalization) if normalization != 0 else 0

def analyze_subsystem_2(config):
    # Irrelevant scoring function (dead path)
    return sum(config.values()) * 2

def dummy_validator(x):
    # Unused function - distractor
    return x % 7 == 0

def compute_fallback_threshold(series):
    # Computation that looks important but isn't used in final path
    avg = sum(series) / len(series) if series else 0
    variance = sum((x - avg) ** 2 for x in series) / len(series) if series else 0
    return math.sqrt(variance) + avg

def evaluate_stability(readings):
    if len(readings) < 5:
        return False
    sorted_vals = sorted(readings)
    median = sorted_vals[len(sorted_vals) // 2]
    return median > 50 and (sorted_vals[-1] - sorted_vals[0]) < 100

def derive_calibration_constant(signal):
    # Bit manipulation that seems critical but is only used in decoy branch
    base = len(signal)
    shifted = (base << 3) & 0xFF
    inverted = shifted ^ 0b11010110
    return inverted | 0b00101001

def process_metrics(signature, load):
    # Core processing with conditional expressions and set operations
    critical_threshold = 75 if len(signature) > 6 else 60
    
    # Real computation begins here
    raw_energy = sum(abs(x) for x in signature)
    adjusted_energy = raw_energy * (0.8 if evaluate_stability(signature) else 1.2)
    
    # Conditional expression with string method distraction
    mode_flag = 'STABLE' if adjusted_energy < 200 else 'FLUCTUATING'
    flag_length = len(mode_flag.strip().lower())  # String method use (partial distraction)
    
    # Set operations used meaningfully but with extra complexity
    unique_contributors = set(abs(x) for x in signature)
    expected_peaks = {x for x in range(10, 100, 15)}
    matched_peaks = unique_contributors.intersection(expected_peaks)
    peak_bonus = len(matched_peaks) * 5 if matched_peaks else -3
    
    # Load-based adjustment using integer division and logical ops
    load_level = (load // 10) if load > 0 else 0
    safety_margin = 10 if (load_level < 8) and (adjusted_energy > 150) else 2
    
    # Final composition using multiple concepts
    preliminary_score = (adjusted_energy + peak_bonus) // safety_margin
    
    # Key conditional expression determining final result
    final_value = preliminary_score if mode_flag in {'STABLE'} else (preliminary_score * 2) + 1
    
    # Decoy calculation that looks like it updates final_value but doesn't
    if derive_calibration_constant(signature) > 100:
        _temp = (final_value >> 1) ^ 0xFFFF
    
    # Actual return (non-obvious due to distractions above)
    return int(final_value)

# Main execution flow
if __name__ == "__main__":
    # Initialize diagnostic parameters
    sensor_readings = [12, -8, 45, 67, 23, 89, -14, 37]
    system_load = 74
    
    # Dead code paths and irrelevant variables
    config_profile = {'threshold': 95, 'gain': 2, 'damping': 5}
    baseline_series = [52, 58, 51, 56, 54]
    fallback_limit = compute_fallback_threshold(baseline_series)
    
    # Meaningful assignment
    health_signature = [x for x in sensor_readings if x != 0]
    
    # Red herring: unused validation
    valid_data = dummy_validator(sum(health_signature))
    
    # Critical statement
    final_diagnostic = process_metrics(health_signature, system_load)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")