from collections import defaultdict, Counter
import math

# Simulated sensor array data from quantum subsystems
turbine_phases = [1.2, 0.8, 1.5, 0.9, 1.1]
thermal_flux = [210, 215, 198, 220, 212]
quantum_readings = [0b1101, 0b1010, 0b1111, 0b0101, 0b1001]

# Irrelevant environmental telemetry (distractor data)
atmospheric_pressure = 1013.25
humidity_levels = [45, 50, 60, 55, 40]
wavelength_cache = {i: 3e8 / (500e-9 * i) for i in range(1, 6)}

# System calibration parameters
calibration_offset = 0b1010
baseline_threshold = sum(turbine_phases) / len(turbine_phases)
noise_floor = max(thermal_flux) - min(thermal_flux)

# Misleading diagnostic routine (never called)
def legacy_diagnostic(seq):
    return sum(x ^ 7 for x in seq[:3]) % 100

# Auxiliary transformation map (partially used)
phase_map = defaultdict(int)
for i, val in enumerate(turbine_phases):
    phase_map[f'phase_{i}'] = int(val * 10) + (calibration_offset & 0b11)

# Decoy statistical summary (unused in final calculation)
stats_summary = {
    'mean_flux': sum(thermal_flux) / len(thermal_flux),
    'median_flux': sorted(thermal_flux)[len(thermal_flux)//2],
    'mode_phase': Counter([round(x) for x in turbine_phases]).most_common(1)[0][0]
}

# Signal harmonics analysis (red herring computation)
harmonics = []
for reading in quantum_readings:
    bit_reversed = int(bin(reading)[:1:-1], 2)  # reverse bits
    harmonics.append((bit_reversed ^ calibration_offset) % 16)

# Secondary processing chain with conditional branching
event_counter = defaultdict(lambda: 0)
trigger_flags = []
for i, flux in enumerate(thermal_flux):
    if flux > stats_summary['mean_flux']:
        event_counter['high_flux'] += 1
        trigger_flags.append(True)
    else:
        event_counter['stable'] += 1
        trigger_flags.append(False)

# Core analysis function with nested logic and distractors
def analyze_system_state(readings, offset):
    cumulative = 0
    adjustment_factor = 1.0
    
    # Process each quantum reading with bit manipulation
    for i, val in enumerate(readings):
        # Relevant bitwise interaction
        masked_val = val & offset
        flipped = val ^ 0b1111  # inverse all bits
        
        # Conditional path that affects result
        if i % 2 == 0 and masked_val > 0:
            # Key computational branch
            temp_score = (flipped << 1) | (masked_val & 0b1)
            cumulative += temp_score * (i + 1)
        else:
            # Dead code path - misleading but harmless
            dummy = (val | offset) >> 2
            adjustment_factor *= 0.95  # never used
    
    # Critical aggregation using collections.Counter
    freq = Counter(readings)
    most_common_val, count = freq.most_common(1)[0]
    
    # Final computation combining multiple concepts
    base_result = cumulative + (most_common_val ^ offset)
    
    # Normalize using system baseline (distraction: uses turbine data)
    phase_weight = sum(phase_map.values()) // len(phase_map)
    normalized = base_result - (phase_weight & 0xFF)  # only lower byte used
    
    # Final adjustment based on logical conditions
    flag_state = any(trigger_flags[-2:]) and not all(trigger_flags)
    correction = 25 if flag_state else -25
    
    return normalized + correction

# Execute primary diagnostic chain
diag_1 = analyze_system_state(quantum_readings[:3], calibration_offset)
diag_2 = analyze_system_state(quantum_readings[2:], calibration_offset)

# Final integrated diagnostic (target execution point)
final_diagnostic = analyze_system_state(quantum_readings, calibration_offset)

print(f"Result: {final_diagnostic}")