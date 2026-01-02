from collections import Counter

def analyze_pattern(data):
    count = Counter(data)
    mode_val = count.most_common(1)[0][1]
    return mode_val

def normalize_value(x):
    return round(x * 0.95, 3)

def calculate_performance(base, logs):
    adjusted = [normalize_value(x) for x in logs if x > base]
    trend = sum(1 for x in adjusted if x > base * 0.9)
    weight = len(adjusted) * 1.1
    raw_score = weight * trend
    offset = len([x for x in logs if x < base]) * 0.5
    final = raw_score - offset
    return round(final, 3)

# Irrelevant utility function (mild distraction)
def to_upper(s):
    return s.upper()

# Main execution
baseline = 72.5
data_stream = [68.1, 75.3, 80.0, 73.2, 69.8, 85.5, 77.1]

# Unused variable (minor interference)
status_flags = {"active": True, "debug": False}

dominant_frequency = analyze_pattern([1, 1, 2, 3, 2, 1])
processed_readings = [round(x + 0.1, 1) for x in data_stream]

final_score = calculate_performance(baseline, processed_readings)
print(f"Target result: {final_score}")