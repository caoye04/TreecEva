#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

struct PacketHeader {
    unsigned int version : 4;
    unsigned int ihl : 4;
    unsigned int ttl : 8;
    unsigned int protocol : 8;
    unsigned int checksum : 16;
};

union HeaderConverter {
    struct PacketHeader fields;
    unsigned int raw;
};

unsigned int (*checksum_func)(unsigned int, unsigned int);

unsigned int compute_checksum(unsigned int a, unsigned int b) {
    return (a ^ b) + (a & b);
}

unsigned int greedy_parser(const char* token_stream) {
    unsigned int state = 0;
    int i = 0;
    while (token_stream[i] != '\0') {
        if (token_stream[i] == '1') {
            state = (state << 1) | 1;
        } else if (token_stream[i] == '0') {
            state = state << 1;
        } else {
            state += token_stream[i] - '0';
        }
        i++;
    }
    return state;
}

int main() {
    volatile unsigned int header_data = 0x4500003c;
    union HeaderConverter converter;
    converter.raw = header_data;
    
    checksum_func = compute_checksum;
    
    const char* tokens = "11010100111000101010111100001111";
    unsigned int parsed_value = greedy_parser(tokens);
    
    unsigned int field_sum = converter.fields.version + 
                             converter.fields.ihl + 
                             converter.fields.ttl + 
                             converter.fields.protocol;
    
    unsigned int final_checksum = checksum_func(field_sum, parsed_value);
    
    printf("Result: %u\n", final_checksum);
    return 0;
}