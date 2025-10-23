#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>
#include <string>
#include <algorithm>
#include <vector>

class CryptoParams {
public:
    int baseKey;
    std::string salt;
    
    CryptoParams(int key, const std::string& s) : baseKey(key), salt(s) {}
};

int computeHash(const std::string& data, int key) {
    int hash = key;
    for (char c : data) {
        hash = (hash << 3) ^ c;
    }
    return hash;
}

int main() {
    auto params = std::make_shared<CryptoParams>(42, "SECRET");
    std::vector<int> sequence = {15, 23, 8, 31, 12};
    
    int intermediate = params->baseKey;
    for (size_t i = 0; i < sequence.size(); ++i) {
        intermediate = (i % 2 == 0) ? 
            (intermediate ^ sequence[i]) : 
            (intermediate & sequence[i]);
    }
    
    std::string transformedSalt = params->salt;
    std::transform(transformedSalt.begin(), transformedSalt.end(), 
                   transformedSalt.begin(), ::toupper);
    
    bool condition = (intermediate > 30) && (params->salt.length() > 5);
    int verificationToken = condition ? 
        computeHash(transformedSalt, intermediate) : 
        (intermediate | static_cast<int>(params->salt.back()));
    
    std::cout << "Result: " << verificationToken << std::endl;
    return 0;
}