# Function to analyze text message content
def analyze_message(message, target_letter):
    # Remove special characters for clarity
    cleaned = message.replace(',', '').replace('.', '')
    
    # Count words starting with the target letter
    count = len([word for word in message.split() if word.lower().startswith(target_letter)])
    
    # Calculate average word length for comparison
    avg_length = sum(len(word) for word in cleaned.split()) / len(cleaned.split()) if cleaned else 0
    
    # Determine if count meets threshold
    meets_threshold = count >= 3
    
    return count

# Sample message to analyze
message = "The teacher told the students to take their textbooks to the library"
target_letter = "t"

# Run analysis and display results
result = analyze_message(message, target_letter)
print(f"Result: {result}")