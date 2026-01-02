import math
from statistics import mean, variance

class Component:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.volume = math.pi * radius**2 * height

# Factory floor grid of components
components_grid = [
    [Component(2, 5), Component(3, 4), Component(1, 6)],
    [Component(2, 3), Component(4, 2), Component(3, 5)],
    [Component(1, 4), Component(2, 6), Component(5, 3)]
]

# State machine for sorting logic
class SortingStateMachine:
    def __init__(self):
        self.state = 'INIT'
        self.sorted_volumes = []
        self.sorting_index = 0
    
    def process_component(self, comp):
        if self.state == 'INIT':
            if comp.volume > 100:
                self.state = 'LARGE'
            else:
                self.state = 'SMALL'
        elif self.state == 'LARGE':
            if comp.volume < 50:
                self.state = 'SMALL'
        elif self.state == 'SMALL':
            if comp.volume > 150:
                self.state = 'LARGE'
        
        self.sorted_volumes.append(comp.volume)
        
    def finalize_sorting(self):
        vol_mean = mean(self.sorted_volumes)
        vol_variance = variance(self.sorted_volumes)
        geometric_factor = math.sqrt(vol_mean * vol_variance)
        
        # Linked list simulation for final indexing
        linked_indices = {}
        prev_index = None
        for i, vol in enumerate(self.sorted_volumes):
            linked_indices[i] = {'value': vol, 'next': i+1 if i+1 < len(self.sorted_volumes) else None, 'prev': prev_index}
            prev_index = i
        
        # Calculate final sorting index based on state transitions and geometric properties
        state_transitions = 0
        current_state = 'INIT'
        for comp in [comp for row in components_grid for comp in row]:
            if current_state != ('LARGE' if comp.volume > 100 else 'SMALL'):
                state_transitions += 1
            current_state = 'LARGE' if comp.volume > 100 else 'SMALL'
        
        # Dictionary comprehension for volume categorization
        volume_categories = {i: 'large' if v > vol_mean else 'small' for i, v in enumerate(self.sorted_volumes)}
        
        # Final calculation using set operations
        large_volume_indices = {i for i, cat in volume_categories.items() if cat == 'large'}
        small_volume_indices = {i for i, cat in volume_categories.items() if cat == 'small'}
        
        self.sorting_index = len(large_volume_indices.intersection(small_volume_indices)) + \
                             int(geometric_factor) + \
                             state_transitions
        
        return self.sorting_index

# Main sorting routine
sorter = SortingStateMachine()
for row in components_grid:
    for component in row:
        sorter.process_component(component)

final_sorting_index = sorter.finalize_sorting()
print(f"Result: {final_sorting_index}")