import hashlib
from collections import deque

class GrowthPhaseNode:
    def __init__(self, phase_id, growth_factor, left=None, right=None):
        self.phase_id = phase_id
        self.growth_factor = growth_factor
        self.left = left
        self.right = right

def compute_environmental_hash(phase_data):
    return int(hashlib.md5(phase_data.encode()).hexdigest()[:8], 16) % 1000

def simulate_growth_phases(root_phase):
    if not root_phase:
        return 0
    
    processing_stack = [root_phase]
    bloom_accumulator = 0
    
    while processing_stack:
        current_phase = processing_stack.pop()
        phase_hash = compute_environmental_hash(current_phase.phase_id)
        
        if phase_hash % 3 == 0:
            bloom_accumulator += current_phase.growth_factor * 2
        elif phase_hash % 3 == 1:
            bloom_accumulator -= current_phase.growth_factor // 2
        else:
            bloom_accumulator ^= current_phase.growth_factor
        
        if current_phase.left and current_phase.right:
            processing_stack.append(current_phase.left)
            processing_stack.append(current_phase.right)
        elif current_phase.left:
            processing_stack.append(current_phase.left)
        elif current_phase.right:
            processing_stack.append(current_phase.right)
    
    return bloom_accumulator

def transform_species_name(name):
    vowels = 'aeiou'
    transformed = ''.join([char.upper() if char in vowels else char.lower() for char in name])
    return transformed[::-1]

# Construct the growth phase tree
primary_phase = GrowthPhaseNode("photosynthesis-optimal", 15)
secondary_left = GrowthPhaseNode("nutrient-rich-soil", 12)
secondary_right = GrowthPhaseNode("high-humidity", 8)
tertiary_left = GrowthPhaseNode("low-light", 5)
tertiary_right = GrowthPhaseNode("wind-exposure", 7)

primary_phase.left = secondary_left
primary_phase.right = secondary_right
secondary_left.left = tertiary_left
secondary_right.right = tertiary_right

# Process the growth simulation
final_bloom_score = simulate_growth_phases(primary_phase)

# Apply species transformation as final step
species_code = transform_species_name("Xerophyta_resilience")
final_bloom_score += len(species_code)

print(f"Result: {final_bloom_score}")