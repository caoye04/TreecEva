import math
from functools import reduce

def phase_transformer(operation_code, value, cycle):
    if operation_code == 'ALPHA':
        return (value * 3 + cycle) % 7
    elif operation_code == 'BETA':
        return int(math.log(value + 1) * 10) if value > 0 else 0
    elif operation_code == 'GAMMA':
        return pow(value, 2, 11)  # Modular exponentiation
    return value

class ExperimentTracker:
    def __init__(self):
        self.stability_states = {
            'INITIAL': 0,
            'PROCESSING': 1,
            'STABILIZING': 2,
            'FINAL': 3
        }
        self.current_state = 'INITIAL'
    
    def transition(self, new_state):
        if new_state in self.stability_states:
            self.current_state = new_state
            return True
        return False

# Initialize experiment parameters
tracker = ExperimentTracker()
particle_metrics = [2, 5, 1, 8, 3]
cumulative_stability_index = 0
phase_sequence = ['ALPHA', 'BETA', 'GAMMA']

# Process each particle through experimental phases
for particle_id, base_metric in enumerate(particle_metrics):
    local_stability = base_metric
    tracker.transition('PROCESSING')
    
    for phase_id, phase_type in enumerate(phase_sequence):
        local_stability = phase_transformer(phase_type, local_stability, particle_id)
        
        # State-dependent adjustment
        if tracker.current_state == 'PROCESSING' and phase_id == 1:
            tracker.transition('STABILIZING')
            local_stability += 5
        
        cumulative_stability_index += local_stability
    
    # Apply dynamic programming optimization for stabilization
    if particle_id > 0:
        cumulative_stability_index = max(cumulative_stability_index, 
                                       cumulative_stability_index - particle_metrics[particle_id-1] + local_stability)

# Final state transition and calculation
tracker.transition('FINAL')
sorted_metrics = sorted(particle_metrics, reverse=True)
final_adjustment = reduce(lambda x, y: (x ^ y) % 13, sorted_metrics)  # Bitwise XOR with modular arithmetic
cumulative_stability_index = (cumulative_stability_index + final_adjustment) % 100

print(f"Result: {cumulative_stability_index}")