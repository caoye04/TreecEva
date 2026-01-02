import math

# Simulated sensor array data from environmental monitoring system
temperature_readings = [23.4, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7, 22.5]
humidity_readings = [56, 61, 58, 64, 70, 68, 62, 59]
co2_levels = [410, 425, 405, 430, 450, 440, 420, 415]

# Irrelevant auxiliary data (distractor)
sound_decibels = [32, 35, 30, 40, 45, 38, 34, 36]
light_lux = [12000, 11000, 13000, 10000, 9000, 11500, 12500, 10500]

# Misleading intermediate transformation (dead path)
def analyze_acoustics(decibels):
    weighted_avg = sum(d * 0.8 for d in decibels) / len(decibels)
    return weighted_avg

acoustic_profile = analyze_acoustics(sound_decibels)  # Dead assignment

# Core processing functions
def normalize_sensor(data):
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) * 1.5, 2) for x in data]  # Amplified deviation

def detect_anomalies(normalized):
    return [abs(x) > 1.8 for x in normalized]

def compute_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data if x > 0]
    return -sum(p * math.log(p) for p in probabilities)

# Apply normalization (relevant)
norm_temp = normalize_sensor(temperature_readings)
norm_humidity = normalize_sensor(humidity_readings)
norm_co2 = normalize_sensor(co2_levels)

# Anomaly detection (relevant)
anomalous_temps = detect_anomalies(norm_temp)
anomalous_humid = detect_anomalies(norm_humidity)

# Decoy function with unused result (red herring)
def simulate_projection(values, days=7):
    trend = sum(values[i+1] - values[i] for i in range(len(values)-1)) / (len(values)-1)
    return [values[-1] + trend * d for d in range(1, days+1)]

projected_temps = simulate_projection(temperature_readings)  # Not used

# Compute derived metrics (relevant)
temp_entropy = compute_entropy([abs(x) for x in norm_temp])
humidity_entropy = compute_entropy([abs(x) for x in norm_humidity])
combined_entropy = round((temp_entropy + humidity_entropy) * 100, 4)

# Create processing chain using list comprehension and filtering
processing_chain = [
    {'stage': i+1, 't_val': t, 'h_val': h, 'c_val': c, 'critical': abs(t) > 2.0}
    for i, (t, h, c) in enumerate(zip(norm_temp, norm_humidity, norm_co2))
    if i % 2 == 0 or c > 0.5
]

# Diagnostic flags with bit manipulation (relevant)
diagnostic_flags = 0
for entry in processing_chain:
    if entry['critical']:
        diagnostic_flags |= 1 << int(entry['stage'])  # Bitwise set
    elif entry['t_val'] < -1.0:
        diagnostic_flags ^= 1 << (entry['stage'] + 1)  # Toggle

# Unused but plausible decoy structure (distraction)
class DataBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [0.0] * capacity
    
    def write(self, val):
        self.buffer.append(val)
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)

buffer = DataBuffer(5)
for val in norm_co2:
    buffer.write(val * 1.1)  # Elaborate dead code

# Final aggregation logic (key computation)
def aggregate_metrics(chain, flags):
    base_score = sum(abs(entry['t_val']) * 10 for entry in chain)
    humidity_factor = sum(entry['h_val'] for entry in chain if entry['h_val'] > 0)
    flag_penalty = bin(flags).count('1') * -3.5
    co2_bonus = len([e for e in chain if e['c_val'] > 1.0]) * 7.2
    
    # Additional irrelevant internal logic
    temp_shadow = [x for x in norm_temp if x > 0]
    shadow_mean = sum(temp_shadow) / len(temp_shadow) if temp_shadow else 0
    fake_correction = math.sin(shadow_mean) * 0  # Zeroed out distraction
    
    final_value = base_score + humidity_factor + flag_penalty + co2_bonus + fake_correction
    return round(final_value, 4)

# Execution point of interest
final_diagnostic = aggregate_metrics(processing_chain, diagnostic_flags)

# Output the target result
print(f"Target result: {final_diagnostic}")