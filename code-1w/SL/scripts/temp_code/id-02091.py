def analyze_workload(phases):
    total_load = 0
    peak_moment = 0
    temp_accumulator = 0

    for i, load in enumerate(phases):
        if i % 3 == 0:
            temp_accumulator += load * 1.5
        elif i % 4 == 0:
            temp_accumulator += load * 0.8
        else:
            temp_accumulator += load

        if temp_accumulator > peak_moment:
            peak_moment = temp_accumulator

        total_load += load

    average_load = total_load / len(phases) if phases else 0
    return total_load, peak_moment, average_load


def filter_segments(segments, threshold):
    filtered = []
    cumulative = 0
    for seg in segments:
        cumulative += seg
        if cumulative > threshold:
            filtered.append(cumulative)
            cumulative = 0  # Reset for next segment grouping
    return filtered or [0]


def calculate_system_capacity(segments):
    base_capacity = 0
    adjustment_factor = 1.25
    penalty = 0

    for i, seg in enumerate(segments):
        if i % 2 == 0:
            base_capacity += seg * adjustment_factor
        else:
            base_capacity += seg * 0.9

        # Simulate cooling cycle every 3rd segment
        if (i + 1) % 3 == 0:
            base_capacity *= 0.98

        # Irrelevant tracking variable (distractor)
        dummy_state = (base_capacity * 17) % 1000

    # Apply nonlinear scaling on final result
    if base_capacity > 100:
        base_capacity = (base_capacity ** 0.5) * 8

    return int(base_capacity)

# Main execution
work_phases = [12, 15, 22, 8, 30, 14, 25, 10, 18]
total_load, peak, avg_load = analyze_workload(work_phases)

# Generate segment candidates using slicing and zip
expanded = work_phases[::2] + [x * 2 for x in work_phases[1::3]]
paired = list(zip(expanded[:-1], expanded[1:]))
segment_candidates = [a + b for a, b in paired]

# Filter to get optimal segments
optimal_segments = filter_segments(segment_candidates, threshold=40)

# Introduce dead code path (misleading)
if len(optimal_segments) > 10:
    optimal_segments = optimal_segments[:5]
elif sum(optimal_segments) < 0:  # Impossible condition
    optimal_segments = [0]

# Key computation point
final_capacity = calculate_system_capacity(optimal_segments)

# Print result as required
print(f"Target result: {final_capacity}")