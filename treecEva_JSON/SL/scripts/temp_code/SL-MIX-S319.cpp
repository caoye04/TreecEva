#define _USE_MATH_DEFINES
#include <iostream>
#include <cstring>

class MemoryBlock {
private:
    char* data;
    size_t size;
    bool owned;

public:
    explicit MemoryBlock(size_t s) : size(s), owned(true) {
        data = new char[size];
        std::memset(data, 0, size);
    }
    
    ~MemoryBlock() {
        if (owned && data) delete[] data;
    }
    
    // Move constructor
    MemoryBlock(MemoryBlock&& other) noexcept 
        : data(other.data), size(other.size), owned(other.owned) {
        other.data = nullptr;
        other.size = 0;
        other.owned = false;
    }
    
    // Move assignment
    MemoryBlock& operator=(MemoryBlock&& other) noexcept {
        if (this != &other) {
            if (owned && data) delete[] data;
            data = other.data;
            size = other.size;
            owned = other.owned;
            other.data = nullptr;
            other.size = 0;
            other.owned = false;
        }
        return *this;
    }
    
    // Disable copy operations
    MemoryBlock(const MemoryBlock&) = delete;
    MemoryBlock& operator=(const MemoryBlock&) = delete;
    
    // Operator overloading for concatenation
    MemoryBlock operator+(const MemoryBlock& other) const {
        MemoryBlock result(this->size + other.size);
        std::memcpy(result.data, this->data, this->size);
        std::memcpy(result.data + this->size, other.data, other.size);
        return result;
    }
    
    size_t getSize() const { return size; }
    char* getData() const { return data; }
};

unsigned int hashString(const char* str) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++))
        hash = ((hash << 5) + hash) + c; // hash * 33 + c
    return hash;
}

int main() {
    MemoryBlock block1(10);
    MemoryBlock block2(20);
    
    // Simulate writing data
    for(size_t i = 0; i < block1.getSize(); ++i)
        block1.getData()[i] = static_cast<char>(i + 1);
    for(size_t i = 0; i < block2.getSize(); ++i)
        block2.getData()[i] = static_cast<char>(i + 11);
    
    // Concatenate using overloaded operator
    MemoryBlock combined = block1 + block2;
    
    // Hash tag for permission check
    const char* tag = "USER_DATA_SEGMENT";
    unsigned int tagHash = hashString(tag);
    
    bool isAdmin = false;
    bool isValidTag = (tagHash % 7 == 4);
    bool sufficientSize = (combined.getSize() > 25);
    
    // Short-circuit evaluation for access control
    int accessLevel = 0;
    if (isAdmin || (isValidTag && sufficientSize)) {
        accessLevel = (tagHash % 100) + static_cast<int>(combined.getSize());
    } else {
        accessLevel = tagHash % 10;
    }
    
    // Move semantics demonstration
    MemoryBlock movedBlock = std::move(combined);
    
    // Additional calculation using moved block
    if (movedBlock.getSize() > 0) {
        accessLevel += static_cast<int>(movedBlock.getData()[0]);
    }
    
    std::cout << "Result: " << accessLevel << std::endl;
    return 0;
}