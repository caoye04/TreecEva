def calculate_word_importance(word, position, is_title=False):
    # Complex word importance calculation
    length_factor = len(word) / 10
    position_factor = 1.0 / (position + 1) if position > 0 else 1.0
    title_bonus = 2.5 if is_title else 1.0
    
    # Misleading calculations that don't affect final result
    sentiment_score = sum(ord(c) % 5 for c in word) / 10
    frequency_penalty = (len(word) % 3) * 0.15
    
    return length_factor * position_factor * title_bonus

def analyze_keyword_matches(text, keywords):
    # Split text into words and remove punctuation
    words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text.lower()).split()
    
    # Count keyword occurrences (relevant)
    keyword_count = sum(1 for word in words if word in keywords)
    
    # Calculate misleading metrics
    avg_word_length = sum(len(word) for word in words) / max(1, len(words))
    unique_words = len(set(words))
    complexity_index = unique_words * avg_word_length / 10
    
    # Return only what matters for final calculation
    return keyword_count

def calculate_document_relevance(documents, keywords):
    # Initialize variables
    total_score = 0
    document_weights = {}
    misleading_factor = 42
    keyword_set = {k.lower() for k in keywords}
    
    # Create document weights - only some will be used
    for i, doc in enumerate(documents):
        # Misleading calculations
        doc_complexity = len(doc['content']) / 100
        doc_age_factor = (i % 5) * 0.8
        readability_score = sum(ord(c) % 7 for c in doc['title'][:5]) / 10
        
        # Only this actually matters
        document_weights[i] = 10 if doc['priority'] == 'high' else 5 if doc['priority'] == 'medium' else 1
    
    # Process documents
    relevant_docs = 0
    irrelevant_counter = 0
    
    for i, doc in enumerate(documents):
        # Misleading processing path for even-indexed documents
        if i % 2 == 0 and i > 0:
            irrelevant_counter += len(doc['title']) // 3
            misleading_factor = misleading_factor * 0.9 + irrelevant_counter
        
        # Calculate matches in title (relevant)
        title_matches = analyze_keyword_matches(doc['title'], keyword_set)
        
        # Calculate matches in content (relevant)
        content_matches = analyze_keyword_matches(doc['content'], keyword_set)
        
        # Conditional expression to determine document score
        doc_score = document_weights[i] * (title_matches * 2 + content_matches)
        
        # Track if document has any matches
        if title_matches > 0 or content_matches > 0:
            relevant_docs += 1
        
        # Accumulate total score
        total_score += doc_score
    
    # Calculate final relevance score with conditional expression
    relevance_multiplier = 1.5 if relevant_docs >= 3 else 1.0
    final_relevance = total_score * relevance_multiplier
    
    # More misleading calculations that don't affect result
    normalized_score = final_relevance / max(1, len(documents))
    adjusted_score = normalized_score * (1 + misleading_factor / 1000)
    
    return int(final_relevance)

# Document collection
documents = [
    {
        'title': 'Introduction to Python Programming',
        'content': 'Python is a high-level programming language known for its readability and simplicity.',
        'priority': 'high'
    },
    {
        'title': 'Data Structures in Computer Science',
        'content': 'Common data structures include arrays, linked lists, trees, and graphs.',
        'priority': 'medium'
    },
    {
        'title': 'Machine Learning Fundamentals',
        'content': 'Machine learning algorithms learn patterns from data to make predictions.',
        'priority': 'high'
    },
    {
        'title': 'Web Development Basics',
        'content': 'HTML, CSS, and JavaScript are fundamental technologies for web development.',
        'priority': 'low'
    }
]

# Keywords to search for
keywords = ['python', 'data', 'algorithms', 'programming']

# Process the documents with misleading temp variables
temp_result = sum(len(d['title']) for d in documents)
processing_factor = (temp_result % 10) * 3.7

# This is the key statement
total_relevance = calculate_document_relevance(documents, keywords)

# More misleading calculations after the key statement
final_output = total_relevance + (processing_factor if processing_factor > 20 else 0)
scaled_result = total_relevance * 1.25 if len(keywords) > 5 else total_relevance

print(f"Result: {total_relevance}")