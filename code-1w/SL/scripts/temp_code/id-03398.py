import math

def preprocess_sensor_data(data):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in data if x > 0]

def validate_calibration(sequence):
    # Distractor function with misleading intermediate logic
    total = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            total += val ** 2
        else:
            total -= val // 3
    return total > 100

def decode_frequency_shift(signal):
    # Unused signal decoding routine (red herring)
    shift = 0
    for bit in signal:
        shift = (shift << 1) | (bit & 1)
    return shift ^ 0xFF

def calculate_thermal_output(stages):
    # Core relevant function with embedded distractions
    base_factor = 1.75
    adjustment = 0.92
    accumulator = 0.0
    peak_memory = []

    # Real logic begins
    for idx, stage in enumerate(stages):
        phase_weight = stage['weight']
        duration = stage['duration']
        mode = stage['mode']

        # Simulate physical thermal integration
        if mode == 'heating':
            contribution = phase_weight * duration * base_factor
            accumulator += contribution
        elif mode == 'cooling':
            contribution = phase_weight * duration * adjustment
            accumulator -= contribution
        else:
            temp = (phase_weight + duration) / 2
            peak_memory.append(temp)  # Distractor: collects but unused

        # Embedded lambda for minor correction (relevant)
        nonlinear_correct = lambda x: x * (1 + 0.03 * math.sin(idx))
        accumulator = nonlinear_correct(accumulator)

        # Early termination check (never triggers due to data design)
        if accumulator < 0:
            accumulator = 0
            break

    # Final transformation using zip and enumerate (key step)
    indices = list(range(len(stages)))
    for i, (idx, stage) in enumerate(zip(indices, stages)):
        if stage['mode'] == 'heating' and i % 2 == 1:
            bonus = stage['weight'] * 0.15
            accumulator += bonus  # Small additive effect

    return accumulator

# Main execution block
if __name__ == '__main__':
    # Sensor readings (irrelevant data structure)
    raw_readings = [23.1, 24.5, -1.0, 26.0, 27.3]
    calibrated = preprocess_sensor_data(raw_readings)

    # Frequency pattern (decoy input)
    freq_signal = [1, 0, 1, 1, 0, 0, 1]
    shift_code = decode_frequency_shift(freq_signal)

    # Actual process flow definition (relevant)
    process_stages = [
        {'weight': 12.0, 'duration': 5, 'mode': 'heating'},
        {'weight': 8.5, 'duration': 3, 'mode': 'heating'},
        {'weight': 10.0, 'duration': 4, 'mode': 'cooling'},
        {'weight': 7.0, 'duration': 6, 'mode': 'heating'}
    ]

    # Validation check (evaluated but does not affect outcome)
    is_valid = validate_calibration([s['duration'] for s in process_stages])

    # Key assignment point
    thermal_capacity = calculate_thermal_output(process_stages)

    # Print final result
    print(f"Result: {thermal_capacity}")