# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    nw=[]
    text = text.split()
    for i in text:
        if i.isalpha():
            new_word = i[1:] + i[0] + "ay"
            nw.append(new_word)
        else:
            nw.append(i)
    return ' '.join(nw)
      