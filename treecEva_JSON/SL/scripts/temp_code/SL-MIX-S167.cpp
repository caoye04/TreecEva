#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int accumulator = 0;
    
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            if ((i + j) % 2 == 0) {
                accumulator += matrix[i][j];
            } else {
                accumulator -= matrix[i][j];
            }
        }
    }
    
    string magic_word = "COMPUTE";
    int char_sum = 0;
    for (char c : magic_word) {
        char_sum += static_cast<int>(c);
    }
    
    double intermediate = pow(accumulator, 2) + sqrt(char_sum);
    int shifted = (static_cast<int>(intermediate) << 2) ^ 0xF0;
    
    vector<int> primes = {29, 31, 37, 41};
    int product = 1;
    for (int p : primes) {
        product *= p;
    }
    
    int final_result = (shifted & 0xFF) + (product % 100);
    cout << "Result: " << final_result << endl;
    return 0;
}