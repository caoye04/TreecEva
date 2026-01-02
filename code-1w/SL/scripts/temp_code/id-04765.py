def calculate_network_capacity(speeds, efficiencies):
    base_capacity = 0
    adjustment_factor = 0.85
    for link, speed in speeds.items():
        if link in efficiencies:
            base_capacity += speed * efficiencies[link]
    return int(base_capacity * adjustment_factor)

# Network link speeds in Mbps
test_links = {
    'router-a': 100,
    'router-b': 200,
    'switch-c': 150,
    'bridge-d': 90
}

# Efficiency ratings for active links
efficiency_ratings = {
    'router-a': 0.92,
    'router-b': 0.88,
    'switch-c': 0.90
}

# Extraneous variable (minimal distraction)
temp_log = "Capacity calculation initiated"

final_capacity = calculate_network_capacity(test_links, efficiency_ratings)
print(f"Result: {final_capacity}")