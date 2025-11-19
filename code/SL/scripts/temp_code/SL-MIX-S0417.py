class TextProcessor:
    def __init__(self):
        self.state = 'START'
        self.position = 0
        self.encoded_chars = []
    
    def process_char(self, char):
        if self.state == 'START':
            if char.isalpha():
                self.state = 'ALPHA'
                transformed = chr((ord(char.lower()) - ord('a') + 5) % 26 + ord('a'))
                self.encoded_chars.append(transformed)
            elif char.isdigit():
                self.state = 'DIGIT'
                doubled = str(int(char) * 2)
                self.encoded_chars.extend(list(doubled))
            else:
                self.state = 'OTHER'
                self.encoded_chars.append(chr(ord(char) ^ 0x5C))
        elif self.state == 'ALPHA':
            if char.isalpha():
                transformed = chr((ord(char.lower()) - ord('a') + 5) % 26 + ord('a'))
                self.encoded_chars.append(transformed)
            elif char.isdigit():
                self.state = 'DIGIT'
                doubled = str(int(char) * 2)
                self.encoded_chars.extend(list(doubled))
            else:
                self.state = 'OTHER'
                self.encoded_chars.append(chr(ord(char) ^ 0x5C))
        elif self.state == 'DIGIT':
            if char.isdigit():
                doubled = str(int(char) * 2)
                self.encoded_chars.extend(list(doubled))
            elif char.isalpha():
                self.state = 'ALPHA'
                transformed = chr((ord(char.lower()) - ord('a') + 5) % 26 + ord('a'))
                self.encoded_chars.append(transformed)
            else:
                self.state = 'OTHER'
                self.encoded_chars.append(chr(ord(char) ^ 0x5C))
        elif self.state == 'OTHER':
            if char.isalpha():
                self.state = 'ALPHA'
                transformed = chr((ord(char.lower()) - ord('a') + 5) % 26 + ord('a'))
                self.encoded_chars.append(transformed)
            elif char.isdigit():
                self.state = 'DIGIT'
                doubled = str(int(char) * 2)
                self.encoded_chars.extend(list(doubled))
            else:
                self.encoded_chars.append(chr(ord(char) ^ 0x5C))
        self.position += 1

# Greedy algorithm to select optimal chunk sizes for processing
input_text = "Hello42World!"
processor = TextProcessor()

for i, char in enumerate(input_text):
    processor.process_char(char)

# Divide and conquer approach to finalize encoding
encoded_length = len(processor.encoded_chars)
print(f"Result: {encoded_length}")