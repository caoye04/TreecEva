from collections import defaultdict

# Simulate sensor data processing pipeline
def analyze_readings(readings):
    stats = defaultdict(int)
    temp_sum = 0
    valid_count = 0

    for val in readings:
        if val < 0:
            stats['negative'] += 1
        elif val > 100:
            stats['overflow'] += 1
        else:
            temp_sum += val
            valid_count += 1
            bucket = (val // 10) * 10
            stats[f'range_{bucket}'] += 1

    average = temp_sum / valid_count if valid_count else 0
    stats['average'] = average
    return stats


def filter_anomalies(logs):
    # Irrelevant preprocessing step - distractor
    clean_logs = []
    anomaly_flags = []
    for log in logs:
        if isinstance(log, str):
            cleaned = ''.join(c for c in log if c.isdigit())
            if len(cleaned) > 0 and int(cleaned) % 7 == 0:
                anomaly_flags.append(True)
            else:
                anomaly_flags.append(False)
    return anomaly_flags  # Not used later


def compute_weighted_tally(counts_dict, base_factor=1.5):
    total = 0
    weights = {'range_0': 0.1, 'range_10': 0.2, 'range_20': 0.3,
               'range_30': 0.4, 'range_40': 0.5, 'range_50': 0.6,
               'range_60': 0.7, 'range_70': 0.8, 'range_80': 0.9, 'range_90': 1.0}
    
    for key, count in counts_dict.items():
        if key in weights:
            total += count * weights[key] * base_factor
    return int(total)


def process_segments(data_list, criteria):
    segment_scores = []
    debug_trace = []
    
    for idx, entry in enumerate(data_list):
        readings = entry['values']
        mode = entry['mode']
        
        analysis = analyze_readings(readings)
        
        # Compute auxiliary metrics (some irrelevant)
        high_freq = analysis['range_50'] + analysis['range_60'] + analysis['range_70']
        spike_ratio = analysis['overflow'] / len(readings) if readings else 0
        
        base_score = compute_weighted_tally(analysis)
        
        adjustment = 0
        if mode == 'aggressive' and analysis['average'] > criteria['threshold_A']:
            adjustment = 15
        elif mode == 'conservative' and analysis['negative'] >= criteria['threshold_B']:
            adjustment = -10
        else:
            adjustment = 5
        
        final_segment = base_score + adjustment
        
        # Dead code path - misleading
        if len(readings) > 1000:
            scaling = len(readings) / 100
            final_segment = int(final_segment * scaling)
        
        segment_scores.append(final_segment)
        debug_trace.append(f'Segment {idx}: {final_segment}')
    
    cumulative = sum(segment_scores)
    penalty = len([s for s in segment_scores if s < 20]) * 3
    final_score = cumulative - penalty
    
    # Unused transformation
    normalized = round(final_score / (len(segment_scores) or 1), 2)
    
    return final_score

# Main execution
if __name__ == '__main__':
    segment_data = [
        {
            'values': [85, 92, 78, 63, 44, 57, 90, 105, -5, 73, 88, 52],
            'mode': 'aggressive'
        },
        {
            'values': [23, 15, 67, 41, 33, 72, 60, 58, 49, 55],
            'mode': 'conservative'
        },
        {
            'values': [95, 87, 91, 89, 102, 110, 40, 76],
            'mode': 'aggressive'
        }
    ]
    
    thresholds = {
        'threshold_A': 65.0,
        'threshold_B': 1
    }
    
    # Irrelevant filtering call - distractor
    _ = filter_anomalies(['log123', 'log456', 'event777', 'entry805'])
    
    final_score = process_segments(segment_data, thresholds)
    print(f"Result: {final_score}")