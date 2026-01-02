def calculate_final_score(records, limits):
    # Irrelevant preprocessing: counting record lengths and storing unused stats
    record_count = len(records)
    total_chars = sum(len(str(r)) for r in records)
    avg_length = total_chars / record_count if record_count > 0 else 0

    # Semi-relevant: filtering valid entries based on string patterns
    valid_entries = []
    invalid_count = 0
    for record in records:
        if isinstance(record, str):
            clean_record = record.strip().lower()
            if clean_record.startswith('usr') and clean_record.endswith('log'):
                if 'error' not in clean_record and 'fail' not in clean_record:
                    valid_entries.append(clean_record)
                else:
                    invalid_count += 1
        else:
            invalid_count += 1

    # Distractor: set operations with unused intermediate results
    unique_parts = set()
    for entry in valid_entries:
        parts = entry.split('_')
        unique_parts.update(parts)
    
    # Unused but plausible computation: counting certain substrings
    critical_flags = {part for part in unique_parts if 'crit' in part or 'alert' in part}
    flag_count = len(critical_flags)  # Not used later

    # Core logic: extract numeric IDs from valid entries (format: usr<ID>_v<version>.log)
    extracted_ids = []
    version_sum = 0.0
    for entry in valid_entries:
        if '_v' in entry and '.log' in entry:
            try:
                id_part = entry.split('_')[0][3:]  # remove 'usr' prefix
                version_part = entry.split('_')[1].split('.')[0][1:]  # remove 'v' prefix
                user_id = int(id_part)
                version = float(version_part)
                extracted_ids.append(user_id)
                version_sum += version
            except (ValueError, IndexError):
                continue

    # Secondary filtering using threshold map (provided)
    filtered_ids = [uid for uid in extracted_ids if uid >= limits.get('min_id', 0)]
    high_version_users = [uid for uid in filtered_ids if uid % 2 == 1]  # only odd IDs considered active

    # Final score calculation: weighted sum
    base_score = sum(filtered_ids) * 0.85
    bonus = len(high_version_users) * 5
    penalty = invalid_count * 2  # penalty for malformed records
    
    # Red herring: unused statistical measure
    if extracted_ids:
        mean_id = sum(extracted_ids) / len(extracted_ids)
        deviation_sum = sum(abs(uid - mean_id) for uid in extracted_ids)
        spread_factor = deviation_sum / len(extracted_ids)  # computed but unused

    final_score = base_score + bonus - penalty

    return int(final_score)  # deterministic integer result

# Input data with mixed validity and distractions
data_set = [
    'USR100_v1.log', 'usr205_v2.log', 'usr101_v1.5.log', 'USR99_v3.log',
    'usr_error_log', 'admin_debug.log', 'usr300_v2.log', 'usr405_v1.log',
    'usr101_v2.5.log', 'usr_invalid_fail.log', None, 'usr205_v3.log'
]

thresholds = {
    'min_id': 100,
    'max_version': 3.0
}

# Key execution point
final_score = calculate_final_score(data_set, thresholds)
print(f"Result: {final_score}")