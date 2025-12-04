from collections import Counter

def process_text(text):
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove punctuation from each word
    clean_words = []
    for word in words:
        clean_word = ''
        for char in word:
            if char.isalnum():
                clean_word += char
        if clean_word:
            clean_words.append(clean_word)
    
    return clean_words

# Sample blog post about programming
blog_post = "Python is amazing! Python offers many libraries for data analysis. When coding in Python, readability matters."

# Process the text
processed_words = process_text(blog_post)

# Count word frequencies
word_counts = Counter(processed_words)

# Find the most common word count
most_common_count = word_counts.most_common(1)[0][1]

# Calculate average word length for comparison
total_length = sum(len(word) for word in processed_words)
avg_length = total_length / len(processed_words)

print(f"Result: {most_common_count}")