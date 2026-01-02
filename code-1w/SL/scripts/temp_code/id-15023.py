def calculate_rating(data):
    base_score = 0
    bonus_multiplier = 1.0
    penalty_applied = False

    # Extract and process engagement metrics
    views = data.get('views', 0)
    likes = data.get('likes', 0)
    shares = data.get('shares', 0)
    duration = data.get('duration_minutes', 0)

    # Irrelevant distraction: user session tracking (not used in final score)
    session_tracker = {}
    for i in range(min(views, 5)):
        session_id = f'sess_{i}'
        session_tracker[session_id] = {'active': True, 'timeout': 30}

    # Core scoring logic
    if views > 1000:
        base_score += 25
        if likes > 500:
            base_score += 20
            if likes / views > 0.1:
                bonus_multiplier *= 1.2

    if shares > 0:
        referral_boost = min(shares * 2, 15)
        base_score += referral_boost

    # Duration impact
    if duration > 10:
        base_score += 10
        if duration > 30:
            base_score += 5

    # Distraction: complex but unused decay function
    def decay_factor(t):
        return 0.95 ** (t / 7) if t > 7 else 1.0

    hypothetical_decay = decay_factor(14)  # Unused

    # Penalty for low engagement ratio
    if views > 0 and (likes + shares) / views < 0.05:
        penalty_applied = True
        base_score -= 10

    # Final computation
    raw_score = base_score * bonus_multiplier
    
    # Round to nearest integer
    final_score = int(round(raw_score))

    # Additional red herring: string manipulation with no effect
    status_msg = "Penalty Applied" if penalty_applied else "All Good"
    status_parts = status_msg.split(' ')
    joined_status = '-'.join(status_parts).lower()
    padded_status = f"[LOG]: {joined_status}"  # Unused log

    return final_score

# Simulated input data
engagement_data = {
    'views': 2500,
    'likes': 300,
    'shares': 8,
    'duration_minutes': 45,
    'category': 'tutorial'
}

# Execution point of interest
final_score = calculate_rating(engagement_data)
print(f"Result: {final_score}")