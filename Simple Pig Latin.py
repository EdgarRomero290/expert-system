#DESCRIPTION:
#Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. Leave punctuation 
# marks untouched.

#Examples
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    r=[]
    for x in text.split():
        if x.isalnum():
            r.append(x[1:]+x[0]+'ay')
        else:
            r.append(x[0])   
    return " ".join(r)

######## Mejor Forma #####

#def pig_it(text):
    #lst = text.split()
    #return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

#def pig_it(text):
    #return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())