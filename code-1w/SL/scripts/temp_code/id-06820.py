from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation over time
raw_readings = [
    {'time': 0, 'sensor': 'temp', 'value': 98.6},
    {'time': 1, 'sensor': 'hr', 'value': 72},
    {'time': 2, 'sensor': 'temp', 'value': 99.1},
    {'time': 3, 'sensor': 'spo2', 'value': 98},
    {'time': 4, 'sensor': 'hr', 'value': 75},
    {'time': 5, 'sensor': 'temp', 'value': 100.4},
    {'time': 6, 'sensor': 'hr', 'value': 78},
    {'time': 7, 'sensor': 'spo2', 'value': 96},
    {'time': 8, 'sensor': 'temp', 'value': 101.3},
    {'time': 9, 'sensor': 'hr', 'value': 82},
    {'time': 10, 'sensor': 'spo2', 'value': 94}
]

# Irrelevant auxiliary mapping (distractor)
sensor_units = defaultdict(lambda: 'unknown')
sensor_units['temp'] = '°F'
sensor_units['hr'] = 'bpm'
sensor_units['spo2'] = '%'

# Aggregating readings by type (relevant)
sensor_data = defaultdict(list)
for reading in raw_readings:
    sensor_data[reading['sensor']].append(reading['value'])

# Derived statistics (some relevant, some not)
avg_temp = sum(sensor_data['temp']) / len(sensor_data['temp'])
avg_hr = sum(sensor_data['hr']) / len(sensor_data['hr'])
avg_spo2 = sum(sensor_data['spo2']) / len(sensor_data['spo2'])

temp_trend = [round(b - a, 1) for a, b in zip(sensor_data['temp'], sensor_data['temp'][1:])]
heart_rate_variability = math.sqrt(sum((x - avg_hr) ** 2 for x in sensor_data['hr']) / len(sensor_data['hr']))

# Decoy function: looks important but unused
def analyze_risk_profile(data):
    score = 0
    if data.get('temp', 0) > 100:
        score += 30
    if data.get('hr', 0) > 80:
        score += 20
    if data.get('spo2', 0) < 95:
        score += 50
    return score  # never called

# Thresholds for health metrics (used later)
thresholds = {
    'fever': 100.4,
    'tachycardia': 80,
    'hypoxia': 95
}

# Data structure transformation (mix of relevant and irrelevant)
summary_stats = {}
for s, values in sensor_data.items():
    summary_stats[s] = {
        'count': len(values),
        'mean': sum(values) / len(values),
        'peak': max(values),
        'trough': min(values),
        'variance': sum((x - sum(values)/len(values))**2 for x in values) / len(values)
    }

# Dead code path (distractor)
if False:
    legacy_format = []
    for k, v in summary_stats.items():
        legacy_format.append(f"{k}: {v['mean']:.1f}")

# Another decoy: complex but unused calculation
fft_simulated = [math.sin(i * 0.5) * math.cos(i * 0.3) for i in range(len(raw_readings))]
fft_magnitude = sum(abs(x) for x in fft_simulated) / len(fft_simulated)

# Health event detection logic
alerts = []
if summary_stats['temp']['peak'] >= thresholds['fever']:
    alerts.append('fever')
if summary_stats['hr']['peak'] >= thresholds['tachycardia']:
    alerts.append('tachycardia')
if summary_stats['spo2']['trough'] < thresholds['hypoxia']:
    alerts.append('hypoxia')

# Mock machine learning model (irrelevant)
class DummyClassifier:
    def predict(self, x):
        return sum(x) % 2

clf = DummyClassifier()
prediction = clf.predict([len(alerts), int(avg_temp)])  # unused

# Core processing function (critical path)
def process_metrics(data, limits):
    fever_count = len([v for v in data['temp'] if v >= limits['fever']])
    high_hr_count = len([v for v in data['hr'] if v >= limits['tachycardia']])
    low_spo2_count = len([v for v in data['spo2'] if v < limits['hypoxia']])
    
    # Composite risk index (intermediate)
    risk_index = (fever_count * 8) + (high_hr_count * 5) + (low_spo2_count * 12)
    
    # Distractor: unused conditional branch
    if risk_index > 50:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.1  # never used
    
    # Secondary analysis with bit manipulation (looks complex, partially relevant)
    encoded_state = 0
    if fever_count > 0:
        encoded_state |= 1 << 3
    if high_hr_count > 0:
        encoded_state |= 1 << 2
    if low_spo2_count > 0:
        encoded_state |= 1 << 1
    
    # Final diagnostic uses arithmetic combination
    base_score = fever_count * 17
    base_score += high_hr_count * 13
    base_score -= low_spo2_count * 7
    base_score += encoded_state  # integrates alert bitmask
    
    # Additional red herring: log computation
    if base_score > 0:
        entropy_proxy = math.log(base_score + 1) * 0.5
    
    # Final adjustment based on trend consistency
    rising_temp = all(t > 0 for t in temp_trend)
    if rising_temp and low_spo2_count > 0:
        base_score += 10
    
    return int(base_score)

# Execute main logic
health_data = sensor_data
final_diagnostic = process_metrics(health_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")