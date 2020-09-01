#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For case insensitive alphabet and be able to handle upper case and lower case.


def encrypt(plain, key, alphabet):
    """ encryption
        plain --- plain text
        key    --- symmetric key
        alphabet --- a string of characters consisting the alphabet
    """
    alphabet = alphabet.lower()

    realkey = 3
    if type(key) == int :
        realkey = key
    else:
        realkey = alphabet.index(key)
        
    numofchar = len(alphabet)
    cipher = []
    for ch in plain:
        if ch.lower() in alphabet:
            if ch.islower():
                cipher.append(alphabet[(alphabet.index(ch)+realkey) % numofchar])
            else:
                cipher.append(alphabet[(alphabet.index(ch.lower())+realkey) % numofchar].upper())
        else:
            cipher.append(ch)
    return "".join(cipher)    
        
def decrypt(cipher, key, alphabet):
    """ decryption
        cipher --- cipher text
        key    --- symmetric key
        alphabet --- a string of characters consisting the alphabet
    """
    realkey = 3
    if type(key) == int :
        realkey = key
    else:
        realkey = alphabet.index(key)    
    
    numofchar = len(alphabet)
    plain = []
    for ch in cipher:
        if ch.lower() in alphabet:
            if ch.islower():
                plain.append(alphabet[(alphabet.index(ch)-realkey) % numofchar])
            else:
                plain.append(alphabet[(alphabet.index(ch.lower())-realkey) % numofchar].upper())
        else:
            plain.append(ch)
    return "".join(plain)    

def demo(alphabet, plaintext, key):
    # print("original plaintext:", plain)
    cipher = encrypt(plain, key, alphabet)
    print(cipher)
    
    #test decryption
    decrypted_plain = decrypt(cipher, key, alphabet)
    print(decrypted_plain)
        
if __name__ == '__main__':
    # test encryption
    # alphabet = ['0','1','2','3','4','5','6','7','8','9']
    #alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain = "Attack In The MORNING!"
    key='d'
    demo(alphabet,plain,key)

    plain = "retrieve"
    key='x'
    demo(alphabet,plain,key)
    
    plain='hot'
    for key in alphabet:
        print(key)
        demo(alphabet,plain,key)
