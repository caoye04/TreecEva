def analyze_system_phases():
    # Simulate a cyclic state machine with interference from auxiliary tracking
    states = ['IDLE', 'ACTIVE', 'PAUSED', 'ERROR', 'RECOVER']
    event_log = [3, 1, 4, 1, 5, 9, 2, 6]
    history = set()
    
    # Primary indices
    active_index = 2
    phase_shift = 0
    accumulator = 0
    
    # Misleading counters and irrelevant calculations
    debug_flag = False
    temp_offset = 0
    shadow_counter = 0
    for i in range(len(event_log)):
        if event_log[i] % 2 == 0:
            shadow_counter += 1
            temp_offset += i * 0.5
        else:
            accumulator += event_log[i]

    # Real logic begins: map events to index transitions
    for idx, val in enumerate(event_log):
        if val > 5:
            phase_shift += 1
        elif val < 3:
            phase_shift -= 1

    # Auxiliary diagnostic block (partially dead code)
    diagnostics = []
    for i, state in enumerate(states):
        if i % 2 == 0:
            diagnostics.append(f"Even-{i}")
    # Unused computation
    unused_magnitude = sum([x**2 for x in event_log if x % 3 == 0])

    # Core state transition logic
    phase_shift = (phase_shift * 2) % 7  # Modulate shift
    temp_state = (active_index + 1) % len(states)
    
    # Critical statement
    final_phase = (active_index + phase_shift) % len(states)
    
    # Red herring: post-processing that doesn't affect result
    if final_phase == 0:
        debug_flag = True
    redundant_list = [x for x in zip(states, enumerate(states))]
    
    # Output the required result
    print(f"Result: {final_phase}")

analyze_system_phases()