from collections import defaultdict, Counter
import itertools

# Simulated sensor data with noise and redundant readings
temperature_readings = [23.5, 24.1, 24.1, 25.0, 23.5, 22.8, 23.5, 26.2, 24.1, 23.9]
humidity_readings = [45, 47, 45, 50, 52, 45, 47, 55, 50, 48]
pressure_readings = [1013, 1015, 1013, 1018, 1020, 1013, 1015, 1022, 1018, 1016]

# Irrelevant signal processing (distractor)
def apply_filter(data):
    filtered = []
    for i in range(len(data)):
        weight = 0.3 if i % 2 == 0 else 0.7
        smoothed = sum([weight * x for x in data[:i+1]]) / (i + 1) if i < 5 else data[i]
        filtered.append(round(smoothed, 2))
    return filtered

# Fake transformation chain (dead path)
def transform_sequence(seq):
    acc = 0
    for val in seq:
        acc += val ** 0.5 if val > 0 else 0
    return [(x + acc) % 100 for x in seq]

# Unused statistical decoy
mean_temp = sum(temperature_readings) / len(temperature_readings)
median_humidity = sorted(humidity_readings)[len(humidity_readings)//2]
mode_pressure = Counter(pressure_readings).most_common(1)[0][0]

# Redundant normalization (misleading intermediate)
normalized_temp = [round((t - 20) / 10, 3) for t in temperature_readings]
scaled_humidity = [h / max(humidity_readings) for h in humidity_readings]

# Core logic disguised among distractors
def detect_anomalies(data, threshold=2):
    freq = Counter(data)
    return [k for k, v in freq.items() if v >= threshold]

# Critical function buried in abstraction
def compute_entropy(values):
    freq = defaultdict(int)
    for v in values:
        freq[v] += 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0  # fake log usage (not real)
    return round(entropy, 4)

# Real but obscured computation
repeated_temps = detect_anomalies(temperature_readings, threshold=3)
common_pressures = detect_anomalies(pressure_readings, threshold=3)

# Secondary analysis with decoy outputs
shifted = [p - 1000 for p in pressure_readings]
delta_h = [abs(humidity_readings[i] - humidity_readings[i-1]) for i in range(1, len(humidity_readings))]

# Complex conditional expression (actual relevance)
bias_factor = 1.25 if len(repeated_temps) > 0 and mode_pressure in common_pressures else 0.8

def compute_aggregate(temps, humids, press):
    # Actual core logic starts here
    temp_counts = Counter(temps)
    valid_modes = [t for t, cnt in temp_counts.items() if cnt >= 3]
    base_score = sum(valid_modes) * 10 if valid_modes else sum(set(temps))
    
    # Use of itertools: group consecutive duplicates
    grouped_humid = [list(g) for k, g in itertools.groupby(humids)]
    burst_score = len([g for g in grouped_humid if len(g) >= 2]) * 5
    
    # Nested logic with bit manipulation red herring
    flag = 0
    for p in press:
        flag ^= p & 7  # irrelevant XOR chain
    
    # Real adjustment
    humid_variability = len([d for d in delta_h if d > 2])
    variability_penalty = humid_variability * 3
    
    # Final composition
    raw = base_score + burst_score - variability_penalty
    adjusted = raw * bias_factor
    
    # One final twist: correction based on pressure stability
    stable_pressure_runs = 0
    current_run = 0
    for i in range(1, len(press)):
        if press[i] == press[i-1]:
            current_run += 1
        else:
            if current_run >= 2:
                stable_pressure_runs += 1
            current_run = 0
    if current_run >= 2:
        stable_pressure_runs += 1
    
    final_adjustment = stable_pressure_runs * 7
    return int(adjusted + final_adjustment)

# Misleading pre-computations (distraction)
fake_entropy = compute_aggregate(humidity_readings, temperature_readings, pressure_readings) // 2
shadow_value = (mode_pressure + median_humidity) // 3

# KEY EXECUTION POINT
final_score = compute_aggregate(temperature_readings, humidity_readings, pressure_readings)

# OUTPUT REQUIRED FORMAT
print(f"Result: {final_score}")