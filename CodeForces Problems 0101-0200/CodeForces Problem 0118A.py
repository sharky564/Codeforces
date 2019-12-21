# String Task
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'w', 'x', 'z')
a = input()


def anti_vowel(s):
    for char in s:
        if char in vowels:
            s = s.replace(char, '')
    return s


def dot_consonant(t):
    for i in consonants:
        if i in t:
            t = t.replace(i, '.' + i)
    return t

print(dot_consonant(anti_vowel(a.lower())))
