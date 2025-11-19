from collections import defaultdict
import itertools

def calculate_security_metrics(attempts_log):
    success_flags = 0b10101010
    failure_flags = 0b01010101
    base_score = 100
    
    user_scores = defaultdict(int)
    access_patterns = set()
    
    for user_id, attempt_flags in attempts_log:
        if attempt_flags & success_flags:
            user_scores[user_id] += (attempt_flags & success_flags).bit_count()
            access_patterns.add(frozenset([user_id, 'success']))
        elif attempt_flags & failure_flags:
            user_scores[user_id] -= (attempt_flags & failure_flags).bit_count()
            if user_scores[user_id] < 0 and len(access_patterns) > 0:
                user_scores[user_id] = 0
            access_patterns.add(frozenset([user_id, 'failure']))
    
    pattern_combinations = list(itertools.combinations(access_patterns, 2))
    security_bonus = len(pattern_combinations) if pattern_combinations else 0
    
    total_user_score = sum(user_scores.values())
    final_security_score = base_score + total_user_score + security_bonus
    
    return final_security_score

# Authentication log: (user_id, bit_flags)
auth_log = [
    ('admin', 0b11001100),
    ('user1', 0b10100010),
    ('guest', 0b00110100),
    ('admin', 0b01010000),
    ('user1', 0b11110000),
    ('guest', 0b00001111)
]

final_security_score = calculate_security_metrics(auth_log)
print(f"Result: {final_security_score}")