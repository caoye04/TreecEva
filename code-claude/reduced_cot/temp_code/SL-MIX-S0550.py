from collections import Counter

# Text processing function to analyze document chunking
def analyze_document(text, chunk_size):
    # Count character frequencies
    char_freq = Counter(text)
    most_common = char_freq.most_common(1)[0][0]
    
    # Calculate optimal number of chunks needed
    optimal_chunks = (len(text) + chunk_size - 1) // chunk_size
    
    # Prepare chunks for processing
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Count spaces in first chunk if it exists
    spaces_in_first = chunks[0].count(' ') if chunks else 0
    
    print(f"Result: {optimal_chunks}")
    return optimal_chunks

# Sample document
text = "Python slicing is a flexible tool that returns a new sequence containing elements from the original sequence."
document_stats = analyze_document(text, 25)