def normalize_string(s):
    return s.strip().lower().replace(' ', '')

raw_entries = [' Alice', 'Bob ', 'Charlie', 'Diana  ']
processed_data = set()

for entry in raw_entries:
    cleaned = normalize_string(entry)
    if len(cleaned) > 4:
        processed_data.add(cleaned)

stats = {}
for name in processed_data:
    vowel_count = sum(1 for c in name if c in 'aeiou')
    stats[name] = vowel_count * 2

base_value = len(processed_data) * 3
bonus = sum(stats.values()) // 2
final_score = base_value + bonus

Result: final_score