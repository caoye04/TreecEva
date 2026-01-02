import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    offset = 2
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant transformation: frequency shift (not used in final result)
def apply_fourier_shift(data):
    shifted = []
    for i in range(len(data)):
        shifted.append(int(data[i] * math.sin(i + 1)))
    return shifted

# Data cleaning with string-based tagging (uses string method)
def clean_and_tag(data):
    cleaned = []
    for val in data:
        tag = f"val_{val}".upper()  # Use of string method
        if '5' in tag or '9' in tag:
            continue  # Skip high tags
        cleaned.append(val)
    return cleaned

# Signal processing with conditional logic and bitwise operations
def process_signal_sequence(data):
    temp_result = 0
    history = []
    for i, x in enumerate(data):
        if i % 3 == 0:
            temp_result += x << 1  # Left shift
        elif i % 3 == 1:
            temp_result -= x & 7   # Bitwise AND
        else:
            temp_result ^= int(x ** 0.5)  # XOR with square root floor
        history.append(abs(temp_result) % 10)
    
    # Dummy checksum (unused but looks important)
    checksum = ''.join(str(h) for h in history).zfill(10)
    return temp_result

# Diagnostic engine with red herring variables
def analyze_signal(signal_value):
    diagnostics = {}
    
    # Complex but irrelevant classification
    if signal_value > 100:
        category = "HIGH"
    elif signal_value > 50:
        category = "MEDIUM"
    else:
        category = "LOW"
    
    # Real computation path
    base_score = abs(signal_value)
    adjustment = 0
    
    # Hidden rule: if sum of digits is even, add 17, else subtract 11
    digit_sum = sum(int(d) for d in str(base_score))
    if digit_sum % 2 == 0:
        adjustment = 17
    else:
        adjustment = -11
    
    # Decoy logic with unused branching
    if base_score % 7 == 0:
        multiplier = 1.5
    elif base_score % 5 == 0:
        multiplier = 0.8
    else:
        multiplier = 1.0  # Final path doesn't use multiplier
    
    # Final result is not multiplied — only adjusted
    final_score = base_score + adjustment  # Key line
    
    # Unused derived metrics (distractors)
    normalized = round(final_score / (1 + len(str(final_score))), 3)
    confidence = math.exp(-abs(normalized - 50) / 100)
    
    diagnostics['score'] = final_score  # Avoid using 'score' as main var per constraints
    diagnostics['level'] = category
    diagnostics['norm'] = normalized
    
    return diagnostics['score']

# Orchestration function with dead paths
def system_diagnostic():
    # Step 1: Collect data
    samples = collect_samples()
    
    # Step 2: Apply irrelevant Fourier shift (result unused)
    _ = apply_fourier_shift(samples)
    
    # Step 3: Clean data with string tagging
    cleaned_data = clean_and_tag(samples)
    
    # Step 4: Process signal through logic chain
    processed_data = process_signal_sequence(cleaned_data)
    
    # Step 5: Generate final diagnostic
    final_diagnostic = analyze_signal(processed_data)
    
    # Dead code branch: simulation override (never reached)
    simulate = False
    if simulate:
        mock_data = [1, 0, 1]
        final_diagnostic = sum(x**3 for x in mock_data)
    
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point
if __name__ == "__main__":
    system_diagnostic()