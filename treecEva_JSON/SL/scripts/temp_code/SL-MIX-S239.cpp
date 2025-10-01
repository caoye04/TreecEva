#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) + log(static_cast<double>(x + 1));
}

int main() {
    vector<map<string, int>> data = {
        {{"a", 5}, {"b", -16}},
        {{"c", 3}, {"d", 8}},
        {{"e", 12}, {"f", -4}}
    };
    
    int accumulator = 0;
    double sum_of_computations = 0.0;
    
    for (const auto& inner_map : data) {
        for (const auto& pair : inner_map) {
            int value = pair.second;
            if (value > 0) {
                accumulator += value;
            } else {
                accumulator ^= abs(value); // Bitwise XOR with absolute value
            }
            sum_of_computations += compute_expression(abs(value), value * 2);
        }
    }
    
    string s = "Hello";
    s += " World!";
    reverse(s.begin(), s.end());
    
    int str_len = static_cast<int>(s.length());
    int mask = (1 << 4) - 1; // 15 in decimal
    int masked_value = accumulator & mask;
    
    double final_computation = ceil(sum_of_computations / str_len);
    int final_result = static_cast<int>(final_computation) + masked_value;
    
    cout << "Result: " << final_result << endl;
    return 0;
}