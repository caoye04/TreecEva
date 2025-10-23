#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <map>
#include <cctype>

int main() {
    std::string input = "hello world";
    std::string processed;
    
    // Convert to uppercase and remove spaces
    for (char c : input) {
        if (c != ' ') {
            processed += std::toupper(c);
        }
    }
    
    // Count frequency of each character
    std::map<char, int> freq;
    for (char c : processed) {
        freq[c]++;
    }
    
    // Calculate weighted score
    int weighted_score = 0;
    for (const auto& pair : freq) {
        weighted_score += static_cast<int>(pair.first) * pair.second;
    }
    
    std::cout << "Result: " << weighted_score << std::endl;
    return 0;
}