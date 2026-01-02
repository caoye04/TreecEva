from collections import defaultdict, Counter
import math

# Simulated sensor feedback stream with diagnostic tags
def generate_feedback_stream():
    raw_data = [
        'metric:latency|value:120|status:ok',
        'metric:cpu|value:75|status:warning',
        'metric:memory|value:88|status:critical',
        'metric:latency|value:95|status:ok',
        'metric:cpu|value:60|status:ok',
        'metric:latency|value:130|status:warning',
        'metric:network|value:45|status:ok'
    ]
    return [dict(pair.split(':') for pair in entry.split('|')) for entry in raw_data]

# Irrelevant helper - analyzes nonexistent 'bandwidth' metric
def analyze_bandwidth_trend(data):
    trends = []
    for entry in data:
        if entry.get('metric') == 'bandwidth':
            trends.append(float(entry['value']))
    return sum(trends) / len(trends) if trends else 0.0

# Misleading preprocessing - normalizes values but never used
def normalize_metrics(data):
    normalized = defaultdict(list)
    for entry in data:
        metric = entry['metric']
        value = float(entry['value'])
        normalized[metric].append(value / 100.0)
    return {k: sum(v)/len(v) for k, v in normalized.items()}

# Decoy function that calculates entropy of status distribution but unused
def calculate_status_entropy(data):
    counts = Counter(entry['status'] for entry in data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Real processing path: extract latency values above threshold
def filter_critical_latencies(data):
    latencies = []
    for entry in data:
        if entry['metric'] == 'latency':
            val = int(entry['value'])
            if val > 100:
                latencies.append(val)
    return latencies

# Secondary valid path: count critical severity incidents
def count_critical_incidents(data):
    return sum(1 for entry in data if entry['status'] == 'critical')

# Unused sorting heuristic based on ASCII sum of status field
def sort_by_status_weight(data):
    return sorted(data, key=lambda x: sum(ord(c) for c in x['status']))

# Core aggregation logic - combines filtered latencies and incident count
def aggregate_performance(stream):
    # Step 1: Extract high-latency events
    bad_latencies = filter_critical_latencies(stream)
    
    # Step 2: Base penalty from average excessive latency
    base_penalty = sum(bad_latencies) / len(bad_latencies) if bad_latencies else 0
    
    # Step 3: Augment by number of critical system incidents
    incident_multiplier = count_critical_incidents(stream) + 1  # avoid zero
    
    # Step 4: Apply diminishing returns via logarithmic scaling
    adjusted_score = base_penalty * incident_multiplier * math.log(incident_multiplier)
    
    # Step 5: Round to nearest integer as final score
    final_score = round(adjusted_score)
    
    # Dead code branch - never reached due to prior assignment
    if False:
        fallback = analyze_bandwidth_trend(stream)
        final_score = int(fallback * 100)
    
    return final_score

# --- Execution Block ---
feedback_stream = generate_feedback_stream()

# Distractor variables - computed but irrelevant to final result
normalization_map = normalize_metrics(feedback_stream)
sorted_stream = sort_by_status_weight(feedback_stream)
entropy_value = calculate_status_entropy(feedback_stream)
unused_trend = analyze_bandwidth_trend(feedback_stream)

# Key statement
final_score = aggregate_performance(feedback_stream)

print(f"Result: {final_score}")