from collections import defaultdict

# Simulate player game statistics with redundant and misleading fields
def generate_player_data():
    data = {
        'player_id': 12345,
        'level': 7,
        'base_points': 850,
        'penalty_points': 45,
        'accuracy_rate': 0.92,
        'completed_levels': [1, 2, 3, 4, 5, 6, 7],
        'session_time_seconds': 2173,
        'power_ups_collected': 12,
        'distance_traveled': 4820.5,
        'enemy_defeated': 38,
        'unused_field_1': 999,  # red herring
        'temp_debug_flag': True  # misleading state
    }
    return data

# Auxiliary function with irrelevant computations
def analyze_session_rhythm(session_events):
    rhythm_pattern = defaultdict(int)
    total_gaps = 0
    for i in range(1, len(session_events)):
        gap = session_events[i] - session_events[i-1]
        rhythm_pattern[gap] += 1
        total_gaps += gap
    avg_gap = total_gaps / len(session_events) if session_events else 0
    # This entire function is dead code — never used in final calculation
    return rhythm_pattern, avg_gap

# Another unused helper to increase interference
def validate_player_progression(unlocked_levels, current_level):
    expected = list(range(1, current_level + 1))
    missing = [lvl for lvl in expected if lvl not in unlocked_levels]
    return len(missing) == 0 and current_level >= 5

# Core logic obscured among distractions
def calculate_final_score(data, multiplier):
    base = data['base_points']
    penalty = data['penalty_points']
    accuracy = data['accuracy_rate']
    level = data['level']

    # Real computation path begins
    raw_score = (base - penalty) * accuracy
    
    # Apply level-based tier modifier
    tier_mod = 1.0
    if level >= 8:
        tier_mod = 1.4
    elif level >= 5:
        tier_mod = 1.2
    else:
        tier_mod = 1.0

    scaled_score = raw_score * tier_mod

    # Bonus logic with conditional multiplier
    if multiplier > 0:
        adjusted_multiplier = min(max(multiplier, 0.5), 2.0)  # clamp multiplier
        scaled_score *= adjusted_multiplier

    # Irrelevant intermediate transformations
    normalized = scaled_score / 100.0
    capped_normalized = min(normalized, 10.0)
    denormalized = capped_normalized * 100.0  # round-trip that cancels effect

    # Final adjustment: apply diminishing returns above threshold
    if denormalized > 900:
        final_value = 900 + (denormalized - 900) * 0.5
    else:
        final_value = denormalized

    # Dead code section — no impact
    debug_info = {
        'raw': raw_score,
        'tier': tier_mod,
        'multiplier_applied': adjusted_multiplier if 'adjusted_multiplier' in locals() else 1.0,
        'overflow_adjusted': denormalized > 900
    }
    
    # Key execution point
    final_score = int(round(final_value))

    # More distractions: unused tracking
    stats_summary = {
        'total_actions': data.get('power_ups_collected', 0) + data.get('enemy_defeated', 0),
        'efficiency_ratio': data['base_points'] / max(data['session_time_seconds'], 1),
        'debug_flag': data['temp_debug_flag']
    }

    return final_score

# Main execution flow
player_data = generate_player_data()
bonus_multiplier = 1.5

# Unused data structures to add cognitive load
session_event_log = [105, 215, 310, 425, 512, 620, 718]
rhythm_analysis = analyze_session_rhythm(session_event_log)
progress_valid = validate_player_progression(player_data['completed_levels'], player_data['level'])

# Critical statement
final_score = calculate_final_score(player_data, bonus_multiplier)

print(f"Result: {final_score}")