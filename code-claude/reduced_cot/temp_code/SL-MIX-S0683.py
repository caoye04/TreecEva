from collections import Counter, defaultdict

def calculate_complexity(task):
    # Complexity score based on string properties
    length_factor = len(task) / 10
    special_chars = sum(1 for char in task if not char.isalnum() and not char.isspace())
    word_count = len(task.split())
    
    # Distracting calculation that looks important
    entropy = sum(ord(c) % 7 for c in task) / max(1, len(task))
    
    return length_factor * 1.5 + special_chars * 2 + word_count * 0.5

def calculate_priority(tasks):
    if not tasks:
        return 0
    
    # Distractor: Creating a frequency counter for words
    all_words = ' '.join(tasks).lower().split()
    word_freq = Counter(all_words)
    common_words = [word for word, count in word_freq.items() if count > 1]
    
    # Task categorization (distractor)
    categories = defaultdict(list)
    for task in tasks:
        if '#urgent' in task.lower():
            categories['urgent'].append(task)
        elif '#important' in task.lower():
            categories['important'].append(task)
        else:
            categories['normal'].append(task)
    
    # Calculate base score from task properties
    complexity_scores = [calculate_complexity(task) for task in tasks]
    avg_complexity = sum(complexity_scores) / len(complexity_scores) if complexity_scores else 0
    
    # Distractor calculations that don't affect final result
    urgency_factor = len(categories['urgent']) * 3 + len(categories['important']) * 1.5
    word_diversity = len(word_freq) / max(1, len(all_words))
    semantic_density = sum(len(w) for w in common_words) / max(1, len(common_words)) if common_words else 0
    
    # This is the actual calculation that matters
    base_score = avg_complexity * 2
    task_count_factor = len(tasks) // 3
    
    # More distractors
    if 'project plan' in ' '.join(tasks).lower():
        semantic_density += 2.5
    
    if any('#blocker' in task.lower() for task in tasks):
        urgency_factor *= 1.25
    
    # The key calculation
    priority_score = int(base_score) + task_count_factor
    
    # Distractor that looks like it modifies the score but doesn't
    if urgency_factor > 5 and semantic_density > 3:
        temp_score = priority_score * 1.2
        print(f"Adjusted score (not used): {temp_score}")
    
    return priority_score

# Main program execution
task_list = [
    "Review design documents #important",
    "Fix login page bug #urgent",
    "Update user documentation",
    "Team meeting preparation #important",
    "Project plan review for Q3",
    "Database optimization research",
    "Code refactoring for payment module #blocker",
    "Test new API endpoints"
]

# Distractor operations
reversed_tasks = task_list[::-1]
alphabetical_tasks = sorted(task_list)
categorized = defaultdict(list)

for task in task_list:
    if '#' in task:
        tag = task.split('#')[1].strip()
        categorized[tag].append(task)
    else:
        categorized['untagged'].append(task)

# Filter tasks (distractor with some relevance)
filtered_tasks = [task for task in task_list if len(task) > 10]

# Distractor calculation
task_complexity_map = {task: calculate_complexity(task) for task in task_list}
max_complexity_task = max(task_complexity_map.items(), key=lambda x: x[1])[0]

# The key statement that calculates the answer
priority_score = calculate_priority(filtered_tasks)

# More distractors
adjusted_score = priority_score + len(categorized.keys())
weighted_score = priority_score * (1 + len(filtered_tasks) / len(task_list))

print(f"Result: {priority_score}")