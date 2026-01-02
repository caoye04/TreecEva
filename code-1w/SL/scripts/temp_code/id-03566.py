from collections import defaultdict, Counter
from itertools import zip_longest, cycle

def analyze_segments(data_stream):
    segment_stats = defaultdict(lambda: {"count": 0, "sum": 0, "flags": []})
    temporal_marks = [0] * len(data_stream)
    decoy_accumulator = 0

    for idx, (val, meta) in enumerate(data_stream):
        bucket = meta['type'] % 4
        segment_stats[bucket]['count'] += 1
        segment_stats[bucket]['sum'] += val ** 0.5
        segment_stats[bucket]['flags'].append(meta['flag'])

        # Irrelevant time-weighting (dead logic path)
        if idx % 7 == 0:
            temporal_marks[idx] = sum(segment_stats[b]['sum'] for b in segment_stats) / (idx + 1)

        # Distractor computation with no downstream use
        decoy_accumulator += val * (idx % 3)

    return segment_stats

def filter_anomalies(records):
    anomalies = []
    baseline = sum(r[0] for r in records) / len(records)
    variance_pool = []

    for val, meta in records:
        deviation = abs(val - baseline)
        if deviation > baseline * 0.6 and meta['flag'] & 2:
            anomalies.append(deviation)
        variance_pool.append(deviation * 0.9)  # Unused pool

    # Dead branch due to constant condition
    if False:
        return sorted(variance_pool, reverse=True)[:5]

    return anomalies

def compute_aggregate(stream):
    cleaned_data = [(v, m) for v, m in stream if m['valid']]
    stats = analyze_segments(cleaned_data)
    
    # Real computation path begins here
    magnitude_key = None
    for k in [3, 1, 0, 2]:
        if stats[k]['count'] > 0:
            magnitude_key = k
            break
    
    primary_component = stats[magnitude_key]['sum']
    
    # Secondary signal from filtered anomalies
    raw_anomalies = filter_anomalies(stream)
    anomaly_signal = sum(raw_anomalies) * 0.3 if raw_anomalies else 12.5
    
    # Tertiary distraction: character frequency analysis (completely irrelevant)
    decoy_text = "".join([f"{m['label']}" for _, m in stream])
    freq_map = Counter(decoy_text)
    rare_chars = [c for c, cnt in freq_map.items() if cnt < 2]
    phantom_score = len(rare_chars) * 3.7  # Never used
    
    # Fourth layer: cyclic padding simulation (distractor)
    padded_values = []
    for a, b in zip_longest([1, 2], cycle([0]), fillvalue=0):
        padded_values.append(a + b)
    padding_sum = sum(padded_values)  # Unused
    
    # Final calculation – only primary_component and anomaly_signal matter
    scaling_factor = len(stats[magnitude_key]['flags']) or 1
    intermediate = primary_component * scaling_factor
    final_score = intermediate - (anomaly_signal * 2)
    
    # Critical execution point
    print(f"Result: {final_score}")
    return final_score

# Input construction
import math
base_sequence = [
    (144, {'type': 5, 'flag': 3, 'valid': True, 'label': 'X'}),
    (81,  {'type': 1, 'flag': 2, 'valid': True, 'label': 'Y'}),
    (64,  {'type': 1, 'flag': 0, 'valid': True, 'label': 'Z'}),
    (25,  {'type': 4, 'flag': 3, 'valid': False, 'label': 'W'}),  # invalid
    (16,  {'type': 1, 'flag': 2, 'valid': True, 'label': 'X'}),
    (9,   {'type': 4, 'flag': 1, 'valid': True, 'label': 'Y'}),
    (4,   {'type': 0, 'flag': 3, 'valid': True, 'label': 'Z'})
]

result = compute_aggregate(base_sequence)