words = ['algorithm', 'function', 'variable', 'iterator', 'parameter']
letter_counts = []

for word in words:
    count = len([char for char in word if char in 'aeiou'])
    letter_counts.append(count)

counts = [x * 2 for x in letter_counts]
final_count = sum(counts)
print(f"Result: {final_count}")