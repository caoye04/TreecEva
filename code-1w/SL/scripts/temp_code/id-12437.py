from itertools import combinations

# System parameters for network capacity calculation
efficiency_factor = 0.85
base_frequency = 2.4  # GHz
link_bandwidths = [100, 200, 150, 300]  # Mbps
max_links = len(link_bandwidths)

# Irrelevant distraction: frequency to wavelength conversion (not used in final result)
wavelength = 299792458 / (base_frequency * 1e9)  # meters
wavelength_rounded = round(wavelength, 2)

# Core logic: compute effective capacity using combinatorial link aggregation
# Only pairs of links are considered due to hardware constraints
active_pairs = list(combinations(link_bandwidths, 2))

# Lambda function to compute aggregated capacity with efficiency loss
calculate_pair_capacity = lambda bw1, bw2: (bw1 + bw2) * efficiency_factor

# Total system capacity is sum of all possible active pair capacities
total_capacity = 0.0
for pair in active_pairs:
    total_capacity += calculate_pair_capacity(pair[0], pair[1])

# Additional distraction: unused variable simulating latency calculation
average_latency = max_links * 0.5  # ms (not related to capacity)

Result: total_capacity