#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

constexpr int binarySearch(const std::vector<std::string>& arr, const std::string& target) {
    int left = 0;
    int right = static_cast<int>(arr.size()) - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    std::string sentence = "algorithm analysis optimization performance efficiency";
    std::vector<std::string> tokens;
    std::string word;
    for (size_t i = 0; i <= sentence.length(); ++i) {
        if (i == sentence.length() || sentence[i] == ' ') {
            if (!word.empty()) {
                tokens.push_back(word);
                word.clear();
            }
        } else {
            word += sentence[i];
        }
    }
    
    std::sort(tokens.begin(), tokens.end());
    
    int target_index = binarySearch(tokens, "optimization");
    
    std::cout << "Result: " << target_index << std::endl;
    
    return 0;
}