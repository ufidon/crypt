#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encryptmod(plain, key, alphabet):
    """ encryption
        plain --- plain text, normal string
        key    --- symmetric key, normal string
        alphabet --- a list of characters consisting the alphabet
    """
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        return
        
    numofchar = len(alphabet)
    cipher = []
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher.append(alphabet[(alphabet.index(p)+alphabet.index(k)) % numofchar])
    return "".join(cipher)    
        
def decryptmod(cipher, key, alphabet):
    """ decryption
        cipher --- cipher text, normal string
        key    --- symmetric key, normal string
        alphabet --- a list of characters consisting the alphabet
    """
    xlen = len(cipher)
    if(xlen !=  len(key)):
        print("ciphertext length should equal key length")
        return
    
    numofchar = len(alphabet)
    plain = []
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain.append(alphabet[(alphabet.index(c)-alphabet.index(k)) % numofchar])
    return "".join(plain) 

def lstr2lnum(txt,alphabet,dox='d'):
    num = ''
    for ch in txt:
        if dox == 'd':
            num += '{:02d} '.format(alphabet.index(ch))
        elif dox == 'x':
            num += '{:02X} '.format(alphabet.index(ch))
        elif dox == 'b':
            num += '{:08b} '.format(alphabet.index(ch))
        
    return num

def demomod(alphabet, plaintext, key):
    """ 
        plain --- plain text, normal string
        key    --- symmetric key, normal string
    """  
    
    print("One time pad cipher by addition module demonstration:")
    print('-----------------------------------------------------')
    print("{:<20}".format("original plaintext:"),plaintext)
    print("{:<20}".format("key:"),key)
    cipher = encryptmod(plain, key, alphabet)
    print("{:<20}".format("ciphertext:"),cipher)
    
    #test decryption
    decrypted_plain = decryptmod(cipher, key, alphabet)
    print("{:<20}".format("decrypted plaintext:"),decrypted_plain)
    
    print("\n")
    nump = lstr2lnum(plaintext,alphabet)
    numk = lstr2lnum(key, alphabet)
    numc = lstr2lnum(cipher, alphabet)
    print("{:<20}".format("plaintext in num:"),nump)
    print("{:<20}".format("key in num:"),numk)
    print("{:<20}".format("cipher in num:"),numc)
    print("\n\n")


def encryptxor(plain, key, alphabet):
    """ encryption
        plain --- plain text, normal string
        key    --- symmetric key, normal string
    """
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        return
        
    cipher = []
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher.append(alphabet.index(p) ^ alphabet.index(k))
    return cipher
        
def decryptxor(cipher, key, alphabet):
    """ decryption
        cipher --- cipher text, normal string
        key    --- symmetric key, normal string
    """
    xlen = len(cipher)
    if(xlen !=  len(key)):
        print("ciphertext length should equal key length")
        return
    
    plain = []
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain.append(alphabet[c ^ alphabet.index(k)])
    return "".join(plain)

def demoxor(alphabet, plaintext, key):
    """ 
        plain --- plain text, normal string
        key    --- symmetric key, normal string
    """    
    print("One time pad cipher by xor demonstration:")
    print('----------------------------------------')
    print("{:<20}".format("original plaintext:"),plaintext)
    print("{:<20}".format("key:"),key)
    cipher = encryptxor(plain, key, alphabet)
    xcipher = ''
    for n in cipher:
        xcipher += '{:02X} '.format(n)
    print("{:<20}".format("ciphertext:"),xcipher)
    
    #test decryption
    decrypted_plain = decryptxor(cipher, key, alphabet)
    print("{:<20}".format("decrypted plaintext:"),decrypted_plain)
    
    print("\n")
    nump = lstr2lnum(plaintext,alphabet,'x')
    numk = lstr2lnum(key, alphabet,'x')
    
    print("{:<20}".format("plaintext in num:"),nump)
    print("{:<20}".format("key in num:"),numk)
    print("{:<20}".format("cipher in num:"),xcipher)
    
    bcipher = ''
    for n in cipher:
        bcipher += '{:08b} '.format(n)
    #print("{:<20}".format("ciphertext:"),bcipher)
    numpb = lstr2lnum(plaintext,alphabet,'b')
    numkb = lstr2lnum(key, alphabet,'b')
    print("{:<20}".format("plaintext in num:"),numpb)
    print("{:<20}".format("key in num:"),numkb)
    print("{:<20}".format("cipher in num:"),bcipher)
    
    print("\n\n")
        
if __name__ == '__main__':
    # test encryption
    # alphabet = ['0','1','2','3','4','5','6','7','8','9']
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plain = "ambushthewestarmy"
    key   = 'letsgotowestville'
    demomod(alphabet,plain,key)
    demoxor(alphabet, plain,key)

    plain = "successful"
    key   = 'iloveyouin'
    demomod(alphabet,plain,key)
    demoxor(alphabet,plain,key)
    

