from collections import defaultdict, Counter
import math

# Simulated sensor array data (temperature readings in millidegrees)
sensor_logs = [
    '723,689,701,715,invalid,730',
    '695,687,703,710,720,690',
    '705,712,709,invalid,714,708',
    '698,700,702,711,706,704',
    '713,707,716,719,701,invalid'
]

# Irrelevant mapping - red herring for device types
device_categories = {
    'A': 'thermocouple', 'B': 'RTD', 'C': 'semiconductor',
    'D': 'thermistor', 'E': 'infrared'
}

def parse_entry(entry):
    """Parse a single log entry, ignoring invalid values."""
    values = []
    for item in entry.split(','):
        if item.isdigit():
            values.append(int(item))
    return values

# Misleading pre-processing: counting invalid entries (not used later)
invalid_count = 0
def count_invalids(logs):
    global invalid_count
    for entry in logs:
        invalid_count += entry.count('invalid')
    return invalid_count

# Dead function - looks useful but unused
def analyze_trend(data_seq):
    trend_score = 0
    for i in range(1, len(data_seq)):
        if data_seq[i] > data_seq[i-1]:
            trend_score += 1
        elif data_seq[i] < data_seq[i-1]:
            trend_score -= 1
    return abs(trend_score)

# Another decoy: computes average deviation but not used
def compute_deviation_stats(values):
    mean_val = sum(values) / len(values)
    dev_sum = sum(abs(v - mean_val) for v in values)
    return dev_sum / len(values) if values else 0

# Real processing begins here
all_readings = []
for log in sensor_logs:
    parsed = parse_entry(log)
    all_readings.extend(parsed)

# Filter out any below 700 (arbitrary calibration threshold)
filtered_data = [x for x in all_readings if x >= 700]

# Decoy dictionary accumulation (never used)
reading_frequency = defaultdict(int)
for val in all_readings:
    reading_frequency[val] += 1

# Another distraction: character analysis of original strings
char_counter = Counter()
for log in sensor_logs:
    for char in log:
        if char.isdigit() or char == 'i':
            char_counter[char] += 1

# Threshold based on length of filtered data (key dependency)
thresh_base = len([r for r in all_readings if r < 700])
threshold = max(3, int(math.sqrt(thresh_base)) + 1) if thresh_base > 0 else 3

# Core logic hidden among noise
principal_sum = sum(filtered_data)
adjustment_factor = len(filtered_data) // threshold if threshold > 0 else 0

# Critical recursive transformation
def transform_magnitude(value, depth):
    if depth <= 0 or value < 500:
        return value
    return transform_magnitude((value // 2) + 100, depth - 1)

adjusted_sum = transform_magnitude(principal_sum, adjustment_factor)

# Secondary processing chain
def process_readings(data, limit):
    if not data:
        return 0
    
    # More distractions inside critical function
    temp_meta = {}
    temp_meta['size'] = len(data)
    temp_meta['max'] = max(data)
    temp_meta['min'] = min(data)
    temp_meta['range'] = temp_meta['max'] - temp_meta['min']
    temp_meta['midpoint'] = (temp_meta['max'] + temp_meta['min']) // 2
    
    # This part is actually used
    clipped = [x for x in data if x <= temp_meta['midpoint'] + 50]
    
    # Use Counter for frequency filtering (required feature)
    freqs = Counter(clipped)
    common_values = [k for k, v in freqs.items() if v >= 2]
    
    # Final computation
    if common_values:
        base = sum(common_values) // len(common_values)
        modifier = len(clipped) - len(common_values)
        return (base * 7) + (modifier * 3)
    else:
        return temp_meta['midpoint']

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold)

# Red herring print statements (commented out)
# print(f'Device categories analyzed: {len(device_categories)}')
# print(f'Invalid fields detected: {count_invalids(sensor_logs)}')
# print(f'Average deviation: {compute_deviation_stats(all_readings):.2f}')

print(f'Target result: {final_diagnostic}')