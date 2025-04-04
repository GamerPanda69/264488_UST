# firstapp.py

# 1. Program to find Permutations of a string
def get_permutations(s, step=0):
    # Allow passing a string directly by converting it to a list in the first call.
    if isinstance(s, str) and step == 0:
        s = list(s)
    if step == len(s):
        print("".join(s))  # Print each permutation
        return
    for i in range(step, len(s)):
        s_list = list(s)
        s_list[step], s_list[i] = s_list[i], s_list[step]  # Swap characters
        get_permutations(s_list, step + 1)  # Recursive call


# 2. Program to make Title (capitalize first letter of each word)
def makeTitle(string):
    if string.istitle():
        print("The given string is already a Title")
    word_list = string.split()
    new_word = [word.capitalize() for word in word_list]
    capitalised_string = ' '.join(new_word)
    print("Title changed:")
    print(capitalised_string)


# 3. Program to Normalize Spaces
def normalizeSpaces(input_sentence):
    new_list = []
    space = False
    for item in input_sentence:
        if item != ' ':
            new_list.append(item)
            space = False
        elif not space:
            new_list.append(' ')
            space = True
    converted_sentence = ''.join(new_list)
    print("Converted sentence:", converted_sentence)
    return converted_sentence


# 4. Program to Get Span
def getspan(s, r):
    count = 0
    spans = []
    start = 0
    while True:
        start = s.find(r, start)
        if start == -1:
            break
        end = start + len(r)
        spans.append((start, end))
        count += 1
        start += 1  # Move to the next character for subsequent occurrences
    return count, spans


# 5. Program to Reverse Words
def reverseWords(s):
    words = s.split()  # Split into words
    reversed_sentence = " ".join(words[::-1])  # Reverse the list of words and join them
    print("Reversed sentence:", reversed_sentence)
    return reversed_sentence


# 6. Program to Remove Punctuation
def removePunctuation(s):
    result = ""
    for char in s:
        if char.isalnum() or char.isspace():  # Keep only letters, numbers, and spaces
            result += char
    print("String without punctuation:", result)
    return result


# 7. Program to Swap Cases and Transform (reverse the string while swapping cases)
def transform(s):
    reversed_string = ""
    for char in s:
        # Swap case manually
        if char.islower():
            new_char = char.upper()
        else:
            new_char = char.lower()
        # Prepend the character to reverse the string
        reversed_string = new_char + reversed_string
    return reversed_string


# 8. Program to Count Words
def countWords(s):
    count = 0
    in_word = False  # Flag to track if we're inside a word
    for char in s:
        if char.isspace():
            in_word = False  # We are outside a word
        elif not in_word:
            count += 1  # Found a new word
            in_word = True  # Now inside a word
    return count


# 9. Program to return a dictionary with characters of s as keys and their frequencies as values
def characterMap(s):
    freq = {}  # Initialize an empty dictionary
    for char in s:
        if char in freq:
            freq[char] += 1  # Increment count if character exists
        else:
            freq[char] = 1  # Initialize count for new character
    return freq

