from collections import Counter

def calculate_threshold(data, mode):
    count_freq = Counter(data)
    most_common_val = count_freq.most_common(1)[0][1]
    avg = sum(data) / len(data)
    if mode == 'strict':
        return avg + (most_common_val * 0.5) if avg > 50 else avg + 2.5
    else:
        return avg

# Sensor readings in milliwatts
readings = [45, 60, 60, 75, 45, 60, 90, 75, 45, 60]
baseline = sum(readings) // len(readings)
mode = 'strict'
previous_limit = 58
energy_threshold = calculate_threshold(readings, mode)
Result: {energy_threshold}