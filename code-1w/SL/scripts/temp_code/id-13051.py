from collections import defaultdict, Counter
import math

def analyze_timing_sequence(events):
    timing_log = []
    accumulator = 0
    temp_cache = {}
    
    for e in events:
        if e % 7 == 0:
            accumulator += e ** 0.5
        elif e % 3 == 0 and e % 9 != 0:
            accumulator -= e // 4
        else:
            accumulator += (e % 5) * 2
        
        if e > 50:
            temp_cache[e] = accumulator % 11
    
    timing_log.append(accumulator)
    timing_log.append(len(temp_cache))
    
    # Irrelevant transformation
    reversed_events = [x for x in reversed(events) if x % 2 == 0]
    sum_of_squares = sum(x**2 for x in reversed_events[:5]) if len(reversed_events) > 0 else 0
    
    # Dead code path (never accessed in control flow)
    if False:
        fallback_data = {i: i*3 for i in range(10)}
        return sum(fallback_data.values())
    
    return timing_log

def evaluate_system_health(sensor_readings):
    stats_summary = defaultdict(int)
    readings_set = set(sensor_readings)
    
    for val in sensor_readings:
        if val < 0:
            stats_summary['negative'] += 1
        if val > 100:
            stats_summary['overload'] += 1
        stats_summary['total'] += 1
    
    # Distractor computation
    outlier_count = 0
    sorted_vals = sorted(readings_set)
    if len(sorted_vals) > 2:
        mid = len(sorted_vals) // 2
        median_val = sorted_vals[mid]
        outlier_threshold = median_val * 1.5
        for v in sensor_readings:
            if v > outlier_threshold:
                outlier_count += 1
    
    # Unused variable
    derived_entropy = math.log(len(readings_set) + 1) if readings_set else 0
    
    return dict(stats_summary)

def extract_signal_pattern(raw_data):
    pattern_trace = []
    bit_state = 0
    
    for d in raw_data:
        shifted = (d << 2) & 0xFF
        xor_key = shifted ^ 0b10101010
        bit_state += bin(xor_key).count('1')
    
    pattern_trace.append(bit_state)
    
    # Decoy string processing
    data_string = ''.join([chr(d % 95 + 32) for d in raw_data[:8]])
    vowel_count = sum(1 for c in data_string if c.lower() in 'aeiou')
    
    # Never used
    if 'x' in data_string:
        bit_state *= 2
    
    return pattern_trace

def combine_diagnostics(logs, flags):
    base_score = logs[0] * 0.8
    penalty = 0
    
    if flags.get('overload', 0) > 5:
        penalty += 15
    if flags.get('negative', 0) > 2:
        penalty += 10
    
    # Complex but irrelevant branching
    if logs[1] > 10:
        intermediate = (base_score / (logs[1] - 9)) * 2.5
    elif logs[1] == 0:
        intermediate = base_score
    else:
        intermediate = base_score - (10 - logs[1])
    
    # Multiple layers of distraction
    dummy_list = [i * i for i in range(12) if i % 3 != 0]
    dummy_sum = sum(dummy_list)
    adjustment_factor = math.sin(math.pi / 6)  # Constant 0.5
    
    final_value = intermediate - penalty + adjustment_factor
    return int(round(final_value))

def aggregate_metrics(logs, flags):
    signal_strength = logs[0]
    cache_size = logs[1]
    adjusted_metric = (signal_strength + cache_size) * 1.1
    
    # Real logic embedded among noise
    flag_penalty = 0
    if 'overload' in flags:
        flag_penalty += flags['overload'] * 3
    if 'negative' in flags:
        flag_penalty += flags['negative'] * 2
    
    # Critical distractor: similar name, unused
    temp_diagnostic = (adjusted_metric - flag_penalty) * 0.9
    
    # Actual answer computation
    final_diagnostic = int(adjusted_metric) - flag_penalty
    
    # Red herring: string-based hash that looks important
    metadata_tag = f"DIAG_{int(adjusted_metric)}_FLAGS{sum(flags.values())}"
    tag_hash = sum(ord(c) for c in metadata_tag) % 1000
    
    # This print is required per format rules
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution sequence
if __name__ == "__main__":
    event_stream = [12, 7, 45, 56, 81, 23, 64, 99, 103, 77]
    sensor_data = [88, -5, 102, 45, 110, 67, -8, 95, 134, 41]
    raw_signal = [65, 72, 68, 70, 89, 90, 71, 66]
    
    # Collect partial results
    timing_log = analyze_timing_sequence(event_stream)
    system_flags = evaluate_system_health(sensor_data)
    signal_pattern = extract_signal_pattern(raw_signal)
    
    # Combine with decoy operations
    auxiliary_data = [x * 1.5 for x in event_stream if x < 50]
    capped_values = list(map(lambda x: min(x, 100), auxiliary_data))
    
    # Key statement
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
