def calculate_message_weight(message):
    # Calculate message importance based on content features
    word_count = len(message.split())
    has_urgent = 'urgent' in message.lower()
    has_important = 'important' in message.lower()
    has_critical = 'critical' in message.lower()
    
    # Base weight calculation
    base_weight = word_count * 0.5
    if has_urgent:
        base_weight += 15
    if has_important:
        base_weight += 10
    if has_critical:
        base_weight += 25
    
    # Modifier based on character count
    char_modifier = min(len(message) / 100, 2.5)
    return base_weight * char_modifier

def analyze_activity_patterns(activity_log):
    # Process user activity data to find patterns
    total_actions = sum(activity_log)
    if total_actions < 10:
        return {'engagement': 'low', 'factor': 0.7}
    elif total_actions < 50:
        return {'engagement': 'medium', 'factor': 1.0}
    else:
        return {'engagement': 'high', 'factor': 1.3}

def calculate_priority(messages, activity):
    # Main function to determine message priority
    security_threshold = 75
    activity_patterns = analyze_activity_patterns(activity)
    
    # Process messages
    weights = []
    categories = []
    
    for idx, msg in enumerate(messages):
        if idx % 3 == 0:  # Every third message gets special processing
            category = "standard"
            if "password" in msg.lower() or "security" in msg.lower():
                category = "security"
                if calculate_message_weight(msg) > security_threshold:
                    # This appears important but is actually a distraction
                    weights.append(security_threshold + 10)
                    categories.append("high_security")
                    continue
            weights.append(calculate_message_weight(msg))
            categories.append(category)
        else:
            # Normal processing for other messages
            weights.append(calculate_message_weight(msg))
            categories.append("standard")
    
    # Calculate priority score based on message weights and user activity
    base_score = 0
    security_count = categories.count("security")
    
    # Process weights and categories together
    for weight, category in zip(weights, categories):
        if category == "security":
            base_score += weight * 1.5
        else:
            base_score += weight
    
    # Apply activity factor
    engagement_factor = activity_patterns['factor']
    adjusted_score = base_score * engagement_factor
    
    # Apply time-based modifiers (distraction)
    time_factor = 0.9
    if security_count > 2:
        time_factor = 1.1
    
    # Calculate bitwise operations for verification code (distraction)
    verification_bits = 0
    for i, w in enumerate(weights):
        if i < 4:  # Only use first few weights
            verification_bits |= (int(w) & 0xFF) << (i * 8)
    
    # Final calculation with XOR verification (distraction)
    verification_check = (verification_bits ^ 0x12345678) % 100
    
    # Apply final adjustments
    result = int(adjusted_score + security_count * 5)
    
    # This is the actual calculation that matters
    if security_count > 0:
        result = result - (result % security_count) + security_count
    
    return result

# Test data
message_data = [
    "Meeting scheduled for tomorrow",
    "Please update your password for security reasons",
    "Team lunch on Friday",
    "URGENT: Server maintenance tonight",
    "Weekly report is ready for review"
]

user_activity = [5, 12, 8, 3, 7, 15, 4, 9]

# Calculate message statistics (distraction)
char_counts = [len(msg) for msg in message_data]
avg_length = sum(char_counts) / len(char_counts)
max_length = max(char_counts)
min_length = min(char_counts)

# Calculate activity statistics (distraction)
activity_sum = sum(user_activity)
activity_avg = activity_sum / len(user_activity)
activity_product = 1
for a in user_activity:
    activity_product *= (a % 5 + 1)

# Process messages and calculate priority
priority_score = calculate_priority(message_data, user_activity)

# Alternative calculations (distractions)
alternative_score = sum([calculate_message_weight(m) for m in message_data]) / len(message_data) * 2
weighted_alternative = alternative_score * (activity_avg / 10)

# Display results
print(f"Average message length: {avg_length:.2f}")
print(f"Activity metrics: {activity_sum}, {activity_avg:.2f}")
print(f"Alternative score: {alternative_score:.2f}")
print(f"Result: {priority_score}")