from collections import defaultdict, Counter
import itertools

# Simulate sensor data aggregation and performance scoring with distractions
def collect_telemetry_data():
    raw_signals = [1.2, 0.8, 1.5, 0.4, 1.1]
    filtered = [x for x in raw_signals if x > 0.5]
    padding = [0] * (10 - len(filtered))
    extended = filtered + padding  # padded with zeros (irrelevant)
    return extended

def compute_checksum(data):
    # Irrelevant cryptographic distraction
    chk = 0
    for d in data[:5]:
        chk ^= int(d * 10) & 0xFF
    return chk + 1000  # decoy number

def analyze_peaks(signal):
    # Real but overcomplicated peak detection
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return len(peaks) if len(peaks) > 0 else -1

def rolling_average(data, window=3):
    avgs = []
    for i in range(len(data) - window + 1):
        avgs.append(sum(data[i:i+window]) / window)
    return avgs + [0]*(len(data) - len(avgs))  # misaligned padding

def accumulate_deltas(values):
    deltas = []
    for i in range(1, len(values)):
        deltas.append(abs(values[i] - values[i-1]))
    total_change = sum(deltas)
    avg_change = total_change / len(deltas) if deltas else 0
    return total_change, avg_change

def calculate_entropy(arr):
    # Distractor: information theory concept not used in final score
    count = Counter(arr)
    probs = [count[c] / len(arr) for c in count]
    from math import log2
    return -sum(p * log2(p) for p in probs)

def extract_features(data_stream):
    features = defaultdict(float)
    
    # Real feature: base average
    features['base_avg'] = sum(data_stream) / len(data_stream)
    
    # Real feature: trend stability
    _, avg_delta = accumulate_deltas(data_stream)
    features['stability'] = 1 / (avg_delta + 1)
    
    # Real feature: peak count
    features['peaks'] = analyze_peaks(data_stream)
    
    # Irrelevant derived stats
    roll_avgs = rolling_average(data_stream)
    features['smoothed_max'] = max(roll_avgs) * 0.95
    
    # Fake complexity
    pairs = list(itertools.combinations_with_replacement(data_stream[:4], 2))
    features['pair_count'] = len(pairs)
    
    # Red herring entropy
    quantized = [int(x * 10) % 7 for x in data_stream]
    features['entropy'] = calculate_entropy(quantized)
    
    # Dummy checksum (never used)
    features['checksum'] = compute_checksum(data_stream)
    
    return dict(features)

def normalize_metric(value, ideal, worst):
    # Normalize toward ideal (higher = better)
    return max(0, min(1, (value - worst) / (ideal - worst)))

def evaluate_performance(metrics, weights):
    # Actual scoring logic buried in noise
    base_norm = normalize_metric(metrics['base_avg'], 1.0, 0.2)
    stability_norm = normalize_metric(metrics['stability'], 1.0, 0.1)
    peak_norm = normalize_metric(metrics['peaks'] + 1, 3.0, 0.0)  # shift to avoid negative
    
    # These are calculated but not used (distraction)
    smooth_norm = normalize_metric(metrics['smoothed_max'], 1.5, 0.5)
    entropy_norm = normalize_metric(metrics['entropy'], 2.0, 0.5)
    
    # Final score uses only first three
    score = (
        weights[0] * base_norm +
        weights[1] * stability_norm +
        weights[2] * peak_norm
    )
    
    # Decoy transformations
    candidate_a = score * metrics['checksum'] / 10000
    candidate_b = score + (metrics['pair_count'] / 100)
    
    # Only score matters
    return int(score * 1000)  # integer scale

# Main execution
if __name__ == "__main__":
    # Initial data collection
    telemetry = collect_telemetry_data()
    
    # Add irrelevant transformation
    shifted = [x + 0.05 for x in telemetry]
    transposed = list(itertools.permutations(shifted[:3]))  # unused
    
    # Feature extraction
    extracted_metrics = extract_features(telemetry)
    
    # Weight vector: only first three used
    importance_weights = [0.4, 0.35, 0.25, 0.1, 0.05]  # last two unused
    
    # Core evaluation
    final_score = evaluate_performance(extracted_metrics, importance_weights)
    
    # Output target result
    print(f"Result: {final_score}")