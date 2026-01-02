import math

# Simulated sensor array data (real and decoy)
sensor_ids = [f'SEN-{i}' for i in range(1, 21)]
raw_readings = [3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 399, 440]

# Irrelevant transformation: frequency mapping (distractor)
frequency_map = {sid: (i * 1.07) for i, sid in enumerate(sensor_ids)}
doppler_shift = lambda x: sum([math.sin(x/10) * 1.5 for _ in range(2)])

# Decoy function: unused but plausible
def calibrate_sensor(signal, factor=0.98):
    return [s * factor for s in signal]

# Real preprocessing with distractors embedded
def preprocess_signal(data):
    # Step 1: Apply offset correction (only odd-indexed matter)
    corrected = []
    for i, val in enumerate(data):
        if i % 2 == 1:
            adjusted = val + 2 * i
            corrected.append(adjusted)
        else:
            # Dead path: even indices are ignored
            fake_adjust = val * 0.95 + 10
            continue
    
    # Step 2: Filter anomalies using modulo pattern (relevant)
    filtered = [x for x in corrected if x % 4 == 0]
    
    # Step 3: Scale down by index-derived factor (relevant)
    scaled = [int(x / (2 + i)) for i, x in enumerate(filtered)]
    
    # Distractor: entropy calculation (unused)
    entropy = sum([-p * math.log(p) for p in [0.1, 0.2, 0.3, 0.4] if p > 0])
    
    return scaled

# Secondary processing with zip and enumerate (required python features)
def extract_patterns(sequence):
    indexed = list(enumerate(sequence))
    paired = zip(indexed[:-1], indexed[1:])
    deltas = []
    for (i, a), (j, b) in paired:
        delta = b - a
        if delta > 0:
            # Only forward increments
            deltas.append(delta)
    return deltas

# Core analysis logic
processed_signals = preprocess_signal(raw_readings)
pattern_deltas = extract_patterns(processed_signals)

# Misleading accumulation (decoy)
total_drift = 0
for d in pattern_deltas:
    total_drift += d * 0.75
    if total_drift > 100:
        total_drift -= 50  # Artificial cap (irrelevant)

# Real diagnostic computation
baseline = sum(processed_signals[:3])
variation = sum([abs(pattern_deltas[i] - pattern_deltas[i-1]) for i in range(1, len(pattern_deltas))])

# Critical red herring: checksum that looks important but isn't used
checksum = 0
for i, v in enumerate(processed_signals):
    checksum ^= (v + i * 3) & 0xFF

# Lambda-based normalization (actual use)
normalize = lambda x: round(x / 1.75, 3)
norm_variation = normalize(variation)

# Final analysis function
def analyze_readings(clean_data):
    # Composite metric based on growth rate
    if len(clean_data) < 3:
        return -1
    
    # Calculate quadratic trend coefficient (a in ax^2 + bx + c)
    n = len(clean_data)
    sx, sy, sxy, sx2, sx3, sx4, syx2 = 0, 0, 0, 0, 0, 0, 0
    for i in range(n):
        x = i
        y = clean_data[i]
        sx += x
        sy += y
        sxy += x * y
        sx2 += x**2
        sx3 += x**3
        sx4 += x**4
        syx2 += y * x**2
    
    # Solve normal equations for quadratic fit
    A = [[n, sx, sx2],
         [sx, sx2, sx3],
         [sx2, sx3, sx4]]
    B = [sy, sxy, syx2]
    
    # Manual 3x3 system solve (no external libs)
    detA = (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) -
            A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) +
            A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))
    
    if abs(detA) < 1e-10:
        return 0
    
    # Cramer's rule for coefficient 'a' (quadratic term)
    A_a = [[B[0], A[0][1], A[0][2]],
           [B[1], A[1][1], A[1][2]],
           [B[2], A[2][1], A[2][2]]]
    detA_a = (A_a[0][0]*(A_a[1][1]*A_a[2][2] - A_a[1][2]*A_a[2][1]) -
              A_a[0][1]*(A_a[1][0]*A_a[2][2] - A_a[1][2]*A_a[2][0]) +
              A_a[0][2]*(A_a[1][0]*A_a[2][1] - A_a[1][1]*A_a[2][0]))
    
    quadratic_coeff = detA_a / detA
    
    # Final diagnostic combines quadratic trend and normalized variation
    result = int((abs(quadratic_coeff) * 1000) + norm_variation)
    return result

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Print target result
print(f"Target result: {final_diagnostic}")