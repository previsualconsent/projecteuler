
import string

def triangle(n):
   return n*(n+1)/2

def word_value(word,value_map):
   return sum([value_map[letter] for letter in word])


tris = set([triangle(n) for n in range(1,100)])
alpha = dict( zip(string.uppercase,range(1,len(string.uppercase)+1)))

f = open("p042_words.txt","r")

count = 0
for word in f.read().split(","):
   if word_value(word.strip("\" "),alpha) in tris:
      print word
      count +=1

print count


