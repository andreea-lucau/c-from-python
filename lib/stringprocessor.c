#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int min(int a, int b) {
    return (a < b) ? a : b;
}


int is_vowel(char c) {
    static char vowels[] = {'a', 'e', 'i', 'o', 'u'};
    int vowels_no = sizeof(vowels) / sizeof(char);

    for (int i = 0; i < vowels_no; i++) {
        if (c == vowels[i]) {
            return 1;
        }
    }

    return 0;
}


int count_vowels(const char *word, int len) {
    if ((word == NULL) || (len == 0)) {
        return 0;
    }

    int vowels = 0;
    for (int i = 0; i < min(strlen(word), len); i++) {
        if (is_vowel(word[i])) {
            vowels += 1;
        }
    }

    return vowels;
}

int main() {
    char* word = "testword";

    printf("Vowels in %s: %d\n", word, count_vowels(word, 5));
}
