from collections import defaultdict, Counter

# Simulate project contribution analysis across teams
def analyze_contributions(team_records):
    contribution_count = defaultdict(int)
    total_effort = 0
    noise_accumulator = 0  # Distractor: used in irrelevant computation

    for team, records in team_records.items():
        for entry in records:
            role = entry['role']
            effort = entry['hours']
            success = entry['success_factor']

            contribution_count[role] += effort * success
            total_effort += effort

            # Irrelevant nested logic (distractor)
            if effort > 20:
                temp_boost = effort * 0.1
                noise_accumulator += temp_boost
                if success > 0.8:
                    noise_accumulator -= temp_boost * 0.3

    return contribution_count, total_effort


def compute_weighted_ranks(contributions):
    ranked_roles = []
    weights = {'senior': 3.0, 'mid': 2.0, 'junior': 1.0}
    decay_factor = 0.95  # Unused in final path but looks important

    for role, score in contributions.items():
        level = role.split('_')[0]
        if level in weights:
            weighted_score = score * weights[level]
            ranked_roles.append((role, weighted_score))

    # Sorting with enumerate to simulate detailed processing
    sorted_roles = sorted(ranked_roles, key=lambda x: x[1], reverse=True)
    final_ranking = {}
    for idx, (role, score) in enumerate(sorted_roles):
        final_ranking[role] = idx + 1  # Rank position

    return final_ranking


def calculate_rating(contributions, impacts):
    base_rating = 0
    bonus_pool = 0.0  # Looks important but partially irrelevant
    penalty = 0

    impact_counter = Counter(impacts)

    for role, value in contributions.items():
        if 'senior' in role:
            base_rating += value * 1.5
        elif 'mid' in role:
            base_rating += value * 1.0
        else:
            base_rating += value * 0.7

        # Complex conditional that appears meaningful
        role_type = role.split('_')[0]
        if role_type in impact_counter and impact_counter[role_type] > 1:
            bonus_pool += value * 0.05

    # Additional logic with early exit red herring
    for impact_level in impacts:
        if impact_level == 'critical':
            penalty -= 5
            break  # Suggests significance, but minimal effect

    # Final adjustment: only base_rating matters
    final_rating = base_rating + penalty  # bonus_pool intentionally excluded

    return int(final_rating)

# Main execution block
if __name__ == '__main__':
    project_data = {
        'team_alpha': [
            {'role': 'senior_lead', 'hours': 45, 'success_factor': 0.9},
            {'role': 'mid_developer', 'hours': 30, 'success_factor': 0.75},
            {'role': 'junior_dev', 'hours': 20, 'success_factor': 0.6}
        ],
        'team_beta': [
            {'role': 'senior_architect', 'hours': 40, 'success_factor': 0.95},
            {'role': 'mid_analyst', 'hours': 35, 'success_factor': 0.8},
            {'role': 'junior_tester', 'hours': 15, 'success_factor': 0.65}
        ]
    }

    # Step 1: Analyze raw contributions
    contributions, effort_sum = analyze_contributions(project_data)

    # Step 2: Compute ranks (not used in final score - distractor)
    rankings = compute_weighted_ranks(contributions)

    # Step 3: Define impact levels (simulates external input)
    impact_levels = ['critical', 'high', 'high', 'medium']

    # Key statement
    final_score = calculate_rating(contributions, impact_levels)

    # Print result as required
    print(f"Result: {final_score}")