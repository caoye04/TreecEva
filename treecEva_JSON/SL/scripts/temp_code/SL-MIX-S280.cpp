#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <memory>

class VaultHasher {
private:
    uint32_t state;

public:
    explicit VaultHasher(uint32_t seed) : state(seed) {}

    void update(char c) {
        uint32_t val = static_cast<uint32_t>(c);
        state ^= (val << 3) & 0xFFFFFFF0;
        state = (state >> 1) | (state << 31);
        state &= 0xFFFFFFFF;
    }

    uint32_t getHash() const { return state; }
};

int main() {
    std::string accessSequence = "SECURE_ACCESS_2025";
    auto hasher = std::make_unique<VaultHasher>(0x12345678);

    for (char c : accessSequence) {
        hasher->update(c);
    }

    uint32_t vaultKeyHash = hasher->getHash();
    std::cout << "Result: " << vaultKeyHash << std::endl;
    return 0;
}