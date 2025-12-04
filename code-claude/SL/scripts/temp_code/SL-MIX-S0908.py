import itertools

# Function to analyze text characteristics
def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    return {'words': word_count, 'chars': char_count}

# Sample book titles and authors
books = {
    'moby_dick': {'author': 'Herman Melville', 'year': 1851},
    'pride_and_prejudice': {'author': 'Jane Austen', 'year': 1813},
    'war_and_peace': {'author': 'Leo Tolstoy', 'year': 1869},
    '1984': {'author': 'George Orwell', 'year': 1949}
}

# Extract author names for comparison
author_names = [info['author'] for title, info in books.items()]

# Calculate publication years difference
year_range = max(info['year'] for info in books.values()) - min(info['year'] for info in books.values())

# Select two authors for character comparison
first_author = author_names[0].lower()
second_author = author_names[2].lower()

# Some analytics that we don't use directly
total_name_length = sum(len(name) for name in author_names)
average_name_length = total_name_length / len(author_names)

# Find character sets
first_chars = set(first_author)
second_chars = set(second_author)
all_chars = first_chars.union(second_chars)
unique_first = first_chars - second_chars

# Create combinations of authors for potential comparison
author_pairs = list(itertools.combinations(author_names, 2))
pair_count = len(author_pairs)

# Find characters common to both selected authors
character_intersection = first_chars.intersection(second_chars)
common_characters = len(character_intersection)

# Display result
print(f"Result: {common_characters}")