from collections import defaultdict, Counter
import math

# Simulated sensor data processing system
def process_sensor_readings(raw_values):
    filtered = [v for v in raw_values if 10 <= v <= 100]
    adjusted = [v * 1.05 for v in filtered]
    return adjusted

# Irrelevant helper: Normalizes values (not used in final path)
def normalize(data):
    max_val = max(data) if data else 1
    return [x / max_val for x in data]

# Decoy function: Looks important but unused
def calculate_entropy(sequence):
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core logic with distractors
def analyze_metrics(values, threshold):
    stats = defaultdict(int)
    temp_results = []
    outlier_count = 0

    for val in values:
        if val > threshold * 1.3:
            stats['high'] += 1
            temp_results.append(val * 0.85)
        elif val < threshold * 0.7:
            stats['low'] += 1
            outlier_count += 1  # Red herring
        else:
            stats['normal'] += 1
            temp_results.append(val * 1.02)

    # Distractor transformation
    modified = [int(x) + 5 for x in temp_results if x > 0]
    shift_offset = len(modified) % 7

    # Bit manipulation decoy
    bitwise_mask = 0b101010
    masked_values = [v ^ bitwise_mask for v in modified[:10]]

    # Critical calculation buried in noise
    base_metric = sum(temp_results) / len(temp_results) if temp_results else 0
    adjustment_factor = 0.9 if stats['high'] > stats['low'] else 1.1
    return base_metric * adjustment_factor

# Unused complex structure
class DataPipeline:
    def __init__(self):
        self.stages = []
        self.enabled = False  # Dead code path

    def add_stage(self, func):
        if self.enabled:
            self.stages.append(func)

# Main evaluation logic
def evaluate_performance(metrics, base):
    # Multiple assignment distraction
    a, b, c = 10, 20, 30
    dummy_list = [a*b, b+c, c-a, a//2]

    # List and set operations (some irrelevant)
    unique_metrics = list(set(metrics))
    sorted_vals = sorted(unique_metrics, reverse=True)

    # Conditional branching with misleading intermediate
    if len(sorted_vals) > 5:
        sample_slice = sorted_vals[1:-1]
        mean_val = sum(sample_slice) / len(sample_slice)
        deviation = abs(mean_val - base)
        score_adjust = deviation * 0.1
    else:
        score_adjust = 0

    # Key computation chain
    primary_result = analyze_metrics(metrics, base)
    secondary_weight = len([x for x in metrics if x > base])

    # Complex but partially irrelevant dictionary ops
    weight_map = defaultdict(float)
    for i, val in enumerate(metrics):
        weight_map[f'item_{i % 5}'] += val * 0.01

    # Critical line with answer determination
    final_score = int(primary_result) + secondary_weight // 3 - int(score_adjust)

    # Dead branch with decoy output
    if False:
        debug_info = {k: v for k, v in weight_map.items() if v > 0.5}
        print(f'Debug: {debug_info}')

    return final_score

# Simulated input data
raw_sensor_data = [5, 15, 23, 45, 67, 89, 95, 105, 12, 18, 24, 50]
processed = process_sensor_readings(raw_sensor_data)
metric_data = [int(x) for x in processed]
base_threshold = 30

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)
print(f'Target result: {final_score}')