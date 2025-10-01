#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

double recursive_transform(int n, double base) {
    if (n <= 1) return base;
    double val = recursive_transform(n - 1, base);
    if (n % 3 == 0) {
        return val * log(n);
    } else if (n % 3 == 1) {
        return val + sin(n);
    } else {
        return val - cos(n);
    }
}

int main() {
    int arr[5][5] = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};
    double matrix[3][3];
    int i, j;
    double accumulator = 0.0;
    
    // Initialize matrix with transformed values from arr
    for(i=0; i<3; i++){
        for(j=0; j<3; j++){
            int index = i*3 + j + 1;
            matrix[i][j] = sqrt(arr[i][j] * index);
        }
    }
    
    // Perform bitwise and arithmetic operations
    for(i=0; i<3; i++){
        for(j=0; j<3; j++){
            int x = static_cast<int>(matrix[i][j]);
            int y = (x << 2) & 60;
            accumulator += (y ^ (x | 5));
        }
    }
    
    // Apply recursive transformation
    double transformed = recursive_transform(7, accumulator);
    
    // Final adjustment using trigonometric identity
    int integer_part = static_cast<int>(transformed);
    double fractional_part = transformed - integer_part;
    double final_result = integer_part * cos(fractional_part) + pow(integer_part % 10, 2);
    
    cout << "Result: " << final_result << endl;
    return 0;
}