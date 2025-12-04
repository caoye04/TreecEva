# Function to analyze text data from a product catalog
def analyze_product_descriptions(text, prefix, min_length):
    # Clean and normalize the text
    text = text.lower()
    
    # Remove special characters
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char
    
    # Split into words
    words = cleaned_text.split()
    
    # Count words that match our criteria
    filtered_count = len([word for word in words if word.startswith(prefix) and len(word) > min_length])
    
    # Calculate average word length for reference
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return filtered_count

# Product catalog sample
catalog_text = "Premium tech gadgets: smartphone, smartwatch, smart-home devices. Smarter choices for modern living!"
prefix = "smart"
min_length = 5

# Analyze the catalog
result = analyze_product_descriptions(catalog_text, prefix, min_length)
print(f"Result: {result}")
