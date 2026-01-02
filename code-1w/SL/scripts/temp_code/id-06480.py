def analyze_tag_combinations():
    tags = ['user', 'admin', 'guest', 'moderator', 'system']
    access_levels = [1, 3, 2, 3, 5]
    
    # Filter tags by length and associate with access
    filtered_tags = [tag for tag in tags if len(tag) > 4]
    tag_data = {tags[i]: access_levels[i] for i in range(len(tags))}
    
    # Dummy string operation to count vowels in all tags (irrelevant but minimal distraction)
    all_text = ''.join(tags)
    vowel_count = sum(1 for c in all_text if c in 'aeiou')
    
    # Count valid access pairs where level > 2
    valid_pairs = 0
    for level in access_levels:
        if level > 2:
            valid_pairs += 1
    
    total_combinations = valid_pairs * len(filtered_tags)
    
    # Additional irrelevant calculation
    avg_length = sum(len(tag) for tag in tags) / len(tags)
    
    print(f"Result: {total_combinations}")

analyze_tag_combinations()