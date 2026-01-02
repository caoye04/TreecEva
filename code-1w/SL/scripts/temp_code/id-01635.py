def preprocess_signal(raw_data, threshold=0.5):
    filtered = [x for x in raw_data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def extract_segments(data, window_size=3):
    segments = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i+window_size]
        segments.append(segment)
    reversed_segments = segments[::-1]  # Distractor: not used later
    return segments


def is_stable(sequence):
    return all(abs(seq - sequence[0]) < 0.1 for seq in sequence)


def compute_coherence(segment):
    # Irrelevant computation
    product = 1
    for val in segment:
        product *= abs(val) + 0.1
    return round(product, 4)


def rank_segments(segments):
    rankings = {}
    for idx, seg in enumerate(segments):
        rankings[idx] = sum(seg) ** 2
    sorted_ranks = sorted(rankings.items(), key=lambda x: x[1], reverse=True)
    top_indices = [i for i, _ in sorted_ranks[:3]]
    return top_indices


def analyze_readings(segments):
    stability_flags = []
    coherence_scores = []
    
    temp_buffer = []
    for s in segments:
        temp_buffer.append(sum(s))
    
    avg_buffer = sum(temp_buffer) / len(temp_buffer)
    offset_correction = abs(avg_buffer) * 0.05
    
    for seg in segments:
        stable = is_stable(seg)
        stability_flags.append(stable)
        score = compute_coherence(seg)
        coherence_scores.append(score)
    
    true_count = stability_flags.count(True)
    false_count = stability_flags.count(False)
    balance_metric = abs(true_count - false_count) * 0.5
    
    # Key logic: counting how many segments have positive sum after index 5
    post_index_sum = 0
    for i in range(6, len(segments)):
        if sum(segments[i]) > 0:
            post_index_sum += 1
    
    # Dead code path - looks important but unused
    if balance_metric > 2:
        fallback = 999
        secondary_check = [c for c in coherence_scores if c > 0.5]
    else:
        fallback = 0
        outlier_detect = [s for s in segments if len(s) == 3 and s[0] < 0]
    
    # Core answer derivation
    diagnostic_weight = 0
    for i, seg in enumerate(segments):
        if i % 2 == 0 and is_stable(seg):
            diagnostic_weight += 1
    
    adjustment = len(coherence_scores) // 3
    final_diagnostic = diagnostic_weight * 7 - adjustment + post_index_sum
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
raw_sensor_data = [0.1, 0.7, 0.72, 0.3, 0.71, 0.69, -0.2, 0.8, 0.81, 0.79, 0.4, -0.6, 0.62]

cleaned = preprocess_signal(raw_sensor_data)
processed_segments = extract_segments(cleaned, window_size=3)

# Unused distractor functions

def legacy_analysis(arr):
    total = 0
    for x in arr:
        if isinstance(x, list):
            total += len(x) * 0.5
    return total

def calculate_baseline(data):
    base = 0
    for i, x in enumerate(data):
        base += x * (i % 4)
    return base * 0.1

interim_test = legacy_analysis(processed_segments)
baseline_ref = calculate_baseline(cleaned)

# Critical statement
final_diagnostic = analyze_readings(processed_segments)