#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = len(sentence),sentence[0]
    if sentence == "":
        return (0, None)
    else:
        return tuple_a
