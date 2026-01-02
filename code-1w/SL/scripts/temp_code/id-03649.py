def analyze_trend(data, threshold):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append('up')
        elif data[i] < data[i-1]:
            trend.append('down')
        else:
            trend.append('same')
    ups = trend.count('up')
    downs = trend.count('down')
    stability_ratio = (len(trend) - abs(ups - downs)) / len(trend) if trend else 1.0
    return stability_ratio > threshold


def extract_features(raw_log):
    tokens = raw_log.split()
    word_count = len(tokens)
    unique_words = len(set(tokens))
    char_freq = {}
    for char in ''.join(tokens):
        char_freq[char] = char_freq.get(char, 0) + 1
    top_char = max(char_freq, key=char_freq.get) if char_freq else ''
    entropy_proxy = unique_words / word_count if word_count else 0
    return {'entropy': entropy_proxy, 'top_char': top_char, 'length': word_count}


def evaluate_performance(metrics, baseline):
    adjustment = 0
    if metrics['stability'] > baseline['stability']:
        adjustment += 15
    else:
        adjustment -= 5

    if metrics['efficiency'] >= baseline['efficiency']:
        adjustment += 10

    outlier_flags = 0
    readings = [98, 99, 100, 101, 102, 115, 116]
    avg_reading = sum(readings) / len(readings)
    std_dev = (sum((x - avg_reading) ** 2 for x in readings) / len(readings)) ** 0.5
    for val in readings:
        if abs(val - avg_reading) > 2 * std_dev:
            outlier_flags += 1

    if outlier_flags == 0:
        adjustment += 20

    temp_data = [1, 1, 2, 3, 5, 8, 13]
    fibonacci_check = all(temp_data[i] == temp_data[i-1] + temp_data[i-2] for i in range(2, len(temp_data)))
    if fibonacci_check:
        adjustment += 5

    slice_sum = sum(temp_data[2:5])
    dummy_map = {i: x**2 for i, x in enumerate(temp_data)}
    ignored_result = [x for x in temp_data if x > 5]

    final_score = 100 + adjustment
    return final_score

# Simulated input data
diagnostic_log = "sys cpu1=98 cpu2=99 cpu3=100 io=101 mem=102 temp=115 disk=116"
log_features = extract_features(diagnostic_log)

sensor_readings = [100, 102, 99, 101, 100, 103, 102]
trend_stable = analyze_trend(sensor_readings, 0.7)

metrics = {
    'stability': 0.85,
    'efficiency': 94.6,
    'consistency': len(set(sensor_readings))
}

baseline = {
    'stability': 0.80,
    'efficiency': 95.0,
    'response_time': 120
}

# Key execution point
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")