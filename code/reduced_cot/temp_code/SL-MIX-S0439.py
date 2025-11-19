from functools import reduce

def custom_hash(s):
    return reduce(lambda acc, c: (acc * 31 + ord(c)) % 1000003, s, 0)

class PaperMetadata:
    def __init__(self, title, authors, year):
        self.title = title
        self.authors = authors
        self.year = year

metadata = PaperMetadata("Advanced Cryptographic Protocols", ["Dr. Smith", "Prof. Johnson"], 2023)
author_set = frozenset(metadata.authors)
sorted_authors = sorted(list(author_set))
primary_author_hash = custom_hash(sorted_authors[0])
title_length = len(metadata.title)
year_mod = metadata.year % 17

# Calculate verification components
component_a = (primary_author_hash * 7) % 1009
component_b = (title_length ** 2) % 1009
component_c = (year_mod * 13) % 1009

# Verification code calculation using ternary logic
intermediate_result = component_a if component_a > component_b else component_b
verification_code = (intermediate_result + component_c) % 1009 if (component_a + component_b + component_c) % 2 == 0 else (intermediate_result * component_c) % 1009

print(f"Result: {verification_code}")