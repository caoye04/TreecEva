import itertools

class AnalysisSession:
    def __enter__(self):
        self.session_active = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session_active = False

def is_palindrome(s):
    return s == s[::-1]

def validate_sequence(seq, min_length=3):
    valid = []
    n = len(seq)
    for i in range(n):
        for j in range(i + min_length, n + 1):
            subseq = seq[i:j]
            if is_palindrome(subseq):
                valid.append(subseq)
    return valid

sequences = ['ATGCAATGC', 'TTACGTAAGT', 'CGCGCG']
validated_palindromes = 0

with AnalysisSession() as session:
    if session.session_active:
        for seq in sequences:
            palindromes = validate_sequence(seq)
            combinations = list(itertools.combinations(palindromes, 2))
            filtered_combinations = [
                (a, b) for a, b in combinations
                if len(a) > 3 and len(b) > 3 and (len(a) % 2 == 1 or len(b) % 2 == 1)
            ]
            validated_palindromes += len(filtered_combinations)

# Apply final logical filter
if validated_palindromes > 0 and (validated_palindromes % 2 == 0 or validated_palindromes > 5):
    validated_palindromes *= 2
else:
    validated_palindromes += 1

print(f"Result: {validated_palindromes}")