from collections import defaultdict

# Simulate player performance analytics in a strategy game
def analyze_player_engagement(player_data):
    engagement_levels = defaultdict(int)
    temp_aggregates = []
    base_multiplier = 1.0

    for session in player_data:
        duration = session['time']
        actions = session['actions']
        level = session['level']

        # Irrelevant computation: track session types (not used later)
        session_type = 'short' if duration < 30 else 'long'
        temp_aggregates.append(session_type)

        # Core engagement logic
        if level > 5:
            base_multiplier += 0.2
        elif level == 5:
            base_multiplier += 0.1

        for action in actions:
            if action == 'attack':
                engagement_levels['combat'] += 1 * base_multiplier
            elif action == 'build':
                engagement_levels['construction'] += 1 * base_multiplier
            elif action == 'explore':
                engagement_levels['exploration'] += 1 * base_multiplier

    # Dead code path: never accessed in current control flow
    if False:
        engagement_levels['dummy'] = sum(temp_aggregates.count(x) for x in temp_aggregates)

    return engagement_levels


def calculate_adjusted_score(engagement_stats, modifiers):
    score = 0
    penalty_factor = 0.95
    bonus_tracker = []

    # Scoring based on engagement distribution
    total_actions = sum(engagement_stats.values())
    combat_ratio = engagement_stats['combat'] / total_actions if total_actions else 0
    construction_ratio = engagement_stats['construction'] / total_actions if total_actions else 0

    # Logical branching with mixed conditions
    if combat_ratio > 0.4:
        score += 85
        bonus_tracker.append('combat_bonus')
    if construction_ratio > 0.3:
        score += 70
        bonus_tracker.append('construction_bonus')

    # Apply external modifiers (difficulty and environment)
    difficulty_mod = modifiers.get('difficulty', 1.0)
    environment_mod = modifiers.get('environment', 1.0)
    final_multiplier = difficulty_mod * environment_mod * penalty_factor

    # Red herring calculation: complex but unused expression
    unused_diagnostic = (sum(bonus_tracker.count(b) for b in bonus_tracker) + len(modifiers)) ** 0.5 if bonus_tracker else 0

    # Final score adjustment
    score *= final_multiplier

    # Additional distraction: update unused dictionary
    diagnostics = {}
    diagnostics['last_updated'] = 'N/A'
    diagnostics['version'] = 'v1.2'

    return int(score)

# Main execution
player_sessions = [
    {'time': 45, 'level': 6, 'actions': ['attack', 'attack', 'build', 'explore']},
    {'time': 25, 'level': 4, 'actions': ['build', 'build', 'attack']},
    {'time': 60, 'level': 7, 'actions': ['explore', 'attack', 'attack', 'attack', 'build']}
]

modifiers_config = {
    'difficulty': 1.15,
    'environment': 0.9,
    'weather': 'stormy',  # Unused field
    'terrain': 'mountain'  # Unused field
}

# Analyze behavior
stats = analyze_player_engagement(player_sessions)

# Compute adjusted score
final_score = calculate_adjusted_score(stats, modifiers_config)

# Output result
print(f"Result: {final_score}")