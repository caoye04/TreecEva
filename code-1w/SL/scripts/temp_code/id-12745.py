def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return sum(x ** 2 for x in sequence if x % 2 == 0)


def compute_checksum(data):
    # Distractor computation - not used in final result
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) % 7
    return checksum

# Simulated sensor readings (with noise and offsets)
sensor_raw = [127, 63, 255, 91, 193, 45, 181]
noise_floor = 42
offset_map = {i: (i * 13) % 17 for i in range(len(sensor_raw))}

calibration_factor = 0.87
scaling_bias = 1.05  # Unused bias term - misleading

# Apply offset correction using zip (relevant)
corrected_readings = []
for val, (idx, offset) in zip(sensor_raw, enumerate(offset_map.values())):
    corrected_readings.append(val - offset if idx % 3 != 0 else val)

# Introduce list comprehension with filtering (partially relevant)
filtered_data = [x for x in corrected_readings if x > 50]

# Add dummy transformation chain
transformed = []
for x in filtered_data:
    temp = (x >> 2) ^ 15
    temp = (temp * 3) + 7
    transformed.append(temp)

# Decoy sorting operation (not used later)
sorted_transformed = sorted(transformed, reverse=True)

# Real processing begins here — key data structure setup
sensor_data = [abs(x - 100) + 10 for x in transformed]

# Secondary distractor: modular arithmetic red herring
mod_accumulator = 0
for i in range(len(sensor_data)):
    mod_accumulator = (mod_accumulator + sensor_data[i] * (i + 1)) % 97

# Conditional expression with nested logic (relevant path)
adjustment = 5 if sum(sensor_data) > 300 else 2

# Core processing function with embedded logic
def process_readings(readings, factor):
    base = 0
    multiplier = int(factor * 100)  # Convert to integer scale
    
    for i, val in enumerate(readings):
        if i % 2 == 0:
            base += val * multiplier
        else:
            base -= (val // 2) * (multiplier // 3)
    
    # Bit manipulation layer
    base = (base ^ 0xAA) & 0xFFFF  # Apply bit mask
    
    # Final adjustment using conditional expression
    base = base - adjustment if base > 500 else base + adjustment
    
    # Inject irrelevant floating point noise
    noise_term = 0.123 * (len(readings) % 4)  # Dead-end float
    
    return base  # Integer result

# Execute main logic
final_diagnostic = process_readings(sensor_data, calibration_factor)

# Print required output
print(f"Target result: {final_diagnostic}")