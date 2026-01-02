from itertools import accumulate

# Simulate a dynamic sensor array processing sequence with noise filtering and flow analysis
def analyze_sensor_pattern(raw_readings):
    filtered_readings = [x for x in raw_readings if x > 0]
    
    # Irrelevant transformation: phase normalization (not used later)
    normalized_phases = list(map(lambda x: (x % 360) / 360.0, raw_readings))
    
    # Compute moving average with window size 2 as secondary check
    avg_check = [(filtered_readings[i] + filtered_readings[i+1]) / 2 
                 for i in range(len(filtered_readings)-1)] if len(filtered_readings) > 1 else [0]
    
    # Primary computation path: extract oscillation envelope
    envelope = [abs(filtered_readings[i] - filtered_readings[i-1]) 
               for i in range(1, len(filtered_readings))]
    
    # Accumulate trend to detect net drift
    drift_accumulation = list(accumulate(envelope, lambda a, x: a + x * 0.5))
    
    # Dummy state tracker (distractor)
    state_log = []
    for val in drift_accumulation:
        if val > 10:
            state_log.append('HIGH')
        elif val > 5:
            state_log.append('MEDIUM')
        else:
            state_log.append('LOW')  # Most frequent, but unused
    
    return envelope

# Calculate net energy flow from rate samples
def calculate_net_flow(rates):
    base_flow = sum(rates)
    adjustment_factor = len(rates) if base_flow != 0 else 1
    
    # Redundant computation: harmonic mean (not used in final result)
    harmonic_mean = 0
    if all(x != 0 for x in rates):
        harmonic_mean = len(rates) / sum(1/x for x in rates)
    
    # Secondary adjustment based on pattern symmetry
    reversed_rates = rates[::-1]
    symmetric_match = sum(1 for a, b in zip(rates, reversed_rates) if a == b)
    
    # Final flow calculation depends only on base_flow and symmetric_match
    net_flow = base_flow + (symmetric_match * 2)
    
    # Dead code branch (never executes due to prior filtering)
    if len(rates) > 100:
        net_flow -= harmonic_mean
    
    return net_flow

# Main execution
sensor_data = [12, -5, 8, 8, 3, 7, -2, 7, 3]
processed_envelope = analyze_sensor_pattern(sensor_data)
rate_sequence = [processed_envelope[i] % 7 for i in range(0, len(processed_envelope), 2)]

# Key assignment point
final_flux = calculate_net_flow(rate_sequence)
print(f"Target result: {final_flux}")