#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>

template<int Modulus>
class EntropyPool {
private:
    int poolValue;

public:
    explicit EntropyPool(int initial) : poolValue(initial % Modulus) {}
    
    void addEntropy(int value) {
        poolValue = (poolValue + value) % Modulus;
    }
    
    int getValue() const {
        return poolValue;
    }
};

class TokenGenerator {
private:
    std::unique_ptr<EntropyPool<100>> primaryPool;
    std::unique_ptr<EntropyPool<75>> secondaryPool;

public:
    TokenGenerator(int seed1, int seed2) {
        primaryPool = std::make_unique<EntropyPool<100>>(seed1);
        secondaryPool = std::make_unique<EntropyPool<75>>(seed2);
    }
    
    int generateSecureToken() {
        int base = primaryPool->getValue();
        int modifier = secondaryPool->getValue();
        
        if (base > 50) {
            primaryPool->addEntropy(13);
        } else {
            secondaryPool->addEntropy(17);
        }
        
        // Execution point Y
        int finalToken = (primaryPool->getValue() * 2 + secondaryPool->getValue() * 3) % 1000;
        return finalToken;
    }
};

int main() {
    TokenGenerator tg(65, 42);
    int finalToken = tg.generateSecureToken();
    std::cout << "Result: " << finalToken << std::endl;
    return 0;
}