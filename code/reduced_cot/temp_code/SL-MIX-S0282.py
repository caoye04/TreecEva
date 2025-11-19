from dataclasses import dataclass
import hashlib

def boundary_correction(position, boundary=100):
    return position % boundary

def energy_filter(particle_hash):
    return int(hashlib.md5(particle_hash.encode()).hexdigest(), 16) % 100 > 75

def interaction_energy(pos1, pos2):
    distance = abs(pos1 - pos2)
    return 100 / (distance + 1) if distance > 0 else 0

@dataclass
class Particle:
    id: str
    x: int
    y: int
    z: int
    
    def corrected_position(self):
        return (boundary_correction(self.x), 
                boundary_correction(self.y), 
                boundary_correction(self.z))
    
    def hash_id(self):
        pos = self.corrected_position()
        return hashlib.sha1(f"{self.id}-{pos}".encode()).hexdigest()[:16]

particles_data = [
    ('P001', 123, 456, 789),
    ('P002', 234, 567, 890),
    ('P003', 345, 678, 901),
    ('P004', 456, 789, 123),
    ('P005', 567, 890, 234)
]

particles = [Particle(*data) for data in particles_data]
significant_interactions_count = 0

for i in range(len(particles)):
    for j in range(i+1, len(particles)):
        p1, p2 = particles[i], particles[j]
        hash1, hash2 = p1.hash_id(), p2.hash_id()
        
        if energy_filter(hash1) and energy_filter(hash2):
            pos1 = p1.corrected_position()
            pos2 = p2.corrected_position()
            avg_distance = sum(abs(a-b) for a,b in zip(pos1,pos2))/3
            
            if avg_distance > 10 and interaction_energy(sum(pos1), sum(pos2)) > 5:
                significant_interactions_count += 1

print(f"Result: {significant_interactions_count}")