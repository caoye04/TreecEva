from collections import defaultdict, Counter
import math

# Simulate a system integrity diagnostic with multiple noise layers
def analyze_component_health(sensor_log, thresholds):
    health_flags = []
    for entry in sensor_log:
        temp = entry['temp']
        pressure = entry['pressure']
        rpm = entry['rpm']
        
        # Distractor: irrelevant computation on vibration (not used later)
        vibration_index = (rpm * 0.02) ** 1.5 if rpm > 3000 else 0
        
        # Real logic: temperature-pressure consistency check
        expected_pressure = 100 * math.exp((temp - 25) / 50)
        deviation = abs(pressure - expected_pressure)
        
        # Threshold-based flag (only this matters)
        if deviation > thresholds['pressure_tolerance']:
            health_flags.append(False)
        else:
            health_flags.append(True)
    
    return all(health_flags)

# Misleading auxiliary function (dead end)
def estimate_lifespan_rbf(features):
    # Radial basis function approximation (never called)
    lifespan = 0
    for f in features:
        lifespan += math.exp(-((f - 50) ** 2) / 100)
    return lifespan

# Core data transformation with red herrings
def build_consistency_graph(metrics):
    graph = defaultdict(list)
    anomalies = []
    
    for i, m in enumerate(metrics):
        # Real dependency: track phase coherence
        phase = m['phase']
        coherence = m['coherence']
        
        # Distractor: power draw analysis (nowhere used)
        power_draw = m['voltage'] * m['current']
        efficiency = (power_draw / 1000) * coherence
        
        # Only this contributes to output
        if coherence < 0.65:
            graph['low_coherence'].append(i)
            anomalies.append(phase % 4 == 0)
        else:
            graph['stable'].append(i)
    
    # Distractor: complex but unused structure
    summary_stats = {
        'anomaly_density': sum(anomalies) / len(anomalies) if anomalies else 0,
        'total_nodes': len(graph['low_coherence']) + len(graph['stable'])
    }
    
    return graph  # Only graph structure matters, not stats

# Main computation buried in noise
def compute_integrity_score(matrix):
    score = 1000
    
    # Critical path: matrix contains diagnostic flags
    for key in matrix:
        if key == 'low_coherence':
            for idx in matrix[key]:
                # Each unstable node reduces score by index-dependent factor
                score -= (idx * 7) % 23
        elif key == 'stable':
            for idx in matrix[key]:
                score += 2  # Minor boost for stable nodes
    
    # Distractor: entropy calculation (computed but unused)
    total_entries = len(matrix.get('low_coherence', [])) + len(matrix.get('stable', []))
    if total_entries > 0:
        p_unstable = len(matrix.get('low_coherence', [])) / total_entries
        entropy = -sum(p * math.log2(p) for p in [p_unstable, 1-p_unstable] if p > 0)
        adjusted = score * (1 - entropy / 3)
    
    # Final score is NOT adjusted — distraction complete
    return score

# Irrelevant global constants (red herrings)
MAX_VOLTAGE = 480
CRITICAL_RPM = 7200
BASELINE_PHASE_NOISE = 0.041

# Sensor log — only temp and pressure matter
sensor_readings = [
    {'temp': 25, 'pressure': 100.2, 'rpm': 1200, 'vibration': 0.03},
    {'temp': 30, 'pressure': 110.1, 'rpm': 1800, 'vibration': 0.05},
    {'temp': 35, 'pressure': 122.0, 'rpm': 2400, 'vibration': 0.04},
    {'temp': 40, 'pressure': 135.5, 'rpm': 3000, 'vibration': 0.07}
]

thresholds_config = {
    'pressure_tolerance': 3.0,
    'vibration_cutoff': 0.1
}

# Run health analysis (produces boolean, used to gate next step)
primary_healthy = analyze_component_health(sensor_readings, thresholds_config)

# Metrics with multiple fields, some decoy
system_metrics = [
    {'phase': 12, 'coherence': 0.72, 'voltage': 220, 'current': 15},
    {'phase': 16, 'coherence': 0.58, 'voltage': 230, 'current': 14},
    {'phase': 20, 'coherence': 0.60, 'voltage': 210, 'current': 16},
    {'phase': 24, 'coherence': 0.55, 'voltage': 240, 'current': 13},
    {'phase': 28, 'coherence': 0.80, 'voltage': 200, 'current': 17},
    {'phase': 32, 'coherence': 0.67, 'voltage': 250, 'current': 12}
]

# Build graph — this is where relevant data is structured
consistency_matrix = build_consistency_graph(system_metrics)

# Final computation — target execution point
final_diagnostic = compute_integrity_score(consistency_matrix)

# Print result as required
print(f"Target result: {final_diagnostic}")