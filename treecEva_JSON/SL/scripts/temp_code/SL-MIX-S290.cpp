#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<string> tokens = {"abc", "def", "ghi"};
    
    int sum_primes = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            sum_primes += val;
        }
    }
    
    double avg_prime = static_cast<double>(sum_primes) / 9.0;
    int rounded_avg = static_cast<int>(round(avg_prime));
    
    string concat_str = "";
    for (const string& s : tokens) {
        concat_str += s;
    }
    
    int str_len = concat_str.length();
    
    vector<int> powers;
    for (int i = 1; i <= 4; ++i) {
        powers.push_back(static_cast<int>(pow(rounded_avg, i)) % 100);
    }
    
    int xor_result = 0;
    for (int p : powers) {
        xor_result ^= p;
    }
    
    vector<int> modified_powers = powers;
    for (size_t i = 0; i < modified_powers.size(); ++i) {
        modified_powers[i] = (modified_powers[i] * str_len) + static_cast<int>(i);
    }
    
    int max_mod_power = *max_element(modified_powers.begin(), modified_powers.end());
    
    int final_result = (max_mod_power * xor_result) % 1000;
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}