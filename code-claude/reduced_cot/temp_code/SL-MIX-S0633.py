def calculate_priority(text):
    # Calculate message priority based on content and urgency markers
    urgency_markers = ['urgent', 'asap', 'immediately']
    importance_markers = ['critical', 'important', 'attention']
    
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Check for urgency and importance in the message
    urgency_score = sum(3 if marker in text_lower else 0 for marker in urgency_markers)
    importance_score = sum(2 if marker in text_lower else 0 for marker in importance_markers)
    
    # Calculate base priority
    base_priority = urgency_score + importance_score
    
    # Apply length modifier (shorter messages might be more direct/urgent)
    length_modifier = max(0, 5 - len(text) // 20)
    
    # Calculate final priority level (1-10 scale)
    raw_priority = base_priority + length_modifier
    
    # Ensure priority is within valid range using conditional expression
    priority_level = min(10, max(1, raw_priority))
    
    return priority_level

# Sample message for testing
message_text = "This is an urgent request that needs immediate attention."

# Calculate the priority level
priority_level = calculate_priority(message_text)

# Display result
print(f"Result: {priority_level}")