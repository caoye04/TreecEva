#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

#define PACKET_COUNT 5

// State machine states
typedef enum {
    STATE_IDLE = 0,
    STATE_HEADER_RECEIVED,
    STATE_PAYLOAD_PROCESSING,
    STATE_CHECKSUM_VALIDATION,
    STATE_COMPLETE
} packet_state_t;

// Function pointer type for state handlers
typedef void (*state_handler_t)(packet_state_t* state, int* checksum);

// Packet data structure
struct network_packet {
    char header[8];
    int payload_size;
    unsigned char flags;
};

// Volatile variable to track state changes
volatile packet_state_t current_state = STATE_IDLE;

// State handler functions
void handle_idle(packet_state_t* state, int* checksum) {
    *checksum += 0x10;
    *state = STATE_HEADER_RECEIVED;
}

void handle_header_received(packet_state_t* state, int* checksum) {
    *checksum ^= 0xAA;
    *state = STATE_PAYLOAD_PROCESSING;
}

void handle_payload_processing(packet_state_t* state, int* checksum) {
    *checksum <<= 2;
    *state = STATE_CHECKSUM_VALIDATION;
}

void handle_checksum_validation(packet_state_t* state, int* checksum) {
    *checksum |= 0xF0;
    *state = STATE_COMPLETE;
}

void handle_complete(packet_state_t* state, int* checksum) {
    *checksum &= 0xFF;
    *state = STATE_IDLE; // Reset for next packet
}

// String hashing function for packet identification
unsigned int hash_string(const char* str) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++))
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    return hash;
}

int main() {
    // Initialize state handler function pointer array
    state_handler_t state_handlers[] = {
        handle_idle,
        handle_header_received,
        handle_payload_processing,
        handle_checksum_validation,
        handle_complete
    };
    
    // Sample packet data
    struct network_packet packets[PACKET_COUNT] = {
        {"PKT_HDR1", 128, 0x01},
        {"PKT_HDR2", 256, 0x02},
        {"PKT_HDR3", 64,  0x04},
        {"PKT_HDR4", 512, 0x08},
        {"PKT_HDR5", 32,  0x10}
    };
    
    int final_state_checksum = 0;
    
    // Process each packet through the state machine
    for (int i = 0; i < PACKET_COUNT; i++) {
        // Pattern matching for packet headers using string hashing
        unsigned int header_hash = hash_string(packets[i].header);
        
        // Simulate state transitions based on header hash values
        switch (header_hash % 5) {
            case 0:
                state_handlers[STATE_IDLE](&current_state, &final_state_checksum);
                break;
            case 1:
                state_handlers[STATE_HEADER_RECEIVED](&current_state, &final_state_checksum);
                break;
            case 2:
                state_handlers[STATE_PAYLOAD_PROCESSING](&current_state, &final_state_checksum);
                break;
            case 3:
                state_handlers[STATE_CHECKSUM_VALIDATION](&current_state, &final_state_checksum);
                break;
            case 4:
                state_handlers[STATE_COMPLETE](&current_state, &final_state_checksum);
                break;
        }
        
        // Apply bitwise operations based on packet flags
        final_state_checksum ^= (packets[i].flags << 4);
    }
    
    // Final adjustment based on last packet's payload size
    final_state_checksum += packets[PACKET_COUNT-1].payload_size;
    
    printf("Result: %d\n", final_state_checksum);
    return 0;
}