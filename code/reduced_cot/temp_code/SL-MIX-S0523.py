def transform_paper_id(paper_title):
    # Convert title to lowercase and remove spaces
    cleaned = paper_title.lower().replace(' ', '')
    # Calculate hash of the cleaned title
    title_hash = hash(cleaned)
    # Extract last 4 digits of hash (absolute value)
    hash_suffix = abs(title_hash) % 10000
    return hash_suffix

def generate_verification_layer(base_value, transformations):
    result = base_value
    for op, operand in transformations:
        if op == 'multiply':
            result *= operand
        elif op == 'add':
            result += operand
        elif op == 'xor':
            result ^= operand
    return result

def create_academic_verifier(paper_titles):
    # Dictionary comprehension to get initial hashes
    paper_hashes = {title: transform_paper_id(title) for title in paper_titles}
    
    # Merge with predefined weights using dictionary merging
    weight_factors = {'quantum': 7, 'neural': 13, 'blockchain': 19}
    enhanced_weights = {**paper_hashes, **{k: v for k, v in weight_factors.items() if k not in paper_hashes}}
    
    # Lambda function for weighted combination
    combine_weighted = lambda x, y: (x * 3 + y * 5) % 1000
    
    # Apply transformations
    transformation_sequence = [
        ('multiply', 3),
        ('add', 127),
        ('xor', 0xABC)
    ]
    
    accumulator = 0
    for title, initial_hash in paper_hashes.items():
        weighted_value = combine_weighted(initial_hash, len(title))
        transformed_value = generate_verification_layer(weighted_value, transformation_sequence)
        accumulator += transformed_value
    
    # Final verification code calculation
    verification_code = (accumulator ^ 0xDEADBEEF) % 9973
    return verification_code

# Academic paper titles for verification
research_papers = [
    "Quantum Computing Approaches",
    "Neural Network Optimization",
    "Blockchain Security Analysis"
]

verification_code = create_academic_verifier(research_papers)
print(f"Result: {verification_code}")