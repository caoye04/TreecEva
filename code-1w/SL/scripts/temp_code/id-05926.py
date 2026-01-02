import math

# Simulated sensor array diagnostics with interference
sensor_readings = [127, 255, 63, 191, 135]
baseline = sum([r & 0x7F for r in sensor_readings]) >> 2
offset_table = {i: (i ** 2) % 128 for i in range(5)}

# Irrelevant transformation chain (dead path)
def legacy_calibrate(x):
    return (x << 3) | 7

# Unused signal filter (red herring)
signal_buffer = list(map(lambda val: (val ^ 0xAA) + 17, sensor_readings))
filtered = [x for x in signal_buffer if x > 100]

# Core diagnostic logic buried in noise
trend_data = 0
for idx, reading in enumerate(sensor_readings):
    if idx % 2 == 0:
        trend_data += reading ^ offset_table[idx]
    else:
        temp = (reading + baseline) // 4
        trend_data -= temp & 0x3F

# Decoy function that computes but is not used
def compute_health_score(data):
    score = 0
    for d in data:
        score ^= d * 3
    return score % 1000

health_warnings = set()
if trend_data < 200:
    health_warnings.add('LOW_SIGNAL')
if baseline > 300:
    health_warnings.add('HIGH_BASELINE')

# Distractor: complex but unused bitwise cascade
system_key = 0xDEADBEEF
key_partials = [(system_key >> (i * 8)) & 0xFF for i in range(4)]
scrambled = 0
for p in key_partials:
    scrambled = (scrambled << 8) | ((p ^ 0x5A) & 0xFF)

# Secondary red herring: floating point accumulation (irrelevant)
cumulative_drift = 0.0
for i in range(len(sensor_readings)):
    cumulative_drift += math.sin(i) * 0.1

# Real computation path (non-obvious due to context)
def aggregate_metrics(value, base):
    adjusted = (value + base) & 0xFFFF
    checksum = 0
    while adjusted:
        checksum ^= adjusted & 0xFF
        adjusted >>= 8
    return checksum * 17

# Hidden dependency: system_flag derived from initial data
system_flag = 0
for r in sensor_readings:
    system_flag ^= (r >> 4) & 0xF
system_flag = (system_flag ^ 0xFF) & 0xF

# Critical execution point — answer hinges on this
final_diagnostic = aggregate_metrics(trend_data, baseline) ^ system_flag

# Output required result
print(f"Result: {final_diagnostic}")