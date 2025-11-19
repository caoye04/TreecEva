from collections import defaultdict
import statistics

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def get_quality_tier(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'

def process_batch(test_results):
    # State machine states: 'initial', 'phase1_complete', 'phase2_complete', 'finalized'
    state = 'initial'
    adjusted_scores = []
    prime_bonus = 0
    
    for i, score in enumerate(test_results):
        if state == 'initial':
            adjusted_scores.append(score + 2)
            state = 'phase1_complete'
        elif state == 'phase1_complete':
            if score > 85:
                adjusted_scores.append(score * 1.1)
            else:
                adjusted_scores.append(score)
            state = 'phase2_complete'
        elif state == 'phase2_complete':
            # Apply bonus if index+1 is prime and score > 80
            n = i + 1
            if n > 1:
                is_prime = True
                for j in range(2, int(n**0.5) + 1):
                    if n % j == 0:
                        is_prime = False
                        break
                if is_prime and score > 80:
                    prime_bonus += 5
            adjusted_scores.append(score - 1)
            state = 'finalized'
    
    # Calculate base rating
    if len(adjusted_scores) > 0:
        mean_score = statistics.mean(adjusted_scores)
        variance = statistics.variance(adjusted_scores) if len(adjusted_scores) > 1 else 0
        
        # Apply modifiers based on variance and prime bonus
        if variance < 10:
            modifier = 3
        elif variance < 50:
            modifier = 1
        else:
            modifier = -2
        
        base_rating = mean_score + modifier + prime_bonus
        
        # Final adjustment based on quality tier
        tier = get_quality_tier(base_rating)
        if tier == 'A':
            final_rating = base_rating * 1.05
        elif tier == 'B':
            final_rating = base_rating
        elif tier == 'C':
            final_rating = base_rating * 0.95
        else:
            final_rating = base_rating * 0.9
        
        return round(final_rating, 2)
    return 0.0

# Factory batch test results
chip_batch_tests = [
    [88, 92, 76],
    [95, 87, 91],
    [78, 82, 85]
]

batch_ratings = list(map(process_batch, chip_batch_tests))
composite_score = sum(batch_ratings)

# Apply LCM adjustment based on batch count
lcm_value = lcm(len(chip_batch_tests), int(statistics.mean(batch_ratings)))
final_batch_rating = composite_score + (lcm_value % 10)

print(f"Result: {final_batch_rating}")