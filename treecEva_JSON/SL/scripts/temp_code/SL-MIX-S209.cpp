#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Initialize data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> primes = {29, 31, 37, 41, 43};
    
    // Complex arithmetic and logical operations
    int a = matrix[1][2] << 2;  // Left shift: 13 << 2 = 52
    int b = (primes[3] & 0x1F) | (matrix[0][1] ^ 3);  // Bitwise operations: (41 & 31) | (3 ^ 3) = 9 | 0 = 9
    double c = pow(matrix[2][0], 1.5) + log(primes[2]) * sin(M_PI / 6);  // Math operations: 17^1.5 + ln(37) * 0.5
    
    // Nested conditional logic with short-circuit evaluation
    int d = 0;
    if ((a > 50) && (b < 10 || c > 50)) {
        d = (int)(c / matrix[0][2]);  // Division with truncation
    } else if ((a <= 50) || (matrix[1][1] != primes[0])) {
        d = matrix[2][2] * 2 - primes[4];
    } else {
        d = a + b + (int)c;
    }
    
    // Complex data manipulation
    vector<int> temp;
    for (int i = 0; i < matrix.size(); i++) {
        int row_sum = 0;
        for (int j = 0; j < matrix[i].size(); j++) {
            row_sum += matrix[i][j] * (i + 1) * (j + 1);
        }
        temp.push_back(row_sum);
    }
    
    // Sorting and mathematical transformations
    sort(temp.begin(), temp.end());
    double e = sqrt(temp[0] * temp[2]) + ceil(c / 10);
    
    // Final calculation combining all previous results
    int result = (d & 0xFF) ^ (int)e ^ (temp[1] % 32);
    
    cout << "Result: " << result << endl;
    return 0;
}