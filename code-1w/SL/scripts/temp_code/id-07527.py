def calculate_final_score(responses, thresholds):
    total_score = 0
    bonus_active = False
    
    for i, (response, threshold) in enumerate(zip(responses, thresholds)):
        base_score = len(response) if len(response) > threshold else threshold - len(response)
        
        # Apply bonus if current response length exceeds index and previous bonus was active
        if i > 0 and len(response) > i and bonus_active:
            total_score += base_score * 1.5
            bonus_active = len(response) % 2 == 0
        else:
            total_score += base_score
            bonus_active = len(response) > threshold
    
    # Final adjustment based on character pattern
    vowel_count = sum(1 for c in ''.join(responses) if c.lower() in 'aeiou')
    total_score += vowel_count if vowel_count % 2 == 0 else -vowel_count

    return int(total_score)

# Input data
responses = ['hello', 'ai', 'benchmark', 'test']
thresholds = [4, 3, 6, 5]

# Execute calculation
total_score = calculate_final_score(responses, thresholds)
print(f"Result: {total_score}")