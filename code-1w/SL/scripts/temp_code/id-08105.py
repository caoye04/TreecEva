import math

def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > 0]
    baseline = sum(filtered) / len(filtered)
    normalized = [x / baseline for x in filtered]
    return normalized

def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return round(total, 6)

def evaluate_stability(risk_profile):
    score = 0
    for i, val in enumerate(risk_profile):
        if i % 3 == 0:
            score += val * 0.5
        elif i % 3 == 1:
            score += val * 0.3
        else:
            score += val * 0.2
    return score > 4.5

def generate_fallback_modes(config_set):
    modes = set()
    for c in config_set:
        if 'A' in c:
            modes.add(1)
        elif 'B' in c:
            modes.add(2)
        else:
            modes.add(3)
    # Irrelevant accumulation
    temp_sum = 0
    for m in modes:
        temp_sum += m * 17
    return list(modes)

def analyze_metrics(signature, load):
    # Core logic starts here
    magnitude = sum(math.sin(x) for x in signature)
    phase_shift = compute_entropy([abs(math.cos(x)) + 0.01 for x in signature])
    
    # Distractor: irrelevant data structure transformation
    shadow_buffer = []
    for i in range(len(signature)):
        if i < 5:
            shadow_buffer.append({'idx': i, 'val': signature[i] * 2.5})
    shadow_hash = len(shadow_buffer) * 19
    
    # Key intermediate value (not the answer)
    coherence = abs(magnitude) * phase_shift
    
    # More red herring: unused control flow
    if coherence < 1.0:
        adjustment_factor = 0.8
        buffer_pool = [coherence * j for j in range(3)]
        final_adjusted = sum(buffer_pool)
    else:
        adjustment_factor = 1.1  # Never actually used
        fallback_list = generate_fallback_modes(['XA', 'YB', 'ZC'])
        stats_summary = {'count': len(fallback_list), 'max': max(fallback_list)}

    # Real computation path
    weighted_load = 0
    for idx, lvl in enumerate(load):
        if idx % 2 == 0:
            weighted_load += lvl * 0.7
        else:
            weighted_load += lvl * 0.3
    
    # Critical line: this is where final_diagnostic is assigned
    final_diagnostic = int((coherence * 1000) + (weighted_load * 10))
    
    # Dead code branch — looks important but never reached
    if False:
        debug_trace = []
        for _ in range(3):
            debug_trace.append({'step': _, 'value': final_diagnostic // (_ + 1)})
        return sum(d['value'] for d in debug_trace)
    
    return final_diagnostic

# Simulated input data
raw_sensor_stream = [0.1, -0.5, 2.3, 0.0, 1.7, 3.1, -2.0, 4.5]
health_signature = preprocess_signal(raw_sensor_stream)
system_load = [8, 5, 12, 7, 9]

# Unused variables — distractions
baseline_metric = sum(health_signature) / len(health_signature)
peak_observed = max(health_signature)
critical_threshold = 0.85
emergency_mode = peak_observed > critical_threshold

# Trigger function call
final_diagnostic = analyze_metrics(health_signature, system_load)
print(f"Result: {final_diagnostic}")