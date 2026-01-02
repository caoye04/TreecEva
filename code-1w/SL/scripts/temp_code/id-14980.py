import math

# Simulated sensor data processing for a distributed monitoring system
def collect_diagnostics():
    raw_readings = [14.2, 18.7, 22.1, 19.5, 25.3, 17.4, 20.8, 23.6]
    timestamp_flags = {'t0': 1, 't1': 3, 't2': 2, 't3': 1}
    device_status = {'active': 8, 'standby': 2, 'failed': 0}

    # Irrelevant aggregation - red herring
    total_devices = sum(device_status.values())
    status_ratio = device_status['active'] / total_devices if total_devices else 0

    # Real computation path begins
    filtered_readings = [x for x in raw_readings if x > 18.0]
    
    # Secondary filter based on position (simulates time-windowed sampling)
    indexed_readings = {i: val for i, val in enumerate(filtered_readings)}
    peak_window = [v for i, v in indexed_readings.items() if 1 <= i <= len(indexed_readings) - 2]

    # Compute moving average over peak window (3-point)
    moving_averages = []
    for i in range(len(peak_window) - 2):
        avg = (peak_window[i] + peak_window[i+1] + peak_window[i+2]) / 3
        moving_averages.append(round(avg, 2))

    # Misleading entropy calculation (unused later)
    def shannon_entropy(lst):
        from collections import Counter
        counts = Counter(lst)
        probs = [count / len(lst) for count in counts.values()]
        return -sum(p * math.log2(p) for p in probs if p > 0)

    entropy_value = shannon_entropy([int(x) for x in raw_readings])  # Dead end

    # Core logic disguised among distractions
    baseline = sum(filtered_readings) / len(filtered_readings)
    variance = sum((x - baseline) ** 2 for x in filtered_readings) / len(filtered_readings)
    std_dev = math.sqrt(variance)

    # Simulated load factor from external subsystem (decoy values)
    decoy_loads = {'cpu': 78, 'memory': 65, 'disk': 44, 'network': 31}
    weighted_decoy = sum(decoy_loads[k] * (i+1) for i, k in enumerate(decoy_loads))  # Unused

    # Actual signal extraction via lambda transformation
    transform_fn = lambda x: (x * 1.8) + 32  # Convert to Fahrenheit-like scale
    transformed_peaks = list(map(transform_fn, peak_window))

    # Data summary includes only relevant metrics
    data_summary = {
        'count': len(transformed_peaks),
        'total': sum(transformed_peaks),
        'stdev': std_dev
    }

    system_load = {
        'base': baseline,
        'threshold': 20.0,
        'critical': False
    }

    # Decoy function that looks important but does nothing
    def analyze_fault_tree(config):
        rules = [
            lambda c: c.get('voltage', 0) > 3.3,
            lambda c: c.get('temp', 0) < 85,
            lambda c: c.get('errors', 0) == 0
        ]
        return all(rule(config) for rule in rules)

    dummy_config = {'voltage': 3.2, 'temp': 90, 'errors': 1}
    safety_ok = analyze_fault_tree(dummy_config)  # Distractor

    # Key statement: actual answer computation
    def process_metrics(summary, load):
        if summary['count'] == 0:
            return 0
        # Composite diagnostic score
        magnitude = summary['total'] / summary['count']
        stability = magnitude - load['base']
        correction = summary['stdev'] * 0.5
        return round(magnitude - stability + correction, 4)

    final_diagnostic = process_metrics(data_summary, system_load)
    print(f"Target result: {final_diagnostic}")

    # Extra red herring: unused cache structure
    cache_pool = {}
    for i in range(5):
        key = f"tmp_{i}"
        cache_pool[key] = {"hash": (i * 17) % 101, "valid": False}

    return final_diagnostic

# Execute and output
result = collect_diagnostics()