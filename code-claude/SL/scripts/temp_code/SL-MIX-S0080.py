from collections import Counter

# Function to analyze text from a customer review
def analyze_review(review_text):
    # Remove spaces and convert to lowercase
    cleaned_text = review_text.replace(" ", "").lower()
    
    # Count letter frequencies
    letter_counts = Counter(cleaned_text)
    
    # Remove non-alphabetic characters
    for char in list(letter_counts.keys()):
        if not char.isalpha():
            del letter_counts[char]
    
    # Get the count of the most common letter
    most_common_letter_count = letter_counts.most_common(1)[0][1]
    
    # Calculate average letter frequency
    avg_frequency = sum(letter_counts.values()) / len(letter_counts) if letter_counts else 0
    
    return most_common_letter_count

# Sample customer review
review = "The product arrived on time and works great! I would buy again."

# Analyze the review
result = analyze_review(review)
print(f"Result: {result}")