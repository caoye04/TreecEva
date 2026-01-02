import math

def collect_metrics(data_stream):
    # Irrelevant function - dead code path
    return [x ** 0.5 for x in data_stream if x > 10]


def filter_anomalies(logs):
    # Distractor: looks important but not used in final computation
    threshold = 75
    anomalies = []
    for i, val in enumerate(logs):
        if val > threshold and i % 2 == 0:
            anomalies.append((i, val))
    return anomalies


def preprocess_signal(raw_data):
    # Real preprocessing with distractors
    normalized = []
    offset = 12
    scaling = 3
    temp_cache = {}  # Unused cache - red herring

    for idx, val in enumerate(raw_data):
        shifted = val - offset
        if shifted <= 0:
            continue
        scaled_val = shifted / scaling
        normalized.append(scaled_val)

    # Sorting irrelevant list
    dummy_list = [4, 1, 9, 2]
    dummy_list.sort()  # Misleading operation

    return normalized


def compute_entropy(values):
    # Unused advanced math - distraction
    total = sum(values)
    probs = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)


def rolling_average(series, window=3):
    averages = []
    for i in range(len(series) - window + 1):
        avg = sum(series[i:i+window]) / window
        averages.append(avg)
    return averages  # Computed but unused


def detect_peaks(signal):
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(i)
    return set(peaks)  # Another unused result


def integrate_segments(filtered_data):
    integral = 0.0
    weights = [1.1, 0.9, 1.05, 0.95, 1.0]
    for i, val in enumerate(filtered_data):
        weight = weights[i % len(weights)]
        integral += val * weight
    return integral


def aggregate_diagnostics(metrics):
    # Complex but irrelevant aggregation
    stats = {
        'max': max(metrics),
        'min': min(metrics),
        'avg': sum(metrics) / len(metrics),
        'range': max(metrics) - min(metrics)
    }
    return stats


def analyze_readings(processed_logs):
    # Core logic hidden among distractions
    base_score = 0
    for i, reading in enumerate(processed_logs):
        if i % 3 == 0:
            base_score += math.sin(reading)
        elif i % 3 == 1:
            base_score += math.cos(reading)
        else:
            base_score += math.tan(reading % (math.pi/3))

    adjustment = 0
    indices = set()
    for j in range(len(processed_logs)):
        if processed_logs[j] > 5.0:
            indices.add(j)

    if len(indices) > 2:
        adjustment = 15
    else:
        adjustment = 5

    # Critical line: this is the key statement
    final_diagnostic = int(base_score + adjustment)

    # Multiple decoy operations below
    decoy_result = []
    for a, b in zip(processed_logs, reversed(processed_logs)):
        decoy_result.append(a * b)
    temp_sum = sum(decoy_result) / len(decoy_result) if decoy_result else 0

    metadata_log = {"timestamp": 1678886400, "version": "2.1", "active": True}
    metadata_log["diagnostic"] = temp_sum

    return final_diagnostic

# Main execution flow
raw_telemetry = [15, 18, 12, 21, 9, 33, 24, 6, 30, 36]
processed_logs = preprocess_signal(raw_telemetry)

# Unused functions calls - red herrings
unused_1 = collect_metrics(raw_telemetry)
unused_2 = filter_anomalies(raw_telemetry)
unused_3 = rolling_average(processed_logs)
unused_4 = detect_peaks(processed_logs)

# Key statement
final_diagnostic = analyze_readings(processed_logs)
print(f"Target result: {final_diagnostic}")