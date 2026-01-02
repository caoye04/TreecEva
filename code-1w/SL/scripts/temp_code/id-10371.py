from collections import defaultdict, Counter
import math

# Simulated sensor readings and system parameters
sensor_data = [144, 25, 36, 49, 121, 81, 169, 100]
calibration_matrix = [2, 3, 1, 4, 2, 3, 1, 4]
system_flags = [True, False, True, True, False, True, False, True]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H3']
temporal_weights = {i: round(math.sin(i * 0.5), 3) for i in range(8)}
baseline_offsets = defaultdict(lambda: 0.0)
for i in range(8):
    baseline_offsets[i] = round(math.cos(i * 0.3), 3)

# Misleading preprocessing path (dead code - not used)
def legacy_transform(values):
    """Incorrect transformation path - irrelevant"""
    return [v ** 0.25 for v in values if v > 30]

# Unused diagnostic function (decoy)
def compute_health_score(flags):
    count = 0
    for f in flags:
        if f:
            count += 2
        else:
            count -= 1
    return max(count, 0)

# Another red herring: frequency analysis on codes (irrelevant)
code_frequency = Counter([c[0] for c in legacy_codes])
letter_ranking = sorted(code_frequency.items(), key=lambda x: x[1], reverse=True)

# Real processing begins here — complex but focused logic
def analyze_squareness(val):
    """Check if number is perfect square and return diagnostic score"""
    root = int(math.sqrt(val))
    if root * root == val:
        return 10 + root  # bonus for being perfect square
    else:
        return -5

def apply_calibration(value, factor, flag):
    """Apply conditional calibration based on system flag"""
    if flag:
        adjusted = value * (factor ** 0.5)
    else:
        adjusted = value * 0.9
    return int(round(adjusted))

def filter_outliers(data_list):
    """Remove values beyond 1.5 IQR (not actually triggered in execution)"""
    sorted_vals = sorted(data_list)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [v for v in data_list if lower_bound <= v <= upper_bound]

# Key processing function with nested logic
def process_readings(readings, matrix):
    temp_results = []
    diagnostic_trace = defaultdict(int)
    
    for idx, (val, fac) in enumerate(zip(readings, matrix)):
        # Step 1: Analyze intrinsic property
        sq_score = analyze_squareness(val)
        diagnostic_trace[f'sq_{idx}'] = sq_score
        
        # Step 2: Apply context-sensitive calibration
        calibrated = apply_calibration(val, fac, system_flags[idx])
        
        # Step 3: Accumulate transformed result with offset (baseline unused)
        shifted = calibrated + int(baseline_offsets[idx])
        
        # Step 4: Conditional boost based on legacy code pattern (never activates)
        if idx < len(legacy_codes) and legacy_codes[idx][0] in ['X', 'Z']:
            shifted *= 1.1
        
        # Step 5: Aggregate meaningful signal
        entropy_component = math.log(max(shifted, 1))
        temp_results.append(int(round(entropy_component * (sq_score + 10))))
    
    # Step 6: Summation of processed diagnostics
    total_signal = sum(temp_results)
    
    # Step 7: Normalize using non-outlier path (filter_outliers not called)
    normalized = total_signal // 3
    
    # Step 8: Final adjustment using mathematical identity check
    if math.isclose(math.sqrt(normalized), int(math.sqrt(normalized)), abs_tol=1e-5):
        final_adjust = 7
    else:
        final_adjust = 13
    
    # Final computation
    return normalized + final_adjust

# Execution point of interest
final_diagnostic = process_readings(sensor_data, calibration_matrix)

# Print result as required
print(f"Target result: {final_diagnostic}")