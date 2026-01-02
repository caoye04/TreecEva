import itertools

# Simulated sensor data block with embedded flags and noise
def process_sensor_readings(raw_stream):
    base_offset = 2023
    temporal_factor = 17
    checksum = 0
    accumulator = 0
    peak_magnitude = -1
    history_buffer = []
    debug_flag = False
    scaling_constant = 1.61803  # Golden ratio - looks important, unused
    mask = 0b1101

    for index, reading in enumerate(raw_stream):
        # Irrelevant preprocessing - red herring
        normalized = (reading + base_offset) * 0.01
        if normalized > 10.0:
            debug_flag = True

        # Decoy transformation chain
        intermediate = int(normalized * temporal_factor) % 256
        transformed = (intermediate ^ 0x5A) & 0xFF
        if transformed < 50:
            history_buffer.append(transformed)

        # Actual relevant logic buried here
        if index % 3 == 0:
            processed_value = reading ^ 0x1F
        elif index % 4 == 0:
            processed_value = reading & 0x3F
        else:
            processed_value = reading | 0x0F

        # Core computation: checksum update using bit manipulation
        checksum = (checksum << 1) ^ processed_value ^ (index & mask)

        # Dead code path - misleading accumulation
        if index in [5, 10, 15]:
            accumulator += transformed * index

        # Fake early exit condition
        if checksum > 10000:
            pass  # No actual effect

        # Unused peak tracking
        abs_reading = abs(reading)
        if abs_reading > peak_magnitude:
            peak_magnitude = abs_reading

    # Post-processing decoy
    final_adjustment = len(history_buffer) * 7
    checksum = (checksum + final_adjustment) & 0xFFFF  # Keep within 16 bits

    return checksum

# Generate deterministic input using itertools
data_stream = list(itertools.accumulate([1], lambda x, _: (x * 3 + 7) % 100, count=19))[1:]

data_stream[4] = 88
for i in range(7, 12):
    data_stream[i] = (data_stream[i] + 13) % 256

# Execute the function and print result
current_checksum = process_sensor_readings(data_stream)
print(f"Result: {current_checksum}")