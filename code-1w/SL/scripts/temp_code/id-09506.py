from itertools import cycle
import math

# Simulate a geothermal energy assessment with layered distractions
def analyze_sensor_array():
    sensor_ids = ['S1', 'S2', 'S3', 'S4']
    readings = [18, 22, 19, 25]
    baseline = 20
    adjusted_readings = [r - baseline for r in readings]

    # Irrelevant transformation: signal smoothing (dead path)
    smoothed = []
    for i in range(len(readings)):
        if i == 0:
            smoothed.append(readings[i])
        else:
            smoothed.append((readings[i] + readings[i-1]) / 2)

    # Distractor: frequency analysis on sensor IDs (no impact)
    freq_map = {}
    for char in ''.join(sensor_ids):
        freq_map[char] = freq_map.get(char, 0) + 1

    return adjusted_readings

# Misleading data fusion function (never called in critical path)
def fuse_data_streams(stream_a, stream_b):
    fused = []
    for a, b in zip(stream_a, stream_b):
        fused.append((a * 1.5) + (b * 0.8))
    return fused

# Decoy calibration using bitwise logic (unused)
def calibrate_device(status_word):
    flags = status_word
    flags ^= 0xFF
    flags &= 0x0F
    flags |= 0xA0
    return flags

# Real processing chain
entropy_flow = 0

def update_entropy(value):
    global entropy_flow
    value = (value * 2) + 7
    value = value ^ 0x1A
    value = value % 100
    entropy_flow += value

for index, val in enumerate(analyze_sensor_array()):
    temp_val = abs(val) * 3
    if temp_val > 5:
        update_entropy(temp_val)
    else:
        # Dead branch - condition never met due to abs(val)*3 >= 6
        entropy_flow -= 10

# Red herring: unused lambda-based filter
outlier_filter = lambda x: x > 30
filtered_data = list(filter(outlier_filter, [abs(x)*3 for x in analyze_sensor_array()]))

# Another distraction: character counting in fake log
system_log = "ERROR:CALIBRATE:RETRY:SYNC"
count_R = sum(1 for c in system_log if c == 'R')

# Core calculation disguised among noise
def transform_sequence(seq):
    transformed = []
    for item in seq:
        item = item * 2
        item = item + (item % 7)
        transformed.append(item)
    return transformed

# Actual answer generator
sequence_bank = [4, 7, 2]
bank_cycle = cycle(sequence_bank)
accumulated_phase = 0

for _ in range(3):
    next_val = next(bank_cycle)
    accumulated_phase += next_val * 2

entropy_flow += accumulated_phase

# Critical computation buried in abstraction
def calculate_thermal_output(ent):
    base = ent * 1.5
    # Apply modular correction
    correction = (ent % 13) * 0.8
    # Bit manipulation red herring (but result used)
    bit_shifted = (ent >> 2) & 0x3F
    final = base + correction - bit_shifted
    return final

thermal_capacity = 0
thermal_capacity = calculate_thermal_output(entropy_flow)

print(f"Result: {thermal_capacity}")