def count_occurrences(text, target_chars):
    # Count occurrences of specified characters
    count = 0
    for char in text.lower():
        if char in target_chars:
            count += 1
    return count

def calculate_priority(message, settings):
    # Initialize priority score
    priority = 0
    
    # Extract message properties
    is_urgent = "urgent" in message.lower()
    is_important = "important" in message.lower()
    has_deadline = "deadline" in message.lower() or "due" in message.lower()
    
    # Check for special keywords (some are distractors)
    special_keywords = {"review": 5, "approve": 8, "reject": 7, "discuss": 3, "consider": 2}
    keyword_bonus = 0
    for keyword, value in special_keywords.items():
        if keyword in message.lower():
            keyword_bonus += value
    
    # Calculate base score
    base_score = len(message) // 10
    
    # Apply keyword modifiers
    if is_urgent and is_important:
        priority = base_score * 3
    elif is_urgent:
        priority = base_score * 2
    elif is_important:
        priority = base_score * 1.5
    else:
        priority = base_score
    
    # Apply deadline modifier
    if has_deadline:
        priority += 15
    
    # Check settings for additional modifiers
    category = settings.get("category", "normal")
    if category == "critical":
        priority *= 2
    elif category == "low":
        priority /= 2
    
    # Apply time-based settings (distractor)
    time_settings = settings.get("time_settings", {})
    if time_settings:
        morning_priority = time_settings.get("morning", 1.0)
        afternoon_priority = time_settings.get("afternoon", 0.9)
        evening_priority = time_settings.get("evening", 0.8)
    
    # Count question and exclamation marks
    question_marks = count_occurrences(message, "?")
    exclamation_marks = count_occurrences(message, "!")
    
    # Apply punctuation modifiers
    priority += exclamation_marks * 5
    priority += question_marks * 2
    
    # Apply keyword bonus
    priority += keyword_bonus
    
    # Apply filters (distractor)
    filters = settings.get("filters", [])
    filter_count = len(filters)
    
    # Round to nearest integer
    return round(priority)

# Test message and settings
message = "Important! Review the proposal before the deadline on Friday."
settings = {"category": "critical", "filters": ["spam", "automated"], "time_settings": {"morning": 1.2, "afternoon": 1.0, "evening": 0.8}}

# Calculate priority score
priority_score = calculate_priority(message, settings)
print(f"Result: {priority_score}")