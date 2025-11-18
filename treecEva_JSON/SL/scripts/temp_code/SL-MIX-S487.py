from functools import reduce
from collections import namedtuple

class Node:
    def __init__(self, species_id, strength):
        self.species_id = species_id
        self.strength = strength
        self.next = None

def build_sonar_chain(detection_data):
    if not detection_data:
        return None
    head = Node(detection_data[0][0], detection_data[0][1])
    current = head
    for species_id, strength in detection_data[1:]:
        current.next = Node(species_id, strength)
        current = current.next
    return head

def analyze_species_strength(chain_head):
    # Extract unique species IDs using set operations
    species_set = set()
    current = chain_head
    while current:
        species_set.add(current.species_id)
        current = current.next
    
    # Calculate average strength per species
    species_strengths = {species_id: [] for species_id in species_set}
    current = chain_head
    while current:
        species_strengths[current.species_id].append(current.strength)
        current = current.next
    
    # Compute mean strength for each species using functional programming
    avg_strengths = {
        species_id: reduce(lambda x, y: x + y, strengths) / len(strengths)
        for species_id, strengths in species_strengths.items()
    }
    
    # Find maximum average strength
    max_avg_strength = max(avg_strengths.values())
    
    # Count species with strength above 75% of maximum
    high_activity_count = sum(
        1 for strength in avg_strengths.values() 
        if strength > 0.75 * max_avg_strength
    )
    
    # Apply floating point operations for final calculation
    normalized_factor = float(high_activity_count) / float(len(species_set))
    final_strength = round(max_avg_strength * normalized_factor, 2)
    
    return final_strength

# Sonar detection data: (species_id, detection_strength)
detections = [
    ('SP-42', 82.3),
    ('SP-17', 65.7),
    ('SP-42', 88.1),
    ('SP-91', 91.2),
    ('SP-17', 72.4),
    ('SP-42', 79.8),
    ('SP-91', 87.6),
    ('SP-17', 68.9)
]

sonar_chain = build_sonar_chain(detections)
final_strength = analyze_species_strength(sonar_chain)
print(f"Result: {final_strength}")