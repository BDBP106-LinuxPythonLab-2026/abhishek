#Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the set() function might be useful here.
sent = ["abhi","abhi","pycharm"]
unique_words = set[str](sent)
print(unique_words)


#or

sent = "abhi abhi pycharm"
s=sent.split()
unique_words = set[str](s)
print(unique_words)