from collections import defaultdict
import math

# Simulate developer contribution analysis with noise and filtering
def analyze_contributions(logs):
    frequency = defaultdict(int)
    total_lines = 0
    noise_counter = 0  # Distractor: tracks irrelevant edits

    for entry in logs:
        action, lines = entry.split(':')
        line_count = int(lines)
        total_lines += line_count

        if 'refactor' in action or 'feat' in action:
            key = action.split('_')[0]
            frequency[key] += line_count
        elif 'docs' in action:
            noise_counter += line_count  # Semi-relevant but not used later
        else:
            continue

    return dict(frequency), total_lines

# Filter out minor contributions
def filter_significant(contribs, threshold=50):
    result = {}
    temp_debug_sum = 0  # Distractor variable

    for k, v in contribs.items():
        if v >= threshold:
            result[k] = v
        temp_debug_sum += v  # Computation not used

    # Additional filtering based on entropy-like measure
    if len(result) > 0:
        avg = sum(result.values()) / len(result)
        for k in list(result.keys()):
            if result[k] < avg * 0.6:
                del result[k]

    return result

# Calculate final rating with weighted scoring
def calculate_rating(contribs, penalty_factor):
    base_score = 0
    debug_weights = []  # Dead storage
    weight_map = {}

    # Assign dynamic weights using enumerate
    for i, (area, lines) in enumerate(contribs.items()):
        raw_weight = (i + 1) * 1.5
        weight_map[area] = raw_weight
        base_score += lines * raw_weight
        debug_weights.append(raw_weight)

    # Apply penalty based on project complexity
    complexity_factor = len(contribs) ** 1.2 if len(contribs) > 0 else 1
    adjusted_score = base_score * complexity_factor

    # Final penalty adjustment
    final_score = adjusted_score * (1 - penalty_factor)

    # Extra computation that looks important but isn't
    outlier_check = [v for v in contribs.values() if v > 200]
    if len(outlier_check) == 0:
        final_score -= 10  # Minor offset, but deterministic

    return int(final_score)

# Entry point
if __name__ == "__main__":
    # Raw development logs (action:type_of_change:number_of_lines)
    raw_logs = [
        "feat_user_auth:120",
        "refactor_db_schema:85",
        "docs_update_readme:30",
        "feat_payment_gateway:210",
        "chore_cleanup:15",
        "feat_ui_redesign:180",
        "refactor_api_layer:95"
    ]

    # Parse logs
    contributions_raw, total_sloc = analyze_contributions(raw_logs)

    # Track auxiliary metrics (not directly used)
    average_commit_size = total_sloc / len(raw_logs)
    high_effort_areas = [k for k, v in contributions_raw.items() if v > 100]

    # Filter significant contributions
    significant_contribs = filter_significant(contributions_raw, threshold=60)

    # Prepare penalty factor based on string patterns in logs
    penalty_basis = ''.join(raw_logs)
    refactor_count = penalty_basis.count('refactor')
    feat_count = penalty_basis.count('feat')
    penalty_factor = (refactor_count / (feat_count + refactor_count)) * 0.1 if (feat_count + refactor_count) > 0 else 0.05

    # Compute final score
    final_score = calculate_rating(significant_contribs, penalty_factor)

    # Print result
    print(f"Result: {final_score}")