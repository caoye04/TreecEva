# Function to analyze common letters between two words
def analyze_words(word1, word2):
    # Remove any spaces and convert to lowercase
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    
    # Find length of each word
    len1 = len(word1)
    len2 = len(word2)
    
    # Calculate the average word length
    avg_len = (len1 + len2) / 2
    
    # Find common letters between the two words
    common_letters = len(set(word1) & set(word2))
    
    # Calculate unique letters in each word
    unique_in_word1 = len(set(word1) - set(word2))
    unique_in_word2 = len(set(word2) - set(word1))
    
    return common_letters, unique_in_word1, unique_in_word2

# Test with two sample words
word1 = "python"
word2 = "program"

# Run the analysis
result, unique1, unique2 = analyze_words(word1, word2)

print(f"Result: {result}")