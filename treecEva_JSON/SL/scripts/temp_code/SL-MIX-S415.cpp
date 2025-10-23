#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

template<typename T>
T process_band(const std::vector<T>& band) {
    if (band.size() <= 1) return band.empty() ? 0 : band[0];
    
    size_t mid = band.size() / 2;
    std::vector<T> left(band.begin(), band.begin() + mid);
    std::vector<T> right(band.begin() + mid, band.end());
    
    T left_result = process_band(left);
    T right_result = process_band(right);
    
    T combined = left_result + right_result;
    return (combined > 100) ? combined / 2 : combined * 2;
}

int main() {
    std::vector<int> frequencies = {15, 25, 35, 45, 55, 65};
    int processed_bands = process_band(frequencies);
    
    if (processed_bands < 200) {
        processed_bands += 50;
    } else {
        processed_bands -= 25;
    }
    
    std::cout << "Result: " << processed_bands << std::endl;
    return 0;
}