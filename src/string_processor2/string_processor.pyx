import atexit
cimport cstring_processor

def count_vowels(str word):
    cdef bytes bword = word.encode("utf-8")
    cdef int word_size = len(word)
    return cstring_processor.count_vowels(bword, word_size)
