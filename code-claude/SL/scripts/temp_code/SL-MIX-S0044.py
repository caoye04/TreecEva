# Email priority analyzer
# This function counts how many priority words appear in a message

def analyze_message(message):
    # Initialize counters
    word_count = len(message.split())
    char_count = len(message)
    
    # List of words that indicate high priority
    priority_words = ["urgent", "important", "immediate", "critical"]
    
    # Count words that match our priority list (case-insensitive)
    priority_count = sum(1 for word in message.split() if word.lower() in priority_words)
    
    # Calculate priority score based on word frequency
    priority_score = priority_count * 10
    
    # Adjust score based on message length (longer messages get lower priority)
    adjusted_score = priority_score - (word_count // 10)
    
    # Return the priority count for testing
    return priority_count

# Test the function with a sample message
message = "This is an URGENT message about an important meeting. Please respond immediately."
result = analyze_message(message)
print(f"Priority word count: {result}")