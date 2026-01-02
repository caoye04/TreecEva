def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    smoothed = [(filtered[i] + filtered[i+1]) / 2 for i in range(len(filtered)-1)]
    return smoothed + [filtered[-1]]


def analyze_trend(data_slice):
    if len(data_slice) < 3:
        return 'insufficient'
    trend_vals = [data_slice[i+1] - data_slice[i] for i in range(len(data_slice)-1)]
    pos_count = sum(1 for t in trend_vals if t > 0)
    neg_count = sum(1 for t in trend_vals if t < 0)
    return 'rising' if pos_count > neg_count else 'falling' if neg_count > pos_count else 'stable'


def calculate_efficiency(dataset, limits):
    base_metric = sum(dataset) / len(dataset)
    peak = max(dataset)
    utilization = sum(1 for x in dataset if x >= limits[0]) / len(dataset)
    penalty = 0.1 * sum(1 for x in dataset if x > limits[1])
    efficiency = (base_metric * utilization) - penalty
    return round(efficiency, 4)

# Simulated sensor network data (simulated for reproducibility)
raw_sensor_data = [5, 15, 23, 45, 67, 89, 95, 102, 44, 68, 77, 110, 29]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 12.5
normalization_factor = 0.98
auxiliary_cache = {'version': '2.1', 'active': False}
dummy_matrix = [[i*j for j in range(3)] for i in range(3)]

# Preprocessing stage
processed_readings = preprocess_readings(raw_sensor_data)

# Extract time window slice (using slicing operation)
current_window = processed_readings[1:6]

# Trend analysis (not directly used in final score but part of workflow)
trend_status = analyze_trend(current_window)

# Define threshold parameters (real impact on result)
threshold_config = (60.0, 90.0)

# State tracking variables (some irrelevant)
execution_log = []
stage_counter = 0
final_output_ready = False

# Efficiency calculation – key statement
efficiency_score = calculate_efficiency(processed_readings, threshold_config)

# Dead code path (misleading control flow)
if final_output_ready and auxiliary_cache['active']:
    scaled_result = efficiency_score * normalization_factor
    execution_log.append(scaled_result)

# Output target result
print(f"Result: {efficiency_score}")