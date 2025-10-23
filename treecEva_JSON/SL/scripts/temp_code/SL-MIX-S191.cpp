#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <numeric>
#include <optional>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    std::string input = "aabbccccdddddd";
    std::map<char, int> frequency;
    
    for (char c : input) {
        frequency[c]++;
    }
    
    int total_chars = input.length();
    int unique_chars = frequency.size();
    
    // Greedy selection of frequencies that are coprime
    std::vector<int> selected_freqs;
    for (const auto& pair : frequency) {
        bool is_coprime = true;
        for (int selected : selected_freqs) {
            if (gcd(pair.second, selected) != 1) {
                is_coprime = false;
                break;
            }
        }
        if (is_coprime) {
            selected_freqs.push_back(pair.second);
        }
    }
    
    int sum_selected = std::accumulate(selected_freqs.begin(), selected_freqs.end(), 0);
    int compression_ratio = (sum_selected * 100) / total_chars;
    
    std::cout << "Result: " << compression_ratio << std::endl;
    return 0;
}