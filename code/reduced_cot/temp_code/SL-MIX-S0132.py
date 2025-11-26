def analyze_text_patterns():
    text_samples = ["python programming", "data analysis", "machine learning", "python scripts", "data processing"]
    keywords = ["python", "data", "analysis"]
    
    # Find text samples containing any of the keywords
    matches = []
    for sample in text_samples:
        for keyword in keywords:
            if keyword in sample:
                matches.append(sample)
                break
    
    # Remove duplicates using set operations
    unique_matches = set(matches)
    
    # Get final count of unique matches
    result = len(unique_matches)
    final_count = result + 2  # Add small offset
    
    print(f"Target result: {final_count}")
    return final_count

analyze_text_patterns()