from collections import defaultdict
import math

# Simulate sensor data aggregation and performance scoring with distractions
def collect_diagnostics():
    readings = [18, 22, 19, 25, 21]
    stats = defaultdict(int)
    temp_sum = 0
    for val in readings:
        stats['count'] += 1
        temp_sum += val
        if val > 20:
            stats['high_count'] += 1
    avg = temp_sum / len(readings)
    stats['average'] = avg
    return stats

# Irrelevant helper: processes unused network latency data
def analyze_latency(packets):
    jitter = 0.0
    for p in packets:
        jitter += abs(p - 50)  # Assume base 50ms
    jitter /= len(packets)
    correction_factor = math.sin(jitter / 10)  # Unused distraction
    normalized = [p * 0.9 for p in packets if p > 10]  # Dead logic path
    return sum(normalized) if normalized else 0

# Core logic obscured by side computations
def preprocess_metrics(raw):
    processed = {}
    shift_key = 3  # For bit manipulation red herring
    for k, v in raw.items():
        shifted = v << 1  # Double value via bit op – misleading
        adjusted = shifted * 0.75  # Arbitrary scale
        processed[k] = max(adjusted, 10)  # Floor at 10
    
    # Distractor block: tuple unpacking with irrelevant transformation
    meta_tags = ('type_a', 'flag_x')
    tag_type, flag_status = meta_tags
    if tag_type == 'type_a':
        processed['bonus'] = 15  # Unused bonus field
    
    return processed

# Scoring logic interwoven with noise
def evaluate_performance(metrics, weights):
    base = 0
    weight_sum = 0
    
    # Real contribution
    for key, value in metrics.items():
        if key in weights:
            base += value * weights[key]
            weight_sum += weights[key]
    
    # Dead code branch – never executed due to prior filtering
    if 'invalid_flag' in metrics:
        base -= 100  # Red herring deduction
    
    # Normalization using actual logic
    score = base / weight_sum if weight_sum else 0
    
    # Extra noise: slicing a generated list that's not needed
    history = list(range(1, 100))
    recent_history = history[-10:]  # Distraction
    decay_factor = sum(recent_history) / 10  # Irrelevant average
    
    # Lambda used as obfuscation
    apply_decay = lambda x, d: x * (0.95 if d > 50 else 1.0)
    final_score = apply_decay(score, decay_factor)  # Actually applied but minor effect
    
    # Critical answer stored here
    return int(round(final_score))

# Main execution flow
if __name__ == "__main__":
    # Initialize real input data
    raw_metrics = {
        'response_time': 24,
        'throughput': 18,
        'stability': 28
    }
    weights = {
        'response_time': 0.4,
        'throughput': 0.3,
        'stability': 0.3
    }
    
    # Call diagnostic function (result used only partially)
    system_stats = collect_diagnostics()
    temperature_baseline = system_stats['average']  # Used in distraction only
    
    # Irrelevant latency analysis
    network_data = [45, 55, 50, 60, 40]
    _ = analyze_latency(network_data)  # Return value ignored
    
    # Preprocess metrics (core step)
    processed_metrics = preprocess_metrics(raw_metrics)
    
    # Remove bonus to prevent influence (demonstrates dead assignment earlier)
    if 'bonus' in processed_metrics:
        del processed_metrics['bonus']
    
    # Key computation: produces the target answer
    final_score = evaluate_performance(processed_metrics, weights)
    
    # Output required for traceability
    print(f"Result: {final_score}")