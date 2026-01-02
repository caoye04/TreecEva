import itertools

# Simulated sensor data processing with decoy analytics
def analyze_readings(data):
    filtered = [x for x in data if x > 0]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    return smoothed if smoothed else [0]

# Irrelevant audio processing stub (dead path)
def process_audio_stream(stream):
    magnitude = sum(abs(s) for s in stream)
    spectrum = [magnitude * 0.1] * 5
    return spectrum  # Never used

# Core logic: performance metric computation
def transform_metrics(raw):
    adjusted = []
    for val in raw:
        if val < 10:
            adjusted.append(val ** 2)
        elif val < 25:
            adjusted.append(val * 1.5)
        else:
            adjusted.append(val - 10)
    return adjusted

# Recursive threshold counter (misleading intermediate)
def count_peaks(values, threshold=15, idx=0):
    if idx >= len(values):
        return 0
    current = 1 if values[idx] > threshold else 0
    return current + count_peaks(values, threshold, idx + 1)

# Main evaluation engine
def evaluate_performance(logs):
    stage_one = transform_metrics(logs)
    
    # Distractor: unused branch analysis
    branches = ['A', 'B', 'C']
    combos = list(itertools.permutations(branches))
    branch_map = {combo: idx for idx, combo in enumerate(combos)}  # Unused
    
    # Critical path begins
    valid_entries = [v for v in stage_one if isinstance(v, (int, float)) and v > 0]
    capped = [min(v, 100) for v in valid_entries]
    
    # Apply decay factor on high values
    decayed = []
    for x in capped:
        if x > 50:
            decayed.append(x * 0.9)
        else:
            decayed.append(x)
    
    # Aggregation through weighted segments
    total_weight = 0
    aggregate = 0
    for i, val in enumerate(decayed):
        weight = 1 + (i * 0.1)  # Increasing importance over time
        aggregate += val * weight
        total_weight += weight
    
    average_score = aggregate / total_weight if total_weight else 0
    
    # Secondary adjustment using bit manipulation (red herring section)
    bit_flag = 0b101010
    masked = int(average_score) & bit_flag  # Computed but not used
    inverted = ~masked & 0b111111  # Dead calculation
    
    # Final nonlinear transformation
    if average_score < 40:
        final_score = average_score * 1.2
    elif average_score < 70:
        final_score = average_score * 1.1
    else:
        final_score = average_score * 0.95
    
    return final_score

# Simulated input data (sensor-derived metric log)
raw_input = [5, 12, 8, 30, 45, 60, 20, 10, 55]

# Phantom audio buffer (irrelevant)
audio_buffer = [-0.5, 0.3, 0.7, -0.2, 0.1]
processed_sound = process_audio_stream(audio_buffer)

# Real data flow
metric_data = raw_input
interim_results = analyze_readings(metric_data)
peak_count = count_peaks(metric_data, threshold=20)

# Key execution point
final_score = evaluate_performance(metric_data)

# Output result
print(f"Result: {final_score}")