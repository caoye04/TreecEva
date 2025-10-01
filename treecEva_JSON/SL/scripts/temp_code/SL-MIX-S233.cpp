#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
    int base = 3;
    double angle = M_PI / 4; // 45 degrees in radians
    string text = "complexity";
    
    int sum = 0;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            sum += matrix[i][j] * pow(base, i + j);
        }
    }
    
    int bitwise = (sum >> 2) & 0xFF;
    double trig_result = sin(angle) * cos(angle) * 100;
    
    int text_length = text.length();
    int combined = (bitwise ^ text_length) + static_cast<int>(trig_result);
    
    vector<int> sequence(10);
    sequence[0] = combined % 10;
    sequence[1] = combined / 10;
    for (int i = 2; i < 10; i++) {
        sequence[i] = (sequence[i-1] * sequence[i-2] + i) % 100;
    }
    
    int result = 0;
    for (int i = 0; i < sequence.size(); i++) {
        result += sequence[i] * pow(-1, i);
    }
    
    cout << "Result: " << result << endl;
    return 0;
}