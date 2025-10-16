
import sys
import json
import traceback

_trace_log = []
_step_counter = [0]

def _record_state(line_num, frame_locals, code_line):
    '''记录执行状态'''
    _step_counter[0] += 1
    
    # 过滤内部变量
    clean_vars = {k: repr(v)[:100] for k, v in frame_locals.items() 
                  if not k.startswith('_') and k not in ['json', 'sys', 'traceback']}
    
    snapshot = {
        'step': _step_counter[0],
        'line': line_num,
        'code': code_line.strip(),
        'vars': clean_vars
    }
    _trace_log.append(snapshot)

# 原始代码包装在函数中
def _traced_main():
        import heapq

    def nucleotide_hash(nucleotide):
        mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
        return mapping.get(nucleotide, 0)

    def rolling_hash(sequence, base=5, mod=1000000007):
        hash_val = 0
        for char in sequence:
            hash_val = (hash_val * base + nucleotide_hash(char)) % mod
        return hash_val

    def max_subseq_sum(seq_values):
        dp = [0] * len(seq_values)
        dp[0] = seq_values[0]
        for i in range(1, len(seq_values)):
            dp[i] = max(dp[i-1] + seq_values[i], seq_values[i])
        return max(dp)

    class HashCache:
        def __init__(self):
            self.cache = {}
    
        def get_or_compute(self, s):
            if s not in self.cache:
                self.cache[s] = rolling_hash(s)
            return self.cache[s]

    def is_palindrome_recursive(s, memo={}):
        if s in memo:
            return memo[s]
        if len(s) <= 1:
            memo[s] = True
            return True
        if s[0] != s[-1]:
            memo[s] = False
            return False
        result = is_palindrome_recursive(s[1:-1], memo)
        memo[s] = result
        return result

    # Main processing pipeline
    sequence = 'GATTACA'
    nucleotides = [nucleotide_hash(c) for c in sequence]
    hash_cache = HashCache()

    # Step 1: Compute rolling hash of entire sequence
    full_hash = hash_cache.get_or_compute(sequence)

    # Step 2: Find maximum sum of any contiguous subsequence using DP
    max_sum = max_subseq_sum(nucleotides)

    # Step 3: Identify all palindromic substrings and their hashes
    pal_hashes = []
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)+1):
            substr = sequence[i:j]
            if is_palindrome_recursive(substr):
                pal_hashes.append(hash_cache.get_or_compute(substr))

    # Step 4: Use min-heap to find smallest 3 palindromic hashes
    heapq.heapify(pal_hashes)
    top_3_min = [heapq.heappop(pal_hashes) for _ in range(min(3, len(pal_hashes)))]

    # Final score calculation
    final_score = full_hash + max_sum + sum(top_3_min)
    print(f"Result: {final_score}")

# 执行追踪
try:
    import sys
    import linecache
    
    def trace_calls(frame, event, arg):
        if event == 'line':
            line_num = frame.f_lineno
            code_line = linecache.getline(frame.f_code.co_filename, line_num)
            _record_state(line_num, frame.f_locals, code_line)
        return trace_calls
    
    sys.settrace(trace_calls)
    _traced_main()
    sys.settrace(None)
    
except Exception as e:
    print(f"TRACE_ERROR: {str(e)}", file=sys.stderr)
    traceback.print_exc()

# 输出追踪日志
print("===TRACE_START===")
print(json.dumps(_trace_log, indent=2))
print("===TRACE_END===")
