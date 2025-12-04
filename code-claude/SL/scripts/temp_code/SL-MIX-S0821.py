# Analyzing text feature overlap between documents

# Initialize document features
primary_features = ['abstract', 'introduction', 'methodology', 'results', 'conclusion']
secondary_features = ['summary', 'references', 'appendix', 'acknowledgments']

# Create document data with feature sets
document_data = [
    ['abstract', 'introduction', 'methodology', 'discussion'],
    ['summary', 'introduction', 'results', 'references'],
    ['abstract', 'methodology', 'results', 'conclusion'],
    ['introduction', 'methodology', 'results', 'appendix'],
    ['summary', 'methodology', 'references', 'acknowledgments']
]

# Calculate importance weights (not directly used in final calculation)
importance = {feature: i + 1 for i, feature in enumerate(primary_features)}
importance.update({feature: len(primary_features) - i for i, feature in enumerate(secondary_features)})

# Define primary feature set for comparison
primary_set = set(primary_features[:3])  # Only first 3 primary features

# Filter documents with at least 2 features
min_features = 2
filtered_count = 0
filtered_data = []

for doc in document_data:
    feature_count = sum(1 for feature in doc if feature in primary_features)
    if feature_count >= min_features:
        filtered_data.append(doc)
        filtered_count += 1

# Calculate secondary metrics (not used in final result)
avg_features = sum(len(doc) for doc in filtered_data) / len(filtered_data) if filtered_data else 0

# Calculate overlap score - this is the key operation
overlap_score = sum(map(lambda x: len(set(x) & primary_set), filtered_data))

# Calculate normalized score (distraction)
normalization_factor = len(primary_set) * len(filtered_data)
normalized_score = overlap_score / normalization_factor if normalization_factor > 0 else 0

# Additional metrics (not used in final answer)
unique_features = set().union(*filtered_data)
coverage_ratio = len(unique_features) / (len(primary_features) + len(secondary_features))

print(f"Result: {overlap_score}")