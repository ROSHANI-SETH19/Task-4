def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

# Example usage:
sentence = "I love programming in Python"
print(find_longest_word(sentence))  # Output: "programming"
