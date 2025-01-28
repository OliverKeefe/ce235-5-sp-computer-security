
#!/usr/bin/env python
from ScoresDict import ScoresDict

class DecryptMessage():
    """
    *   To acces the class members like the alphabet you must use the self atribute like : self.alphabet
    *   To call methods from the object itself like shift() or shift_char() you must use 
        the self atribute like self.shift() or self.shift_char()
    """

    def __init__(self):
        """
        Initializes the alphabet and the NLP Tool
        """
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.nlptool = ScoresDict()

    def decrypt(self,ciphertext):
        """
        Write code to find the original plaintext:
        1. Compute each one of the 26 shift combinations by calling shift() and storing them at the all_shifts array
        2. Determine which of the 26 combinations more likely to be the original plaintext 
           by using the provided Natural language tool ( these is already provided to you self.nlptool.argmax(all_shifts) )
        """
        all_shifts = []
        ## YOUR CODE GOES HERE

        return self.nlptool.argmax(all_shifts)

    def shift(self,ciphertext,shift):
        """
        Write the code to shift a given ciphertext n times. Shift each character and append it 
        to the plaintext variable until there are no more characters to shift.
        HINT : Shift every character of the ciphertext by calling shift_char()
        """
        plaintext = ""
        ## YOUR CODE GOES HERE

        return plaintext

    def shift_char(self,char,shift):
        """
        Write the code to shift a given character n times. You may call get_char_pos() to obtain the character position
        within the alphabet. You can retrieve an element from the alphabet array as self.alphabet[index]
        HINT : Use modulus operations to make the array cyclic.
        """
        if char.isalpha():
            ## YOUR CODE GOES HERE
            pos: int = self.get_char_pos(char)
            new_char_pos: int = (pos + shift) % len(self.alphabet)

            return self.alphabet[new_char_pos]
        else:
            return char

    def get_char_pos(self,char):
        """
        Returns the index position of a character within the alphabet
        """
        return self.alphabet.index(char)

if __name__ == "__main__":
    
    ciphertext = open('ciphertext.txt','r').read()

    dm = DecryptMessage()
    plaintext = dm.decrypt(ciphertext)
    
    open('plaintext.txt','w+').write(plaintext)