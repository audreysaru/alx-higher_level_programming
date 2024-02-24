#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence:
        # Return a tuple with length and first character of sentence
        return len(sentence), sentence[0]
    else:
        # If the sentence is empty, return (0, None)
        return 0, None
