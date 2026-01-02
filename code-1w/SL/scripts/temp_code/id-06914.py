from collections import Counter

def calculate_threshold(data):
    avg = sum(data) / len(data)
    filtered = [x for x in data if x > avg]
    freq = Counter(filtered)
    return max(freq.keys()) - min(freq.keys())

readings = [12, 15, 10, 20, 18, 22, 14, 19]
sensor_status = 'active'
baseline = 15
adjustment_factor = 0.8

# Key statement
energy_threshold = calculate_threshold(readings)

print(f"Result: {energy_threshold}")