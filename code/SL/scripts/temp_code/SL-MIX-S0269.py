first_set = {'python', 'java', 'c++', 'javascript', 'ruby'}
second_set = {'python', 'javascript', 'go', 'rust', 'swift'}
language_count = len(first_set)
framework_count = len(second_set)
total_overlap = len(first_set & second_set)
print(f"Result: {total_overlap}")