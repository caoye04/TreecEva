from collections import defaultdict
import itertools

# Simulate sensor data processing with noise filtering and performance scoring
def analyze_readings(raw_data, threshold=50):
    filtered = [x for x in raw_data if x > threshold]
    count_map = defaultdict(int)
    for val in filtered:
        count_map[val // 10] += 1

    # Distractor: unused computation on bit patterns
    bit_analysis = sum((val & (val - 1)) == 0 for val in raw_data)  # counts powers of two

    return dict(count_map)


def calculate_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 1
    # Irrelevant transformation
    mirrored = [values[-i] for i in range(1, len(values)+1)]
    return trend_score

# Main data
baseline = [45, 52, 55, 60, 47, 58]
readings = [51, 49, 56, 70, 75, 80, 40, 65, 54, 53, 59]

# Preprocessing steps with red herrings
extended_readings = readings + [x + 10 for x in baseline if x < 55]
duplicate_check = [item for item, count in itertools.groupby(sorted(extended_readings)) if len(list(count)) > 1]

stats = analyze_readings(extended_readings, threshold=52)

# Compute derived metrics
magnitude = sum(stats.keys())
frequency = sum(stats.values())

# Distractor block: complex but unused structure
combinations = list(itertools.combinations_with_replacement([2, 3], 2))
shadow_score = 0
for a, b in combinations:
    shadow_score += a ** b

# Real calculation chain
trend = calculate_trend(readings)
temp_offset = abs(baseline[0] - readings[0])
raw_influence = len(readings) - len(baseline)

# Key statement
final_score = (magnitude + frequency) + (trend * temp_offset) - raw_influence

Result: final_score