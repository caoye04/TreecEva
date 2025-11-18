from functools import reduce

def process_signal_phases():
    # Define signal contributions as a list of tuples (initial_value, modifier)
    signal_contributions = [(45, 2), (90, -1), (180, 3), (270, -2), (315, 1)]
    
    # State transition rules encoded in a dictionary
    state_machine = {
        0: lambda x: (x + 90) % 360,
        90: lambda x: (x * 2) % 360,
        180: lambda x: (x - 45) % 360,
        270: lambda x: (x // 2) % 360
    }
    
    # Initial phase state
    current_phase = 0
    
    # Process each contribution
    for initial, modifier in signal_contributions:
        adjusted_signal = (initial * modifier) % 360
        if current_phase in state_machine:
            current_phase = state_machine[current_phase](adjusted_signal)
        else:
            current_phase = (current_phase + adjusted_signal) % 360
    
    # Apply a secondary transformation using set operations
    phase_markers = {0, 90, 180, 270}
    active_markers = {p for p in phase_markers if current_phase >= p}
    marker_sum = sum(active_markers)
    
    # Final phase calculation using divide and conquer approach via reduce
    components = [current_phase, marker_sum, len(active_markers)]
    final_phase_state = reduce(lambda a, b: (a + b) % 360, components, 0)
    
    return final_phase_state

final_phase_state = process_signal_phases()
print(f"Result: {final_phase_state}")