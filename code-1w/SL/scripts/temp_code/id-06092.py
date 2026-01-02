def process_developer_metrics(dev_data_str):
    # Parse developer activity data from string
    entries = dev_data_str.split(',')
    raw_values = [entry.strip().lower() for entry in entries]

    # Extract contributions and distractions
    contributions = []
    temp_logs = []
    auxiliary_sum = 0

    for val in raw_values:
        if 'feat' in val:
            num = int(val.replace('feat', ''))
            contributions.append(num * 1.5)
        elif 'bug' in val:
            num = int(val.replace('bug', ''))
            auxiliary_sum += num ** 2  # Red herring: not used later
        else:
            temp_logs.append(val)  # Dead storage

    # Irrelevant transformation
    temp_logs = [log.upper() for log in temp_logs if len(log) > 3]

    # Secondary filtering distraction
    filtered_contributions = []
    for c in contributions:
        if c > 5:
            filtered_contributions.append(c + 2)
        else:
            filtered_contributions.append(c)

    # Unused aggregation
    total_aux = sum([x % 4 for x in filtered_contributions])

    # Real computation begins
    base_total = sum(contributions)
    count_bonus = len(contributions) * 0.8

    # Simulate penalty factor based on length patterns (misleading but structured)
    penalty_factor = 1.0
    if len(temp_logs) > 2:
        penalty_factor *= 0.9
    else:
        penalty_factor *= 1.1

    def calculate_rating(contribs, penalty):
        raw_rating = sum(contribs) + count_bonus
        adjusted = raw_rating * penalty
        if adjusted > 50:
            return int(adjusted // 2)
        elif adjusted > 30:
            return int(adjusted // 1.5)
        else:
            return int(adjusted)

    final_score = calculate_rating(contributions, penalty_factor)
    
    # Additional irrelevant state tracking
    audit_trail = f'Score computed with {len(contributions)} items'
    audit_trail += f' and {len(temp_logs)} logs'

    print(f"Result: {final_score}")
    return final_score

# Execute with sample data
data_string = "feat10, feat2, bug5, feat7, docupdate, feat3"
process_developer_metrics(data_string)