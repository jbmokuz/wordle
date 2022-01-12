from wordList import *

dLetters = {}

for i in range(0x61,0x7a+1):
    dLetters[chr(i)] = set()

for w in solutions:
    for c in w:
        dLetters[c].add(w)

maxSize = 0
bestWords = []
for w in solutions:
    s = set([])
    for c in w:
        s.update(dLetters[c])
    if len(s) > maxSize:
        bestWords = []
        maxSize = len(s)
    if len(s) == maxSize:
        bestWords.append(w)

print(bestWords)
    
