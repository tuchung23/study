
# This program take a phrase and replaces any vowels with the letter 'g'

def translate(phrase):
    # initialise string
    translation=""

    # loop through the word
    for single_letter in phrase:
        #print(single_letter)
        if single_letter in "AEIOUaeiou":
            translation=translation + "g"
        else:
            translation=translation +  single_letter
    return translation

print(translate(input("Enter a phrase: ")))