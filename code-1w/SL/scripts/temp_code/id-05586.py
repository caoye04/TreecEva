import math

# System health monitoring simulation with diagnostic analysis

def collect_sensor_data():
    raw_readings = [
        (1, 23.5, 880, True), (2, 24.1, 875, False), (3, 25.3, 892, True),
        (4, 26.0, 888, True), (5, 27.8, 901, True), (6, 28.1, 899, False),
        (7, 29.5, 910, True), (8, 30.2, 915, True), (9, 31.0, 920, True)
    ]
    return raw_readings


def filter_anomalies(data):
    normal_range = set(range(1, 10))
    anomaly_flags = [not entry[3] for entry in data]
    filtered = [e for e in data if e[3]]
    ids = {e[0] for e in filtered}
    missing_ids = normal_range - ids
    # Irrelevant transformation
    squared_map = {i: i**2 for i in missing_ids}
    return filtered


def compute_trend(readings):
    temps = [r[1] for r in readings]
    diffs = [temps[i+1] - temps[i] for i in range(len(temps)-1)]
    avg_slope = sum(diffs) / len(diffs) if diffs else 0
    # Distractor calculation
    volatility = sum(abs(d) for d in diffs) / len(diffs) if diffs else 0
    return avg_slope


def extract_metrics(readings):
    metrics = []
    for r in readings:
        idx, temp, pressure, status = r
        normalized_p = pressure / 1000.0
        adjusted_t = temp + 273.15
        # Decoy computation
        entropy = math.log(temp) if temp > 0 else 0
        score = (normalized_p * 100) + (adjusted_t / 10)
        metrics.append({'id': idx, 'score': score, 'temp_k': adjusted_t})
    return metrics


def build_baseline(metrics):
    scores = [m['score'] for m in metrics]
    mean_score = sum(scores) / len(scores)
    variance = sum((s - mean_score) ** 2 for s in scores) / len(scores)
    threshold = mean_score - math.sqrt(variance)
    # Unused but misleading structure
    profile_map = {i+1: s for i, s in enumerate(scores)}
    return {'mean': mean_score, 'threshold': threshold}


def detect_outliers(metrics, threshold):
    # This function is defined but not used — dead code path
    outliers = [m for m in metrics if m['score'] < threshold]
    return outliers


def aggregate_diagnostics(metrics):
    total = 0
    for m in metrics:
        if m['id'] % 2 == 1:
            total += int(m['score'])
        else:
            total -= int(m['score'] * 0.1)
    checksum = total ^ 0xABC  # Bitwise red herring
    verification = (checksum & 0xFF) + (checksum >> 8)
    return total  # Actual relevant result


def analyze_readings(metrics, baseline):
    base_val = baseline['mean']
    aggregate = aggregate_diagnostics(metrics)
    trend_factor = compute_trend(collect_sensor_data())
    # Complex but irrelevant set operation
    id_set = {m['id'] for m in metrics}
    complement = {i for i in range(1, 20) if i not in id_set}
    decoy_result = sum(complement) % 1000
    # Another misleading intermediate
    adjustment = math.sin(math.radians(decoy_result))
    final_diagnostic = aggregate + int(base_val) - int(trend_factor * 100)
    return final_diagnostic

# Main execution flow
raw_data = collect_sensor_data()
filtered_data = filter_anomalies(raw_data)
processed_metrics = extract_metrics(filtered_data)
baseline_profile = build_baseline(processed_metrics)
# Dead function call placeholder (never invoked)
# detect_outliers(processed_metrics, baseline_profile['threshold'])
final_diagnostic = analyze_readings(processed_metrics, baseline_profile)
print(f"Result: {final_diagnostic}")