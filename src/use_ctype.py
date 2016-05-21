"""Example of using C code in Python with ctype."""

import ctypes
import ctypes.util
import os


_libstringprocessor = None


class Error(Exception):
    pass


def load_libstringprocessor():
    """Load the C library and setup the count_vowel method."""
    global _libstringprocessor
    if _libstringprocessor:
        return

    basepath = os.path.dirname(os.path.abspath(__file__))
    _libstringprocessor_name = os.path.join(basepath, 'libstringprocessor.so')
    _libstringprocessor = ctypes.CDLL(_libstringprocessor_name)

    _libstringprocessor.count_vowels.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int)
    _libstringprocessor.count_vowels.restype = ctypes.c_int


def count_vowels(word):
    """Get the number of vowels in a string.

    Args:
        word: string, the string to process

    Returns:
        int, the number of vowels in the string
    """
    # Make sure the library is loaded
    load_libstringprocessor()

    # Convert the arguments to ctype data type
    word = word.encode("utf-8")
    c_word = ctypes.create_string_buffer(word)
    c_len = ctypes.c_int(len(word))

    # Call the function from the library
    return _libstringprocessor.count_vowels(c_word, c_len)


def main():
    test_word = 'testword'
    print '"%s" has %d vowels' % (test_word, count_vowels(test_word))


if __name__ == "__main__":
    main()
