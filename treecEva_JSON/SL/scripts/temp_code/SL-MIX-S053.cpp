#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <functional>

int main() {
    std::string config = "CONFIG_MODE_ALPHA";
    size_t mid = config.length() / 2;
    std::string first_half = config.substr(0, mid);
    std::string second_half = config.substr(mid);
    
    std::hash<std::string> hasher;
    size_t hash1 = hasher(first_half);
    size_t hash2 = hasher(second_half);
    
    size_t combined_hash = (hash1 ^ hash2) % 1000;
    
    std::cout << "Result: " << combined_hash << std::endl;
    return 0;
}