def analyze_text_samples(samples):
    # Process multiple text samples to find character frequencies
    char_counts = {}
    for idx, sample in enumerate(samples):
        # Track sample statistics (not used in final calculation)
        sample_length = len(sample)
        vowels_count = sum(1 for c in sample.lower() if c in 'aeiou')
        consonants_count = sum(1 for c in sample.lower() if c in 'bcdfghjklmnpqrstvwxyz')
        
        # Process each character in the sample
        for char in sample.lower():
            if char.isalpha():
                if char not in char_counts:
                    char_counts[char] = set()
                char_counts[char].add(idx)
    
    # Calculate word density metric (distraction)
    word_count = sum(len(s.split()) for s in samples)
    avg_words_per_sample = word_count / len(samples) if samples else 0
    
    # Find characters that appear in all samples
    counts = {}
    all_samples_set = set(range(len(samples)))
    for char, sample_indices in char_counts.items():
        # Track character frequency across all samples
        if len(sample_indices) == len(samples):
            counts[char] = 1
            
        # Characters in at least half the samples (distraction)
        half_threshold = len(samples) // 2
        if len(sample_indices) >= half_threshold:
            pass
    
    # Calculate the count of common characters
    common_letters = sum(counts.values())
    
    # Prepare additional statistics (distraction)
    unique_chars = len(char_counts)
    max_freq = max([len(indices) for indices in char_counts.values()]) if char_counts else 0
    
    print(f"Result: {common_letters}")
    return common_letters

# Test with sample data
text_samples = [
    "Python programming is fun!",
    "Python helps solve problems efficiently.",
    "Learning Python opens many opportunities."
]
result = analyze_text_samples(text_samples)