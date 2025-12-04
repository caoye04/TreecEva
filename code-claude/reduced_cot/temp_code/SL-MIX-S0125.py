# Text analysis for unique word processing

text = "The quick brown fox jumps over the lazy dog. The dog remains lazy while the fox is quick."

# Pre-processing phase
text = text.lower()
punctuation = {'.', ',', '!', '?', ';', ':'}
for p in punctuation:
    text = text.replace(p, '')
    
# Word extraction
words = text.split()
word_lengths = {len(word) for word in words}
avg_length = sum(word_lengths) / len(word_lengths)

# Word frequency analysis
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Apply transformations based on criteria
processed_words = []
reversed_words = [word[::-1] for word in words if len(word) > 3]
unused_score = sum(1 for word in reversed_words if word.startswith('e'))

# Process words with conditional logic
for word in words:
    if word.startswith('t'):
        processed_words.append(word + '_t')
    elif word in ['fox', 'dog']:
        processed_words.append(word + '_animal')
    else:
        processed_words.append(word)
        
# Filter irrelevant words (wouldn't affect the result)
irrelevant = lambda w: w.endswith('y') and len(w) < 5
filtered_words = list(filter(lambda w: not irrelevant(w), processed_words))

# Calculate metrics
unique_count = len(set(processed_words))
total_chars = sum(len(word) for word in processed_words)
average_word_length = total_chars / len(processed_words) if processed_words else 0

# Final result calculation
result_metric = unique_count
print(f"Result: {result_metric}")