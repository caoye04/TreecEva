class BiodiversityTracker:
    def __init__(self):
        self.observations = set()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def add_species(self, species_list):
        self.observations.update(species_list)
    
    def get_unique_count(self):
        return len(self.observations)

def analyze_zones():
    zone_a_species = {'Panthera leo', 'Loxodonta africana', 'Giraffa camelopardalis'}
    zone_b_species = {'Panthera pardus', 'Loxodonta africana', 'Syncerus caffer'}
    zone_c_species = {'Giraffa camelopardalis', 'Panthera tigris', 'Elephas maximus'}
    
    with BiodiversityTracker() as tracker:
        tracker.add_species(zone_a_species)
        tracker.add_species(zone_b_species)
        tracker.add_species(zone_c_species)
        unique_species_count = tracker.get_unique_count()
    
    return unique_species_count

# Execution
unique_species_count = analyze_zones()
print(f"Result: {unique_species_count}")