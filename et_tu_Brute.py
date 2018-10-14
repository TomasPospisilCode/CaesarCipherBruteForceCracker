#!/usr/bin/env

def etTuBrute():
    #I split alphabet to two parts, one containing big letters and one small
    smallAlphabet = "abcdefghijklmnopqrstuvwxyz"
    largeAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Caesar alphabet can be shifted by 0-26 characters
    key = "0"

    #User enter ciphered text
    cipheredText = input("Enter ciphered text[without spaces]: ")

    #Go through all keys
    for key in range(27):
        # Go through every character in ciphered text
        translatedText = ""
        for character in cipheredText:
            currentAlphabet = ""

            # Find out, if character is big letter or small letter and set correct alphabet
            if character.isupper():
                currentAlphabet = largeAlphabet
            else:
                currentAlphabet = smallAlphabet
            #We find current character that we are deciphering in our alphabet and substract key from it, so we got index of deciphered character
            indexOftranslatedChar = currentAlphabet.find(character) - key

            #Check for overflow, that should do the work but I'm not entirely sure
            if indexOftranslatedChar > len(currentAlphabet):
                indexOftranslatedChar = indexOftranslatedChar - len(currentAlphabet)
            elif indexOftranslatedChar < 0:
                indexOftranslatedChar = indexOftranslatedChar + len(currentAlphabet)

            translatedText = translatedText + currentAlphabet[indexOftranslatedChar]

        print('%s Attempt: %s'%(str(key), translatedText))

etTuBrute()