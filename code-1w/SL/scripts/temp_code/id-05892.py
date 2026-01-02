def calculate_network_capacity(speeds, factor):
    adjusted = [speed * (1.5 if speed > 100 else 1.0) for speed in speeds]
    total_bandwidth = sum(adjusted)
    redundancy_loss = total_bandwidth * (factor / 100)
    return int(total_bandwidth - redundancy_loss)

# System link configurations
test_links = [45, 200, 75, 300]
decoy_value = 999  # Irrelevant variable for minimal interference
redundancy_factor = 15

# Critical computation point
final_capacity = calculate_network_capacity(test_links, redundancy_factor)
print(f"Result: {final_capacity}")