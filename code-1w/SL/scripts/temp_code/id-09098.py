import math

# Simulated system telemetry and diagnostic processing pipeline
def collect_telemetry():
    raw_signals = [0.88, 0.72, 0.91, 0.64, 0.55]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    weighted_avg = sum(s * w for s, w in zip(raw_signals, weights))
    
    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(raw_signals)):
        left = max(0, i-1)
        right = min(len(raw_signals), i+2)
        smoothed.append(sum(raw_signals[left:right]) / (right - left))
    
    # Unused transformation chain (dead path)
    transformed = list(map(lambda x: math.log(1 + x**2), raw_signals))
    normalized = [x / max(transformed) for x in transformed]
    
    return {
        'baseline': 0.75,
        'current': weighted_avg,
        'peaks': [x for x in raw_signals if x > 0.8],
        'timestamp': 1698765432
    }

# Auxiliary function with misleading relevance
def calculate_health_score(data):
    score = 100.0
    if data['current'] < 0.6:
        score -= 40
    elif data['current'] < 0.7:
        score -= 20
    
    # Decoy logic with unused branches
    if len(data.get('peaks', [])) > 2:
        adjustment = -15
    else:
        adjustment = 0  # Never used
    
    score += len(data.get('peaks', [])) * 5
    return int(score)

# Core diagnostic processor
def analyze_patterns(events):
    patterns = {}
    for e in events:
        key = e % 10
        if key not in patterns:
            patterns[key] = 0
        patterns[key] += 1
    
    # Red herring: complex but unused pattern analysis
    entropy = 0.0
    total = sum(patterns.values())
    for count in patterns.values():
        p = count / total
        entropy -= p * math.log(p)
    
    # Actual relevant computation (obscured)
    mode = max(patterns, key=patterns.get)
    return mode * 100

# Main metric processor
def process_metrics(log_data, state):
    # Key variable initialization
    diagnostics = {}
    temp_log = []
    
    # Real computation buried in noise
    base_value = log_data['current'] * 1000
    offset = analyze_patterns(state['event_sequence'])
    diagnostics['level'] = base_value + offset
    
    # Multiple layers of irrelevant processing
    temp_log.append(base_value)
    temp_log.append(offset)
    
    # Distractor: complex dictionary transformations with no impact
    summary = {
        k.upper(): f"{v:.2f}" for k, v in log_data.items() if isinstance(v, float)
    }
    summary['FLAG'] = any(float(v) > 0.8 for v in summary.values())
    
    # Fake aggregation chain
    aggregator = lambda a, b: a + b * 0.1
    fake_total = 0
    for val in temp_log:
        fake_total = aggregator(fake_total, val)
    
    # Final red herring function (never called)
    def validate_integrity(checksum):
        return (checksum ^ 0xAAAA) & 0xFFFF
    
    # The real answer is constructed here
    final_diagnostic = int(diagnostics['level']) + state['calibration_offset']
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    # System state with meaningful and irrelevant fields
    system_state = {
        'status': 'ACTIVE',
        'event_sequence': [23, 45, 67, 23, 89, 23, 56],  # Mode: 23 -> contributes 2300
        'version': '2.1.5',
        'calibration_offset': -150,
        'debug_mode': False,
        'buffer': [0]*100  # Unused large structure (distraction)
    }
    
    # Log data containing key values
    log_data = collect_telemetry()
    
    # Misleading pre-check (no effect on result)
    health = calculate_health_score(log_data)
    
    # Critical execution point
    final_diagnostic = process_metrics(log_data, system_state)
    
    # Print required output
    print(f"Result: {final_diagnostic}")