#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <memory>

int binary_search_code(const std::vector<std::pair<int, std::string>>& codes, const std::string& target) {
    int left = 0;
    int right = codes.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (codes[mid].second == target) {
            return codes[mid].first;
        }
        if (codes[mid].second < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    // Encoding map: character -> binary code
    std::map<char, std::string> encoding_map = {{'A', "0"}, {'B', "10"}, {'C', "110"}, {'D', "111"}};
    
    // Decoding map: binary code -> character (sorted by code length for efficient search)
    std::vector<std::pair<char, std::string>> decoding_vector = {{'A', "0"}, {'B', "10"}, {'C', "110"}, {'D', "111"}};
    
    // Sort by code for binary search
    std::sort(decoding_vector.begin(), decoding_vector.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
    });
    
    // Encoded message
    std::string encoded_message = "110100111";
    
    // Decoding process
    std::string current_code = "";
    int decoded_length = 0;
    
    for (char bit : encoded_message) {
        current_code += bit;
        char decoded_char = binary_search_code(decoding_vector, current_code);
        if (decoded_char != -1) {
            decoded_length++;
            current_code = "";
        }
    }
    
    // END OF DECODING PROCESS
    
    std::cout << "Result: " << decoded_length << std::endl;
    return 0;
}