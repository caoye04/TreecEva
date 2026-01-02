import math

# Simulated environmental monitoring system for volcanic activity prediction

def collect_seismic_data():
    raw_signals = [0.7, 1.2, 0.9, 2.3, 1.8, 0.5, 3.1, 2.7]
    baseline = 1.5
    filtered = [x for x in raw_signals if x > baseline]  # Only significant tremors
    return filtered


def calculate_magma_pressure(temperature, depth, gas_ratio):
    # Complex pressure model (simplified)
    base_pressure = temperature * 8.31 / (depth + 1)
    adjustment = math.log(gas_ratio + 1) * 2.7
    return base_pressure + adjustment


def normalize_readings(readings):
    if not readings:
        return [0]
    max_val = max(readings)
    return [round(x / max_val, 3) for x in readings]


def detect_anomalies(normalized):
    threshold = 0.75
    anomalies = []
    for i, val in enumerate(normalized):
        if val > threshold:
            anomalies.append((i, val))
    return anomalies


def compute_trend_score(anomalies):
    score = 0
    for idx, value in anomalies:
        contribution = (idx + 1) * value
        score += contribution
    return round(score, 4)


def generate_simulation_matrix(size):
    # Irrelevant function - simulates geological layers (dead code path)
    matrix = [[(i*j) % 7 for j in range(size)] for i in range(size)]
    return matrix


def evaluate_stress_patterns(data):
    # Misleading intermediate computation
    total_energy = sum([x**2 for x in data])
    avg_energy = total_energy / len(data)
    fluctuation_index = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    
    # Dummy stress levels - not used in final result
    stress_levels = ['low', 'medium', 'high']
    assigned = []
    for x in data:
        if x < 1.0:
            assigned.append(stress_levels[0])
        elif x < 2.0:
            assigned.append(stress_levels[1])
        else:
            assigned.append(stress_levels[2])
    return avg_energy  # Not actually used later


def process_volcanic_indicators(raw_data, temp, depth, ratio):
    # Main processing pipeline
    pressure = calculate_magma_pressure(temp, depth, ratio)
    normalized_data = normalize_readings(raw_data)
    anomalies = detect_anomalies(normalized_data)
    trend = compute_trend_score(anomalies)
    
    # Decoy calculations with irrelevant variables
    entropy = -sum(p * math.log(p) for p in normalized_data if p > 0)
    dispersion = max(normalized_data) - min(normalized_data)
    
    # Critical intermediate result
    instability_factor = pressure * trend
    
    # Unused simulation (distractor)
    sim_matrix = generate_simulation_matrix(6)
    eigen_sum = sum(sim_matrix[i][i] for i in range(len(sim_matrix)))  # Red herring
    
    return {
        'instability': instability_factor,
        'readings': normalized_data,
        'anomalies': anomalies
    }


def analyze_readings(processed):
    # Final diagnostic logic
    raw_instability = processed['instability']
    
    # Apply environmental correction factor
    correction = 1.0
    if len(processed['anomalies']) > 2:
        correction *= 1.2
    if max(processed['readings']) > 0.9:
        correction *= 1.15
    
    adjusted_risk = raw_instability * correction
    
    # Additional decoy logic
    warning_level = ''
    if adjusted_risk < 5:
        warning_level = 'green'
    elif adjusted_risk < 10:
        warning_level = 'yellow'
    else:
        warning_level = 'red'
    
    # Final computation
    diagnostic_code = int(round(adjusted_risk * 100))
    
    # More red herrings
    phase_state = math.sin(diagnostic_code % 10) > 0.5
    resonance = (diagnostic_code ^ 255) & 127
    
    return diagnostic_code

# Execution flow
if __name__ == '__main__':
    # Initial data collection
    seismic_data = collect_seismic_data()
    
    # Environmental parameters
    current_temp = 850      # Celsius
    crustal_depth = 4.2     # km
    co2_ratio = 0.43        # CO2 fraction in gas emissions
    
    # Evaluate stress (irrelevant call - misleading)
    _ = evaluate_stress_patterns(seismic_data)
    
    # Process the real data
    processed_data = process_volcanic_indicators(seismic_data, current_temp, crustal_depth, co2_ratio)
    
    # Compute final diagnostic (KEY STATEMENT)
    final_diagnostic = analyze_readings(processed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")