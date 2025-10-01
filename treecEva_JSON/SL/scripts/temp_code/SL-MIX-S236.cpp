#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> primes;
    string code = "PRIME_SUM";
    int accumulator = 0;
    int result = 0;
    
    // Step 1: Extract diagonal elements and compute their factorial sum
    for (int i = 0; i < 3; i++) {
        int diag = matrix[i][i];
        int fact = 1;
        for (int j = 1; j <= diag; j++) {
            fact *= j;
        }
        primes.push_back(fact);
        accumulator += fact;
    }
    
    // Step 2: Perform bitwise operations on accumulator
    accumulator = (accumulator >> 2) & 0xFF;
    
    // Step 3: Manipulate string and use its length
    string modified = code.substr(0, 5);
    int len = modified.length();
    accumulator ^= len;
    
    // Step 4: Mathematical transformations
    double temp = sqrt(accumulator);
    temp = pow(temp, 3);
    accumulator = static_cast<int>(floor(temp));
    
    // Step 5: Final complex calculation
    result = (accumulator * 3) + (primes[0] % 7) - (primes[2] / primes[1]);
    
    cout << "Result: " << result << endl;
    return 0;
}