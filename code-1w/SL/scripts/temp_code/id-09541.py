def analyze_pattern(sequence):
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Irrelevant helper function (dead code path)
def unused_helper(arr):
    return [x ** 2 for x in arr if x % 3 == 0]

# Another red herring computation
temp_offset = sum([i * 2 for i in range(5)]) - 10  

thresholds = {'A': 65, 'B': 70, 'C': 75}
data = ['Alice', 'Bob', 'Charlie', 'Diana']
grades = [88, 72, 91, 67]

# Misleading intermediate processing with zip and enumerate
grade_map = {}
for i, name in enumerate(data):
    grade_val = grades[i]
    adjusted = grade_val + (i % 3)  # Minor obfuscation
    grade_map[name] = adjusted

# Character analysis side calculation (partially relevant)
name_lengths = [len(name) for name in data]
char_count_data = ''.join(data)
character_freq = analyze_pattern(char_count_data)

# Core logic hidden among distractions
passing_names = []
bonus_points = 0
for name, base_grade in grade_map.items():
    first_char = name[0]
    freq = character_freq.get(first_char, 0)
    if freq > 1:
        bonus_points += 2
    if len(name) % 2 == 0:
        bonus_points += 1
    passing_names.append(name)

# Secondary loop with enumerate and zip usage
penalty = 0
for idx, (name, grade) in enumerate(zip(data, grades)):
    if idx % 2 == 1:
        penalty += 1
    if grade < 70:
        penalty += 2

# Final decision logic
primary_sum = sum(grade_map.values())
secondary_modifier = bonus_points - penalty

# Key variable computed here
final_score = primary_sum + secondary_modifier

# Distractor: unused transformation
tuple_pairs = list(zip(passing_names, grades))
distinct_chars = len(set(char_count_data))

print(f"Result: {final_score}")