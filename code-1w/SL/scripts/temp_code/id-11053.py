from collections import defaultdict

# Simulate server load distribution across regions
regions = ['north', 'east', 'south', 'west']
capacity_list = [85, 90, 75, 95]

# Initialize capacity mapping using defaultdict for safety
capacities = defaultdict(int)
for i, region in enumerate(regions):
    capacities[region] = capacity_list[i]

# Redundant counter for operational logs (distractor)
log_counter = defaultdict(int)
log_counter['init'] += 1

# Update south region due to maintenance downgrade
capacities['south'] = max(50, capacities['south'] - 15)

# Critical computation: available load after reserving minimum capacity
reserve_margin = 5
total_load = sum(capacities.values()) - min(capacities.values())
total_load -= reserve_margin

# Additional unrelated logging (minimal interference)
log_counter['final'] += 1

print(f"Result: {total_load}")