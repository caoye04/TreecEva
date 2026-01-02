import math

# Simulated sensor network diagnostic system
def collect_readings():
    raw_data = [127, 255, 193, 64, 222, 145, 89, 37]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_data]
    return adjusted

def filter_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    threshold = 1.5 * std_dev
    filtered = [x for x in data if abs(x - mean_val) <= threshold]
    return filtered

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def generate_checksum(seq):
    # Irrelevant function - red herring
    return sum(x ^ 255 for x in seq) % 1000

def decode_signal(pattern):
    # Unused decoy function
    return [((x << 2) & 255) | (x >> 6) for x in pattern]

def accumulate_diagnostics(logs):
    # Complex but irrelevant accumulation
    accumulator = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    for i, log in enumerate(logs):
        phase = (log * weights[i % 4]) + (i % 17)
        accumulator += math.sin(phase) * 10
    return round(accumulator, 3)

def analyze_readings(readings):
    # Key processing path
    logs = [int(r) for r in readings if r > 75]
    
    # Dead code path - never executed due to condition
    if len(logs) < 2:
        fallback = [x * 2 for x in readings]
        logs = [x for x in fallback if x % 10 == 0]
    
    # Distractor variables
    temp_snapshot = [x + 10 for x in logs]
    mirror_copy = logs.copy()
    logs.append(999)  # This mutation has no effect on result
    logs.clear()
    
    # Actual computation hidden among distractions
    base_sum = sum(mirror_copy)
    count_adj = len(mirror_copy) + (5 if base_sum > 300 else -2)
    adjustment = compute_entropy(mirror_copy)
    raw_diagnostic = base_sum / count_adj if count_adj != 0 else 0
    final_diagnostic = int(raw_diagnostic + adjustment)
    
    # Additional red herring operations
    dummy_matrix = [[i*j for j in range(3)] for i in range(3)]
    checksum_probe = generate_checksum(mirror_copy)
    
    return final_diagnostic

def main_pipeline():
    # Orchestration with misleading intermediate outputs
    readings = collect_readings()
    processed_logs = filter_outliers(readings)
    
    # Print distraction - not part of answer
    debug_stats = {
        'size': len(processed_logs),
        'max': max(processed_logs),
        'entropy': compute_entropy(processed_logs)
    }
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_logs)
    
    # Decoy analysis
    alt_result = accumulate_diagnostics(processed_logs)
    signal_code = decode_signal([int(x) for x in processed_logs])
    
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

result = main_pipeline()