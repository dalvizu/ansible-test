vowels = ['a', 'e', 'i', 'o', 'u']

def pig_latin_word(word):
    for j, letter in enumerate(word):
        if letter in vowels:
            return word[j:] + word[:j] + "ay"
    return word + "ay"

def to_pig_latin(words):

    pig_latin = []
    for i, word in enumerate(words.split(' ')):
        if word[0] in 'aeiou':
            pig_latin.append("Word: " + words[0] + "ay")
        else:
            pig_latin.append(pig_latin_word(word))

    return ' '.join(pig_latin)

class FilterModule(object):
    def filters(self):
        return { 'to_pig_latin': to_pig_latin}
