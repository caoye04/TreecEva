def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append(1)
        elif data[i] < data[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return sum(t for t in trend if abs(t) >= threshold)


def normalize_values(entries):
    total = sum(abs(x) for x in entries)
    return [x / total for x in entries] if total != 0 else entries

# Irrelevant helper function (dead code path)
def unused_compatibility_check(config):
    return all(isinstance(c, str) and c.isalpha() for c in config)

# Misleading metric calculation with side effects
def update_cache(record, cache={}):
    key = ''.join(str(int(r)) for r in record if isinstance(r, float))
    cache[key] = len(cache) + 1
    return cache.get('999', 0)

# Distractor: complex string-based checksum
def compute_string_hash(obj):
    if isinstance(obj, (list, tuple)):
        obj = ''.join(str(round(float(item), 1)) if isinstance(item, (int, float)) else str(item) for item in obj)
    return sum(ord(c) * (i + 1) for i, c in enumerate(obj)) % 1000

# Core logic buried among distractions
def evaluate_performance(metrics, base):
    adjusted = [m * (1.5 if m > base else 0.7) for m in metrics]
    
    # Conditional expression used
    penalty = 10 if len([a for a in adjusted if a < base]) > 2 else 5
    
    raw_score = sum(adjusted) - penalty
    
    # Bit manipulation red herring
    magic_offset = (len(adjusted) << 2) ^ 7
    
    # Actual answer influenced by conditional path
    if raw_score > 30:
        final = raw_score + magic_offset
    else:
        final = raw_score - (magic_offset >> 1)
    
    # Another distractor call (no effect on result)
    _ = compute_string_hash(['debug', 1.2, 3.4])
    
    return int(final)

# Main execution block with realistic domain context (sensor array calibration)
sensor_readings = [0.8, 1.2, 0.9, 1.5, 1.1]
baseline = 1.0

# Irrelevant preprocessing chain
trend_strength = analyze_trend(sensor_readings)
normalized_readings = normalize_values(sensor_readings)
_ = update_cache(normalized_readings)

# Key statement embedded in noise
auxiliary_data = ['calib', 'mode', 'active']
config_flag = 'valid' if 'active' in auxiliary_data else 'pending'
dummy_hash = compute_string_hash(auxiliary_data)

final_score = evaluate_performance(sensor_readings, baseline)
print(f"Result: {final_score}")