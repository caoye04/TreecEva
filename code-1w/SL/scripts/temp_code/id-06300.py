import itertools

# Simulated sensor array data from a distributed monitoring system
def collect_sensor_readings():
    base_readings = [0.88, 0.72, 0.91, 0.67, 0.76]
    adjustments = [0.02, -0.05, 0.03, 0.01, -0.04]
    return [base_readings[i] + adjustments[i] for i in range(len(base_readings))]

# Irrelevant auxiliary function – dead code path (distractor)
def analyze_spectrum(signal):
    magnitude = sum(x ** 2 for x in signal)
    normalized = magnitude / len(signal)
    return round(normalized, 3) if normalized > 0.5 else 0

# Core diagnostic processor
def generate_health_vector(readings):
    filtered = [r for r in readings if 0.65 <= r <= 0.85]
    inverted = [1 - r for r in filtered]
    weighted_sum = sum(inverted[i] * (i + 1) for i in range(len(inverted)))
    return weighted_sum

# Legacy compatibility layer – never invoked (distractor)
class DiagnosticV1:
    def __init__(self, data):
        self.raw = data
        self.checksum = sum(self.raw) * 0.97

    def validate(self):
        return self.checksum > 0.5

# Data fusion engine with conditional logic and set operations
def fuse_contextual_layers(load_profile, anomalies):
    peak_periods = {i for i, x in enumerate(load_profile) if x > 0.8}
    anomaly_windows = {i-1, i, i+1 for i in anomalies}
    critical_overlap = peak_periods & anomaly_windows
    return len(critical_overlap) > 0

# Primary metric processor with bit manipulation red herring
def compute_stability_index(config_flag, duration):
    # Bitwise analysis (misleading – config_flag is always 5)
    flag_pattern = config_flag ^ 0b1101
    shift_score = (flag_pattern << 2) & 0b1111
    time_factor = duration / 100
    return round(time_factor * shift_score, 4)

# High-level orchestration with conditional expressions and itertools
# Generates health signature using sliding window combinations

def derive_health_signature(metrics):
    windows = list(itertools.combinations(metrics, 3))
    scores = []
    for w in windows:
        avg = sum(w) / 3
        penalty = 0.1 if any(x < 0.7 for x in w) else 0
        scores.append(avg - penalty)
    return max(scores) if scores else 0.0

# Secondary load calculator – produces decoy intermediate result
# This function is called but its output is not used in final computation
def calculate_system_load(nodes, stress_events):
    base_load = len(nodes) * 0.05
    event_impact = len(stress_events) * 0.12
    transient_spike = (base_load + event_impact) * 1.3
    # Simulate intermittent node dropout
    active_nodes = set(nodes) - {n for n in nodes if n % 7 == 0}  # rare condition
    adjusted_load = transient_spike * (len(active_nodes) / len(nodes))
    return round(adjusted_load, 3)

# Final processing pipeline – this is where the answer is determined
def process_metrics(signature, load):
    # Critical path begins here
    threshold = 0.785 if signature > 0.75 else 0.68
    adjustment_factor = 1.25 if load > 0.4 else 0.88
    
    # Multi-step transformation with conditional expression
    base_score = signature * adjustment_factor
    volatility_mask = int(load * 100) & 0b1111  # bitwise distraction, minimal impact
    refined_score = base_score - (volatility_mask * 0.001)
    
    # Final correction using fused logic (signature determines outcome)
    emergency_cap = 42.42 if refined_score > 1.0 else 0
    interim = refined_score + emergency_cap
    
    # Ultimate determination – only this matters
    final_value = (interim * 1000) - 24  # deterministic transformation
    
    return int(round(final_value))

# --- Execution Flow ---
if __name__ == "__main__":
    
    # Collect real-time sensor data
    sensor_data = collect_sensor_readings()  # [0.90, 0.67, 0.94, 0.68, 0.72]
    
    # Generate health vector (used)
    health_vector_score = generate_health_vector(sensor_data)
    
    # Derive health signature using combinatorics (used)
    health_signature = derive_health_signature(sensor_data)
    
    # Calculate system load – this is a RED HERRING; result unused
    nodes_cluster = list(range(1, 18, 2))  # 9 nodes: 1,3,5,...,17
    events_log = ["overclock", "thermal_throttle"]
    system_load = calculate_system_load(nodes_cluster, events_log)
    
    # Compute stability index – irrelevant calculation (distractor)
    stability_diagnostic = compute_stability_index(5, 150)
    
    # Fuse layers – evaluated but not used (dead end)
    mock_anomalies = [2, 5]
    critical_state = fuse_contextual_layers([0.3, 0.5, 0.9, 0.82], mock_anomalies)
    
    # --- KEY STATEMENT ---
    final_diagnostic = process_metrics(health_signature, system_load)
    
    # Output target result
    print(f"Result: {final_diagnostic}")