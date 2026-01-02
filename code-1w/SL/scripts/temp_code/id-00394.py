def analyze_temperatures(temps):
    avg = sum(temps) / len(temps)
    deviation = sum((t - avg) ** 2 for t in temps) / len(temps)
    return avg, deviation

# Environmental sensor data (irrelevant to final result)
sensor_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
baseline_temp, thermal_variance = analyze_temperatures(sensor_readings)

# Irrelevant financial calculation block
def calculate_roi(revenue, cost):
    if cost == 0:
        return 0
    return (revenue - cost) / cost

annual_revenue = 50000
cost_investment = 30000
project_roi = calculate_roi(annual_revenue, cost_investment)

# Core data processing chain
raw_data = [8, 12, 15, 7, 20, 13, 9]
weights = [0.1, 0.2, 0.15, 0.05, 0.3, 0.2]

# Misleading normalization step (partially unused)
normalized = [(x - min(raw_data)) / (max(raw_data) - min(raw_data)) * 100 for x in raw_data]
dummy_sum = sum(normalized[:4])

# Key processing function with distractors
def process_metrics(data, w):
    total_weighted = 0
    temp_flags = []

    # Use enumerate and zip as required
    for i, (val, weight) in enumerate(zip(data[:-1], w)):
        adjusted_val = val * weight
        
        # Bitwise interference (XOR with index)
        masked_val = int(adjusted_val) ^ (i + 1)
        
        # Conditional red herring
        if masked_val > 100:
            temp_flags.append(True)
        else:
            temp_flags.append(False)
            
        # Only this accumulation matters
        total_weighted += adjusted_val
    
    # Modular arithmetic distraction
    checksum = sum(data) % 7
    parity_check = len(w) & 1
    
    # Actual answer computation (only depends on weighted sum)
    base_score = total_weighted * 10
    
    # One more irrelevant transformation
    if checksum > parity_check:
        final_score = base_score + 5
    else:
        final_score = base_score - 3
    
    # Dead code path
    if False:
        final_score = 999
        
    return final_score

# Unused helper that looks important
def validate_consistency(arr, thres=0.1):
    return all(abs(arr[i] - arr[i+1]) < thres for i in range(len(arr)-1))

# Execution point of interest
data = [v + 1 for v in raw_data]  # Shift data: [9,13,16,8,21,14,10]
final_score = process_metrics(data, weights)

# Output the target result
print(f"Target result: {final_score}")