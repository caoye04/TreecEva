import collections
import statistics

def caesar_decode(text, shift):
    decoded = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded += chr((ord(char) - base - shift) % 26 + base)
        else:
            decoded += char
    return decoded

encoded_surveys = [
    'Rating: 75 Uliwkh#vxlwdeoh#udwh',
    'Rating: 82 Wkh#judgh#lv#jrrg',
    'Rating: 68 Dqrwkhu#udwh#hduob'
]
shift_value = 3

decoded_ratings = []
for survey in encoded_surveys:
    decoded_text = caesar_decode(survey, shift_value)
    # Extract the rating (assumes format 'Rating: XX ...')
    rating_str = decoded_text.split()[1]
    decoded_ratings.append(int(rating_str))

mean_rating = statistics.mean(decoded_ratings)
print(f"Result: {mean_rating}")