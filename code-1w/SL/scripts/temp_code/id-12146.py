def process_data(buffer, threshold):
    temp_sum = 0
    magnitude = 0
    filtered_data = []
    debug_trace = []
    
    for index, val in enumerate(buffer):
        if val < 0:
            adjusted = abs(val) * 1.5
        else:
            adjusted = val + (index % 3)
            
        if adjusted > threshold * 1.2:
            magnitude += adjusted ** 0.5
            filtered_data.append(adjusted)
        elif adjusted > threshold * 0.8 and index % 2 == 0:
            magnitude += adjusted * 0.1
            filtered_data.append(adjusted)
        else:
            continue

    # Irrelevant string processing distraction
    status_log = "Data processed at level {}".format(threshold)
    log_parts = status_log.split(' ')
    code_signature = ''.join([part[0] for part in log_parts if len(part) > 0])
    checksum = sum(ord(c) for c in code_signature) % 50

    # Dummy state tracking with no real impact
    state_flags = [False, True, False]
    for i in range(len(filtered_data)):
        if i + 1 > checksum:
            state_flags[0] = not state_flags[0]

    # Actual computation path
    base_accum = 0
    for item in filtered_data:
        if item % 2 == 0:
            base_accum += int(item)
        else:
            base_accum -= int(item // 1.5)

    scaling_factor = len(filtered_data) + (magnitude // 10)
    intermediate_result = base_accum * (scaling_factor if scaling_factor > 0 else 1)

    # Secondary red herring: unused transformation
    transformed = tuple(round(x * 0.95, 2) for x in filtered_data)
    size_label = "L" if len(transformed) > 4 else "S"

    final_output = intermediate_result + checksum - len(state_flags)
    return final_output

# Input setup
stream_buffer = [4, -6, 8, 12, -3, 7, 11]
activation_threshold = 7

# Execution
final_output = process_data(stream_buffer, activation_threshold)
print(f"Result: {final_output}")