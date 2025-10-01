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
    
    // Mathematical operations and variable assignments
    double x = pow(2.0, 3) + sqrt(144);
    int y = static_cast<int>(x) & 15;  // Bitwise AND operation
    
    // String manipulation
    string s1 = "Hello";
    string s2 = "World";
    string s3 = s1 + s2;
    int str_length = s3.length();
    
    // Complex calculations using matrix data
    int matrix_sum = 0;
    for(int i=0; i<matrix.size(); i++) {
        for(int j=0; j<matrix[i].size(); j++) {
            matrix_sum += matrix[i][j] * (i+j);
        }
    }
    
    // Function-like operations using primes array
    int prime_product = 1;
    for(int i=0; i<primes.size(); i++) {
        prime_product *= primes[i];
        if(prime_product > 100000) {
            prime_product /= primes[i];
            break;
        }
    }
    
    // Boolean logic and conditional operations
    bool condition1 = (matrix_sum > 100) && (str_length == 10);
    bool condition2 = (prime_product < 50000) || (y < 10);
    int logical_result = condition1 ? (condition2 ? 1 : 2) : (condition2 ? 3 : 4);
    
    // Advanced programming constructs
    int accumulator = 0;
    for(int i=1; i<=10; i++) {
        if(i % 2 == 0) {
            accumulator += i * 2;
        } else {
            accumulator -= i;
        }
    }
    
    // Final complex calculation combining all previous results
    int final_result = (static_cast<int>(matrix_sum * 0.5) ^ y) + (prime_product % 100) - str_length + logical_result * accumulator;
    
    cout << "Result: " << final_result << endl;
    return 0;
}