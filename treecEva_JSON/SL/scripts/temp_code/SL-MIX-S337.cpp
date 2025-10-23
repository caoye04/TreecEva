#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

constexpr int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

template<typename T>
void alternating_sort(std::vector<T>& vec) {
    bool ascending = true;
    for (size_t i = 0; i < vec.size(); i += 2) {
        if (ascending) {
            if (i+1 < vec.size() && vec[i] > vec[i+1])
                std::swap(vec[i], vec[i+1]);
        } else {
            if (i+1 < vec.size() && vec[i] < vec[i+1])
                std::swap(vec[i], vec[i+1]);
        }
        ascending = !ascending;
    }
}

int main() {
    std::vector<int> phonemes = {3, 1, 4, 1, 5};
    int synthesis_score = 0;
    
    // Remove duplicates for permutation calculation
    std::sort(phonemes.begin(), phonemes.end());
    auto last = std::unique(phonemes.begin(), phonemes.end());
    phonemes.erase(last, phonemes.end());
    
    // Calculate number of permutations
    int perm_count = factorial(phonemes.size());
    
    // Generate all permutations and apply alternating sort
    std::vector<std::vector<int>> all_perms;
    do {
        std::vector<int> temp = phonemes;
        alternating_sort(temp);
        all_perms.push_back(temp);
    } while (std::next_permutation(phonemes.begin(), phonemes.end()));
    
    // Calculate synthesis score
    for (const auto& perm : all_perms) {
        synthesis_score += std::accumulate(perm.begin(), perm.end(), 0);
    }
    
    synthesis_score *= perm_count;
    
    std::cout << "Result: " << synthesis_score << std::endl;
    return 0;
}