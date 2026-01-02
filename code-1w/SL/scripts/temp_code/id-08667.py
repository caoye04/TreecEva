import math

# Simulated sensor data processing pipeline for environmental monitoring
raw_readings = [14.2, -5.3, 9.8, 23.1, -0.5, 17.9, 3.4, -2.2]
offset_calibration = 1.7
filter_threshold = 10.0
time_weights = [0.8, 1.1, 0.9, 1.2, 1.0, 1.3, 0.7, 1.4]

# Irrelevant auxiliary arrays (distractor)
legacy_codes = [0xAB, 0xCD, 0xEF, 0x10, 0x2B]
system_flags = {"debug": True, "safe_mode": False, "logging": 'verbose'}
buffer_cache = [[1, 2], [3, 4], [5, 6]]  # Unused

# Misleading pre-processing step with dead logic
adjusted_readings = []
for val in raw_readings:
    if val > filter_threshold:
        adjusted_readings.append(val * 1.1)
    elif val < -filter_threshold:
        adjusted_readings.append(val * 0.9)  # Never reached
    else:
        adjusted_readings.append(val + offset_calibration)

# Decoy transformation function (never called)
def legacy_transform(x):
    return [math.sin(z) * 0.5 for z in x if z > 0]  # Distractor logic

# Real transformation using list comprehension and conditional expression
transformed_data = [
    (x + offset_calibration) * w if i % 2 == 0 else (x * 1.1) * w
    for i, (x, w) in enumerate(zip(raw_readings, time_weights))
]

# Bitwise decoy computation (irrelevant)
checksum = 0
for code in legacy_codes:
    checksum ^= code
    checksum &= 0xFF

# Configuration object with red herring fields
class Config:
    def __init__(self):
        self.debug_trace = True
        self.max_iterations = 15
        self.use_enhanced = False
        self.threshold = 5.0  # Misleading: not used in final calculation
        self.scale_factor = 1.6  # Actually used below

config = Config()

# Auxiliary helper (looks important but only one part matters)
def smooth_data(seq, factor):
    return [math.cos(x) * factor for x in seq]  # Unused path

def aggregate_metrics(data, cfg):
    base_sum = sum(data)
    
    # Apply scale from config
    scaled = base_sum * cfg.scale_factor
n    
    # Fake complex adjustment with unused branches
    adjustment = 0
    if len(data) > 10:
        adjustment = math.log(len(data))
    elif len(data) == 8:
        adjustment = 0.4  # Hidden relevant constant
    else:
        adjustment = -0.1
        
    # Additional fake signal processing
    fft_sim = sum([data[i] * (-1)**i for i in range(len(data))])  # Computed but unused
    
    # Critical line: inject adjustment based on length condition
    intermediate = scaled + adjustment
    
    # Final non-linear correction using lambda and conditional
    non_linear = (lambda x: x * 1.05 if x > 100 else x * 0.95)(intermediate)
    
    # Dead branch based on unreachable flag
    if cfg.debug_trace and False:  # Always skipped
        non_linear -= 10
        
    return non_linear

# Key execution point
final_diagnostic = aggregate_metrics(transformed_data, config)

# Print result as required
print(f"Result: {final_diagnostic}")