from collections import defaultdict, Counter

def analyze_pattern(sequence):
    freq = Counter(sequence)
    most_common = freq.most_common(1)[0][1]
    least_common = freq.most_common()[-1][1]
    return most_common - least_common

def adjust_weights(data, factor=1.5):
    weighted = [x * factor for x in data]
    offset = sum(weighted) / len(weighted)
    adjusted = [x + offset for x in weighted]
    return adjusted

def track_state(events):
    state_log = defaultdict(int)
    temp_buffer = []
    for e in events:
        state_log[e] += 1
        if e % 2 == 0:
            temp_buffer.append(e * 2)
    # Some irrelevant aggregation
    stats = {"total_events": sum(state_log.values()), "unique_states": len(state_log)}
    return stats["total_events"] - stats["unique_states"]
def calculate_performance(log, config):
    segment_a = log[:config['midpoint']]
    segment_b = log[config['midpoint']:]
    
    # Real computation branch
    raw_diff = sum(segment_b) - sum(segment_a)
    pattern_score = analyze_pattern(log)
    
    # Distractor: complex adjustment with no impact
    dummy_weights = adjust_weights(segment_a, factor=0.8)
    dummy_shift = [w ** 0.5 for w in dummy_weights if w > 5]
    shadow_metric = sum(dummy_shift) // len(dummy_shift) if dummy_shift else 0
    
    # Another red herring: state tracking that computes something unused
    side_effect = track_state(log[::2])
    buffer_cache = [x for x in log if x in segment_a]
    
    # Actual logic contributing to result
    base_score = raw_diff * pattern_score
    if base_score < 0:
        base_score = abs(base_score) + config['penalty_offset']
    else:
        base_score += config['bonus_threshold']
    
    # Final computation using relevant components only
    scaling_factor = config['scale'] if len(segment_b) > len(segment_a) else 1.0
    final_score = int((base_score * scaling_factor))
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == "__main__":
    event_log = [3, 7, 3, 9, 7, 3, 8, 7, 3]
    config_params = {
        'midpoint': 4,
        'scale': 2.5,
        'penalty_offset': 6,
        'bonus_threshold': 4
    }
    final_score = calculate_performance(event_log, config_params)