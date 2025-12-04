# Function to analyze text for unique characters
def analyze_text(text):
    # Convert text to lowercase for consistency
    text = text.lower()
    
    # Remove spaces for character counting
    no_spaces = text.replace(" ", "")
    total_chars = len(no_spaces)
    
    # Filter text to only include alphabetic characters
    filtered_text = "".join(char for char in text if char.isalpha())
    
    # Count unique letters in the filtered text
    unique_letters = len(set(filtered_text))
    
    # Calculate the ratio of unique to total characters (not used in final result)
    if total_chars > 0:
        uniqueness_ratio = unique_letters / total_chars
    else:
        uniqueness_ratio = 0
    
    return unique_letters

# Sample text to analyze
sample = "The quick brown fox jumps over the lazy dog"

# Call the function and print the result
result = analyze_text(sample)
print(f"Result: {result}")