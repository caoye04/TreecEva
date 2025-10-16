#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>
#include <regex>
#include <string>

int main() {
    std::unique_ptr<int> telemetry_code = std::make_unique<int>(0);
    std::string signal_packets[] = {"ID:0x1A STATUS:VALID", "ID:0x2B STATUS:ERROR", "ID:0x3C STATUS:VALID", "ID:0x4D STATUS:VALID"};
    std::regex valid_pattern("ID:0x([0-9A-F]+) STATUS:VALID");
    
    for (const auto& packet : signal_packets) {
        std::smatch matches;
        if (std::regex_search(packet, matches, valid_pattern)) {
            *telemetry_code += std::stoi(matches[1].str(), nullptr, 16);
        }
    }
    
    std::cout << "Result: " << *telemetry_code << std::endl;
    return 0;
}