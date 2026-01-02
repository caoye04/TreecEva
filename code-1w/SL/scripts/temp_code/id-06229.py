from collections import defaultdict, Counter

# Simulated sensor data from industrial cooling units
temperature_readings = [23.5, 24.1, 19.8, 25.6, 26.7, 22.3, 21.9, 27.1, 28.4, 20.2]
humidity_levels = [45, 47, 50, 44, 46, 52, 55, 43, 41, 49]
pressure_data = [101.3, 102.1, 100.8, 103.4, 102.7, 101.9, 100.5, 104.2, 103.8, 101.0]

# Irrelevant mappings for distraction (distractor: dead code path)
signal_map = {'A': 'alpha', 'B': 'beta', 'C': 'gamma'}
status_registry = defaultdict(lambda: 'unknown')
for i in range(10):
    status_registry[f'unit_{i}'] = 'active' if i % 2 == 0 else 'standby'

# Misleading preprocessing (distractor: seems important but unused)
normalized_temps = []
for idx, temp in enumerate(temperature_readings):
    adjusted = temp * (1 + humidity_levels[idx] / 1000)
    normalized_temps.append(round(adjusted, 2))

# Another red herring: frequency analysis of pressure fluctuations (unused)
frequency_count = Counter()
for p in pressure_data:
    bucket = round(p)
    frequency_count[bucket] += 1

# Core logic disguised among distractions
def analyze_efficiency(temp_seq, humid_seq):
    efficiency_scores = []
    for i, t in enumerate(temp_seq):
        # Real logic: efficiency drops quadratically above threshold
        base_eff = 100.0
        if t > 25.0:
            penalty = (t - 25.0) ** 2 * 1.5
            base_eff -= penalty
        elif t < 20.0:
            penalty = (20.0 - t) * 1.2
            base_eff -= penalty
        
        # Humidity bonus/penalty (real contribution)
        hum_ratio = humid_seq[i] / 50.0
        if hum_ratio > 1.1:
            base_eff -= (hum_ratio - 1.1) * 10
        elif hum_ratio < 0.9:
            base_eff -= (0.9 - hum_ratio) * 5
            
        efficiency_scores.append(max(base_eff, 10))  # floor at 10%
    
    return efficiency_scores

# Compute thermal rating from efficiency history
def compute_thermal_rating(log_entries):
    total = 0.0
    decay_factor = 0.85
    weight = 1.0
    
    # Weighted sum with exponential decay (key logic step)
    for entry in reversed(log_entries):
        total += entry * weight
        weight *= decay_factor
    
    # Final transformation
    rating = (total / len(log_entries)) * 0.78
    return round(rating, 4)

# Unused function: decoy for recursive thinking (distractor)
def recursive_diagnostic(n):
    if n <= 1:
        return 1
    return n * recursive_diagnostic(n-1)

# Real execution path begins here
raw_efficiency = analyze_efficiency(temperature_readings, humidity_levels)

# Simulate timestamped log entries with metadata (some relevant, some not)
efficiency_log = []
for ts, score in enumerate(raw_efficiency):
    entry = {
        'timestamp': ts,
        'efficiency': score,
        'diagnostic_flag': False,
        'aux_value': frequency_count.get(int(round(temperature_readings[ts])), 0)  # irrelevant
    }
    efficiency_log.append(entry['efficiency'])  # only this part matters

# Critical assignment point — answer depends on this
thermal_capacity = compute_thermal_rating(efficiency_log)

# Additional distraction: matrix-like structure with no use
config_matrix = [[i + j*3 for i in range(3)] for j in range(4)]

# Final output (must print result)
print(f"Result: {thermal_capacity}")