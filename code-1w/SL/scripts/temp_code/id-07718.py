import math

# Sensor simulation and analysis system for environmental monitoring

def generate_noise(length, seed=42):
    # Irrelevant function: generates noise but not used in final computation
    result = []
    val = seed
    for i in range(length):
        val = (val * 937) % 10007
        result.append(val)
    return result

def collect_raw_readings():
    # Simulate raw sensor inputs (temperature, pressure, humidity)
    return [
        (23.5, 101.3, 45.0),
        (24.1, 101.5, 47.2),
        (19.8, 100.9, 53.1),
        (26.7, 102.1, 39.8),
        (22.4, 101.0, 48.5)
    ]

def filter_outliers(data, threshold=3.0):
    # Irrelevant filtering logic — data has no outliers
    mean_temp = sum(x[0] for x in data) / len(data)
    filtered = [x for x in data if abs(x[0] - mean_temp) < threshold]
    return filtered or data  # fallback

def compute_dew_point(temp, humidity):
    # Helper to compute dew point from temp and humidity
    a, b = 17.27, 237.7
    alpha = ((a * temp) / (b + temp)) + math.log(humidity / 100.0)
    return (b * alpha) / (a - alpha)

def process_environmental_data(raw_readings):
    # Main processing pipeline with distractors
    temps = [r[0] for r in raw_readings]
    pressures = [r[1] for r in raw_readings]
    humidities = [r[2] for r in raw_readings]
    
    # Distractor: unused derived metrics
    avg_pressure = sum(pressures) / len(pressures)
    max_humidity = max(humidities)
    pressure_deviation = [(p - avg_pressure) ** 2 for p in pressures]
    total_variance = sum(pressure_deviation)
    
    # Relevant transformation: compute adjusted temperature index
    adjusted_temps = []
    for t, h in zip(temps, humidities):
        dew = compute_dew_point(t, h)
        adjustment = 0.6 * (t - dew)  # heat index approximation
        adjusted_temps.append(t + adjustment)
    
    # Distractor: dead-end signal smoothing (not used later)
    smoothed = []
    for i in range(len(adjusted_temps)):
        left = max(0, i-1)
        right = min(i+2, len(adjusted_temps))
        smoothed.append(sum(adjusted_temps[left:right]) / (right - left))
    
    # Key transformation: apply non-linear gain only to original temps
    amplified = list(map(lambda x: x * 1.08 + 2.1, temps))
    
    # Return processed signals including red herrings
    return {
        'amplified_temps': amplified,
        'smoothed_adjusted': smoothed,
        'raw_dew_points': [compute_dew_point(t, h) for t, h in zip(temps, humidities)],
        'control_checksum': sum(int(t) for t in temps) * 100  # misleading metric
    }

def extract_frequency_components(signal):
    # Fake FFT-like decomposition — irrelevant
    n = len(signal)
    components = []
    for k in range(n//2):
        comp = sum(signal[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        components.append(abs(comp))
    return components

def validate_signal_integrity(amplified_temps):
    # Distractor validation that isn't actually checked
    total = 0
    for val in amplified_temps:
        if val > 30:
            total += val * 0.1
        elif val < 20:
            total -= val * 0.05
    return total

def analyze_readings(processed_signals):
    # Critical function: computes final diagnostic score
    amplified = processed_signals['amplified_temps']
    checksum = processed_signals['control_checksum']  # decoy value
    
    # Real computation path
    base_score = 0
    for idx, temp in enumerate(amplified):
        # Weight by position using enumerate
        weight = 1 + (idx * 0.1)
        contribution = temp * weight
        base_score += contribution
    
    # Apply correction based on unused frequency analysis (misleading call)
    freqs = extract_frequency_components(amplified)
    if freqs:  # always true
        base_score -= sum(freqs[:2]) * 0.01  # minor reduction, still deterministic
    
    # Final adjustment using lambda-based normalization
    normalize = lambda x: round(x, 3)
    final_score = normalize(base_score)
    
    # Dead code paths below
    if final_score < 0:
        final_score = 0
    elif final_score > 1e6:
        final_score = 1e6
        
    return final_score

# Execution flow
raw_data = collect_raw_readings()
denoised_data = filter_outliers(raw_data)
processed_signals = process_environmental_data(denoised_data)
final_diagnostic = analyze_readings(processed_signals)
print(f"Target result: {final_diagnostic}")