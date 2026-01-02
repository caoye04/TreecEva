from itertools import cycle, islice

def simulate_growth(base_rate, inhibitors, promoters):
    # Irrelevant complex-looking computation (not used in final result)
    dummy_calc = sum([i ** 2 for i in inhibitors]) * len(promoters) % 997
    growth = base_rate
    for p in promoters:
        growth *= (1 + p / 10)
    for i in inhibitors:
        growth *= (1 - i / 20) if i < 10 else 0.5
    return int(growth)

def evaluate_stability(readings):
    # Distractor function: processes sensor data but not used in answer
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return variance < 5

def normalize_sequence(seq):
    # Unused helper with misleading relevance
    total = sum(seq)
    return [s / total for s in seq] if total != 0 else seq

def filter_outliers(data, threshold=2):
    # Dead code path — never called
    mean = sum(data) / len(data)
    return [x for x in data if abs(x - mean) <= threshold]

def harvest_results(cycles):
    # Core logic embedded in noise
    cumulative = 0
    adjustment_factor = 0.85
    for cycle_data in cycles:
        phase = cycle_data['phase']
        raw_output = cycle_data['output']
        if phase == 'growth':
            # Only this branch contributes to final result
            adjusted = raw_output * adjustment_factor
            cumulative += int(adjusted)
        elif phase == 'decay':
            cumulative -= 5  # Minor red herring, but actually used
        else:
            temp_hold = raw_output // 4  # Distractor assignment
            cumulative += temp_hold % 7  # Minimal impact, looks significant
    return cumulative + 17  # Final adjustment

# Main execution block
sensor_logs = [85, 87, 86, 90, 84, 88, 89]
stability = evaluate_stability(sensor_logs)  # Computed but unused

# Simulate production phases (only 'output' and 'phase' matter)
base_production = [120, 140, 160]
inhibitors = [3, 7, 2]
promoters = [1.5, 2.0]

# Heavily disguised generation of relevant structure
raw_cycles = []
temp_tracker = []
for idx, val in enumerate(base_production):
    rate = simulate_growth(val, inhibitors, promoters)  # Looks important
    temp_tracker.append(rate)
    phase_type = 'growth' if idx == 0 else 'decay' if idx == 2 else 'maintenance'
    raw_cycles.append({'output': rate + 10, 'phase': phase_type})

# Add decoy entries with misleading keys
raw_cycles.append({'output': 999, 'phase': 'debug', 'diagnostic': {'level': 'critical'}})
raw_cycles.append({'output': 0, 'phase': 'idle'})

# Use itertools to create illusion of complexity
production_cycle_stream = list(islice(cycle(raw_cycles), 0, 10))
filtered_production = [item for item in production_cycle_stream if item['phase'] in ['growth', 'decay', 'maintenance']]

# Key computation buried in distractions
final_yield = 0
intermediate_flags = {"optimized": False, "verified": True}
log_entry = "YIELD_CALC_PHASE_1"

# Actual answer-determining step
final_yield = harvest_results(filtered_production)

# Print required output
print(f"Target result: {final_yield}")