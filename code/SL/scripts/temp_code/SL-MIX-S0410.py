def count_thread_occurrences(pattern_index):
    if pattern_index == 0:
        return 0
    return str(pattern_index % 3).count('1') + count_thread_occurrences(pattern_index // 3)

total_patterns = 10
thread_counter = sum(map(count_thread_occurrences, range(total_patterns + 1)))
print(f"Result: {thread_counter}")