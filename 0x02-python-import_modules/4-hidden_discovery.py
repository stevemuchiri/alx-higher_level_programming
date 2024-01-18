#!/usr/bin/python3
if __name__ == "__main__":
    """all words  without __"""
    import hidden_4

    words = dir(hidden_4)
    for words in words:
        if words[:2] != "__":
            print(words)
