from collections import defaultdict

# Simulate employee feedback aggregation across multiple departments
def collect_feedback():
    raw_data = [
        ('engineering', 'Alice', [4, 5, 5, 4]),
        ('marketing', 'Bob', [3, 4, 4, 5]),
        ('engineering', 'Charlie', [5, 5, 4, 4]),
        ('sales', 'Diana', [4, 4, 3, 5]),
        ('marketing', 'Eve', [3, 3, 4, 4])
    ]

    feedback_dict = defaultdict(lambda: defaultdict(list))
    for dept, emp, ratings in raw_data:
        feedback_dict[dept][emp].extend(ratings)

    return feedback_dict

# Calculate average per employee and apply weighting logic
def compute_avg_ratings(feedback_dict):
    avg_dict = {}
    temp_tracker = {}  # Irrelevant tracking variable (distractor)

    total_employees = 0
    cumulative_sum = 0  # Semi-relevant accumulator (not used later)

    for dept, employees in feedback_dict.items():
        avg_dict[dept] = {}
        for emp, ratings in employees.items():
            avg_rating = sum(ratings) / len(ratings)
            avg_dict[dept][emp] = round(avg_rating, 2)
            cumulative_sum += avg_rating
            total_employees += 1

            # Dead code branch - never executed due to logic
            if len(ratings) > 100:
                temp_tracker[emp] = 'overloaded'

    return avg_dict

# Evaluate final performance score with weighted criteria
def evaluate_performance(feedback_dict, weights):
    dept_counts = defaultdict(int)
    dept_totals = defaultdict(float)

    # Count employees per department
    for dept, employees in feedback_dict.items():
        for emp, ratings in employees.items():
            dept_counts[dept] += 1
            dept_totals[dept] += sum(ratings) / len(ratings)

    # Compute department averages
    dept_averages = {d: dept_totals[d] / dept_counts[d] for d in dept_counts}

    # Weighted score calculation (only engineering weight matters)
    base_score = 0.0
    for dept, avg in dept_averages.items():
        if dept == 'engineering':
            base_score += avg * weights['engineering']
        elif dept == 'marketing':
            base_score += avg * weights['marketing']
        else:
            base_score += avg * 1.0  # Default weight (unused path)

    # Apply arbitrary scaling factor (distractor computation)
    adjustment_factor = len(dept_averages) * 0.1
    adjusted_score = base_score + adjustment_factor

    # Final non-linear transformation
    final_score = int((adjusted_score ** 1.5) + 0.5)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution flow
if __name__ == "__main__":
    feedback_data = collect_feedback()
    averaged_data = compute_avg_ratings(feedback_data)

    # Define weighting scheme
    weights = {
        'engineering': 1.2,
        'marketing': 1.0,
        'sales': 0.9
    }

    # Key execution point
    final_score = evaluate_performance(feedback_data, weights)