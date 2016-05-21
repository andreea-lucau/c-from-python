import os

import string_processor1
import string_processor2


def setup():
    lib_path = os.path.dirname(os.path.abspath(__file__))
    lib_path = os.path.join(os.path.dirname(lib_path), "lib")

    if lib_path not in os.environ.get('LD_LIBRARY_PATH', ''):
        os.environ['LD_LIBRARY_PATH'] = lib_path + ':' + os.environ['LD_LIBRARY_PATH']


def main():
    setup()

    test_word = 'testword'
    print '[ctype]  "%s" has %d vowels' % (test_word, string_processor1.count_vowels(test_word))
    print '[cython] "%s" has %d vowels' % (test_word, string_processor2.count_vowels(test_word))


if __name__ == "__main__":
    main()
