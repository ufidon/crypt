#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encrypt(plain, key, alphabet, algorithm):
    """ encryption
        plain --- plain text
        key    --- symmetric key
        alphabet --- a list of characters consisting the alphabet
        algorithm --- confusion algorithm
    """
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        return
        
    numofchar = len(alphabet)
    cipher = []
    for ch in plain:
        cipher.append(alphabet[(alphabet.index(ch)+realkey) % numofchar])
    return "".join(cipher)    
        
def decrypt(cipher, key, alphabet, algorithm):
    """ decryption
        cipher --- cipher text
        key    --- symmetric key
        alphabet --- a list of characters consisting the alphabet
        algorithm --- confusion algorithm
    """
    realkey = 3
    if str(key).isdigit() :
        realkey = key
    else:
        realkey = alphabet.index(key)    
    
    numofchar = len(alphabet)
    plain = []
    for ch in cipher:
        plain.append(alphabet[(alphabet.index(ch)-realkey) % numofchar])
    return "".join(plain)    

def demo(alphabet, plaintext, key):
    # print("original plaintext:", plain)
    cipher = encryptmod(plain, key, alphabet)
    print(cipher)
    
    #test decryption
    decrypted_plain = decryptmod(cipher, key, alphabet)
    print(decrypted_plain)
        
if __name__ == '__main__':
    # test encryption
    # alphabet = ['0','1','2','3','4','5','6','7','8','9']
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plain = "attackinthemorning"
    key='d'
    demo(alphabet,plain,key)

    plain = "retrieve"
    key='x'
    demo(alphabet,plain,key)
    
    plain='hot'
    for key in alphabet:
        print(key)
        demo(alphabet,plain,key)
