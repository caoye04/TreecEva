import itertools

def analyze_component(x, y):
    # Irrelevant helper with misleading purpose
    temp = (x ^ y) >> 1
    return (x + y) % 7

def collect_diagnostics(data):
    # Dead code path - never used in final computation
    results = []
    for i, val in enumerate(data):
        if val % 3 == 0:
            results.append(val * 2)
    return results

def filter_outliers(seq):
    # Distractor function: looks important but unused
    return [x for x in seq if 10 <= x <= 90]

def shift_window(values, offset=3):
    # Unused transformation with red herring logic
    rotated = values[-offset:] + values[:-offset]
    return rotated

def compute_baseline(samples):
    # Seemingly relevant but ultimately irrelevant calculation
    total = 0
    for idx, s in enumerate(samples):
        total += s * (idx % 4 + 1)
    baseline = total / len(samples) if samples else 0
    adjustment = baseline * 0.1
    return baseline - adjustment

def evaluate_performance(metrics, reference):
    # Core logic buried among distractions
    
    # Irrelevant intermediate arrays
    temp_cache = [0] * len(metrics)
    for i in range(len(metrics)):
        temp_cache[i] = metrics[i] * 2 - 1
    
    # Misleading pre-processing
    scaled_metrics = [m * 1.5 for m in metrics if m > 5]
    
    # Real logic begins here — hidden in noise
    cumulative = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    
    # Actual relevant data transformation using zip and enumerate
    for i, (m, r) in enumerate(itertools.zip_longest(metrics, reference, fillvalue=1)):
        if i % 2 == 0:
            contribution = (m * r) / (i + 1)
        else:
            contribution = m ** 2 / (r + 1)
        cumulative += contribution * weights[i % len(weights)]
    
    # Secondary correction based on parity count
    even_count = sum(1 for x in metrics if x % 2 == 0)
    if even_count > 2:
        cumulative *= 1.25
    
    # Final manipulation
    final_score = int(cumulative + 0.5)  # Round to nearest integer
    
    # Decoy assignment that looks like it might override
    local_result = cumulative * 0.9  # Never used
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data with meaningful names from system telemetry domain
    cpu_load_ticks = [12, 18, 25, 33]
    benchmark_data = [8, 14, 20, 30]
    
    # Irrelevant auxiliary variables
    calibration_sequence = list(range(5, 50, 6))
    diagnostic_trace = {k: v for k, v in enumerate(calibration_sequence)}
    metadata_flags = (True, False, True)
    
    # Simulated preprocessing that feeds nothing
    processed = []
    for a, b in zip(cpu_load_ticks, benchmark_data):
        processed.append((a + b) // 2)
    
    # Key statement containing the actual answer computation
    final_score = evaluate_performance(cpu_load_ticks, benchmark_data)
    
    # Print result as required
    print(f"Result: {final_score}")