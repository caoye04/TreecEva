import itertools

def analyze_stability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return variance < 5.0

def generate_thresholds(base, count):
    return [base * (1.1 ** i) for i in range(count)]

def filter_active_phases(phases, min_duration):
    # Irrelevant filtering - not used in final logic
    return [p for p in phases if p[1] > min_duration]

def trigger_sequence(phases, thresholds):
    state_log = []
    activation_count = 0
    temp_buffer = []  # Dead variable - not used later
    
    for i, (phase_id, duration, power) in enumerate(phases):
        # Simulate complex monitoring logic
        if i % 2 == 0:
            cumulative_power = sum(p[2] for p in phases[:i+1])
            normalized = cumulative_power / (i + 1)
            if normalized > thresholds[i % len(thresholds)]:
                state_log.append(True)
                activation_count += 1
            else:
                state_log.append(False)
        else:
            # Alternate path with dummy computation
            dummy_calc = (power ** 2) % 7
            if dummy_calc > 3:
                state_log.append(True)
                activation_count += 1
            else:
                state_log.append(False)
    
    # Critical decision point
    if len(state_log) >= 4 and activation_count >= 3:
        cycle_complete = True
        for window in itertools.pairwise(state_log):
            if window == (True, False):
                cycle_complete = False
                break
    else:
        cycle_complete = False
    
    # Final phase determination
    if cycle_complete:
        final_phase = 1
    else:
        final_phase = 0
    
    # Unrelated diagnostic output (no effect)
    diagnostics = {"transitions": len(list(itertools.groupby(state_log))), "max_run": max(sum(1 for _ in group) for key, group in itertools.groupby(state_log))}
    
    return final_phase

# Main execution
phases = [
    (1, 12, 8.5),
    (2, 8, 9.1),
    (3, 15, 7.3),
    (4, 6, 10.2),
    (5, 10, 8.8)
]

thresholds = generate_thresholds(8.0, 5)
active_phases = filter_active_phases(phases, 7)  # Computed but unused

final_phase = trigger_sequence(phases, thresholds)
print(f"Result: {final_phase}")