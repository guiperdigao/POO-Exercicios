import string

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+\"\'\’—,“./:;<=>?@‘[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                                ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

f = open("Alice’s Adventures in Wonderland.txt", "r")
content = f.read()
f.close()

words = text_to_words(content)

words_counts = {}
for word in words:
    words_counts[word] = words_counts.get(word,0)+1

word_items = list(words_counts.items())
word_items.sort()
g = open("alice_words.txt", "w")
g.write("Word              Count\n=======================\n")
for (palavra,quant) in word_items:
    g.write('{:<18s}{:<4d}\n'.format(palavra,quant))

g.close()