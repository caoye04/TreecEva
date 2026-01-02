import math

# Simulated sensor array and calibration constants
def get_sensor_data():
    raw = [0.1, 0.3, 0.5, 0.9, 1.2, 1.8, 2.1, 2.5]
    offset = 0.05
    calibrated = [round(x + offset, 2) for x in raw]
    return calibrated

# Irrelevant auxiliary function - decoy
def analyze_pattern(seq):
    if len(seq) < 5:
        return False
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    return all(d > 0 for d in diffs)

# Unused transformation chain - red herring
transform_chain = [
    lambda x: x ** 2,
    lambda x: x + 1 if x < 1 else x - 1,
    lambda x: abs(x)
]

# Misleading intermediate processing (dead path)
system_flags = {
    'debug': False,
    'legacy_mode': True,
    'emulation_active': False
}

if system_flags['debug']:
    print("Debug mode active - skipping validation")
elif system_flags['legacy_mode']:
    temp_buffer = [math.sin(x) for x in range(10)]
    # This block runs but doesn't contribute to final result
    checksum = sum(temp_buffer) % 7

# Core logic disguised among distractions
def system_status(condition_checker):
    def evaluator(data_stream):
        nonlocal condition_checker
        count_met = 0
        total_samples = len(data_stream)
        
        # Bitwise analysis of sample indices - relevant but obscured
        for i, value in enumerate(data_stream):
            index_flag = i & 3  # Every 4th pattern
            if index_flag == 0:
                # Only process every 4th element starting from 0
                transformed = value * 2.5
                if condition_checker(transformed):
                    count_met += 1
            elif index_flag == 2:
                # Decoy operation with side effect that does nothing
                _ = math.floor(value) ^ 1
        
        # Hidden weighting mechanism
        weight = 3 if count_met >= 2 else 1
        return count_met * weight
    return evaluator

# Secondary irrelevant computation - distractor
aggregation_modes = ['avg', 'max', 'sum']
mode_weights = {m: len(m) for m in aggregation_modes}
scaling_factor = sum(mode_weights.values()) / len(mode_weights)

# Threshold defined via complex expression - looks arbitrary but used
base_ref = 4.0
adjustment = math.log(8, 2)  # evaluates to 3
threshold = base_ref - adjustment + 0.5  # threshold = 1.5

# Sensor data acquisition
sensor_data = get_sensor_data()  # [0.15, 0.35, ..., 2.55]

# Spurious list comprehension - no side effects
_ = [x for x in sensor_data if x < 1.0 and x * 10 % 2 == 0]

# Critical execution point
final_diagnostic = system_status(lambda x: x > threshold)(sensor_data)

# Output required format
print(f"Result: {final_diagnostic}")