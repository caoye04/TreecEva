import itertools

# Function to check if words share common letters with target
def analyze_words(word_list, target_letters):
    # Dictionary to store results
    results = {}
    
    # Process each word
    for word in word_list:
        # Convert word to lowercase for consistency
        word = word.lower()
        
        # Find unique letters that appear in both word and target_letters
        unique_letters = len(set(word) & set(target_letters))
        
        # Store word length for reference
        word_length = len(word)
        
        # Store results
        results[word] = {'common_letters': unique_letters, 'length': word_length}
    
    return results

# Sample data
words = ['python', 'coding', 'challenge']
letters = 'algorithm'

# Get the second word from the list
word = words[1]

# Find unique letters that appear in both the word and target letters
unique_letters = len(set(word) & set(letters))

# Display result
print(f"Result: {unique_letters}")