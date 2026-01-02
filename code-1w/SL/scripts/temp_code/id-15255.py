import math

# Simulated sensor data (temperature, pressure, humidity)
sensor_readings = [
    {'temp': 23.5, 'pressure': 101.3, 'humidity': 45.2},
    {'temp': 25.1, 'pressure': 102.0, 'humidity': 47.8},
    {'temp': 22.0, 'pressure': 99.7, 'humidity': 50.1},
    {'temp': 26.3, 'pressure': 103.4, 'humidity': 44.6},
    {'temp': 24.8, 'pressure': 101.8, 'humidity': 46.3}
]

# System configuration with red herrings
default_thresholds = {'temp': 30.0, 'pressure': 110.0, 'humidity': 60.0}
active_filters = ['temp', 'pressure']
filter_enabled = True
log_level = 'DEBUG'
debug_mode = False
max_history_size = 100

# Irrelevant statistical cache
cached_stats = {
    'mean_temp': None,
    'std_dev_pressure': None,
    'correlation_tph': None
}

# Decoy transformation functions
def smooth_data(data_list):
    # Unused smoothing function (dead code path)
    return [round(x * 0.9 + 2.0, 2) for x in data_list]

def normalize_range(value, old_min, old_max, new_min, new_max):
    # Not actually used in main logic
    return ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min

# Signal processing core
valid_types = ['temp', 'pressure', 'humidity']
scaling_factor = 1.85
offset_correction = 0.15

# Misleading intermediate aggregates
total_weighted_sum = 0.0
aggregation_counter = 0

# Hidden reference thresholds (used later)
reference_baseline = {
    'temp_ref': 20.0,
    'pressure_ref': 100.0,
    'humidity_ref': 40.0
}

# Precompute unused correlation matrix (distractor)
correlation_matrix = {}
for t in valid_types:
    for s in valid_types:
        key = f'{t}_vs_{s}'
        correlation_matrix[key] = round(math.sin(hash(t+s)) % 1, 3)

# Filter criteria (some are misleading)
min_acceptable = 18.0
stability_window = 3
required_fields = ['temp', 'pressure']

# Actual filtering logic
filtered_data = []
for reading in sensor_readings:
    if all(key in reading for key in required_fields):
        if reading['temp'] >= min_acceptable:
            filtered_data.append(reading)

# Unused history buffer (red herring)
history_buffer = []
for _ in range(5):
    history_buffer.append({'timestamp': 0, 'data': {}})

# Configuration dictionary with multiple decoy keys
class Config:
    def __init__(self):
        self.scaling = scaling_factor
        self.offset = offset_correction
        self.mode = 'AGGRESSIVE'
        self.dry_run = False
        self.timeout = 30
        self.buffer_size = 2048
        self.retries = 3
        self.verbose = False
        self.algorithm = 'WEIGHTED_DIFF'

config = Config()

# Auxiliary function: computes deviation but only uses temp and pressure
def calculate_deviation(reading, baseline):
    dev_temp = abs(reading['temp'] - baseline['temp_ref'])
    dev_pressure = abs(reading['pressure'] - baseline['pressure_ref'])
    return (dev_temp * 0.7) + (dev_pressure * 0.3)

# Another decoy utility
def predict_next_value(sequence):
    if len(sequence) < 2:
        return 0
    avg_diff = (sequence[-1] - sequence[0]) / len(sequence)
    return sequence[-1] + avg_diff

# Main processing function
processed_values = []

for item in filtered_data:
    # Compute composite score
    raw_score = 0.0
    if item['temp'] > reference_baseline['temp_ref']:
        raw_score += (item['temp'] - reference_baseline['temp_ref']) * config.scaling
    if item['pressure'] > reference_baseline['pressure_ref']:
        raw_score += (item['pressure'] - reference_baseline['pressure_ref']) * 0.5
    
    # Apply artificial penalty for high humidity (not obvious)
    if item['humidity'] > reference_baseline['humidity_ref']:
        raw_score -= (item['humidity'] - reference_baseline['humidity_ref']) * 0.2
    
    processed_values.append(raw_score)

# Secondary transformation via list comprehension (relevant)
normalized_scores = [
    round(score + config.offset, 3) 
    for score in processed_values 
    if score > -5.0  # filter negligible values
]

# Destructuring assignment (tuple unpacking) - partially irrelevant
first_score, *remaining_scores = normalized_scores + [0.0] * (4 - len(normalized_scores))

# Complex conditional aggregation
if len(normalized_scores) >= 3:
    top_three_avg = sum(sorted(normalized_scores, reverse=True)[:3]) / 3
else:
    top_three_avg = sum(normalized_scores) / len(normalized_scores) if normalized_scores else 0

# Final signal processor
def process_signals(data_list, cfg):
    if not data_list:
        return 0
    
    # Bit manipulation red herring
    magic_seed = 0b101010
    mask = (magic_seed << 2) ^ 0xFF
    masked_value = len(data_list) & mask
    
    # Real logic: weighted sum using config
    total = 0.0
    for i, val in enumerate(normalized_scores):
        weight = 1.0 + (i * 0.1)
        total += val * weight
    
    # Final adjustment
    result = total * cfg.scaling - 10.5
    return int(round(result))

# Execute main logic
final_output = process_signals(filtered_data, config)

# Print result as required
print(f"Target result: {final_output}")