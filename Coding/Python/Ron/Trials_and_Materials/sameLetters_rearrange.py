"""
What is an anagram?
Well, two words are anagrams of each other if they both contain the same letters.
For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

def isCorrect(word, key):
    word_set=set(word)
    if len(list(set(word))) >= len(list(set(key))):
        for w in word_set:
            amt = word.count(w)
            if key.count(w) != amt:
                return False
        return True
    else:
        return False

def anagrams(word,words):
    result = []
    for key in words:
        if isCorrect(word, key):
            result.append(key)
    return(result)

# clever way
# def anagrams(word, words):
#     return list(filter(lambda x: sorted(word.lower())==sorted(x.lower()),words))



x, y = "aaddc", "acdda"
m, n = "asda", "afdg"
foo = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
print(foo)
zoo = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print(zoo)
