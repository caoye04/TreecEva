#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

double recursive_sum(vector<int>& arr, int index) {
    if (index >= arr.size()) return 0.0;
    return sqrt(abs(arr[index])) + recursive_sum(arr, index + 2);
}

int main() {
    vector<int> data = {16, -9, 25, -4, 36, -49, 64};
    int mask = 0xF0; // 240 in decimal, 11110000 in binary
    int shift_val = 3;
    double intermediate = 0.0;
    int combined_ops = 0;
    
    for (int i = 0; i < data.size(); i++) {
        if (i % 2 == 0) {
            data[i] = data[i] ^ mask;
        } else {
            data[i] = data[i] << shift_val;
        }
        combined_ops += (data[i] & 0x0F); // Add last 4 bits
    }
    
    // Apply a trigonometric adjustment
    for (int i = 0; i < data.size(); i++) {
        data[i] = static_cast<int>(data[i] * cos(M_PI / 4));
    }
    
    intermediate = recursive_sum(data, 0);
    
    int result = static_cast<int>(intermediate) ^ combined_ops;
    
    // Final computation
    result = result & 0xFF; // Mask to last 8 bits
    
    cout << "Result: " << result << endl;
    return 0;
}