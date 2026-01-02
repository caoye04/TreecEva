import itertools

# Simulated sensor data readings (temperature, pressure, humidity)
data = [
    (23.5, 1013, 45),
    (25.0, 1010, 50),
    (22.8, 1015, 47),
    (26.1, 1008, 52),
    (24.3, 1012, 49)
]

# Irrelevant auxiliary data (decoy)
aux_data = [(x*0.1, x//2) for x in range(10)]

# Weight configuration for metrics (real weights used in computation)
weights = {'temp': 0.4, 'pressure': 0.3, 'humidity': 0.3}

# Phantom weights (red herring - not used)
phantom_weights = {'t': 0.2, 'p': 0.5, 'h': 0.3}

# Precomputed magic numbers (distractor)
magic_table = {i: i**2 + 3*i for i in range(15)}

# Decoy function that appears useful but is never called
def analyze_pattern(seq):
    return [a - b for a, b in zip(seq[1:], seq[:-1])]

# Auxiliary transformation (not used in main path)
shifted_data = [(t+273.15, p*0.001, h/100) for t, p, h in data]

# Flag to control hypothetical branch (always false - dead code path)
debug_mode = False

# Secondary derived dataset (unused - distraction)
normalized = [
    tuple(val / max(data[j][i] for j in range(len(data))) 
    for i, val in enumerate(row)) for row in data
]

# Core processing function with multiple concepts
def process_metrics(readings, config):
    # Step 1: Extract baseline averages
    avg_temp = sum(r[0] for r in readings) / len(readings)
    avg_pressure = sum(r[1] for r in readings) / len(readings)
    avg_humidity = sum(r[2] for r in readings) / len(readings)

    # Step 2: Compute deviations (some used, some ignored)
    temp_devs = [abs(r[0] - avg_temp) for r in readings]
    pressure_devs = [abs(r[1] - avg_pressure) for r in readings]

    # Step 3: Apply weighting logic using lambda and zip
    base_scores = list(map(
        lambda x: x[0]*config['temp'] + x[1]*config['pressure'] + x[2]*config['humidity'],
        readings
    ))

    # Step 4: Normalize scores using min-max scaling
    min_score, max_score = min(base_scores), max(base_scores)
    if max_score != min_score:
        normalized_scores = [(s - min_score) / (max_score - min_score) for s in base_scores]
    else:
        normalized_scores = [0.5] * len(base_scores)

    # Step 5: Aggregate using moving average simulation (itertools.cycle used as distractor below)
    window_size = 3
    cumulative = 0
    trend_adjusted = []
    cycle_iter = itertools.cycle([1, -1])  # Distractor iterator

    for i, score in enumerate(normalized_scores):
        window = normalized_scores[max(0, i - window_size + 1):i + 1]
        moving_avg = sum(window) / len(window)
        trend_factor = moving_avg * 0.1 * next(cycle_iter)  # Introduces oscillation but net zero effect
        trend_adjusted.append(moving_avg + trend_factor)

    # Step 6: Final aggregation with conditional boost
    raw_final = sum(trend_adjusted) / len(trend_adjusted)
    
    # Conditional adjustment based on deviation threshold (uses only temp devs)
    high_variation = any(d > 1.5 for d in temp_devs)
    
    if high_variation and raw_final < 0.7:
        final_value = raw_final * 1.2
    elif not high_variation:
        final_value = raw_final * 0.95
    else:
        final_value = raw_final

    # Step 7: Scale to integer-like metric (simulate calibration offset)
    calibrated = int(final_value * 1000) / 1000.0  # Truncate to 3 decimals

    # Step 8: Apply phantom correction (never actually changes value - red herring)
    corrections = {'offset': 0, 'gain': 1.0}  # Neutral correction
    applied = (calibrated + corrections['offset']) * corrections['gain']

    # Final scoring with rounding
    result = round(applied * 1000)  # Convert to scaled integer

    return result

# Dead code block - unreachable due to early structure
if debug_mode:
    print("Debug mode active")
    temp_analysis = analyze_pattern([row[0] for row in data])

# Main execution
final_score = process_metrics(data, weights)

# Print result as required
print(f"Target result: {final_score}")