import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 52, 58, 41, 60, 55, 39, 47, 50]
pressure_readings = [1013, 1015, 1010, 1018, 1009, 1014, 1020, 1016, 1011]

# Irrelevant auxiliary measurements (distractor)
sound_levels = [34, 36, 45, 33, 40, 38, 42, 35, 37]  # dB levels - not used
light_intensity = [890, 910, 870, 920, 850, 880, 930, 860, 900]  # lux - not used

# Preprocessing: zipping and filtering based on quality score (simulated)
raw_data = list(zip(temperature_readings, humidity_readings, pressure_readings))
data_with_quality = [(t, h, p, (t * 2 + h) % 7) for t, h, p in raw_data]  # synthetic quality metric

# Filter out low-quality readings (quality < 3)
filtered_data = [entry for entry in data_with_quality if entry[3] >= 3]

# Decoy transformation - looks important but unused (dead path)
transformed = []
for t, h, p, q in filtered_data:
    transformed.append({
        'temp_adj': round(t * 1.02, 2),
        'humidity_index': h * 1.1,
        'pressure_norm': p / 1013.0
    })

# Threshold configuration map for diagnostics (critical)
threshold_map = {
    'temp_high': 24.0,
    'humid_high': 55,
    'press_trend': 'rising'
}

# Auxiliary function that appears complex but only one path matters
def analyze_trend(values):
    sorted_vals = sorted(values)
    median = sorted_vals[len(sorted_vals)//2]
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    trend_score = avg - median  # misleading metric
    return 'rising' if avg > sorted_vals[1] else 'falling'  # simplified logic

# Unused recursive decoy (red herring)
def binary_search(arr, val, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == val:
        return mid
    elif arr[mid] < val:
        return binary_search(arr, val, mid + 1, hi)
    else:
        return binary_search(arr, val, lo, mid - 1)

# Real processing begins here — key function with distractors
def process_readings(data, thresholds):
    temp_alerts = 0
    humid_alerts = 0
    pressure_trend = []

    for reading in data:
        temp, humid, press, qual = reading

        # Relevant conditionals
        if temp > thresholds['temp_high']:
            temp_alerts += 1

        if humid > thresholds['humid_high']:
            humid_alerts += 1

        pressure_trend.append(press)

    # Compute actual diagnostic (this is what matters)
    trend_status = analyze_trend(pressure_trend)
    press_alert = 1 if trend_status == thresholds['press_trend'] else 0

    # Irrelevant aggregation (distraction)
    total_combinations = len(list(itertools.combinations([t[0] for t in data], 2)))
    entropy_proxy = len(set(round(t[0]) for t in data))  # fake complexity

    # Final computation — only this output is correct
    base_score = temp_alerts * 100 + humid_alerts * 10 + press_alert
    adjustment = sum(1 for t in data if t[0] < 21) * 2  # correction for cool temps
    final_score = base_score - adjustment

    # Critical result variable
    final_diagnostic = final_score + 333

    # Dead code block (never reached)
    if False:
        backup = 0
        for x in data:
            backup += hash(str(x))
        final_diagnostic = backup % 1000

    return final_diagnostic

# Execute main logic
temp_above_threshold = [t for t, h, p, q in filtered_data if t > 25]  # unused side calc
avg_humidity_filtered = sum(h for t, h, p, q in filtered_data) / len(filtered_data)  # red herring

final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")