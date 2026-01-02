import math

# Simulated sensor data from industrial monitoring system
temperature_readings = [23.5, 24.1, 25.0, 26.3, 25.8, 24.7, 23.9, 22.8, 21.5, 20.3]
humidity_readings = [45, 47, 50, 55, 60, 62, 58, 53, 48, 44]
pressure_readings = [1013, 1015, 1017, 1016, 1014, 1012, 1011, 1010, 1009, 1008]

# Irrelevant statistical red herring variables
temp_variance = sum((x - sum(temperature_readings)/len(temperature_readings))**2 for x in temperature_readings) / len(temperature_readings)
hum_skewness = (sum((x - sum(humidity_readings)/len(humidity_readings))**3 for x in humidity_readings) / len(humidity_readings)) / (temp_variance ** 1.5) if temp_variance > 0 else 0

# Unused transformation function (decoy)
def transform_pressure(p):
    return [math.log(x) * 1.05 for x in p if x > 1000]

# Distractor: complex but unused data structure
class SensorNode:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.data = []

    def append(self, val):
        self.data.append(val)

node_1 = SensorNode('A1', 'thermal')
for t in temperature_readings:
    node_1.append(t * 1.02)

# Real processing begins here
valid_ranges = {
    'temp': (20.0, 27.0),
    'humidity': (40, 65),
    'pressure': (1005, 1020)
}

# Linear search for first anomaly
anomaly_index = -1
for i in range(len(temperature_readings)):
    t, h, p = temperature_readings[i], humidity_readings[i], pressure_readings[i]
    if not (valid_ranges['temp'][0] <= t <= valid_ranges['temp'][1] and 
            valid_ranges['humidity'][0] <= h <= valid_ranges['humidity'][1] and 
            valid_ranges['pressure'][0] <= p <= valid_ranges['pressure'][1]):
        anomaly_index = i
        break

# Data transformation pipeline
sanitize = lambda x: [val for val in x if isinstance(val, (int, float)) and not math.isnan(val)]
smooth_data = lambda x: [sum(x[max(0,i-1):min(len(x),i+2)]) / min(3, i+2, len(x)-i+1) for i in range(len(x))]

filtered_temps = sanitize(temperature_readings)
processed_logs = smooth_data(filtered_temps)

# Conditional expression to mask normal fluctuations
baseline_temp = 24.0
adjusted_logs = [val if abs(val - baseline_temp) <= 1.5 else (val + baseline_temp) / 2 for val in processed_logs]

# Accumulation with potential overflow guard (unused path)
running_total = 0
overflow_count = 0
for val in adjusted_logs:
    running_total += val
    if running_total > 1000:
        running_total -= 500
        overflow_count += 1

# Core diagnostic logic (obscured by distractions)
def detect_trend(data):
    increasing = decreasing = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increasing += 1
        elif data[i] < data[i-1]:
            decreasing += 1
    return 'rising' if increasing > decreasing else 'falling'

# Secondary validation using character encoding checksum (red herring)
def compute_checksum(text):
    return sum(ord(c) * (i+1) for i, c in enumerate(text)) % 100

checksum_probe = compute_checksum(f"sensor_{detect_trend(adjusted_logs)}")

# Real analysis function
analyze_readings = lambda data: (
    sum(math.sin(x * math.pi / 180) for x in data) * 
    (1 if detect_trend(data) == 'rising' else -1)
)

# Key assignment statement
final_diagnostic = analyze_readings(processed_logs)

# Irrelevant string manipulation block
device_id = "THS-2023"
segment_sum = sum(int(d) for d in device_id if d.isdigit())
id_prefix = ''.join(chr(ord(c)+1) if c.isalpha() else c for c in device_id[:3])

# Final result output
print(f"Result: {final_diagnostic}")