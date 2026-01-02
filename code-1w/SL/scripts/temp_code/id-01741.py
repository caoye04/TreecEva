import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [0.88, -1.22, 3.14, -0.55, 2.71]
    scale_factor = 1.7
    offset = 0.3
    adjusted = [round((x + offset) * scale_factor, 4) for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function - dead code path (distractor)
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 4)

# Signal conditioning with red herring transformations
def filter_noise(signal):
    filtered = []
    noise_floor = 0.25
    amplification_curve = lambda x: math.tanh(x) + 0.1 * x
    for val in signal:
        processed = amplification_curve(abs(val))
        if processed > noise_floor:
            # Misleading intermediate transformation
            decoy_shift = (processed ** 2) % 1.3
            filtered.append(processed + 0.05)
        else:
            filtered.append(0.0)
    return filtered

# Data envelope extraction (relevant)
def extract_envelope(data):
    peak = max(data)
    avg = sum(data) / len(data)
    return {'peak': peak, 'avg': avg, 'ratio': peak / avg if avg != 0 else 0}

# Conditional signal classification (uses comparison and case conversion via string op)
def classify_signal(strength):
    if strength > 2.0:
        label = "HIGH"
    elif strength > 1.0:
        label = "MEDIUM"
    else:
        label = "LOW"
    # Distractor: meaningless case toggling
    toggled = ''.join(c.lower() if c.isupper() else c.upper() for c in label)
    return toggled.lower()  # Back to original form

# Core recursive feature extractor (simple recursion with distractors)
def recursive_moment(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 0.0
    mid = len(seq) // 2
    left_part = seq[:mid] if mid > 0 else []
    right_part = seq[mid+1:]
    center_val = seq[mid] if mid < len(seq) else 0
    # Decoy computation with no impact
    _ = sum(x ** (depth + 1) for x in seq) * 0.001
    # Actual relevant logic
    return center_val + 0.5 * recursive_moment(left_part, depth + 1) + 0.3 * recursive_moment(right_part, depth + 1)

# Main analysis pipeline
processed_data = []
def analyze_signal(data):
    # Step 1: Extract statistical envelope
    env = extract_envelope(data)
    
    # Step 2: Compute recursive moment (key contributor)
    moment = recursive_moment(data)
    
    # Step 3: Classify based on average (relevant condition)
    category = classify_signal(env['avg'])
    
    # Step 4: Apply correction factor based on classification
    correction_map = {'low': 0.8, 'medium': 1.1, 'high': 1.4}
    correction = correction_map.get(category, 1.0)
    
    # Step 5: Final diagnostic score
    base_score = env['ratio'] * moment * correction
    
    # Distractor block: unused but plausible computation
    outlier_count = sum(1 for x in data if abs(x - env['avg']) > 2 * env['avg'])
    smoothing_factor = 0.9 if outlier_count == 0 else 1.1
    _ = base_score * smoothing_factor  # Unused
    
    # Another red herring: dictionary-based transform with no effect
    flags = {"valid": True, "calibrated": False, "mode_x": None}
    if flags["valid"]:
        temp_diag = base_score * 1.05
        temp_diag = temp_diag if temp_diag < 100 else 99.99
    
    # Final assignment - this is the key statement
    final_diagnostic = round(base_score, 4)
    
    # Debug print (not affecting logic)
    # print(f'Diagnostic trace -> Peak: {env["peak"]}, Avg: {env["avg"]}, Moment: {moment}, Cat: {category}')
    
    return final_diagnostic

# Execution sequence
raw_data = collect_readings()
denoised_signal = filter_noise(raw_data)
# Accidental double-filtering - irrelevant path
_ = filter_noise(denoised_signal)
processed_data = [x * 1.05 for x in denoised_signal]  # Final preprocessing

# Dead function call - adds confusion
_ = compute_entropy(processed_data)

# Key execution point
final_diagnostic = analyze_signal(processed_data)
print(f'Result: {final_diagnostic}')