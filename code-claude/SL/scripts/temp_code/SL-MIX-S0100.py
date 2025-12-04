# Analyzing text from a customer feedback survey
feedback = "The product works well but shipping was delayed"

# Clean up the text for processing
processed_text = feedback.lower().strip()

# Extract all words from the feedback
words = processed_text.split()

# Calculate length of each word
word_lengths = [len(word) for word in words]

# Find the longest and shortest word lengths
max_length = max(word_lengths)
min_length = min(word_lengths)

# Calculate the average word length
avg_length = sum(word_lengths) / len(word_lengths)

# Round to 2 decimal places for reporting
rounded_avg = round(avg_length, 2)

print(f"Result: {avg_length}")