from collections import Counter

# Sensor data analysis for environmental monitoring
def analyze_readings(readings):
    high_freq = Counter(readings)
    modes = [k for k, v in high_freq.items() if v == max(high_freq.values())]
    return min(modes)

# Determine stability based on fluctuation threshold
def is_stable(data, limit):
    return all(abs(data[i] - data[i-1]) <= limit for i in range(1, len(data)))

# Main calculation function
def calculate_final_score(values, bounds):
    filtered = [v for v in values if v >= bounds[0]]
    if not filtered:
        return 0
    
    # Apply transformation only if sequence is stable
    tolerance = bounds[1]
    if is_stable(filtered, tolerance):
        transformed = list(map(lambda x: x ** 0.5 if x > 25 else x / 2, filtered))
    else:
        transformed = [x for x in filtered if x % 2 == 0]
    
    mode_value = analyze_readings([round(x) for x in transformed])
    adjustment = len([x for x in transformed if x > mode_value])
    return int(sum(transformed) - adjustment)

# Input data
temperatures = [30, 34, 34, 28, 30, 36, 38]
thresholds = (30, 5)

result = calculate_final_score(temperatures, thresholds)
print(f"Result: {result}")