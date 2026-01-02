import math

# Simulated sensor data and configuration (realistic domain: IoT signal processing)
sensor_readings = [
    (1, 142.5, 'active'), (2, 148.0, 'idle'), (3, 139.8, 'active'),
    (4, 140.1, 'active'), (5, 152.3, 'overload'), (6, 137.9, 'active'),
    (7, 145.2, 'active'), (8, 150.8, 'overload'), (9, 136.5, 'active'),
    (10, 141.7, 'active')
]

# Irrelevant auxiliary data — distractor
temp_history = [22.1, 22.3, 21.9, 22.5, 23.0, 22.8, 22.7, 23.1, 23.3, 23.4]
pressure_levels = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1019, 1020, 1018]

# Configuration with misleading fields — red herring
class Config:
    def __init__(self):
        self.threshold = 140.0
        self.sensitivity = 'high'
        self.calibration_offset = 2.5  # unused in logic
        self.max_records = 100
        self.debug_mode = True  # never used
        self.noise_filter = lambda x: x * 0.98  # decoy function

config = Config()

# Decoy functions — dead code paths
def legacy_calibrate(data):
    return [x + 1.2 for x in data if x > 100]  # unused

def validate_checksum(records):
    total = 0
    for r in records:
        total += r[0] * 3
    return total % 7 == 0  # computed but not used

# Distractor computation
validate_checksum(sensor_readings)

# Real processing begins here
status_map = {'active': 1, 'idle': 0, 'overload': -1}

# Extract numeric values and map status using enumerate and zip
indices, values, statuses = zip(*[(i, r[1], r[2]) for i, r in enumerate(sensor_readings)])
numeric_statuses = [status_map[s] for s in statuses]

# Filter only active signals — key filtering step
active_mask = [s == 'active' for s in statuses]
filtered_data = [values[i] for i in range(len(values)) if active_mask[i]]

# Misleading intermediate transformation — looks important but unused
smoothed_data = list(map(lambda x: round(x, 1), filtered_data))
baseline_avg = sum(smoothed_data) / len(smoothed_data) if smoothed_data else 0  # looks critical

# Unused statistical decoys
variance_proxy = sum((x - baseline_avg) ** 2 for x in smoothed_data) / len(smoothed_data) if smoothed_data else 0
deviation_flag = variance_proxy > 5.0  # calculated but irrelevant

# Core logic: detect anomalies above threshold within filtered active data
anomalies = [x for x in filtered_data if x > config.threshold]

# Count corrections needed — real path
correction_count = len(anomalies)

# Apply fake calibration that does nothing
def apply_offset(batch, offset=0.0):
    return [val + offset for val in batch]  # never called

# Real processing function with nested logic and lambda
process_signals = lambda data, cfg: (
    sum(  
        [int(val // 10) for val in data if val > cfg.threshold]  
    ) * 2 
    + ( 
        # Nested expression with integer division and rounding
        len(data) // 2 
        if len(data) > 3 
        else 0 
    ) 
    - ( 
        # Bit manipulation red herring: looks complex but neutral effect
        (len([v for v in data if v < 140]) << 1) >> 1  
    )
)

# Critical execution point
final_output = process_signals(filtered_data, config)

# Output result as required
print(f"Target result: {final_output}")