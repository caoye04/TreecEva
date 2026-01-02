from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis
def collect_readings():
    raw_signals = [
        (1, [0.8, 1.2, 0.9, 1.5]),
        (2, [2.1, 1.8, 2.3, 2.0]),
        (3, [0.5, 0.3, 0.7, 0.4]),
        (4, [3.0, 3.2, 2.9, 3.1])
    ]
    return raw_signals

def filter_noise(signal_list, noise_floor=0.6):
    filtered = []
    total_suppressed = 0  # Distractor: not used later
    for node_id, readings in signal_list:
        clean_reads = [r for r in readings if r >= noise_floor]
        if clean_reads:
            filtered.append((node_id, clean_reads))
    return filtered

def compute_variability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance)

def derive_stability_index(variability, base_score=100):
    # Higher variability reduces stability
    return max(0, base_score - variability * 10)

def generate_threshold_map(nodes):
    # Irrelevant mapping for hypothetical future use
    decoy_map = {i: {'warn': 1.5, 'fail': 2.8} for i in range(1, nodes+1)}
    actual_map = {1: 1.0, 2: 2.0, 3: 0.6, 4: 3.0}
    meta_info = sum(decoy_map.keys()) * 0.1  # Red herring computation
    return actual_map

def process_node_data(filtered_data):
    processed = defaultdict(dict)
    summary_stats = Counter()  # Distractor: initialized but not critical
    
    for node_id, readings in filtered_data:
        variability = compute_variability(readings)
        stability = derive_stability_index(variability)
        peak = max(readings)
        duration = len(readings) * 0.5  # Simulated time in seconds
        
        # Dummy aggregation to simulate complex processing
        if peak > 2.0:
            summary_stats['high_peak'] += 1
        elif stability < 70:
            summary_stats['low_stability'] += 1

        processed[node_id] = {
            'variability': variability,
            'stability': stability,
            'peak': peak,
            'duration': duration
        }
    
    # Fake post-processing step with no real impact
    if len(summary_stats) > 0:
        adjustment_factor = 0.95
        for nid in processed:
            processed[nid]['stability'] *= adjustment_factor  # Minor obfuscation

    return processed

def evaluate_health_status(stability, peak, threshold):
    if stability < 65:
        return 'CRITICAL'
    elif peak > threshold:
        return 'WARNING'
    else:
        return 'NORMAL'

def analyze_readings(processed_data, threshold_map):
    diagnostics = []
    status_counter = defaultdict(int)
    fake_correlation_score = 0.0  # Dead variable
    
    for node_id, data in processed_data.items():
        stability = data['stability']
        peak = data['peak']
        threshold = threshold_map.get(node_id, 1.0)
        
        # Complex conditional logic with red herrings
        if stability >= 85 and peak <= threshold:
            score_mod = 1.2
        elif stability < 65:
            score_mod = 0.5
        else:
            score_mod = 0.8
        
        raw_diagnostic = stability * score_mod
        
        # Multiple layers of logic masking the final computation
        health_status = evaluate_health_status(stability, peak, threshold)
        status_counter[health_status] += 1
        
        # Key transformation: only this contributes to final answer
        if health_status == 'NORMAL':
            diagnostics.append(raw_diagnostic)

    # Misleading aggregation
    if status_counter['CRITICAL'] > 0:
        fallback = sum(status_counter.values()) * -10
        return fallback

    # Actual answer path
    final_value = int(sum(diagnostics)) if diagnostics else 0
    
    # Decoy operations
    normalized = final_value / (len(diagnostics) + 1e-8)
    adjusted = math.floor(normalized * 1.05)
    
    return final_value

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    raw_data = collect_readings()
    
    # Step 2: Filter out low-amplitude noise
    cleaned = filter_noise(raw_data)
    
    # Step 3: Generate threshold configuration (contains irrelevant computation)
    threshold_map = generate_threshold_map(len(raw_data))
    
    # Step 4: Process each node's data into structured metrics
    processed_data = process_node_data(cleaned)
    
    # Step 5: Perform final diagnostic analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    print(f"Result: {final_diagnostic}")