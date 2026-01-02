import math

# Simulated environmental sensor network diagnostics
sensors = [107, 231, 154, 92, 188, 205, 133, 176, 167, 144]

def calculate_entropy(data):
    entropy = 0.0
    total = sum(data)
    for x in data:
        prob = x / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

# Irrelevant diagnostic function (dead code path)
def legacy_diagnostic(seq):
    return [x ^ 255 for x in seq if x % 2 == 0]

# Distractor: unused calibration curve
calibration_curve = [math.sin(i * 0.1) for i in range(100)]

# Real processing begins here
active_mask = list(map(lambda x: x > 150, sensors))
filtered_sensors = [sensors[i] for i in range(len(sensors)) if active_mask[i]]

# Secondary filtering based on bit properties (relevant)
high_bit_density = [x for x in filtered_sensors if bin(x).count('1') > 3]

# Misleading intermediate transformation (unused)
temp_normalization = [(x - 128) ** 2 for x in sensors if x < 150]

# Critical recursive reducer
def reduce_with_factor(acc, val, factor):
    if acc <= factor:
        return acc + val % 7
    return reduce_with_factor(acc - factor, val + 1, factor // 2) if factor > 1 else acc ^ val

# Orchestration function
def analyze_readings(readings):
    base = sum(readings) // len(readings)
    
    # Complex conditional expression with nested logic
    adjustment = sum(
        [reduce_with_factor(r, base, 8) for r in readings if r % 3 == 1]
    ) if len(readings) > 2 else reduce_with_factor(readings[0], 100, 8)
    
    # Dummy control flow (red herring)
    outlier_flag = False
    for idx, val in enumerate(readings):
        if val > 200 and idx % 2 == 0:
            temp_offset = val >> 3
            outlier_flag = True
            break

    # Unused but plausible-looking statistical measure
    variance_proxy = sum((x - base) ** 2 for x in readings) / len(readings) if readings else 0

    # Core calculation buried in distractions
    raw_energy = math.floor(math.sqrt(sum([x * x for x in high_bit_density])))
    
    # Final threshold computation (answer)
    energy_threshold = (raw_energy + adjustment) & 0xFFFF
    
    # More decoys
    signal_quality = sum(1 for x in readings if bin(x).count('1') % 2 == 0)
    normalization_factor = math.log(signal_quality + 1) if signal_quality > 0 else 1
    
    return {
        'threshold': energy_threshold,
        'quality': normalization_factor,
        'size': len(readings)
    }

# Execution chain
entropy_metric = calculate_entropy(sensors)
analysis_summary = {'initial': len(sensors)}
final_analysis = analyze_readings(filtered_sensors)
energy_threshold = final_analysis['threshold']

# Output requirement
print(f"Result: {energy_threshold}")