from itertools import cycle

# Simulate temperature readings from sensors in a chemical process
sensor_data = [23.5, 24.1, 25.0, 26.8, 27.3, 28.0, 29.1, 30.5]

# Process stage names and thresholds
target_temps = {'initiation': 25.0, 'reaction': 28.0, 'completion': 30.0}
stage_keys = list(target_temps.keys())

# Misleading auxiliary data (distractor)
system_log = [(1, 'start'), (2, 'calibrate'), (3, 'flow_on'), (4, 'sample'), (5, 'flow_off')]
status_flags = {i: True for i in range(len(system_log))}

# Helper function to determine current process stage based on temperature
def get_current_stage(temp, temp_thresholds):
    if temp < temp_thresholds['initiation']:
        return 'preparation'
    elif temp < temp_thresholds['reaction']:
        return 'initiation'
    elif temp < temp_thresholds['completion']:
        return 'reaction'
    else:
        return 'completion'

# Function to compute thermal output based on active stages and dwell times
def calculate_thermal_output(stages):
    accumulated_heat = 0.0
    stage_durations = {key: 0 for key in stages}
    prev_stage = None
    start_index = 0

    # Use enumerate and zip to align sensor readings with cycling stage keys
    for idx, (reading, stage_cycle) in enumerate(zip(sensor_data, cycle(stage_keys))):
        current_stage = get_current_stage(reading, target_temps)

        # Track duration only for valid process stages (not preparation/completion)
        if current_stage in stage_durations:
            stage_durations[current_stage] += 1

        # Accumulate heat only during reaction phase
        if current_stage == 'reaction' and prev_stage != 'reaction':
            start_index = idx  # Mark entry into reaction
        if current_stage != 'reaction' and prev_stage == 'reaction':
            accumulated_heat += (idx - start_index) * 1.5  # Time spent in reaction

        prev_stage = current_stage

    # Additional irrelevant computation (distractor)
    avg_duration = sum(stage_durations.values()) / len(stage_durations) if stage_durations else 0
    stability_score = len([d for d in stage_durations.values() if d > 1])

    # Final thermal output depends only on accumulated_heat from reaction phase
    final_output = accumulated_heat * 10.0

    # More red herring variables
    calibration_offset = 0.05
    total_samples = len(sensor_data)
    efficiency_ratio = stability_score / total_samples if total_samples else 0

    return final_output

# Main logic path
process_phases = ['initiation', 'reaction', 'completion']

# Key execution point
thermal_capacity = calculate_thermal_output(process_phases)

# Print result as required
print(f"Result: {thermal_capacity}")