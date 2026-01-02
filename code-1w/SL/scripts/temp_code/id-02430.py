def analyze_sensor_pattern(sequence):
    """Irrelevant helper: analyzes repeating substrings in sensor IDs."""
    if not sequence:
        return 0
    longest = 1
    current = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)


def validate_checksum(data):
    """Decoy function: computes sum of squares modulo prime."""
    prime = 97
    total = 0
    for x in data:
        total += (x * x) % prime
    return total % prime

# Simulated raw sensor readings (temperature in tenths of °C)
raw_readings = [234, 235, 233, 240, 250, 260, 255, 245, 230, 225, 220, 218, 215, 210, 205]

# Irrelevant string metadata from sensor network
sensor_id_log = "SNSR-TEMP-A7,SNSR-TEMP-B2,SNSR-HUM-C3,SNSR-TEMP-D1"
sensor_set = set(sensor_id_log.split(','))
id_substring = ''.join([s[-1] for s in sorted(sensor_set) if 'TEMP' in s])
analysis_stub = analyze_sensor_pattern(id_substring)  # Dead-end computation

# Distractor: historical thresholds (not used)
historical_min = [200, 195, 190, 188, 185]
historical_max = [270, 275, 280, 285, 290]
rolling_avg = sum(historical_max) // len(historical_max)  # Unused

# Critical configuration
OPERATIONAL_FLOOR = 210
ALERT_CEILING = 255
threshold = (ALERT_CEILING + OPERATIONAL_FLOOR) // 4  # Cleverly disguised: 116

# Filter logic: isolate elevated temperatures
filtered_data = []
for temp in raw_readings:
    if temp > ALERT_CEILING:
        adjusted = temp - ALERT_CEILING
        filtered_data.append(adjusted)
    elif temp < OPERATIONAL_FLOOR:
        normalized = abs(temp - OPERATIONAL_FLOOR)
        filtered_data.append(normalized // 2)

# Another decoy: bit manipulation on checksum
checksum = validate_checksum(raw_readings)
masked_checksum = (checksum << 3) & 0xFF
inverted = (~masked_checksum) & 0xFF

# Auxiliary transformation: reverse accumulation
accumulated = []
cumulative = 0
for i in range(len(filtered_data) - 1, -1, -1):  # Reverse order
    cumulative += filtered_data[i]
    accumulated.append(cumulative)

# Real processing function (looks similar to decoys)
def process_readings(data, limit):
    if not data:
        return 0
    # Apply limit as divisor in summation
    transformed = []
    for val in data:
        # Integer division and modular arithmetic
        step1 = (val + limit) // 2
        step2 = (step1 * 3) % 100
        transformed.append(step2)
    
    # Summation with rounding
    total = sum(transformed)
    if total > 150:
        total = round(total * 0.75)
    else:
        total = round(total * 1.1)
    
    # Set operation side-channel (irrelevant)
    flags = {f'F{x}' for x in transformed if x > 20}
    flag_count = len(flags)  # Not used in output
    
    return total + flag_count  # Subtle but consistent

# Key statement
final_diagnostic = process_readings(filtered_data, threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")