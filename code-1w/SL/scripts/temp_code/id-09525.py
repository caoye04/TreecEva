import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(x):
    return sum([i * 2 for i in x if i > 5])

# Decoy signal processing chain
def legacy_filter(data):
    return [d ** 0.5 for d in data if d % 2 == 0]

# Real transformation pipeline
def clean_noise(val, factor=0.9):
    return val * factor if val > 10 else val * 1.1

def apply_window(signal, window_type='hann'):
    size = len(signal)
    if window_type == 'hann':
        return [signal[i] * (0.5 - 0.5 * math.cos(2 * math.pi * i / (size - 1))) for i in range(size)]
    return signal

# Complex conditional logic with early returns
def classify_magnitude(x):
    if x < 0:
        return 'negative'
    elif x < 10:
        return 'low'
    elif x < 50:
        return 'medium'
    else:
        return 'high'

# Bit manipulation red herring
def obfuscate_index(i, key=0xABCDEF):
    shifted = (i << 3) & 0xFFFF
    return shifted ^ key

# Main processing core
initial_samples = [12, 18, 25, 8, 33, 41, 7]
offset_correction = 3

# Step 1: Apply baseline correction (irrelevant to final result but looks important)
corrected_data = [s + offset_correction for s in initial_samples]

# Step 2: Filter out low values — only values >= 20 are kept
filtered_data = [v for v in corrected_data if v >= 20]

# Step 3: Clean noise using multiplicative factor
noisy_metric = sum(filtered_data) / len(filtered_data) if filtered_data else 0
denoised_values = [clean_noise(v) for v in filtered_data]

# Step 4: Apply Hann window (actual effect on computation)
windowed_data = apply_window(denoised_values, 'hann')

# Step 5: Transform via lambda-based mapping (critical step)
power_boost = lambda x: x ** 1.5 if classify_magnitude(x) == 'medium' else x ** 0.8
transformed_data = tuple(power_boost(w) for w in windowed_data)

# Step 6: Define thresholding logic using closure (looks complex, only one branch matters)
def make_threshold_ref(base):
    dynamic_adj = base * 0.1
    def check(val):
        if val < base - dynamic_adj:
            return False
        if val > base * 2:
            # Dead condition — never reached due to data range
            temp_buf = [val >> i for i in range(3)]
            return sum(temp_buf) % 2 == 0
        return True  # Only this line matters
    return check

threshold_func = make_threshold_ref(15.0)

# Step 7: Process signal with conditional aggregation
def process_signal(data, threshold):
    total = 0.0
    count = 0
    for val in data:
        raw_int = int(val)
        # Bitwise decoy
        masked = raw_int ^ 0xFF
        inverted = ((masked >> 1) | (masked << 7)) & 0xFF
        
        # Only this condition contributes
        if threshold(val):
            total += val * 0.95
            count += 1
        else:
            # Unused path with misleading calculation
            debug_val = math.log(abs(val) + 1)
            continue
    
    # Early return red herring
    if count == 0:
        return -999.0

    avg_contrib = total / count if count else 0

    # Final adjustment using integer division and rounding
    scale_factor = 2
    scaled = avg_contrib * scale_factor
    final_shift = int(scaled) // 3  # Integer division side effect
    
    return round(scaled - final_shift, 6)

# Execution point of interest
final_output = process_signal(transformed_data, threshold_func)

# Print result as required
print(f"Target result: {final_output}")