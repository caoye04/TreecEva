from collections import Counter

def analyze_text_similarity(text1, text2):
    # Convert texts to lowercase and count character frequencies
    freq1 = Counter(text1.lower())
    freq2 = Counter(text2.lower())

    # Irrelevant distraction: unused variable
    ignored_var = len(text1) + len(text2)

    # Find common characters based on minimum frequency in both texts
    common_chars = set(freq1.keys()) & set(freq2.keys())
    
    # Calculate count of common characters weighted by minimum frequency
    common_chars_count = []
    for char in common_chars:
        common_chars_count.append(min(freq1[char], freq2[char]))
    
    result = sum(common_chars_count)
    return result

# Main execution
document_a = "data analysis with machine learning models"
document_b = "machine learning models improve data accuracy"

final_score = analyze_text_similarity(document_a, document_b)
result = final_score
print(f"Result: {result}")