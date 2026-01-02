def validate_entry(data):
    errors = 0
    rules = {
        'min_length': 5,
        'has_digit': True,
        'max_repeats': 2
    }
    
    if len(data['name']) < rules['min_length']:
        errors += 1
    
    if not any(c.isdigit() for c in data['name']):
        errors += 1
    
    consecutive = 1
    for i in range(1, len(data['name'])):
        if data['name'][i] == data['name'][i-1]:
            consecutive += 1
            if consecutive > rules['max_repeats']:
                errors += 1
                break
        else:
            consecutive = 1
    
    # Irrelevant metric (mild distraction)
    warning_count = data.get('warnings', 0)
    
    score = 10 - (errors * 2)
    threshold_score = score if score >= 6 else 0
    
    return threshold_score

entry = {
    'name': 'bobby1',
    'warnings': 3
}

threshold_score = validate_entry(entry)
print(f"Result: {threshold_score}")