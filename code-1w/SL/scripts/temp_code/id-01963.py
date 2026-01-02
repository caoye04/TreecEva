def analyze_performance(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_buffer = []
    for entry in logs:
        if 'ERROR' in entry:
            continue
        if 'WARNING' in entry:
            temp_buffer.append(entry)
            continue
        valid_count += 1

    clean_data = logs[:total_entries]  # Redundant but misleading
    filtered = [entry for entry in clean_data if 'INFO' in entry]
    return valid_count, len(temp_buffer), len(filtered)

logs_input = [
    'INFO: System started',
    'INFO: User login',
    'WARNING: High memory usage',
    'INFO: Data processed',
    'ERROR: Disk failure',
    'INFO: Backup completed',
    'WARNING: CPU spike'
]

valid, warnings, info_count = analyze_performance(logs_input)

baseline = 100
adjustment = 0.95
penalty_factor = (warnings * 2) + 5

# Simulate contribution scoring using slicing and string analysis
def calculate_contribution_score(entries):
    scores = []
    for entry in entries:
        if 'INFO' in entry:
            # Use string method and slicing to derive weight
            keyword = entry.split(':')[1].strip().lower()
            score = len(keyword) + sum(1 for c in keyword if c in 'aeiou')
            scores.append(score)
        else:
            scores.append(0)
    return sum(scores) if scores else 0

contributions = calculate_contribution_score(logs_input)

# Auxiliary computation that looks relevant but isn't used directly
auxiliary_metric = (valid * info_count) - len([e for e in logs_input if 'WARNING' in e])

# Core logic hidden among distractions
temp_result = contributions * adjustment
offset_value = sum([len(s) for s in logs_input]) % 4  # Minor obfuscation

intermediate = (temp_result - penalty_factor) + offset_value

scaling_factor = 1.1  # Unused variable - red herring

final_score = 0
final_score = calculate_rating(contributions, penalty_factor)

def calculate_rating(contribs, penalty):
    base = contribs * 2.5
    deduction = min(penalty * 3, 20)
    extra_boost = 0
    if contribs > 10:
        extra_boost = 5
    rating = base - deduction + extra_boost
    return int(rating)

Result: {final_score}