import math
from collections import defaultdict

class BuildingProposal:
    def __init__(self, start_pos, radius):
        self.start_pos = start_pos
        self.radius = radius
        self.end_pos = start_pos + 2 * radius

def calculate_max_non_overlapping(proposals):
    if not proposals:
        return 0
    
    # Sort by end position for greedy algorithm
    proposals.sort(key=lambda x: x.end_pos)
    
    count = 1
    last_end = proposals[0].end_pos
    
    for i in range(1, len(proposals)):
        if proposals[i].start_pos >= last_end:
            count += 1
            last_end = proposals[i].end_pos
    
    return count

# Building proposals along a street (position represents distance from origin)
building_proposals = [
    BuildingProposal(2, 1.5),   # Building with radius 1.5 at position 2
    BuildingProposal(5, 1),     # Building with radius 1 at position 5
    BuildingProposal(6, 1.5),   # Building with radius 1.5 at position 6
    BuildingProposal(10, 2),    # Building with radius 2 at position 10
    BuildingProposal(13, 1),    # Building with radius 1 at position 13
    BuildingProposal(15, 1.5),  # Building with radius 1.5 at position 15
    BuildingProposal(18, 2),    # Building with radius 2 at position 18
    BuildingProposal(22, 1)     # Building with radius 1 at position 22
]

# City planning constraint: minimum separation between buildings
MIN_SEPARATION = 0.5

# Adjust proposals for minimum separation
adjusted_proposals = []
for proposal in building_proposals:
    adjusted_start = proposal.start_pos - MIN_SEPARATION/2
    adjusted_radius = proposal.radius + MIN_SEPARATION/2
    adjusted_proposals.append(BuildingProposal(adjusted_start, adjusted_radius))

max_non_overlapping_buildings = calculate_max_non_overlapping(adjusted_proposals)

print(f"Result: {max_non_overlapping_buildings}")