# Function to analyze text for a password strength checker
def analyze_text_complexity(text):
    # Remove spaces for processing
    processed_text = text.replace(" ", "")
    
    # Check if text meets minimum length
    meets_length = len(processed_text) >= 8
    
    # Filter out digits and special characters, keep only letters
    filtered_text = ''.join(char for char in processed_text if char.isalpha())
    
    # Count unique letters (case insensitive)
    unique_letters = len(set(filtered_text.lower()))
    
    # Calculate strength score based on unique characters
    strength_score = unique_letters * 2 if meets_length else unique_letters
    
    return unique_letters, strength_score

# Sample text to analyze
sample_text = "Hello Python 123"

# Get analysis results
unique_count, score = analyze_text_complexity(sample_text)

print(f"Result: {unique_count}")