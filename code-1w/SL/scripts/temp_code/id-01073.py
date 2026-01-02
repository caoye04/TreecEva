from collections import defaultdict, Counter
import math

def analyze_sequence(seq):
    # Irrelevant helper function – never called
    return sum(x ** 2 for x in seq if x > 0)

def auxiliary_hash(data):
    # Dead code path – looks important but unused
    result = 0
    for item in data:
        result ^= hash(str(item)) % 10007
    return result

def evaluate_stability(ring_buffer, tolerance=1e-4):
    # Distractor function: appears relevant but not used in main logic
    variance = sum((x - sum(ring_buffer)/len(ring_buffer))**2 for x in ring_buffer) / len(ring_buffer)
    return variance < tolerance

def compute_baseline(dataset):
    # Unused but plausible-sounding preprocessing function
    filtered = [x for x in dataset if x >= 0]
    if not filtered:
        return 0.0
    log_scaled = [math.log(x + 1) for x in filtered]
    return sum(log_scaled) / len(log_scaled)

def extract_signatures(events):
    # Another decoy function with complex logic
    sig_map = defaultdict(int)
    for idx, event in enumerate(events):
        if isinstance(event, str):
            for char in set(event):
                sig_map[char] += idx + 1
    return dict(sig_map)

def process_metrics(data_stream, config):
    # Core logic hidden among distractions
    
    # Initialize tracking variables (some irrelevant)
    stats = defaultdict(float)
    event_count = 0
    total_magnitude = 0.0
    peak_anomalies = []
    rolling_window = []
    
    # Red herring variables
    temp_checksum = 0
    debug_trace = []
    fallback_mode = False
    
    # Simulate multi-stage processing
    for timestamp, entry in enumerate(data_stream):
        if 'type' not in entry or 'value' not in entry:
            continue
            
        event_type = entry['type']
        raw_value = entry['value']
        
        # Real computation begins
        if event_type == 'sensor_read':
            event_count += 1
            total_magnitude += abs(raw_value)
            
            # Actual key transformation
            normalized = abs(raw_value) ** 0.5
            if normalized > config.get('critical_level', 100):
                peak_anomalies.append(normalized)
            
            # Update rolling stats
            stats['sum_sqrt'] += math.sqrt(abs(raw_value) + 1e-5)
            stats['harm_count'] += 1
            
        elif event_type == 'system_ping':
            # Looks important, but only increments a distractor
            debug_trace.append(f"Ping at {timestamp}")
            temp_checksum ^= timestamp % 256
            
        elif event_type == 'log_anchor':
            # Used to inflate complexity
            rolling_window.append(len(entry.get('tags', [])))

    # Secondary analysis on collected stats
    harmonic_mean = 0.0
    if stats['harm_count'] > 0 and stats['sum_sqrt'] > 0:
        harmonic_mean = stats['harm_count'] / stats['sum_sqrt']
    
    # Real answer derivation buried here
    anomaly_score = len(peak_anomalies) * 1000
    base_integral = int(total_magnitude // (event_count + 1))
    
    # Final computation interweaves multiple concepts
    diagnostic_code = base_integral + anomaly_score
    
    # More red herrings
    metadata_summary = Counter(debug_trace)
    final_weight = diagnostic_code % 10001
    
    # This is the actual target variable
    final_diagnostic = diagnostic_code + int(harmonic_mean * 100)
    
    # Early return trap – condition never met
    if fallback_mode:
        return temp_checksum % 1000
        
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Simulated input data – realistic structure
    log_data = [
        {'type': 'sensor_read', 'value': 256.0, 'seq': 1},
        {'type': 'sensor_read', 'value': 81.0, 'seq': 2},
        {'type': 'system_ping', 'value': None, 'seq': 3},
        {'type': 'sensor_read', 'value': 625.0, 'seq': 4},
        {'type': 'sensor_read', 'value': 10000.0, 'seq': 5},
        {'type': 'log_anchor', 'tags': ['A','B'], 'seq': 6},
        {'type': 'sensor_read', 'value': 400.0, 'seq': 7},
        {'type': 'sensor_read', 'value': 144.0, 'seq': 8},
    ]
    
    system_thresholds = {
        'critical_level': 20.0,
        'stability_window': 5
    }
    
    # Irrelevant pre-processing steps
    sorted_indices = [i for i, _ in sorted(enumerate(log_data), key=lambda x: str(x[1]))]
    zipped_pairs = list(zip(sorted_indices, [item['seq'] for item in log_data]))
    
    # Key assignment
    final_diagnostic = process_metrics(log_data, system_thresholds)
    
    # Output required format
    print(f"Result: {final_diagnostic}")