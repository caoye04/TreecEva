def analyze_pattern(sequence, threshold=0.7):
    """Irrelevant pattern analysis function (dead code path)"""
    if len(sequence) == 0:
        return False
    avg = sum(sequence) / len(sequence)
    return sum(1 for x in sequence if x > avg) / len(sequence) > threshold

# Simulated sensor readings and system constants
temp_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
pressure_log = [101.3, 102.1, 100.9, 103.5, 104.0, 102.7, 101.8]
baseline_offset = 17

# Distractor: unused transformation pipeline
transform_pipeline = [
    lambda x: x * 1.01,
    lambda x: x + 0.5 if x < 24 else x - 0.3,
    lambda x: round(x, 1)
]

# Health signature derived from bit manipulation of key metrics
raw_signal = 0
for i, t in enumerate(temp_readings[:4]):
    raw_signal ^= int(t * 10) << (i % 3)

# Irrelevant set operations as distraction
unique_temps = set(int(t) for t in temp_readings)
unique_pressures = set(int(p) for p in pressure_log)
divergence_set = unique_temps.symmetric_difference(unique_pressures)
spurious_flag = len(divergence_set) > 5

# Core logic disguised among distractors
rolling_adjustment = 0
for p in pressure_log[1:4]:
    rolling_adjustment += int(p) % 7

# Decoy calculation with misleading intermediate result
phantom_index = (len(temp_readings) * baseline_offset) // 3 - 9
status_flags = {1, 2, 4, 8, 16}
active_mask = 0
for flag in sorted(status_flags, reverse=True):
    if flag <= phantom_index:
        active_mask |= flag

# Real signal processing begins
health_signature = raw_signal & 0xFFFF  # Keep lower 16 bits

# Another red herring: conditional never triggers due to data
if spurious_flag and analyze_pattern(temp_readings):
    health_signature = ~health_signature & 0xFFFF

# Actual computation chain
shift_correction = (rolling_adjustment ^ baseline_offset) % 13
health_signature = (health_signature >> 2) | ((health_signature << 14) & 0xFFFF)

# Define critical processing function
def process_metrics(sig, offset):
    # Complex transformation with modular arithmetic and integer division
    a = (sig * 3 + offset) % 97
    b = (sig + offset * 2) // 5
    c = (a ^ b) & 0xFF
    
    # Use of lambda in non-trivial context
    integrator = lambda x, y: (x + y * 2) % 64
    d = integrator(c, offset)
    
    # Conditional expression affecting final result
    e = d if (a + b) % 3 == 0 else (d * 5) % 101
    
    # Final composition using multiple steps
    f = (e * e + offset) % 89
    g = (f + (f >> 3)) & 0x7F
    return (g * 7) - 42

# Execution point of interest
final_diagnostic = process_metrics(health_signature, baseline_offset)

# Print result as required
print(f"Target result: {final_diagnostic}")