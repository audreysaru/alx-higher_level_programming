#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence:
        # Return a tuple with the length and the first character of the sentence
        return len(sentence), sentence[0]
    else:
        # If the sentence is empty, return (0, None)
        return 0, None
