def analyze_productivity(hours_worked, tasks_completed):
    efficiency_ratio = []
    idle_time_penalty = 0
    bonus_factor = 1.0

    for i, (hours, tasks) in enumerate(zip(hours_worked, tasks_completed)):
        if hours == 0:
            continue
        productivity = tasks / hours
        efficiency_ratio.append(productivity)

        if tasks > 5:
            bonus_factor += 0.1

        # Distractor: tracking irrelevant session count
        session_count = i + 1  

    avg_efficiency = sum(efficiency_ratio) / len(efficiency_ratio) if efficiency_ratio else 0
    return avg_efficiency, bonus_factor


def calculate_downtime_loss(schedule):
    total_downtime = 0
    for period in schedule:
        if period < 1:
            total_downtime += 1
    return total_downtime * 5  # arbitrary penalty per downtime


def calculate_performance_rating():
    # Core data
    hours_worked = [8, 6, 0, 7, 5]
    tasks_completed = [10, 4, 0, 9, 5]
    weekly_schedule = [2, 1, 3, 0, 4, 1]

    # Real computation path
    avg_efficiency, bonus = analyze_productivity(hours_worked, tasks_completed)
    
    # Distractor: unrelated string manipulation
    status_labels = ['active', 'idle', 'break', 'focus']
    status_concat = ''.join([label[0] for label in status_labels])
    magic_offset = len(status_concat)  # This will not affect final result

    # More distractors
    hypothetical_tasks = [t * 1.1 for t in tasks_completed]
    projected_effort = sum(hypothetical_tasks[:3])

    # Actual scoring logic
    base_score = avg_efficiency * 100
    adjusted_score = base_score * bonus
    
    # Another red herring: unused min/max calculation
    peak_productivity = max(avg_efficiency, 2.0) if avg_efficiency > 0 else 1.0
    floor_adjustment = min(adjusted_score, 50)

    # Final adjustment using only relevant variables
    downtime_loss = calculate_downtime_loss(weekly_schedule)
    final_score = adjusted_score - downtime_loss

    # Key output
    print(f"Result: {final_score}")
    return final_score

# Entry point
final_score = calculate_performance_rating()