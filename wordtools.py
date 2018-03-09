import string

from unit_tester import test


def cleanword(st):
    st_cleaned = ""
    for letter in st:
        if letter not in string.punctuation:
            st_cleaned += letter
    return st_cleaned

def has_dashdash(st):
    count = 0
    for letter in st:
        if letter == "-":
            count += 1
        else:
            count = 0
        if count == 2:
            return True
    return False

def extract_words(st):
    st_cleaned = ""
    for letter in st:
        if letter not in string.punctuation:
            st_cleaned += letter
        else:
            st_cleaned += " "
    tt = st_cleaned.lower()
    wds = tt.split()
    return wds

def wordcount(st,lista):
    count = 0
    for i in range(len(lista)):
        if st == lista[i]:
            count += 1
    return count

def wordset(lista):
    l_limpa = []
    for word in lista:
        if word not in l_limpa:
            l_limpa.append(word)
    l_limpa.sort()
    return l_limpa

def longestword(st):
    count = 0
    for word in st:
        if len(word) > count:
            count = len(word)
    return count

