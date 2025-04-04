from firstapp import (
    get_permutations, makeTitle, normalizeSpaces,
    getspan, reverseWords, removePunctuation,
    transform, countWords, characterMap
)

# 1. Permutations test
input_str = "ABC"
print("Permutation Test")
print("Input:", input_str)
print("Output:")
get_permutations(input_str)

# 2. Make Title test
input_str = "this is a sample title"
print("\nMake Title Test")
print("Input:", input_str)
print("Output:")
makeTitle(input_str)

# 3. Normalize Spaces test
input_str = "This     has  so      many        spaces"
print("\nNormalize Spaces Test")
print("Input:", input_str)
print("Output:")
normalizeSpaces(input_str)

# 4. Get Span test
s = "This is a test. Testing is fun."
r = "test"
print("\nGet Span Test")
print("Input String:", s)
print("Input Span:", r)
count, spans = getspan(s, r)
print("Output:")
print(f"Number of occurrences of '{r}' in '{s}': {count}")
print(f"Spans of '{r}' in '{s}': {spans}")

# 5. Reverse Words test
input_str = "Reverse the order of these words"
print("\nReverse Words Test")
print("Input:", input_str)
print("Output:")
reverseWords(input_str)

# 6. Remove Punctuation test
input_str = "Hello, world! Welcome to the test."
print("\nRemove Punctuation Test")
print("Input:", input_str)
print("Output:")
removePunctuation(input_str)

# 7. Transform test
input_str = "Hello World"
print("\nTransform Test")
print("Input:", input_str)
print("Output:")
print(transform(input_str))

# 8. Count Words test
input_str = "adsd adasd assa"
print("\nCount Words Test")
print("Input:", input_str)
print("Output:")
print("Word count:", countWords(input_str))

# 9. Character Map test
input_str = "hello"
print("\nCharacter Map Test")
print("Input:", input_str)
print("Output:")
print(characterMap(input_str))
