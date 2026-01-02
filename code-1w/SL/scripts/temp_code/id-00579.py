import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [i * 0.25 for i in range(200)]
    noise_floor = [math.sin(x) * 0.3 for x in raw_samples]
    return [raw_samples[i] + noise_floor[i] for i in range(len(raw_samples))]


def filter_outliers(data, threshold=1.5):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev], mean_val, std_dev


def segment_signal(clean_data):
    n = len(clean_data)
    return [
        clean_data[:n//4],
        clean_data[n//4:2*n//4],
        clean_data[2*n//4:3*n//4],
        clean_data[3*n//4:]
    ]

# Irrelevant helper - dead path (not used in main logic)
def deprecated_normalization(vec):
    max_val, min_val = max(vec), min(vec)
    return [(v - min_val) / (max_val - min_val) for v in vec] if max_val != min_val else vec

# Unused transformation chain
def time_warp_correction(signal):
    corrected = []
    for i, s in enumerate(signal):
        if i % 3 == 0:
            corrected.append(s * 1.02)
        elif i % 5 == 0:
            corrected.append(s * 0.98)
        else:
            corrected.append(s)
    return corrected  # Never called

# Distractor function with plausible but unused logic
def calculate_entropy(data):
    from collections import Counter
    counts = Counter([round(x, 1) for x in data])
    total = len(data)
    entropy = -sum((freq/total) * math.log(freq/total) for freq in counts.values())
    return entropy

# Real processing begins here
def extract_features(segment):
    peak = max(segment)
    trough = min(segment)
    mid_point = (len(segment) // 2)
    center_avg = sum(segment[mid_point-5:mid_point+5]) / 10
    trend = segment[-1] - segment[0]
    return {
        'amplitude': peak - trough,
        'center_drift': center_avg,
        'trend_slope': trend,
        'stability': abs(trend) < 0.5
    }


def assess_coherence(features_list):
    stable_count = sum(1 for f in features_list if f['stability'])
    total = len(features_list)
    return stable_count / total if total else 0


def analyze_signal(segments):
    features = [extract_features(seg) for seg in segments]
    
    # Red herring computation: complex but unused metric
    composite_risk = 0
    for i, f in enumerate(features):
        risk_factor = (f['trend_slope'] ** 2) * (1 + i)
        adjustment = math.cos(f['center_drift']) if f['center_drift'] != 0 else 1
        composite_risk += risk_factor * adjustment
    
    # Another decoy variable - looks important but isn't final
    diagnostic_score = sum(f['amplitude'] for f in features) / len(features)
    
    coherence_ratio = assess_coherence(features)
    
    # Actual answer depends on sliced trend analysis
    trends = [f['trend_slope'] for f in features]
    recent_trends = trends[1:]  # slice excluding first segment
    avg_recent_trend = sum(recent_trends) / len(recent_trends)
    
    # Final logic buried among distractions
    baseline = features[0]['center_drift']
    deviation = abs(baseline - sum(f['center_drift'] for f in features[1:]) / 3)
    
    # Key determinant: combination of coherence and adjusted trend
    final_diagnostic = int((coherence_ratio * 100) + (avg_recent_trend * 10) - (deviation * 5))
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    all_readings = collect_readings()
    
    # Step 2: Filter statistical outliers
    filtered_data, avg, spread = filter_outliers(all_readings)
    
    # Step 3: Break into temporal segments
    segmented = segment_signal(filtered_data)
    processed_segments = []
    
    for idx, segment in enumerate(segmented):
        if idx % 2 == 0:
            # Apply light smoothing on even segments
            smoothed = [segment[0]]
            for i in range(1, len(segment)-1):
                smoothed.append((segment[i-1] + segment[i] + segment[i+1]) / 3)
            smoothed.append(segment[-1])
            processed_segments.append(smoothed)
        else:
            # Keep odd segments unchanged
            processed_segments.append(segment)
    
    # Step 4: Analyze signal characteristics
    final_diagnostic = analyze_signal(processed_segments)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")