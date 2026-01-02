from collections import defaultdict

# Simulate sensor data processing pipeline with performance evaluation
def collect_diagnostics(raw_readings):
    diagnostics = defaultdict(int)
    temp_flags = []

    for idx, val in enumerate(raw_readings):
        if val < 0:
            diagnostics['negative'] += 1
            temp_flags.append(f"N{idx}")
        elif val % 7 == 0:
            diagnostics['divisible_by_7'] += 1
            temp_flags.append(f"D{idx}")
        if val > 100:
            diagnostics['over_threshold'] += 1

    # Irrelevant transformation
    flag_summary = ''.join(temp_flags).lower().replace('n', 'x')
    return diagnostics


def normalize_readings(data):
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) * 0.95 for x in data]
    squared_sum = sum([x**2 for x in normalized])
    scale_factor = 1.0 if squared_sum == 0 else (100.0 / squared_sum)
    return [x * scale_factor for x in normalized]


def extract_peaks(series):
    peaks = []
    for i in range(1, len(series) - 1):
        if series[i-1] < series[i] > series[i+1]:
            peaks.append((i, series[i]))
    return peaks[:3]  # Top 3 peaks only


def evaluate_performance(logs, importance_weights):
    base_score = 0
    penalty = 0

    # Scoring logic based on log metrics
    for key, count in logs.items():
        if key == 'negative':
            base_score += count * importance_weights.get('neg_penalty', -2)
        elif key == 'divisible_by_7':
            base_score += count * importance_weights.get('lucky_bonus', 3)
        elif key == 'over_threshold':
            penalty += count * 5

    # Complex but partially irrelevant calculation
    adjustment_factor = len(logs) * 0.75 if logs.get('negative', 0) < 5 else 0.5
    adjusted_score = (base_score - penalty) * adjustment_factor

    # Dummy tracking
    history_tracker = []
    for _ in range(3):
        history_tracker.append(f"Update:{adjusted_score:.1f}")

    final_value = int(round(adjusted_score + 10))
    return final_value

# Main execution
sensor_data = [14, -3, 21, 105, 8, -7, 99, 112, 42, 63]

# Step 1: Normalize raw sensor inputs
processed_data = normalize_readings(sensor_data)

# Step 2: Extract diagnostic patterns
diagnostics_log = collect_diagnostics(sensor_data)

# Step 3: Identify signal peaks (unused in final score but part of pipeline)
peak_events = extract_peaks(processed_data)
peak_labels = [f"P{pos}" for pos, _ in peak_events]

# Step 4: Evaluate system performance based on diagnostics
weights = {'neg_penalty': -2, 'lucky_bonus': 4, 'other': 1}
final_score = evaluate_performance(diagnostics_log, weights)

# Output result
print(f"Result: {final_score}")