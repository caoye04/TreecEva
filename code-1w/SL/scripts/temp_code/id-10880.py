def analyze_pattern(sequence):
    counts = {c: sequence.count(c) for c in set(sequence)}
    unique_chars = len(counts)
    max_freq = max(counts.values()) if counts else 0
    entropy_proxy = unique_chars * max_freq
    return entropy_proxy


def validate_stability(readings):
    avg = sum(readings) / len(readings) if readings else 0
    variance = sum((x - avg) ** 2 for x in readings) / len(readings) if readings else 0
    stable = variance < 15
    return stable, avg

# Simulated diagnostic data from system logs
diagnostic_log = "aaabbcacccbaa"
reading_sequence = [3, 5, 7, 4, 6, 5, 8, 5, 3]

# Extract character pattern features
pattern_metric = analyze_pattern(diagnostic_log)

# Assess signal stability
is_stable, mean_value = validate_stability(reading_sequence)

# Generate auxiliary metrics (partially irrelevant)
signal_power = sum(r**2 for r in reading_sequence) / len(reading_sequence)
noise_floor = 2.5 if not is_stable else 1.2
adjustment_factor = 0.8 if pattern_metric > 10 else 1.1

# Base performance indicators
base_metrics = {
    'baseline': 42,
    'efficiency': 0.93,
    'complexity_weight': len(diagnostic_log) // 3
}

# Bonus conditions based on combined heuristics
bonus_flags = []
if pattern_metric >= 9 and is_stable:
    bonus_flags.append('PATTERN_STABLE')
if mean_value > 5:
    bonus_flags.append('HIGH_MEAN')
if 'a' in diagnostic_log and diagnostic_log.count('c') % 2 == 0:
    bonus_flags.append('SYMMETRY_C')

# Misleading intermediate calculation (distractor)
temp_correction = (signal_power - noise_floor) * adjustment_factor
impact_summary = [temp_correction * 0.1 for _ in range(3)]  # Not used later

# Core logic: compute final score using relevant state
def calculate_performance(flags, base):
    score = base['baseline']
    multiplier = base['efficiency']
    
    if 'PATTERN_STABLE' in flags:
        score += 15
    if 'HIGH_MEAN' in flags:
        score += 10 * base['complexity_weight']
    if 'SYMMETRY_C' in flags:
        multiplier *= 1.2
    
    # Apply compound effect
    score *= multiplier
    
    # Additional tweak based on auxiliary state (semi-relevant)
    if is_stable and len(flags) >= 2:
        score += 5
    
    return int(score)

# Final computation
calculate_performance.__globals__.update(globals())
final_score = calculate_performance(bonus_flags, base_metrics)

print(f"Result: {final_score}")