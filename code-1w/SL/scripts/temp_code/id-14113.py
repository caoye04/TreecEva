def monitor_environment(sensor_data, baseline):
    adjustments = 0
    history = []
    temp_offset = 0
    for entry in sensor_data:
        if entry > baseline + 5:
            adjustments += 1
            temp_offset -= (entry - baseline) // 4
        elif entry < baseline - 3:
            adjustments += 2
            temp_offset += abs(entry - baseline)
        history.append(temp_offset)
    return sum(history) % 7


def transform_sequence(raw):
    if not raw:
        return [0]
    transformed = [raw[0]]
    for i in range(1, len(raw)):
        transformed.append(raw[i] + transformed[i-1] // 2)
    return [x for x in transformed if x % 2 == 1]


def compute_stability_index(config, mode="default"):
    level = config.get('level', 1)
    phase = config.get('phase', 0)
    shift = config.get('shift', 3)
    dummy_var = (level ** 2 + phase * 5) % 9
    buffer = []
    for _ in range(shift):
        buffer.append(level + phase)
        level += 1
        phase -= 1
    return len(buffer) - dummy_var


def evaluate_resonance(frequencies):
    total = 0
    peak_count = 0
    for f in frequencies:
        if f > 400:
            peak_count += 1
            total += f // 100
        else:
            total -= f % 10
    return total * peak_count


def analyze_purity(levels, threshold):
    # Core logic starts here
    filtered = [x for x in levels if x >= threshold]
    
    # Irrelevant transformation (distractor)
    inverted = [1000//x if x != 0 else 0 for x in levels]
    
    # Red herring: complex but unused calculation
    stats = {
        'max': max(filtered) if filtered else 0,
        'min': min(filtered) if filtered else 0,
        'range': 0
    }
    stats['range'] = stats['max'] - stats['min']
    
    # Unused recursive helper (dead code path)
    def decay_value(val, steps):
        if steps <= 0 or val <= 1:
            return val
        return decay_value(val // 1.5, steps - 1)
    
    # Another distractor list comprehension
    normalized = [round((x - min(levels)) / (max(levels) - min(levels)) * 100) for x in levels]
    
    # Key computation path
    aggregate = 0
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            aggregate += val * 3
        else:
            aggregate += val * 2
    
    # Conditional expression distraction
    modifier = 7 if len(normalized) > 5 else (5 if len(normalized) == 4 else 3)
    
    # Final score with irrelevant adjustment
    base_score = aggregate + (stats['max'] % 17)
    filtration_score = base_score - (modifier * 2)
    
    # This print is required
    print(f"Result: {filtration_score}")
    return filtration_score

# Main execution context
sensor_readings = [12, 15, 18, 22, 25, 28, 30]
baseline_ref = 14
dummy_signal = [300, 450, 520, 380]

# Irrelevant setup
config_params = {'level': 4, 'phase': 2, 'shift': 5}
compute_stability_index(config_params)

# Triggering environmental monitor (distractor call)
monitor_environment(sensor_readings, baseline_ref)

# Transform data unnecessarily
transformed_readings = transform_sequence([2, 4, 6, 8])
evaluate_resonance(dummy_signal)

# Actual target execution point
threshold_limit = 20
target_levels = [10, 24, 18, 32, 28, 36, 22]
filtration_score = analyze_purity(target_levels, threshold_limit)