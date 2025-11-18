import heapq
import itertools

token_stream = ['{', 'IF', '(', 'x', '>', '0', ')', '{', 'LOOP', '{', '}', '}', '}']
scope_heap = []
nesting_level = 0
processed_scope_count = 0

for token in token_stream:
    if token == '{':
        nesting_level += 1
        heapq.heappush(scope_heap, (-nesting_level, token))
    elif token == '}':
        if scope_heap:
            current_depth, _ = heapq.heappop(scope_heap)
            if -current_depth == nesting_level:
                processed_scope_count += 1
        nesting_level -= 1
    else:
        # For non-scope tokens, check if they're control keywords
        if token in ['IF', 'LOOP'] and scope_heap:
            depth, _ = scope_heap[0]  # Peek at highest priority item
            if -depth > 1:  # Only process if inside nested scope
                processed_scope_count += 1

# Final adjustment based on remaining unmatched scopes
remaining_scopes = [item[0] for item in scope_heap]
if remaining_scopes and all(depth <= -2 for depth in remaining_scopes):
    processed_scope_count *= 2

print(f"Result: {processed_scope_count}")