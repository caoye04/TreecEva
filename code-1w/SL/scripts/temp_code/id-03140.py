import math

def sensor_validation(readings):
    """Irrelevant validation function - distractor"""
    if not readings:
        return False
    return all(0 <= r <= 1024 for r in readings)

def normalize_vector(vec):
    """Dead utility function - never called"""
    norm = math.sqrt(sum(x ** 2 for x in vec))
    return [x / norm for x in vec] if norm else vec

def parse_sensor_string(data_str):
    # Real but indirect data processing
    raw_parts = data_str.split('|')
    id_tag = raw_parts[0].strip().lower()
    values = [float(x) for x in raw_parts[1].split(',')]
    timestamp = raw_parts[2]
    return id_tag, values, timestamp

def filter_outliers(arr, factor=1.5):
    # Heavily misleading preprocessing step
    sorted_vals = sorted(arr)
    q1 = sorted_vals[len(sorted_vals) // 4]
    q3 = sorted_vals[3 * len(sorted_vals) // 4]
    iqr = q3 - q1
    low, high = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in arr if low <= x <= high], (q1, q3, iqr)

def rolling_average(data, window=3):
    # Distractor: complex smoothing that isn't used in final path
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(data[start:i+1]) / (i - start + 1))
    return smoothed

def transform_coordinates(x, y, mode='polar'):
    # Unused transformation chain
    if mode == 'polar':
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        return r, theta
    return x, y

def compute_entropy(data):
    # Red herring: looks important, not used
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 6)

def analyze_readings(cleaned, limit):
    # Core logic buried in distractions
    magnitude = sum(x ** 2 for x in cleaned) ** 0.5
    adjusted = [x * 0.87 for x in cleaned if x > limit / 2]
    if len(adjusted) < 2:
        score = magnitude * 1.5
    else:
        peak = max(adjusted)
        avg_adj = sum(adjusted) / len(adjusted)
        score = (peak * 0.7) + (avg_adj * 0.3)
    
    # Critical misdirection: multiple paths, only one matters
    if magnitude > limit:
        flag = 'OVERLOAD'
        correction = math.log(magnitude)
        score -= correction
    elif len(cleaned) > 8:
        flag = 'STABLE_LONG'
        score += 0.5
    else:
        flag = 'BASELINE'
        decay = 0.95 ** len(cleaned)
        score *= decay
    
    # Final computation - depends only on specific branch
    diagnostic = int(score * 100) if flag != 'STABLE_LONG' else int((score + 10) * 100)
    return diagnostic

# Simulated sensor input - realistic domain context
raw_input = "sensor_7b|34.5,28.1,45.2,19.8,56.3,22.7,41.0,33.2,27.5,38.9|2023-11-05T14:22:10Z"

tag, unfiltered_data, time_stamp = parse_sensor_string(raw_input)

# Irrelevant metadata processing
node_id = tag.split('_')[1] if '_' in tag else 'unknown'
version_code = sum(ord(c) for c in node_id) % 7

# Actual relevant path begins here
filtered_data, quartiles = filter_outliers(unfiltered_data, factor=1.8)

# Decoy statistical analysis
entropy_value = compute_entropy([round(x) for x in filtered_data])
sorted_copy = sorted(filtered_data, reverse=True)
avg_filtered = sum(sorted_copy) / len(sorted_copy)
median_val = sorted_copy[len(sorted_copy)//2]

# Another red herring list transformation
shifted_data = [x - avg_filtered for x in sorted_copy]
abs_shifted = [abs(x) for x in shifted_data]
suppressed_data = [x for x in abs_shifted if x < median_val * 0.75]

# Key assignment: this is where relevant data stabilizes
processed_data = [x * 1.08 for x in filtered_data]  # Final form

# Multiple distracting thresholds
threshold = 40.0
alt_threshold = 35.0 if len(processed_data) > 7 else 45.0
effective_limit = min(threshold, alt_threshold)

# Dead control flow with misleading condition
if version_code > 5 and 'b' in node_id:
    effective_limit *= 0.9
elif entropy_value > 3.0:
    effective_limit *= 1.1  # This won't trigger
else:
    baseline_offset = 2.5  # unused

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold)

# Print required result
print(f"Result: {final_diagnostic}")