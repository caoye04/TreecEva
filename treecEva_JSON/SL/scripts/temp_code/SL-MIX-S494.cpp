#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> primes;
    
    // Step 1: Flatten the matrix and filter primes using a custom condition
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            int num = matrix[i][j];
            bool is_prime = true;
            if (num <= 1) is_prime = false;
            for (int k = 2; k <= sqrt(num); k++) {
                if (num % k == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) {
                primes.push_back(num);
            }
        }
    }
    
    // Step 2: Perform bitwise operations on the primes
    int xor_result = 0;
    for (int i = 0; i < primes.size(); i++) {
        xor_result ^= primes[i];
    }
    
    // Step 3: String manipulation and conversion
    string binary_str = "";
    for (int i = 31; i >= 0; i--) {
        binary_str += ((xor_result >> i) & 1) ? '1' : '0';
    }
    
    // Remove leading zeros
    binary_str.erase(0, binary_str.find_first_not_of('0'));
    if (binary_str.empty()) binary_str = "0";
    
    // Step 4: Convert binary string back to integer
    int converted_value = 0;
    for (int i = 0; i < binary_str.length(); i++) {
        converted_value = converted_value * 2 + (binary_str[i] - '0');
    }
    
    // Step 5: Mathematical operations
    double log_val = log2(converted_value);
    int rounded_log = (int)round(log_val);
    
    // Step 6: Final calculation
    int final_result = (converted_value * rounded_log) % 1000;
    
    cout << "Result: " << final_result << endl;
    return 0;
}