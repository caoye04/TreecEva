from collections import defaultdict

# Simulate employee performance metrics across shifts
def analyze_shift_data(entries):
    shift_count = defaultdict(int)
    total_hours = 0
    distractions = 0  # Irrelevant counter for noise

    for entry in entries:
        shift_type = entry['shift']
        shift_count[shift_type] += 1
        total_hours += entry['hours']
        if entry['distractions'] > 5:
            distractions += 1  # Distractor: not used later

    return dict(shift_count), total_hours

def calculate_efficiency(logs):
    efficiency_map = {}
    placeholder_sum = 0

    for log in logs:
        task = log['type']
        time_spent = log['time']
        completed = log['completed']

        # Conditional expression with some red herring logic
        base_efficiency = 1.0 if completed else 0.5
        penalty = 0.1 if time_spent > 8 else 0.05 if time_spent > 4 else 0
        adjusted = base_efficiency - penalty

        efficiency_map[task] = max(adjusted, 0.0)
        placeholder_sum += time_spent  # Not used afterward

    # Use string method to generate fake metric
    key_string = "efficiency_tracking_log"
    char_count = len(key_string.replace('_', ''))  # Distractor: 19, unused

    return efficiency_map

def evaluate_performance(output, defects):
    base = sum(output)
    deduction = sum([d * 2 for d in defects if d > 1])  # Only penalize significant defects
    bonus = 10 if len(defects) < 3 else 0

    # Critical logical chain with interdependent steps
    temp_result = base - deduction + bonus
    scaling_factor = 1.5 if temp_result > 50 else 1.2
    final_score = int(temp_result * scaling_factor)  # This will be the answer

    # Dead code path — never executed but adds cognitive load
    if False:
        fallback = 0
        for i in range(len(defects)):
            fallback += defects[i] // (i + 1)
        final_score = fallback

    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    shift_entries = [
        {'shift': 'morning', 'hours': 8, 'distractions': 3},
        {'shift': 'evening', 'hours': 7, 'distractions': 6},
        {'shift': 'night', 'hours': 6, 'distractions': 2},
        {'shift': 'morning', 'hours': 9, 'distractions': 4}
    ]

    task_logs = [
        {'type': 'coding', 'time': 6, 'completed': True},
        {'type': 'review', 'time': 10, 'completed': True},
        {'type': 'debug', 'time': 3, 'completed': False}
    ]

    # Step 1: Analyze shifts (produces unused data)
    shift_summary, total_worked = analyze_shift_data(shift_entries)

    # Step 2: Calculate efficiency map (semi-relevant)
    efficiencies = calculate_efficiency(task_logs)

    # Step 3: Prepare productivity and error arrays (core inputs)
    productivity = [80, 90, 75]
    error_rates = [2, 0, 3]  # Only values >1 matter in evaluation

    # Key statement
    final_score = evaluate_performance(productivity, error_rates)

    print(f"Result: {final_score}")