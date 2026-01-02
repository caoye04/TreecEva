def analyze_packet_loss(loss_rate, threshold=0.05):
    return "stable" if loss_rate < threshold else "unstable"


def calculate_efficiency(speed, latency):
    base_efficiency = speed * 0.85
    adjusted = base_efficiency - (latency ** 2) / 100
    penalty = 0
    
    # Conditional expression for jitter impact
    jitter_impact = 1.5 if latency > 120 else 0.8
    
    adjusted *= jitter_impact
    
    # Simulate some irrelevant state tracking
    status_log = []
    temp_buffer = [speed // 10, latency // 5]
    for i in range(2):
        status_log.append(f"Phase {i+1}: Active")
    
    # Distractor: unused intermediate calculations
    theoretical_max = speed * 1.2
    overhead_estimate = theoretical_max * 0.15
    dummy_mask = 0b1101 & int(latency)
    masked_result = dummy_mask ^ 0b1010
    
    # More red herring: extra function call with side effect that doesn't affect output
    def update_cache(val):
        cache_file = open('/dev/null', 'w')  # Simulated write (harmless)
        cache_file.write(str(val))
        cache_file.close()
        return True
    
    update_cache(masked_result)
    
    # Actual determining logic path
    if adjusted > 500:
        adjusted *= 0.9
    elif adjusted > 300:
        adjusted *= 0.95
    else:
        adjusted *= 1.0
    
    return int(adjusted)

# Main execution
link_speed = 750
latency_factor = 95

# Irrelevant pre-computations
baseline_metric = (link_speed + latency_factor) // 7
shadow_copy = link_speed
packet_status = analyze_packet_loss(0.03)
dummy_list = [x * 2 for x in range(5)]

# Key statement
final_bandwidth = calculate_efficiency(link_speed, latency_factor)

# Print result as required
print(f"Target result: {final_bandwidth}")