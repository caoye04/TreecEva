from typing import Set

# Network tower coverage analysis for urban planning
initial_towers: Set[str] = {'A1', 'B2', 'C3', 'D4', 'E5'}
planned_towers: Set[str] = {'C3', 'D4', 'F6', 'G7'}

# Identify newly covered regions from expansion
new_coverage: Set[str] = planned_towers.difference(initial_towers)
expanded_regions: Set[str] = initial_towers.union(new_coverage)

# Zones marked for infrastructure upgrade
priority_zones: Set[str] = {'X9', 'Y10', 'D4', 'F6'}
upgraded_zones: Set[str] = {'D4', 'F6', 'Z11'}

# Simulate region consolidation after policy update
temporary_buffer: Set[str] = {'A1', 'Z11'}  # Irrelevant operational buffer
final_regions: Set[str] = expanded_regions.copy()
final_regions.discard('E5')  # Remove decommissioned region

# Key statement
coverage_overlap = final_regions.intersection(upgraded_zones)

print(f"Result: {coverage_overlap}")