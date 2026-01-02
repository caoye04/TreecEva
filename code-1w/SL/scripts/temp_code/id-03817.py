def calculate_network_capacity(speeds, factor):
    adjusted_speeds = [speed * 0.9 for speed in speeds if speed > 100]
    total_bandwidth = sum(adjusted_speeds)
    redundant_links = len(adjusted_speeds) // 2 + 1
    return total_bandwidth * factor / redundant_links

# System link configurations
temp_buffer = [50, 75, 200, 300, 150]  # irrelevant buffer data
link_speeds = [100, 200, 300, 400, 250]
redundancy_factor = 1.2

# Calculation of final network capacity
final_capacity = calculate_network_capacity(link_speeds, redundancy_factor)
print(f"Result: {final_capacity}")