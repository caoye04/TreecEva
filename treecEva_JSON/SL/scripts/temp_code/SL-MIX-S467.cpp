#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> primes;
    string code = "HELLO";
    int accumulator = 0;
    int mask = 0xF0; // 240 in decimal
    
    // Step 1: Process matrix to extract primes
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            int value = matrix[i][j];
            bool is_prime = true;
            if (value < 2) is_prime = false;
            for (int k = 2; k <= sqrt(value); k++) {
                if (value % k == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) {
                primes.push_back(value);
            }
        }
    }
    
    // Step 2: Perform bitwise operations on primes
    for (int i = 0; i < primes.size(); i++) {
        primes[i] = primes[i] & mask;
    }
    
    // Step 3: Manipulate string and calculate ASCII sum
    reverse(code.begin(), code.end());
    int ascii_sum = 0;
    for (char c : code) {
        ascii_sum += static_cast<int>(c);
    }
    
    // Step 4: Mathematical computation
    double product_log = 1.0;
    for (int p : primes) {
        if (p > 0) {
            product_log *= log(static_cast<double>(p));
        }
    }
    
    // Step 5: Combine results
    int final_result = static_cast<int>(product_log) + ascii_sum + primes.size();
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}