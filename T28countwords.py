def count_words(sentence):
    # Remove leading and trailing whitespace
    sentence = sentence.strip()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Return the number of words
    return len(words)

# Example usage:
sentence = "I love programming in Python"
print(count_words(sentence))  # Output: 5