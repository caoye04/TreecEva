import math

# Simulated sensor fusion system for environmental monitoring
def collect_readings():
    # Real data generation
    temp_readings = [23.5, 24.1, 22.7, 25.3, 26.0]
    humidity_readings = [45, 47, 50, 44, 60]
    pressure_readings = [1013, 1012, 1015, 1010, 1008]
    
    # Irrelevant auxiliary readings (distractors)
    noise_floor = [0.1, 0.2, 0.15, 0.3, 0.25]  # unused
    calibration_offset = 0.05  # unused
    sampling_rate = 10  # unused
    
    return list(zip(temp_readings, humidity_readings, pressure_readings))

def validate_data(stream):
    valid_count = 0
    for temp, hum, pres in stream:
        if not (10 <= temp <= 50):
            continue
        if not (0 <= hum <= 100):
            continue
        if not (950 <= pres <= 1050):
            continue
        valid_count += 1
    return valid_count == len(stream)

def normalize(value, min_val, max_val):
    # Unused helper (red herring)
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def compute_thermal_index(t, h):
    # Heat index approximation
    return t + 0.55 * (6.11 * math.exp(5418 * (1/273 - 1/(273+t))) - 10)

def analyze_trend(sequence):
    # Distractor function - never called
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return sum(1 for d in diffs if d > 0)

def adjust_for_altitude(pressure, altitude=50):
    # Unused adjustment logic (dead path)
    return pressure * (1 - altitude / 44330) ** 5.255

def extract_key_metrics(dataset):
    temps = [d[0] for d in dataset]
    hums = [d[1] for d in dataset]
    presses = [d[2] for d in dataset]
    
    avg_temp = sum(temps) / len(temps)
    median_hum = sorted(hums)[len(hums)//2]
    
    # Misleading intermediate calculation (not used in final result)
    outlier_count = sum(1 for h in hums if h > 55)
    stability_score = 100 - abs(avg_temp - 24.5) * 5
    
    # Real feature: vapor pressure
    es = 6.11 * 10**(7.5 * avg_temp / (237.7 + avg_temp))
    actual_vapor_pressure = es * median_hum / 100
    
    # Tuple unpacking with meaningful and irrelevant components
    metadata = ('SITE_A', '2023-08-15', 'VALID')
    location, date, status = metadata
    
    # Conditional expression to determine correction factor
    correction = 1.05 if median_hum > 48 else 0.98
    
    # Return only relevant metrics despite extra computation
    return (avg_temp, actual_vapor_pressure, correction)

def process_results(data, weights):
    metrics = extract_key_metrics(data)
    avg_temp, vapor_press, corr = metrics
    
    # Weights: temperature sensitivity, humidity impact, pressure stability
    w1, w2, w3 = weights
    
    # Complex composite score with red herrings
    base_score = avg_temp * w1
    humidity_factor = vapor_press * w2
    
    # Bit manipulation decoy (looks sophisticated but unused)
    encoded = int(vapor_press) ^ int(avg_temp)
    checksum = (encoded >> 3) | 0xABCDE
    
    # Real calculation path
    adjusted_score = (base_score + humidity_factor) * corr
    
    # Integer division and rounding used meaningfully
    rounded_adjustment = int(adjusted_score * 1000) // 100  / 10.0
    
    # Early termination decoy (never triggers due to valid data)
    if len(data) < 3:
        return -999
    
    # Final computation
    penalty = 0
    for reading in data:
        temp, hum, _ = reading
        if hum > 55:
            penalty += 1.5
    
    final_score = rounded_adjustment - penalty
    
    # This print is NOT the target - distractor output
    print(f'Debug: vapor pressure={vapor_press:.2f}, checksum={checksum}')
    
    return final_score

# Main execution flow
data = collect_readings()

# Irrelevant preprocessing step (no effect)
sorted_data = sorted(data, key=lambda x: x[0])
filtered_data = [d for d in data if d[1] >= 40]  # not actually used

# Weight configuration (only this set matters)
weights = (3.2, 0.8, 0.4)

# Critical statement
final_score = process_results(data, weights)

# Target result output (required format)
print(f'Result: {final_score}')