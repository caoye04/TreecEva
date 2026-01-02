import math

# Simulated sensor data from agricultural fields
temperature_readings = [23.4, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [61, 58, 65, 54, 50, 59, 62]
soil_moisture_levels = [310, 330, 280, 360, 400, 320, 305]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.87
CALIBRATION_OFFSET_B = -1.02
REFERENCE_VOLTAGE = 5.0

# Decoy function - appears useful but unused in critical path
def calibrate_sensor(raw_value, offset):
    return raw_value * 1.05 + offset

# Data processing pipeline
processed_data = []
aggregated_metrics = {}

# Bit manipulation for data encoding (redundant but plausible)
def encode_moisture_level(level):
    encoded = (level << 2) ^ 0b1101
    return encoded & 0xFFFF

# Misleading intermediate transformation (not used in final result)
encoded_values = [encode_moisture_level(level) for level in soil_moisture_levels]

# Real processing begins: filter anomalous readings
valid_entries = []
for i in range(len(temperature_readings)):
    temp = temperature_readings[i]
    humidity = humidity_readings[i]
    moisture = soil_moisture_levels[i]
    
    # Valid condition: moderate temp, decent humidity, sufficient moisture
    is_valid = (22 <= temp <= 26) and (humidity > 52) and (moisture > 290)
    if is_valid:
        valid_entries.append((temp, humidity, moisture))

# Compute derived indices
normalized_indices = []
for temp, hum, moist in valid_entries:
    # Crop health index: combination of environmental factors
    chi = (temp - 22) * 0.3 + (hum - 50) * 0.2 + (moist / 10 - 25) * 0.5
    normalized_indices.append(round(chi, 4))

# Lambda-based transformation chain (core logic)
data_enhancer = lambda x: x ** 2 if x > 4 else x + 1.5
enhanced_indices = list(map(data_enhancer, normalized_indices))

# Slicing to exclude potential outlier (first entry suspected)
effective_indices = enhanced_indices[1:]

# Aggregate using string-based key generation (plausible but indirect)
key_parts = ['yield', 'factor']
metric_key = ''.join(key_parts).upper() + '_AVG'

aggregated_metrics[metric_key] = sum(effective_indices) / len(effective_indices) if effective_indices else 0

# Secondary decoy structure (unused)
class ClimateBuffer:
    def __init__(self, size=5):
        self.data = [0] * size
    
    def update(self, val):
        self.data.pop(0)
        self.data.append(val)

buffer = ClimateBuffer()
for v in temperature_readings:
    buffer.update(v)  # Dead code path

# Harvesting logic depends on conditional expression chain
intermediate_yield = 0
if aggregated_metrics['YIELDFactor_AVG'] > 5:
    intermediate_yield = aggregated_metrics['YIELDFactor_AVG'] * 120
elif aggregated_metrics['YIELDFactor_AVG'] > 3:
    intermediate_yield = aggregated_metrics['YIELDFactor_AVG'] * 85
else:
    intermediate_yield = aggregated_metrics['YIELDFactor_AVG'] * 60

# Final adjustment based on bitwise safety check (actual use)
def safe_adjust(value, flag_code):
    if (flag_code & 0b1010) == 0b1000:  # Specific bit pattern required
        return value * 1.1
    return value

# Determine flag from length of valid entries (subtle but deterministic)
flag_input = len(valid_entries) << 1
adjusted_yield = safe_adjust(intermediate_yield, flag_input)

# Final yield calculation
final_yield = adjusted_yield

# Additional red herring: string slicing on numeric conversion
yield_str = f"Yield_{final_yield:.2f}_Est"
truncated_tag = yield_str[5:-5]  # Looks meaningful but unused

# Print final result as required
print(f"Result: {final_yield}")