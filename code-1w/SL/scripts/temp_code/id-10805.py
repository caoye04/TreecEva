from collections import defaultdict, Counter
from itertools import zip_longest

# Simulate regional warehouse inventory distribution
regions = ['North', 'South', 'East', 'West']
base_stock = [120, 85, 95, 110]
threshold = 100

# Track surplus and deficit regions
surplus = []
deficit = []
stock_map = {}
for r, s in zip(regions, base_stock):
    stock_map[r] = s
    if s > threshold:
        surplus.append((r, s - threshold))
    elif s < threshold:
        deficit.append((r, threshold - s))

# Misleading: unused computation for average deviation
avg_deviation = sum(abs(s - threshold) for s in base_stock) / len(base_stock)
deviation_warning = avg_deviation > 15

# Simulate container transfer units (each holds 7 units)
container_size = 7
excess_containers = []
for region, excess in surplus:
    containers = excess // container_size
    excess_containers.extend([f'{region}_C{i}' for i in range(containers)])

# Misleading: dead code path for partial containers
partial_holds = []
for region, excess in surplus:
    partial = excess % container_size
    if partial > 0:
        partial_holds.append(partial * 0.5)  # Half-weighted for stability

# Map deficit regions by need (in units)
deficit_units = []
for region, gap in deficit:
    deficit_units.extend([region] * gap)

# Distribute whole containers first
deficit_counter = Counter(deficit_units)
deficit_regions = list(deficit_counter.keys())

# Helper function to simulate optimized redistribution
def optimize_distribution(containers, regions):
    # Each container adds 7 units; distribute across deficit regions cyclically
    distribution_cycle = []
    for i, region in enumerate(regions):
        needed = deficit_counter[region]
        received = min(len(containers) // len(regions) + (1 if i < len(containers) % len(regions) else 0), needed // 7 + 1)
        distribution_cycle.append(received)
    
    # Calculate total fulfilled capacity (in container units)
    fulfilled = sum(min(d * container_size, deficit_counter[r]) for d, r in zip(distribution_cycle, regions))
    
    # Final metric: net capacity increase after distribution
    initial_deficit = sum(deficit_counter.values())
    remaining_deficit = max(0, initial_deficit - fulfilled)
    transferred = initial_deficit - remaining_deficit
    
    # Compute efficiency-adjusted final capacity
    efficiency_rate = 0.98 if transferred > 0 else 0.0
    adjusted_transfer = int(transferred * efficiency_rate)
    
    # Final available capacity post-redistribution
    final_capacity = adjusted_transfer + sum(base_stock)
    
    # Distractor: unused health metrics
    health_scores = [final_capacity / (threshold * 4) * 100]
    system_health = 'Stable' if health_scores[0] > 80 else 'Unstable'
    
    return final_capacity

# Execute critical statement
final_capacity = optimize_distribution(excess_containers, deficit_regions)
print(f"Result: {final_capacity}")