import itertools

# Simulated system performance metrics
def generate_diagnostics():
    return {
        'cpu_load': [0.78, 0.82, 0.91, 0.85, 0.77],
        'mem_usage': [0.64, 0.71, 0.75, 0.78, 0.83],
        'disk_io': [120, 135, 110, 145, 150],
        'net_latency': [23, 21, 26, 28, 25],
        'temp_cores': [67, 70, 73, 71, 69]
    }

def analyze_trends(data):
    # Irrelevant trend analysis (distractor)
    trends = {}
    for key, values in data.items():
        avg = sum(values) / len(values)
        trend = 'increasing' if values[-1] > values[0] else 'decreasing'
        trends[key] = {'average': avg, 'trend': trend}
    return trends

def filter_outliers(seq, threshold=1.5):
    # Dead code path - never actually used in final computation
    mean = sum(seq) / len(seq)
    var = sum((x - mean) ** 2 for x in seq) / len(seq)
    std = var ** 0.5
    return [x for x in seq if abs(x - mean) <= threshold * std]

def calculate_efficiency_ratio(load, usage):
    # Efficiency model (partially relevant)
    weighted_sum = sum(l * u for l, u in zip(load, usage))
    max_possible = sum(max(l, u) for l, u in zip(load, usage))
    return weighted_sum / max_possible if max_possible > 0 else 0

def validate_stability(logs):
    # Misleading function: looks important but unused
    if not logs:
        return False
    diffs = [abs(logs[i] - logs[i-1]) for i in range(1, len(logs))]
    return all(d < 5 for d in diffs)

def compute_thermal_coefficient(temp_data, factor=0.89):
    # Decoy calculation with plausible-sounding name
    squared_mean = (sum(t**2 for t in temp_data) / len(temp_data)) ** 0.5
    return squared_mean * factor

def aggregate_diagnostic_score(diag_data):
    # Real computation begins here
    cpu = diag_data['cpu_load']
    mem = diag_data['mem_usage']
    io = diag_data['disk_io']
    lat = diag_data['net_latency']

    # Step 1: Normalize I/O and latency to 0-1 scale
    norm_io = [i / 200 for i in io]  # Assume max expected is 200
    norm_lat = [1 - (l / 50) for l in lat]  # Lower latency is better

    # Step 2: Compute composite load index
    composite_load = [
        (c + m) / 2 * (1 - (i + nl) / 2)
        for c, m, i, nl in zip(cpu, mem, norm_io, norm_lat)
    ]

    # Step 3: Apply time decay weighting using itertools
    weights = list(itertools.accumulate([0.5] * 5, lambda w, _: w * 1.1))
    total_weight = sum(weights)
    weighted_performance = sum(w * (1 - val) for w, val in zip(weights, composite_load))

    raw_score = weighted_performance / total_weight

    # Step 4: Apply correction based on hidden pattern
    adjustments = [0.05, -0.03, 0.02, -0.01, 0.04]
    adjustment_factor = sum(
        a * (0.9 ** i) for i, a in enumerate(reversed(adjustments))
    )

    return raw_score + adjustment_factor

def extract_signatures(data):
    # Unused complex transformation (red herring)
    sigs = []
    for k, v in data.items():
        if isinstance(v, list) and k != 'temp_cores':
            packed = ''.join(f'{int(x*100):02x}' if x < 10 else f'{x%100:02x}' for x in v[:3])
            sigs.append(packed)
    return sigs

def process_performance(metrics, base_ref):
    # Core logic with interference from decoy variables
    
    # Irrelevant preprocessing (distraction)
    _ = analyze_trends(metrics)
    _ = extract_signatures(metrics)
    _ = compute_thermal_coefficient(metrics['temp_cores'])

    # Actual work starts here
    base_score = aggregate_diagnostic_score(metrics)
    
    # Hidden logic: compare against baseline using bit manipulation
    offset = int((base_ref['initial'] - 50) * 2)  # assumed baseline shift
    shift_amount = base_ref['level'] % 5
    
    # Critical step: combine via arithmetic and bitwise ops
    intermediate = int((base_score * 10000) ^ (offset << shift_amount))
    
    # Final adjustment using logical conditions
    flags = [
        metrics['cpu_load'][-1] > 0.85,
        metrics['mem_usage'][-1] > 0.80,
        base_ref['critical']
    ]
    
    penalty = 15 if all(flags) or (not flags[0] and flags[2]) else 0
    
    # Answer emerges here
    final_score = intermediate - penalty
    
    # Print required for traceability
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == "__main__":
    diagnostics = generate_diagnostics()
    baseline_config = {
        'initial': 47,
        'level': 7,
        'critical': True,
        'version': '2.3.1',  # unused field
        'timeout': 30        # dead parameter
    }
    # Key statement
    final_score = process_performance(diagnostics, baseline_config)