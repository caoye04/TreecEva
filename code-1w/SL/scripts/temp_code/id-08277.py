def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    peak_activity = 0
    distraction_count = 0  # Distractor: not used in final result

    for day, hours in enumerate(logs, start=1):
        if hours > 8:
            peak_activity += 1
        elif hours < 4:
            idle_periods += 1
        total_hours += hours

        # Fake complexity: irrelevant pattern detection
        if day % 3 == 0 and hours < 5:
            distraction_count += 1

    average_load = total_hours / len(logs)
    return total_hours, average_load, peak_activity, idle_periods


def calculate_rating(contribs, efficiency_map):
    base_rating = 0
    bonus_factor = 0.0
    temp_result = []

    # Real logic mixed with red herring
    for i, (name, count) in enumerate(contribs.items()):
        scale = efficiency_map.get(name, 1.0)
        contribution_score = count * scale
        
        # Meaningless transformation
        if contribution_score > 10:
            bonus_factor += 0.1
        
        temp_result.append((i, contribution_score))

    # Core calculation
    aggregated = sum(score for _, score in temp_result)
    adjustment = len(temp_result) * bonus_factor
    return int(aggregated + adjustment)

# Simulated dataset
project_logs = [7, 8, 6, 9, 5, 7, 10]
_, avg_utilization, _, _ = analyze_productivity(project_logs)

contributions = {'frontend': 12, 'backend': 15, 'devops': 8, 'docs': 6}
efficiency = {'frontend': 1.2, 'backend': 1.5, 'devops': 1.1}  # Note: 'docs' missing intentionally

# Key computational step
final_score = calculate_rating(contributions, efficiency)

# Print required output
print(f"Result: {final_score}")