import math

# Simulated sensor readings with noise
def get_raw_readings():
    return [127, 255, 64, 191, 32, 223, 15, 88, 176, 48]

# Misleading transformation - not actually used in final result
def transform_noise_level(data):
    return [x ^ 0xFF for x in data if x > 100]

# Critical data processing pipeline
def analyze_signal_strength(readings):
    # Step 1: Normalize readings using bitwise mask to extract lower 6 bits
    normalized = [r & 0x3F for r in readings]
    
    # Step 2: Apply logarithmic scaling (base 2) to compress dynamic range
    scaled = [math.log2(x + 1) for x in normalized]
    
    # Step 3: Flag anomalies (values above threshold)
    anomaly_flags = {i: val > 4.0 for i, val in enumerate(scaled)}
    
    # Step 4: Create shifted shadow copy (distractor)
    shifted = [scaled[i] * 0.5 if i % 2 == 0 else scaled[i] * 1.5 for i in range(len(scaled))]
    
    # Step 5: Compute moving average of original scaled values (unused path)
    moving_avg = []
    for i in range(len(scaled)):
        window = scaled[max(0, i-2):i+1]
        moving_avg.append(sum(window) / len(window))
    
    # Step 6: Filter valid signals: must be even index AND normalized > 20
    valid_indices = {i for i in range(len(normalized)) if i % 2 == 0 and normalized[i] > 20}
    
    # Step 7: Extract corresponding scaled values at valid positions
    filtered_data = [scaled[i] for i in range(len(scaled)) if i in valid_indices]
    
    # Step 8: Compute final metric
    filtered_sum = sum(filtered_data)
    
    # BEGIN DISTRACTOR BLOCK - UNUSED BUT COMPELLING
    # Simulate calibration offset (never applied)
    calibration = sum([normalized[i] for i in range(0, len(normalized), 3)]) * 0.1
    
    # Fake correction based on anomaly density
    anomaly_density = len([f for f in anomaly_flags.values() if f]) / len(anomaly_flags)
    if anomaly_density > 0.3:
        adjusted = [val * 0.9 for val in filtered_data]
    else:
        adjusted = [val * 1.1 for val in filtered_data]
    
    # Dead-end statistical analysis
    variance_proxy = sum([(x - filtered_sum/len(filtered_data))**2 for x in filtered_data])
    # END DISTRACTOR BLOCK
    
    # Final output uses only filtered_sum
    return filtered_sum

# Orchestration function with red herring call
def main_pipeline():
    raw = get_raw_readings()
    
    # Distractor: complex but unused signal transformation
    noise_adjusted = transform_noise_level(raw)
    enhanced = [x + 10 for x in noise_adjusted if x < 150]
    
    # Real processing begins here
    result = analyze_signal_strength(raw)
    
    # Print final answer as required
    print(f"Result: {result}")
    return result

# Execute
if __name__ == "__main__":
    main_pipeline()