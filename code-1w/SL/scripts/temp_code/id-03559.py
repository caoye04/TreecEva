from itertools import groupby

def calculate_final_score(records):
    # Convert all names to uppercase for uniformity
    processed_records = [
        {**record, 'name': record['name'].upper()} for record in records
    ]
    
    # Group by name and compute average score per person
    sorted_records = sorted(processed_records, key=lambda x: x['name'])
    grouped = {key: list(group) for key, group in groupby(sorted_records, key=lambda x: x['name'])}
    
    averages = {}
    for name, group in grouped.items():
        total = sum(entry['score'] for entry in group)
        count = len(group)
        averages[name] = total / count
    
    # Compute final score as the sum of average scores multiplied by number of unique individuals
    base_final = sum(averages.values())
    bonus = len(averages)  # One point per unique person
    final_score = base_final * bonus
    
    return final_score

# Example dataset
data = [
    {'name': 'alice', 'score': 85},
    {'name': 'Bob', 'score': 90},
    {'name': 'Alice', 'score': 95},
    {'name': 'bob', 'score': 80},
    {'name': 'Charlie', 'score': 70}
]

result = calculate_final_score(data)
print(f"Result: {result}")