def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return [x * 2 for x in filtered] if len(filtered) > 3 else [x / 2 for x in filtered]

# Irrelevant signal processing branch (dead path)
def process_audio(signal):
    fft_result = [abs(x) ** 0.5 for x in signal]
    return [y * 1.5 for y in fft_result if y > 1]

# Unused helper function (decoy)
def normalize_vector(vec):
    mag = sum(x**2 for x in vec) ** 0.5
    return [z / mag for z in vec] if mag else vec

def transform_features(raw_inputs):
    # Apply slicing and transformations
    segment = raw_inputs[1:6]
    shifted = [(x << 1) & 7 for x in segment]  # Bitwise manipulation
    return shifted + [sum(shifted[:3]), shifted[0] ^ shifted[-1]]

def evaluate_integrity(values):
    # Logical checks with red herring logic
    valid = True
    for v in values:
        if v < 0 or v > 100:
            valid = False
    audit_flag = valid and (len(values) >= 5)
    # Below line does nothing important
    temp_audit = [v for v in values if v % 2 == 0] if audit_flag else [0]
    return audit_flag

def evaluate_performance(metrics, weights):
    # Core computation buried in noise
    base_scores = [m * w for m, w in zip(metrics, weights)]
    adjustment_factor = 1.0
    
    # Distracting conditional block (misleading path)
    if len(base_scores) > 4:
        temp_val = sum(base_scores) / len(base_scores)
        if temp_val < 10:
            adjustment_factor = 0.8
    
    # Actual key logic
    sliced_metrics = metrics[2:5]
    weight_slice = weights[2:5]
    bonus = 0
    
    for i in range(len(sliced_metrics)):
        if sliced_metrics[i] > 5 and weight_slice[i] > 0.2:
            bonus += 2
    
    # Main calculation
    total = sum(base_scores) + bonus * 3
    
    # Red herring transformation
    fake_adjustment = sum([x ^ int(y * 10) for x, y in zip(metrics, weights)]) % 10
    
    # Final score computation
    final_score = int(total - fake_adjustment + 5)  # fake_adjustment cancels out due to logic
    return final_score

# Irrelevant data structures (distractors)
audio_stream = [0.1, -0.3, 0.7, 1.2, -0.9, 0.0]
unused_matrix = [[1,2],[3,4],[5,6]]

# Key data inputs
feature_set = [4, 8, 12, 15, 9, 3]
weights_list = [0.1, 0.3, 0.5, 0.7, 0.4, 0.2]

# Signal processing diversion (not used in main path)
filtered_data = analyze_signal(audio_stream, 0.4)
transformed_features = transform_features(feature_set)

# Integrity check that evaluates but doesn't affect result
is_valid = evaluate_integrity(transformed_features)

# Decoy assignment
placeholder_result = process_audio(audio_stream)

# Critical execution point
final_score = evaluate_performance(transformed_features, weights_list)

print(f"Result: {final_score}")