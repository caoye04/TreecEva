import math

def analyze_readings(readings):
    # Irrelevant helper function (dead code path)
    cumulative_score = 0
    for val in readings:
        if val > 50:
            cumulative_score += math.sqrt(val)
    return cumulative_score

def validate_signal(signal):
    # Distractor function: looks important but unused
    if len(signal) == 0:
        return False
    peak = max(signal)
    return peak > 30 and sum(signal) % 2 == 0

def compute_entropy(data):
    # Another red herring: computes something complex but unused
    total = sum(data)
    probabilities = [x / total for x in data if x > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def filter_outliers(values, limit=25):
    # Seemingly relevant preprocessing that's not actually used in final logic
    cleaned = [v for v in values if v < limit]
    return cleaned or [0]

def process_metrics(data, config):
    # Core logic with multiple steps and nesting
    baseline = config['base']
    critical_set = set(config['critical_indices'])
    temp_flags = []
    adjustment_factor = 1.75

    for i, entry in enumerate(data):
        measurement = entry['value']
        category = entry['type']

        # Bit manipulation decoy
        encoded = measurement ^ 255
        if encoded < 100:
            temp_flags.append(True)

        # Conditional expression distraction
        status = 'high' if measurement > baseline else ('low' if measurement < baseline - 10 else 'normal')

        # Real logic begins here: tracking specific indices
        if i in critical_set:
            if category == 'sensor' and measurement % 2 == 1:
                adjustment_factor *= 0.9
            elif category == 'auxiliary':
                adjustment_factor += 0.05

    # Set operation: meaningful use
    index_set = set(range(len(data)))
    overlap = critical_set & index_set  # Actual use of set intersection

    # Complex composite calculation
    base_total = sum(e['value'] for e in data)
    modifier = len(overlap) * adjustment_factor

    intermediate = base_total * modifier

    # Early termination red herring (never triggered due to data)
    if intermediate < 0:
        return -1

    # Key transformation
    transformed = abs(intermediate - 512.87)

    # Final computation with conditional expression
    final_diagnostic = transformed if transformed > 100 else (transformed ** 2)

    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Real input data
    health_data = [
        {'value': 45, 'type': 'sensor'},
        {'value': 67, 'type': 'sensor'},
        {'value': 23, 'type': 'auxiliary'},
        {'value': 89, 'type': 'sensor'},
        {'value': 12, 'type': 'sensor'}
    ]

    # Misleading variables (distractors)
    signal_data = [44, 67, 23, 89, 12, 95, 34]
    performance_log = {'entries': 7, 'errors': 2}
    system_state = {'power': 'stable', 'mode': 'diagnostic'}

    # Threshold configuration (used in main logic)
    thresholds = {
        'base': 50,
        'critical_indices': [1, 3, 4]  # Indices 1, 3, 4 are critical
    }

    # Unused but plausible computations
    entropy_value = compute_entropy([45, 67, 23, 89, 12])
    filtered = filter_outliers(signal_data, limit=30)

    # Key execution point
    final_diagnostic = process_metrics(health_data, thresholds)