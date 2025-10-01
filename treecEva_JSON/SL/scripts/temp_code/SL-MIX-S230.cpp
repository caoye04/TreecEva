#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize complex nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> primes = {29, 31, 37, 41, 43};
    
    // Mathematical operations with nested loops
    int accumulator = 0;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            accumulator += matrix[i][j] * pow(-1, i + j);
        }
    }
    
    // Bitwise operations combined with logical conditions
    int bitwise_result = 0;
    for (int i = 0; i < primes.size(); i++) {
        if ((primes[i] & 1) && (primes[i] > 30)) {
            bitwise_result ^= primes[i];
        }
    }
    
    // String manipulation and conversion
    string num_str = "";
    for (int i = 0; i < 4; i++) {
        num_str += to_string(primes[i] % 10);
    }
    int converted_num = stoi(num_str);
    
    // Complex conditional logic with multiple variables
    int condition_result = 0;
    if ((accumulator > 0) && (bitwise_result != 0)) {
        condition_result = (int)sqrt(converted_num) + (accumulator & bitwise_result);
    } else if (accumulator <= 0) {
        condition_result = accumulator | bitwise_result;
    } else {
        condition_result = accumulator ^ bitwise_result;
    }
    
    // Final calculation combining all previous results
    int final_result = 0;
    switch (condition_result % 5) {
        case 0:
            final_result = accumulator + bitwise_result + converted_num;
            break;
        case 1:
            final_result = accumulator * bitwise_result - converted_num;
            break;
        case 2:
            final_result = pow(accumulator, 2) + sqrt(bitwise_result) * converted_num;
            break;
        case 3:
            final_result = (accumulator << 2) + (bitwise_result >> 1) - converted_num;
            break;
        default:
            final_result = accumulator ^ bitwise_result ^ converted_num;
            break;
    }
    
    // Apply final transformation
    final_result = abs(final_result) % 1000;
    
    cout << "Result: " << final_result << endl;
    return 0;
}