import math

def preprocess_sensor(value, scale=1.0, offset=0.0):
    # Irrelevant preprocessing with red herring parameters
    if value < 0:
        value = abs(value)
    normalized = (value * scale) + offset
    return int(normalized * 100) / 100.0


def transform_sequence(data_list):
    # Distractor function: looks important but only used partially
    shifted = [(x + 3) * 0.9 for x in data_list if x > 10]
    return [round(y, 2) for y in shifted]


def filter_outliers(stream):
    mean_val = sum(stream) / len(stream)
    deviances = [abs(x - mean_val) for x in stream]
    threshold = mean_val * 0.5
    filtered = [stream[i] for i in range(len(stream)) if deviances[i] <= threshold]
    return filtered  # Used, but some logic above is exaggerated


def accumulate_diagnostic(values):
    # Core logic buried in noise
    running_total = 0
    for v in values:
        if v % 2 == 0:
            running_total += int(math.sqrt(v))
        else:
            running_total -= (v % 7)
    return running_total


def compute_integrity_score(records):
    # Dead path - never called
    score = 0
    for r in records:
        score += r ** 0.1
    return round(score, 3)

# Simulated sensor readings (real input data)
sensor_readings = [16, 25, 14, 9, 22, 30, 11, 18]

# Irrelevant transformation chain
scaled_readings = [preprocess_sensor(x, scale=1.1) for x in sensor_readings]
dummy_shift = transform_sequence(scaled_readings)

# Actual preprocessing step (looks similar to distractors)
processed_signals = filter_outliers(sensor_readings)

# Hidden accumulation logic using bitwise and arithmetic mix
intermediate_flags = []
for val in processed_signals:
    flag = (val ^ 15) & 7  # Bitwise red herring
    intermediate_flags.append(flag)

# Real computation hidden among decoys
aggregate = 0
for idx, val in enumerate(processed_signals):
    if idx % 2 == 0:
        aggregate += val // 2
    else:
        aggregate -= val % 4

# Core diagnostic analysis (key statement)
def analyze_readings(signal_list):
    base_sum = sum(signal_list)
    adjustments = 0
    for i, x in enumerate(signal_list):
        if i == 0:
            adjustments += 5
        elif i % 3 == 0:
            adjustments -= 2
        if x > 20:
            adjustments += 1
    # Final computation combining arithmetic and list logic
    result = base_sum + adjustments + accumulate_diagnostic(signal_list)
    return result

# Unused variables - red herrings
reindexed_data = {i: sensor_readings[i] for i in range(len(sensor_readings))}
weighted_avg = sum(scaled_readings) / len(scaled_readings)
status_map = {'ok': True, 'faulty': False, 'calibrated': True}

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

# Output result as required
print(f"Result: {final_diagnostic}")