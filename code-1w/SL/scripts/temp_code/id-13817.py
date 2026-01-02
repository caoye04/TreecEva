from collections import Counter

def analyze_pattern(sequence):
    count = Counter(sequence)
    modes = [k for k, v in count.items() if v == max(count.values())]
    return sorted(modes)[0] if modes else 0

def evaluate_stability(readings):
    readings = [x for x in readings if x > 0]
    avg = sum(readings) / len(readings) if readings else 0
    deviation = sum((x - avg) ** 2 for x in readings)
    return avg - (deviation * 0.1)

def calculate_performance(data):
    pattern_key = analyze_pattern([len(item) for item in data])
    stability = evaluate_stability([sum(ord(c) for c in s) for s in data])
    adjustment = len(data[0]) if data else 0
    raw_score = stability * pattern_key + adjustment
    final_score = int(raw_score // 1.5)
    return final_score

# Simulated sensor data stream
sensor_logs = [
    "ax9m2kl",
    "bx8n3km",
    "cx7o4kn",
    "dx6p5ko",
    "ex5q6kp"
]

# Irrelevant auxiliary variable (minimal distraction)
metadata_index = sum(len(log) for log in sensor_logs) % 7

final_score = calculate_performance(sensor_logs)
print(f"Result: {final_score}")