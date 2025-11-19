import math
from collections import defaultdict
from functools import reduce

def calculate_elevation_variance(elevations):
    if len(elevations) < 2:
        return 0
    mean = sum(elevations) / len(elevations)
    return sum((x - mean) ** 2 for x in elevations) / (len(elevations) - 1)

# Robot state tracking
robot_states = defaultdict(lambda: 0)  # Default state is calibration
robot_positions = {
    'ROV-Alpha': 0b11011010,
    'ROV-Beta': 0b10110101,
    'ROV-Gamma': 0b11100011
}

# Mission status initialization
mission_status_code = 0

for rover_id, position_flag in robot_positions.items():
    # Extract quadrant info (bits 6-7)
    quadrant = (position_flag >> 6) & 0b11
    
    # Check for valid exploration zone (quadrants 1 or 2)
    if quadrant in [1, 2]:
        # Transition to exploration mode
        robot_states[rover_id] = 1
        
        # Process elevation data based on position
        elevation_data = [
            math.log(position_flag + 10),  # Add offset to ensure positive values
            math.exp(quadrant),
            math.sqrt(position_flag)
        ]
        
        # Calculate variance using custom function
        variance = calculate_elevation_variance(elevation_data)
        
        # Analysis mode transition condition
        if variance > 2.5:
            robot_states[rover_id] = 2  # Switch to analysis mode
            
            # Compute mission status update using bitwise operations
            status_update = (position_flag ^ int(variance * 10)) & 0xFF
            mission_status_code |= status_update  # Accumulate updates
            
            # Early exit if critical threshold reached
            if mission_status_code > 200:
                break
    else:
        # Invalid quadrant - maintain calibration
        continue

# Final adjustment using functional approach
adjustments = list(map(lambda x: x & 0xF0, [mission_status_code]))
mission_status_code = reduce(lambda a, b: a | b, adjustments, 0)

print(f"Result: {mission_status_code}")