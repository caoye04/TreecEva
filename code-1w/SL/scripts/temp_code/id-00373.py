def process_readings(readings):
    checksum = 0
    thermal_capacity = 0
    baseline = 1024
    offset_table = [i ** 2 % 17 for i in range(15)]
    status_flags = {"idle": False, "active": True, "pending": False}
    readings_log = []  # Unused logging structure (distractor)

    def validate_entry(entry):
        return entry & 1 == 1  # Checks if odd (unused in main logic)

    def calculate_efficiency(idx, state):
        factor = 1.8 if state else 0.9
        adjustment = offset_table[idx % len(offset_table)]
        raw = idx * 13 + adjustment
        if raw > 100:
            raw //= 2
        return int(raw * factor)

    for i, reading in enumerate(readings):
        phase_state = (reading ^ i) % 3 == 0
        temp_flag = False

        if reading < 0:
            reading = abs(reading)
            temp_flag = True

        shifted = reading << 1
        shifted |= (shifted >> 5) & 1

        # Irrelevant transformation chain (distractor)
        encoded = ''.join([chr((reading + j) % 26 + 97) for j in range(3)])
        encoded = encoded.upper().replace('A', 'X')  # String manipulation (distractor)

        if i % 4 == 0:
            checksum += reading * 2
        elif i % 4 == 1:
            checksum -= reading // 3
        else:
            checksum += reading % 7

        # Key computation — answer derived here
        thermal_capacity = calculate_efficiency(i, phase_state)

        # Dead code path (distractor)
        if temp_flag and phase_state:
            for k in range(2):
                baseline ^= (baseline >> k)
        else:
            continue  # Misleading control flow

        readings_log.append(f"Entry-{i}: {encoded}")  # Unused append

    # Final red herring operation (irrelevant to answer)
    final_shift = baseline >> 3
    result_str = f"Final: {final_shift}".strip()  # String method use (distractor)

    print(f"Result: {thermal_capacity}")
    return thermal_capacity

# Input data with deterministic behavior
sensor_data = [42, 88, -13, 91, 17, 56]
result = process_readings(sensor_data)