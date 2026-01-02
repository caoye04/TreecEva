import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [127, 63, 255, 31, 15, 7, 1, 0]
    processed = []
    for val in raw:
        if val > 100:
            processed.append(val ^ 17)
        elif val > 50:
            processed.append(val + (val << 1))
        else:
            processed.append(val ** 2)
    return processed

# Irrelevant auxiliary function - decoy
def compute_entropy(data):
    entropy = 0.0
    total = sum(data)
    for x in data:
        prob = x / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

# Data transformation pipeline
def transform_signal(seq):
    shifted = seq[2:] + seq[:2]  # Rotate left by 2
    filtered = [x for x in shifted if x % 2 == 1]  # Keep odd values
    amplified = [x * 3 for x in filtered]
    return amplified

# Diagnostic pattern analyzer
def analyze_pattern(signal, limit):
    temp_results = []
    accumulator = 0
    
    # Complex conditional filtering and accumulation
    for i, val in enumerate(signal):
        if i % 3 == 0 and val < limit:
            accumulator += int(math.sqrt(val))
        elif val % 7 == 0:
            accumulator -= val // 10
        else:
            accumulator += (val % 5) * 2
            
        temp_results.append(accumulator)
    
    # Red herring: unused intermediate calculation
    peak_magnitude = max(temp_results) - min(temp_results) if temp_results else 0
    normalization_factor = math.log(peak_magnitude + 2) if peak_magnitude > 0 else 1
    
    # Final computation path (depends only on accumulator's last state)
    score = accumulator * 3
    adjustment = 0
    
    # Dead code branch - never executed due to logic
    if len(signal) > 100:
        adjustment = sum(signal) // 100
    elif len(signal) == 0:
        adjustment = -5
        
    final_score = score + adjustment
    return final_score

# Unused helper - distractor
def validate_checksum(arr):
    checksum = 0
    for i, n in enumerate(arr):
        checksum ^= (n + i) * 3
    return checksum % 13

# Main execution flow
def main():
    readings = collect_readings()           # Step 1: Generate initial data
    readings.append(42)                     # Add known test point
    extended_data = readings + [99, 111]    # Augment with extra values
    
    # Compute irrelevant metrics
    avg_val = sum(extended_data) / len(extended_data)
    bit_weight = sum([bin(x).count('1') for x in extended_data])
    
    transformed_data = transform_signal(extended_data)  # Key transformation
    
    # Misleading intermediate result
    dummy_analysis = [x for x in transformed_data if x > 100]
    
    threshold = 85
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print required result
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()