import re

def count_palindromic_subsequences(s):
    n = len(s)
    # dp[i][j] will store count of palindromic subsequences in s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = 1
    
    # Fill for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 3  # s[i], s[i+1], s[i]+s[i+1]
        else:
            dp[i][i+1] = 2  # s[i], s[i+1]
    
    # Fill for substrings of length 3 and more
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
    
    return dp[0][n-1]

# Ancient manuscript encoding
manuscript = "aaba"

# Filter for significant linguistic markers using regex
filtered_chars = re.findall(r'[ab]', manuscript)
refined_text = ''.join(filtered_chars)

# Apply dynamic programming to count palindromic subsequences
palindrome_count = count_palindromic_subsequences(refined_text)

print(f"Result: {palindrome_count}")