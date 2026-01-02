from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.7, 'errors': 2, 'timestamp': 1000},
    {'node': 'B', 'load': 0.9, 'errors': 5, 'timestamp': 1001},
    {'node': 'A', 'load': 0.3, 'errors': 0, 'timestamp': 1002},
    {'node': 'C', 'load': 0.8, 'errors': 8, 'timestamp': 1003},
    {'node': 'B', 'load': 0.6, 'errors': 1, 'timestamp': 1004},
    {'node': 'C', 'load': 0.2, 'errors': 0, 'timestamp': 1005}
]

# Irrelevant utility function (decoy)
def analyze_throughput(data):
    total = 0
    for entry in data:
        if entry['load'] > 0.5:
            total += entry['load'] * 100
    adjustment = math.floor(total / 10) * 0.1
    return adjustment if adjustment < 50 else 50

# Misleading metric accumulator (dead path)
class LegacyAnalyzer:
    def __init__(self):
        self.history = []
        self.threshold = 0.75
    
    def update(self, val):
        self.history.append(val > self.threshold)
    
    def get_stability(self):
        return sum(self.history) / len(self.history) if self.history else 0

# Unused but plausible-looking data transformation
def shift_phase_signal(signal):
    shifted = []
    for i in range(len(signal)):
        phase = (signal[i] * 1.618) % 1
        shifted.append(math.sin(phase * 2 * math.pi))
    return shifted

# Core logic disguised among distractors
def preprocess_metrics(raw_telemetry):
    node_loads = defaultdict(list)
    error_count = Counter()
    temporal_gaps = []
    
    for i in range(len(raw_telemetry)):
        entry = raw_telemetry[i]
        node = entry['node']
        node_loads[node].append(entry['load'])
        error_count[node] += entry['errors']
        
        if i > 0:
            delta = entry['timestamp'] - raw_telemetry[i-1]['timestamp']
            temporal_gaps.append(delta)
    
    # Distractor computation
    avg_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0
    peak_frequency = len([g for g in temporal_gaps if g == 1])
    
    # Relevant aggregation
    avg_loads = {node: sum(loads)/len(loads) for node, loads in node_loads.items()}
    return avg_loads, dict(error_count)

# Secondary processing with early termination red herring
def normalize_metrics(load_dict, err_dict):
    normalized = {}
    scaling_factor = 1.0
    
    for node in load_dict:
        load = load_dict[node]
        errors = err_dict.get(node, 0)
        
        if load < 0.5 and errors == 0:
            scaling_factor = 0.8  # Efficient node bonus (distractor)
            continue  # Skip further processing for low-load nodes
            
        # This path is actually never taken due to structure above
        risk_score = errors * 2 + (1 - load) * 10
        normalized[node] = {
            'risk': risk_score,
            'penalty': errors ** 1.5
        }
    
    # Actual relevant transformation happens here after loop
    high_risk_nodes = len([v for v in normalized.values() if v['risk'] > 15])
    return scaling_factor, high_risk_nodes, normalized

# Main evaluation with hidden logic chain
def evaluate_performance(metrics_tuple, baseline):
    avg_loads, err_dict = metrics_tuple
    scale, risky_count, details = normalize_metrics(avg_loads, err_dict)
    
    # Hidden critical calculation
    stability_metric = 0
    for load in avg_loads.values():
        stability_metric += abs(load - 0.5) * 2
    
    # Decoy usage of collections
    decoy_counter = Counter()
    decoy_counter.update(['A']*3, ['B']*5, ['C']*2)
    decoy_counter.subtract(['A']*2)
    irrelevant_sum = sum(decoy_counter.values())
    
    # Critical path: composite score based on balanced performance
    balance_score = 0
    for node, load in avg_loads.items():
        deviation = abs(load - baseline[node])
        balance_score += deviation * 100
    
    # Final computation - only this matters
    raw_errors = sum(err_dict.values())
    adjustment = (risky_count * 10) - (scale * 5)
    final_component = int((balance_score + raw_errors * 3) - adjustment)
    
    # The actual answer is embedded here
    final_score = int(1000 - final_component)  # This is the key result
    return final_score

# Orchestration with misleading setup
if __name__ == '__main__':
    # Baseline reference values
    baseline_ref = {'A': 0.5, 'B': 0.7, 'C': 0.4}
    
    # Dead initialization
    analyzer = LegacyAnalyzer()
    for t in telemetry_stream:
        analyzer.update(t['load'])
    
    # Signal processing decoy
    signal_data = [e['load'] for e in telemetry_stream]
    processed_signal = shift_phase_signal(signal_data)
    coherence = sum(abs(x) for x in processed_signal) / len(processed_signal)
    
    # Real pipeline
    metric_data = preprocess_metrics(telemetry_stream)
    final_score = evaluate_performance(metric_data, baseline_ref)
    
    # Output required variable
    print(f"Result: {final_score}")