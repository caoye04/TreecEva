import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8]
humidity_readings = [55.2, 58.7, 61.3, 59.0, 53.8, 50.1, 52.6]
pressure_readings = [1013, 1011, 1009, 1015, 1020, 1022, 1018]

# Irrelevant auxiliary arrays (distractor)
color_codes = ['FF0000', '00FF00', '0000FF', 'FFFF00', 'FF00FF', '00FFFF', 'FFFFFF']
station_names = ['North Ridge', 'East Valley', 'West Bluff', 'South Peak', 'Central Mesa', 'Upper Pass', 'Lower Glen']

# Misleading preprocessing path (dead code path)
def legacy_normalization(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]  # Never actually used

# Unused transformation function (decoy)
def fourier_approximation(signal):
    result = []
    for k in range(len(signal)):
        acc = 0
        for n, x in enumerate(signal):
            angle = 2 * math.pi * k * n / len(signal)
            acc += x * (math.cos(angle) + 1j * math.sin(angle))
        result.append(acc)
    return result  # Computed but not used anywhere

# Signal processing with red herrings
def enhance_signal(raw_signal):
    filtered = []
    threshold = sum(raw_signal) / len(raw_signal)
    
    # Distractor: complex bit manipulation with no real effect on logic
    magic_seed = 0b101010
    for i, val in enumerate(raw_signal):
        if i % 2 == 0:
            perturbed = val ^ (magic_seed & 0b111)  # Bitwise XOR distraction
        else:
            perturbed = val | (magic_seed >> 2)       # Bitwise OR distraction
        
        # Actual relevant transformation
        enhanced_val = val * math.log(2 + i) if val > 0 else val
        filtered.append(round(enhanced_val, 3))
    
    return filtered

# Redundant sorting operations (misleading intermediate results)
sorted_temp_indices = sorted(range(len(temperature_readings)), key=lambda i: temperature_readings[i])
sorted_humid_indices = sorted(range(len(humidity_readings)), key=lambda i: humidity_readings[i], reverse=True)

# Real signal chain begins here
raw_signals = [temperature_readings, humidity_readings]
processed_signals = []

for idx, sig in enumerate(raw_signals):
    amplified = [x * 1.5 for x in sig]
    shifted = [x + 5 for x in amplified]  # Offset applied
    processed = enhance_signal(shifted)
    processed_signals.append(processed)

# Decoy container with unused computations
snapshot_log = {}
for i, (temp, humid) in enumerate(zip(temperature_readings, humidity_readings)):
    heat_index = temp + 0.5 * humid  # Plausible but unused metric
    dew_point = temp - ((100 - humid) / 5)  # Another plausible but irrelevant calculation
    snapshot_log[station_names[i]] = {
        'heat_index': round(heat_index, 2),
        'dew_point': round(dew_point, 2),
        'color': color_codes[i]
    }

# Core analysis function with conditional logic and enumeration
def analyze_metrics(signals):
    combined_score = 0.0
    
    for signal_idx, sig in enumerate(signals):
        local_maxima = 0
        trend_bias = 0
        
        # Analyze trend using enumeration
        for i, val in enumerate(sig):
            if i > 0 and val > sig[i-1]:
                trend_bias += 1
            elif i > 0 and val < sig[i-1]:
                trend_bias -= 1
            
            # Detect peaks
            if 0 < i < len(sig)-1 and sig[i-1] < val > sig[i+1]:
                local_maxima += 1
        
        # Conditional scoring logic
        if signal_idx == 0:
            contribution = trend_bias * 1.8
        elif signal_idx == 1:
            contribution = local_maxima * 4.2
        else:
            contribution = 0  # Dead branch
        
        combined_score += contribution
    
    # Final nonlinear transformation (critical path)
    if combined_score != 0:
        final_adjustment = math.sin(combined_score / 10) * math.sqrt(abs(combined_score))
    else:
        final_adjustment = 0
    
    return round(final_adjustment, 6)

# Key execution point
final_diagnostic = analyze_metrics(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")