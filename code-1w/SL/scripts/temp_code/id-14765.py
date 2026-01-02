import itertools

def calculate_turbulence(sequence):
    turbulence = 0
    for a, b in itertools.pairwise(sequence):
        turbulence += abs(a - b)
    return turbulence

def analyze_pattern(data):
    if len(data) < 3:
        return 0
    peak_count = 0
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] > data[i+1]:
            peak_count += 1
    return peak_count

def adjust_flux(flux, mode):
    # Core adjustment logic
    modifier = 1.75 if mode == 'HIGH' else 0.85
    flux = flux * modifier
    
    # Distractor: irrelevant intermediate calculation
    temp_buffer = [flux * (i % 3 + 1) for i in range(5)]
    avg_temp = sum(temp_buffer) / len(temp_buffer)
    
    # More distraction: unused state tracking
    status_log = {}
    for step in range(3):
        status_log[f'step_{step}'] = f'active'
    
    # Actual meaningful adjustment
    if flux > 100:
        flux -= 23
    elif flux < 50:
        flux += 15
    
    # Dead code path (never executed due to prior conditions)
    if 50 <= flux <= 50:
        flux *= 1.1
    
    return int(flux)

# Main execution flow
readings = [12, 45, 23, 67, 34, 78]
base_turbulence = calculate_turbulence(readings)
peak_analysis = analyze_pattern(readings)

# Irrelevant transformation chain
shifted = [x + 10 for x in readings]
doubled = [x * 2 for x in shifted]
compressed = [val for val in doubled if val > 50]

# Core variables for final computation
base_flux = base_turbulence + len(readings)
mode_flag = 'HIGH' if peak_analysis > 1 else 'LOW'

# Key statement
final_flux = adjust_flux(base_flux, mode_flag)

# Print result as required
print(f"Result: {final_flux}")