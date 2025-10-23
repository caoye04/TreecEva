#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

constexpr int calculate_weight(int freq, int len) {
    return freq * len + (len > 1 ? (1 << (len - 1)) : 0);
}

int main() {
    std::string input = "aabbccdddeeeff";
    std::map<std::string, int> freq_map;
    
    // Tokenization and frequency counting
    for (size_t i = 0; i < input.length(); ) {
        size_t j = i;
        while (j < input.length() && input[j] == input[i]) j++;
        std::string token = input.substr(i, j - i);
        freq_map[token]++;
        i = j;
    }
    
    // Dynamic programming table for optimal merging
    std::vector<int> dp(freq_map.size() + 1, 0);
    std::vector<std::string> tokens;
    for (const auto& pair : freq_map) {
        tokens.push_back(pair.first);
    }
    
    // Greedy merging with short-circuit evaluation
    int compression_score = 0;
    for (size_t i = 0; i < tokens.size(); ++i) {
        const std::string& token = tokens[i];
        int freq = freq_map[token];
        int len = token.length();
        
        // Short-circuit: skip if token is too short or frequency is low
        if (len < 2 && freq < 3) continue;
        
        // Calculate weight using constexpr function
        int weight = calculate_weight(freq, len);
        
        // Bitwise encoding: shift and XOR
        int encoded = (weight << 2) ^ (len & 0x3);
        
        // Ternary operator for dynamic programming update
        dp[i+1] = (i > 0) ? std::max(dp[i], dp[i-1] + encoded) : encoded;
        
        // Accumulate compression score
        compression_score += (encoded > 0) ? encoded : 0;
    }
    
    // Final adjustment using move semantics
    std::vector<int> temp_dp = std::move(dp);
    compression_score ^= temp_dp.back() & 0xFF;
    
    std::cout << "Result: " << compression_score << std::endl;
    return 0;
}