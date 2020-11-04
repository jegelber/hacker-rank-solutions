# Score: 25/25

# put magazine words in Counter
# put note words in Counter
# loop through

from collections import Counter

def checkMagazine(magazine, note):
    magazine_words = Counter(magazine)
    note_words = Counter(note)
    if (note_words - magazine_words) == {}:
        print("Yes")
    else:
        print("No")

checkMagazine(['ive','Got','some','coconuts','yay'],['ive','got','some','coconuts'])
