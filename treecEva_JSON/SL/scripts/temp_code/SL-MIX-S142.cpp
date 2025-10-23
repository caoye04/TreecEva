#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <regex>
#include <algorithm>

class HexByteSequence {
private:
    std::vector<std::string> bytes;

public:
    HexByteSequence(std::initializer_list<std::string> init) : bytes(init) {}
    
    // Overloaded operator to concatenate all bytes into a single string
    std::string operator()() const {
        std::string result;
        for (const auto& b : bytes) result += b;
        return result;
    }
    
    // Variadic template function to check multiple patterns
    template<typename... Patterns>
    int findLongestMatch(Patterns... patterns) const {
        std::string sequence = operator()();
        std::vector<std::regex> regexes = {patterns...};
        
        int maxLength = 0;
        
        // Greedy algorithm to find longest matching substring
        for (size_t i = 0; i < sequence.length(); ++i) {
            for (size_t j = i + 3; j <= sequence.length(); ++j) {  // Minimum length is 3
                std::string substring = sequence.substr(i, j - i);
                for (const auto& re : regexes) {
                    if (std::regex_match(substring, re)) {
                        maxLength = std::max(maxLength, static_cast<int>(substring.length()));
                    }
                }
            }
        }
        
        return maxLength;
    }
};

int main() {
    HexByteSequence networkTraffic{
        "A1", "0B", "C3", "0D", "E5", "0F", "1A", "2B", 
        "3C", "0D", "4E", "5F", "6A", "0B", "7C", "8D"
    };
    
    // Define the suspicious pattern
    std::regex suspiciousPattern("[0-9A-F]{2}0[0-9A-F]");
    
    // Find the longest match using our greedy algorithm
    int longestMatchLength = networkTraffic.findLongestMatch(suspiciousPattern);
    
    std::cout << "Result: " << longestMatchLength << std::endl;
    
    return 0;
}