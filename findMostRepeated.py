# Description: Find the most repeated character in a text

SENTENCE = "abc"

# Convert the text to lowercase and remove spaces
SENTENCE = SENTENCE.replace(" ", "").lower()

# Create a dictionary to store the frequency of each character
char_frequency = {}

for char in SENTENCE:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1


char_frequency_sorted = sorted(char_frequency.items(),  # Convert the dictionary to a list of (key, value) tuples
                        key=lambda keyValuePair: keyValuePair[1], # Sort the list based on the value of each tuple
                        reverse=True)

print(char_frequency_sorted)

if not char_frequency_sorted:
    print("No characters found")
else:
    print(f"Most repeated character: {char_frequency_sorted[0][0]}")
