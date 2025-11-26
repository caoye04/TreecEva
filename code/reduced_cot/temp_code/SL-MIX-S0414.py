from collections import Counter

names = ['alice', 'bob', 'charlie', 'diana', 'alice', 'bob', 'eve', 'frank']
name_counts = Counter(names)
threshold = 2
filtered_names = [name for name in names if name_counts[name] >= threshold]
final_count = len(filtered_names)
print(f"Result: {final_count}")