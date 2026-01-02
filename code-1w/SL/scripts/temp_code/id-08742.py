import math

# Irrelevant helper function (dead code path)
def legacy_calibrate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Unused constant (distractor)
CALIBRATION_OFFSET = 0.00314159

# Simulated sensor noise generator (red herring)
def generate_noise(level=0.01):
    return sum([level * math.sin(i) for i in range(5)])

# Core data transformation pipeline
thermal_matrix = [i * 1.5 for i in range(100) if i % 3 != 0]
contaminants = {i**2 for i in range(10, 25)}  # Set of contaminant thresholds

# Efficiency factors with multiple distractors
baseline_efficiency = 0.87
adjustment_curve = lambda x: math.log(x + 2) / (x + 1)
efficiency_factor = sum(adjustment_curve(i) for i in range(1, 6)) * baseline_efficiency

# Secondary irrelevant list comprehension
auxiliary_diagnostics = [math.cos(math.pi * j / 10) for j in range(20)]

# Main processing function with nested logic and early returns
def process_stream(data, impurities):
    if not data:
        return []
    
    # Irrelevant intermediate normalization (misleading)
    normalized = [x * 0.95 for x in data]
    
    # Key filtering logic buried among distractions
    filtered = []
    for val in normalized:
        temp = int(val)
        if temp < 10:
            continue
        elif temp > 100:
            break  # Early termination based on sorted nature
        else:
            # Check against contaminant set using set operation
            if temp not in impurities and (temp % 7 != 0):  # Additional filter
                filtered.append(val * 1.1)  # Boost valid elements
    
    # Dead code branch (never reached due to break above)
    if len(filtered) > 100:
        return [x * 1.2 for x in filtered]
        
    return filtered

# Secondary unused recursive function (decoy)
def recursive_decay(n, acc=1.0):
    if n <= 0:
        return acc
    return recursive_decay(n - 1, acc * 0.9)

# Analysis function with lambda and conditional expression
analyze_purity = lambda signal_data, factor: (
    sum(signal_data) * factor if signal_data else 0.0
)

# Misleading precomputation (irrelevant result)
phantom_diagnostic = len(auxiliary_diagnostics) * generate_noise()

# Critical execution point — answer determined here
filtration_score = analyze_purity(process_stream(thermal_matrix, contaminants), efficiency_factor)

# Final output
print(f"Result: {filtration_score}")