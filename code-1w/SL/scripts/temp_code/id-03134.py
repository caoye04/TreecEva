import math

# Simulated sensor array data with noise and redundancy
data_stream = [145, 178, 203, 188, 256, 134, 190, 205, 176, 168, 182, 195, 210, 180, 170]
noise_floor = 150
calibration_factor = 0.87
redundant_cache = {'temp': 23.5, 'humidity': 45, 'pressure': 1013}

# Irrelevant preprocessing: frequency analysis (dead path)
freq_map = {}
for val in data_stream:
    bin_key = val // 10 * 10
    freq_map[bin_key] = freq_map.get(bin_key, 0) + 1

# Decoy transformation using unused lambda
offset_corrector = lambda x: x - 12 if x > 180 else x + 8

# Actual filtering logic buried among distractions
elevated_readings = []
for reading in data_stream:
    if reading > noise_floor:
        elevated_readings.append(reading)

# Red herring: sorting that isn't used later
sorted_elevated = sorted(elevated_readings, reverse=True)

# Another decoy: set operations with no impact
unique_set = set(elevated_readings)
overlap_check = unique_set.intersection({178, 188, 198, 208})

# Core processing chain begins here — obscured by prior noise
working_buffer = []
for v in elevated_readings:
    adjusted = v * calibration_factor
    if adjusted % 2 == 0:
        working_buffer.append(int(adjusted))
    else:
        working_buffer.append(int(adjusted) + 1)  # Normalize to even

# Secondary filter: exclude values outside modal range
mode_base = 170
range_span = 40
filtered_data = [x for x in working_buffer if mode_base <= x <= mode_base + range_span]

# Misleading aggregation (unused)
avg_spurious = sum(sorted_elevated) / len(sorted_elevated) if sorted_elevated else 0
trend_analysis = list(map(lambda x: x - avg_spurious, sorted_elevated))

# Real computation hidden in modular arithmetic and dictionary transform
def process_readings(readings, factor):
    stats = {
        'sum': 0,
        'count': 0,
        'max_val': float('-inf'),
        'history': []
    }

    for r in readings:
        stats['sum'] += r
        stats['count'] += 1
        if r > stats['max_val']:
            stats['max_val'] = r
        
        # Bit manipulation red herring
        bit_shifted = (r << 1) ^ 255
        if bit_shifted > 1000:
            continue  # Dead condition

    # Actual key calculation
    raw_average = stats['sum'] / stats['count'] if stats['count'] > 0 else 0
    
    # Final adjustment using trigonometric weight (obscured purpose)
    angle = math.pi * (stats['count'] % 4) / 2
    weight = math.cos(angle) if angle != 0 else 0.5
    
    # Critical early return based on control flow trap
    if weight == 0:
        return int(stats['max_val'] * factor)
    
    intermediate = raw_average + (weight * 12.5)
    
    # Modular correction to stabilize output
    corrected = (intermediate * 100) % 89
    
    # Final nonlinear transform
    result = int((corrected ** 1.5) / 3.7)
    
    return result

# Trigger point: this assignment contains the answer
diagnostic_snapshot = {'stage': 'post-process', 'verified': False}
final_diagnostic = process_readings(filtered_data, calibration_factor)
diagnostic_snapshot['result'] = final_diagnostic

diagnostic_snapshot['verified'] = True if final_diagnostic > 50 else False

# Output the target result
print(f"Target result: {final_diagnostic}")