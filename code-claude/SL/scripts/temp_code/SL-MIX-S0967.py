def process_string_weights(text):
    # Extract potential weight values from text
    parts = text.split(':')
    if len(parts) > 1 and parts[1].strip().isdigit():
        return int(parts[1].strip())
    
    # Fallback weight calculation based on character frequency
    weight = 0
    for char in text.lower():
        if char.isalpha():
            weight += (ord(char) - ord('a') + 1) % 10
    return weight

def calculate_task_priority(task_info):
    # Extract task components
    task_id, description, status, tags = task_info
    
    # Process status - only 'active' tasks get prioritized
    if status.lower() != 'active':
        return -1
    
    # Calculate base priority from task_id
    base_priority = 0
    if isinstance(task_id, str) and task_id.startswith('T'):
        try:
            base_priority = int(task_id[1:]) % 100
        except ValueError:
            base_priority = len(task_id) * 2
    else:
        base_priority = 50  # Default priority
    
    # Calculate description weight
    desc_weight = process_string_weights(description)
    
    # Process tags for priority modifiers
    tag_modifier = 0
    urgent_multiplier = 1
    for tag in tags:
        tag_lower = tag.lower()
        if tag_lower == 'urgent':
            urgent_multiplier = 2
        elif tag_lower == 'low':
            urgent_multiplier = 0.5
        elif tag_lower.startswith('weight'):
            try:
                tag_modifier += process_string_weights(tag)
            except:
                tag_modifier += 5
    
    # Misleading calculations that don't affect result
    complexity_score = len(description) // 10
    time_estimate = complexity_score * 2.5
    resource_allocation = complexity_score * urgent_multiplier + 10
    
    # Calculate final priority
    raw_priority = (base_priority + desc_weight + tag_modifier) * urgent_multiplier
    
    # Normalize to 0-100 scale with misleading intermediate steps
    normalized = min(100, max(0, raw_priority))
    adjusted = normalized * 1.2 - 10  # Misleading adjustment
    capped = min(100, max(0, adjusted))  # Misleading capping
    
    # Final calculation
    final_priority = round((base_priority + desc_weight) * urgent_multiplier)
    
    return final_priority

# Task data: (id, description, status, tags)
task_alternative = ('T245', 'System backup and recovery', 'Pending', ['critical', 'weekend'])
task_data = ('T42', 'Update user documentation: version 3.0', 'Active', ['urgent', 'weight:15'])
backlog_tasks = [
    ('T103', 'Fix login page CSS', 'Active', ['frontend', 'low']),
    ('T97', 'Database optimization', 'Completed', ['backend', 'urgent'])
]

# Process multiple tasks to create distraction
all_priorities = {}
for task in [task_alternative] + backlog_tasks:
    priority = calculate_task_priority(task)
    all_priorities[task[0]] = priority

# Calculate the target task priority
final_priority = calculate_task_priority(task_data)

# Misleading post-processing
weighted_average = sum(all_priorities.values()) / len(all_priorities)
adjusted_priority = (final_priority + weighted_average) / 2

print(f"All task priorities: {all_priorities}")
print(f"Weighted average: {weighted_average}")
print(f"Adjusted priority: {adjusted_priority}")
print(f"Result: {final_priority}")