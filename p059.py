#!/usr/bin/python2
from itertools import product
from string import lowercase
from Words import words

wordset = set(words)
def decrypt(s,key):
    return "".join([chr(a^ord(key[i%len(key)])) for i,a in enumerate(s)])

encrypted = [int(i) for i in open("p059_cipher.txt").read().split(',')]

n_spaces = [(decrypt(encrypted,l).lower().count("e"), l) for l in lowercase]
n_spaces.sort(reverse=True)
print n_spaces[:10]
max_words = 0
for key in product([l for n,l in n_spaces[:10]],repeat=3):
    s = decrypt(encrypted,key)
    w =  len(set(s.lower().split()) & wordset)
    if w > max_words:
        max_words = w
        max_key = key
        max_string = s
        print max_words, max_string

print max_key,max_string
print sum( [ord(a) for a in max_string])

for a in lowercase:
    print a, max_string.lower().count(a)
