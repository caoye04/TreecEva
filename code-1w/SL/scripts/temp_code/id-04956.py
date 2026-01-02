def analyze_compliance(records):
    base_threshold = 75
    penalty_factor = 0.9
    bonus_multiplier = 1.2
    temporal_weight = 0.85
    dummy_counter = 0
    redundant_sum = 0
    placeholder_data = [0] * len(records)

    for i, record in enumerate(records):
        if isinstance(record, dict) and 'status' in record:
            if record['status'] == 'active':
                dummy_counter += 1
                if 'last_audit' in record:
                    days_ago = 2023 - record['last_audit']
                    if days_ago > 2:
                        placeholder_data[i] = base_threshold * penalty_factor
                    else:
                        placeholder_data[i] = base_threshold * bonus_multiplier
                else:
                    placeholder_data[i] = base_threshold * temporal_weight
            elif record['status'] == 'suspended':
                placeholder_data[i] = base_threshold * 0.5
        else:
            placeholder_data[i] = 0

    # Irrelevant aggregation (dead path)
    for x in placeholder_data:
        redundant_sum += x ** 0.5 if x > 0 else 0

    # Decoy function that's never called
    def decoy_normalization(data):
        return [d / max(data) for d in data if d > 0]

    # Real processing begins here
    valid_records = list(filter(lambda r: isinstance(r, dict) and r.get('status') == 'active', records))
    total_weight = 0.0
    weighted_score = 0.0

    audit_years = [r['last_audit'] for r in valid_records if 'last_audit' in r]
    year_counts = {y: audit_years.count(y) for y in set(audit_years)}

    for record in valid_records:
        weight = 1.0
        if 'last_audit' in record:
            year = record['last_audit']
            frequency = year_counts[year]
            if frequency > 1:
                weight *= 1.1
            if year == 2023:
                weight *= 1.15
        if 'flags' in record:
            flag_count = len([f for f in record['flags'] if f.startswith('compliance_')])
            weight *= (0.95 ** flag_count)

        total_weight += weight
        weighted_score += base_threshold * weight

    average_score = weighted_score / total_weight if total_weight > 0 else 0

    # Secondary distraction: unused transformation chain
    zipped = list(zip(audit_years, [temporal_weight] * len(audit_years)))
    mapped = list(map(lambda x: x[0] * x[1], zipped))
    filtered = [m for m in mapped if m > 1700]

    # Actual key computation path
    recent_audits = sum(1 for r in valid_records if r.get('last_audit') == 2023)
    total_active = len(valid_records)
    compliance_ratio = recent_audits / total_active if total_active > 0 else 0

    process_efficiency = average_score / base_threshold

    # Critical statement
    filtration_score = process_efficiency * compliance_ratio

    # Unrelated string processing (distractor)
    log_entry = "Audit summary complete: {} records processed".format(len(records))
    log_tokens = log_entry.upper().split()
    token_lengths = [len(token) for token in log_tokens]
    avg_token_len = sum(token_lengths) / len(token_lengths) if token_lengths else 0

    # Output target result
    print(f"Result: {filtration_score}")

    return filtration_score

# Input data
input_records = [
    {'status': 'active', 'last_audit': 2023, 'flags': ['compliance_doc_missing']},
    {'status': 'active', 'last_audit': 2022},
    {'status': 'active', 'last_audit': 2023},
    {'status': 'suspended'},
    {'status': 'active', 'last_audit': 2023, 'flags': ['compliance_update_pending', 'compliance_doc_missing']},
    {'status': 'active', 'last_audit': 2021},
    {'status': 'inactive'}
]

result = analyze_compliance(input_records)