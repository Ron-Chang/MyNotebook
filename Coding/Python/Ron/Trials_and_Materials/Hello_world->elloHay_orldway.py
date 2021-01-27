"""
Move the first letter of each word to the end of it, then "ay" to the end of the word.
Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""
from string import punctuation

def pig_it(text):
    sentence = text.split(" ")
    result =""
    for word in sentence:
        if len(word) == 1 and word[0] in punctuation:
            result += word+" "
        elif word[0] not in punctuation and word[-1] not in punctuation:
            word = word[1:]+word[0]+"ay"
            result += word+" "
        elif word[0] not in punctuation and word[-1] in punctuation:
            word = word[1:-1]+word[0]+"ay"+word[-1]
            result += word+" "
        else:
            word+="ay"
            result += word+" "

    return result.strip()

# # clever one
# import re

# def pig_it(text):
#     return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)

x = pig_it("! Pig, latin is cool")
y = pig_it("Hello world!")

print(f"!, Pig, latin is cool\n{x}\nHello world !\n{y}")
