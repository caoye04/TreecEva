def analyze_pattern(sequence):
    count = 0
    temp_sum = 0
    for i in range(len(sequence)):
        if sequence[i] % 3 == 0 and sequence[i] % 5 != 0:
            count += 1
            temp_sum += sequence[i]
    return count, temp_sum


def validate_checksum(items):
    checksum = 0
    for item in items:
        checksum = (checksum + item * 3) % 101
    return checksum


def format_timestamp(millis):
    seconds = millis // 1000
    minutes = seconds // 60
    hours = minutes // 60
    return f'{hours:02}:{minutes%60:02}:{seconds%60:02}'


def process_metrics(data):
    # Extract numeric metrics
    values = [x for x in data if isinstance(x, int)]
    
    # Irrelevant string processing (distractor)
    labels = [str(x) for x in data if isinstance(x, str)]
    clean_labels = [lbl.strip().upper() for lbl in labels if lbl.strip()]
    label_lengths = {lbl: len(lbl) for lbl in clean_labels}
    
    # Real computation begins
    total = sum(values)
    valid_count = 0
    adjusted_total = 0
    
    for v in values:
        if v < 0:
            continue
        if v % 2 == 0:
            adjusted_total += v // 2
        else:
            adjusted_total += v * 2
        valid_count += 1
    
    # Nested conditional with modular arithmetic
    if total % 7 == 0:
        if valid_count > 5:
            adjusted_total -= (total // 7) % 10
        else:
            adjusted_total += 5
    else:
        adjusted_total += (total % 7)

    # Dummy dictionary operations (semi-relevant)
    stats = {
        'count': len(values),
        'sum': total,
        'adjusted': adjusted_total,
        'flag': 'OK' if valid_count >= 3 else 'LOW'
    }
    
    # Another distractor: unused function call
    _ = analyze_pattern(values)
    
    # Final transformation
    final_score = stats['adjusted']
    
    # Unused timestamp generation
    _ = format_timestamp(3650000)
    
    return final_score

# Main execution
data = [4, -2, 9, 14, 'temp', 5, 'sensor_1', 8, 11]
final_score = process_metrics(data)
print(f"Result: {final_score}")