from collections import defaultdict, Counter
import math

# Simulated agricultural yield prediction with noise and red herrings
def load_sensor_metadata():
    return {
        'sensor_01': {'calibration': 1.02, 'region': 'north'},
        'sensor_02': {'calibration': 0.98, 'region': 'south'},
        'sensor_03': {'calibration': 1.05, 'region': 'east'},
        'irrelevant_04': {'calibration': 0.89, 'region': 'west'}  # decoy
    }

def generate_baseline_grid():
    # Creates a 5x5 grid of hypothetical soil quality scores (distraction)
    return [[i + j for j in range(5)] for i in range(5)]

def deprecated_normalization(data):
    # Obsolete function - never called but looks important
    return [x / max(data) for x in data]

def parse_legacy_config():
    # Unused config parser - adds distraction
    config = {}
    for i in range(3):
        config[f'mode_{i}'] = (i ** 3) % 7
    return config

def filter_outliers(readings, threshold=50):
    # Filters out values above threshold (used once, but logic masked)
    return [r for r in readings if r <= threshold]

def rolling_average(values, window=3):
    # Smoothing function that gets used only on a subset
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

def calculate_harvest(data, factor):
    # Core calculation buried among distractions
    processed = []
    for idx, val in enumerate(data):
        if idx % 2 == 0:
            processed.append(val * factor * 1.1)
        else:
            processed.append(val * factor * 0.9)
    
    # Key transformation: cumulative sum with alternating scale
    cumulative = 0
    for i, p in enumerate(processed):
        if i % 3 == 0:
            cumulative += p * 1.2
        elif i % 3 == 1:
            cumulative += p * 0.8
        else:
            cumulative += p * 1.0
    
    # Final adjustment based on index patterns
    index_weight = sum(1 for i in range(len(processed)) if i % 4 == 0)
    return int(cumulative / index_weight)

# --- Irrelevant Data Structures ---
weather_archive = [
    {'temp': 22, 'humidity': 60, 'pressure': 1013},
    {'temp': 25, 'humidity': 55, 'pressure': 1009},
    {'temp': 19, 'humidity': 65, 'pressure': 1015}
]

system_logs = []
for tick in range(7):
    entry = f"LOG{tick}: STATUS_OK"
    system_logs.append(entry)

# --- Misleading Intermediate Calculations ---
baseline_matrix = generate_baseline_grid()
flattened = [item for row in baseline_matrix for item in row]
avg_soil_quality = sum(flattened) / len(flattened)
adjusted_readings = [x * 1.3 for x in flattened if x % 2 == 1]

config_modes = parse_legacy_config()
deprecated_normalized = deprecated_normalization([10, 20, 30, 40])

# --- Sensor Data (some relevant, some not) ---
sensor_metadata = load_sensor_metadata()
raw_projections = [18, 23, 19, 24, 21, 27, 20]  # Weekly projected yields (in tons)
filtered_projections = filter_outliers(raw_projections, threshold=25)
smoothed_data = rolling_average(filtered_projections, window=2)

# --- Core Variables ---
projection_data = [18, 23, 19, 24, 21]  # First five projections (critical input)
adjustment_factor = 1.07                     # Environmental adjustment

# --- Decoy Operations ---
temp_analysis = []
for i, val in enumerate(smoothed_data):
    temp_analysis.append((i, val ** 0.5))

lookup_table = defaultdict(int)
for char in "harvest2024":
    lookup_table[char] += 1

counter_summary = Counter(str(projection_data))

# --- Actual Execution Point ---
final_yield = calculate_harvest(projection_data, adjustment_factor)

# --- Unrelated String Processing ---
patterns = ['a', 'b', 'c']
indexed = list(enumerate(patterns))
zipped = list(zip(projection_data, smoothed_data))

# --- Output ---
print(f"Result: {final_yield}")