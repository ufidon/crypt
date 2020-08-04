#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def encryptmodb(plain, key):
    """ encryption
        plain --- plain text, binary string
        key    --- symmetric key, binary string
    """
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        return
        
    cipher = bytearray(b'0'*xlen)
    i = 0
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher[i] = int((p+k) % 256) #.to_bytes(1,byteorder='little')
        i = i+1
    return cipher  
        
def decryptmodb(cipher, key):
    """ decryption
        cipher --- cipher text, binary string
        key    --- symmetric key, binary string
    """
    xlen = len(cipher)
    if(xlen !=  len(key)):
        print("ciphertext length should equal key length")
        return
    
    plain = bytearray(b'0'*xlen)
    i = 0
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain[i] = int((c-k) % 256) #.to_bytes(1,byteorder='little')
        i = i+1
    return plain 


def encryptxorb(plain, key):
    """ encryption
        plain --- plain text, binary string
        key    --- symmetric key, binary string
    """
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        return
        
    cipher = bytearray(b'0'*xlen)
    i = 0
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher[i] = int(p ^ k) #.to_bytes(1,byteorder='little')
        i = i+1
    return cipher
        
def decryptxorb(cipher, key):
    """ decryption
        cipher --- cipher text, binary string
        key    --- symmetric key, binary string
    """
    xlen = len(cipher)
    if(xlen !=  len(key)):
        print("ciphertext length should equal key length")
        return
    
    plain = bytearray(b'0'*xlen)
    i = 0
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain[i] = int(c ^ k) #.to_bytes(1,byteorder='little')
        i = i+1
    return plain


        
if __name__ == '__main__':
    ##### encryption & edecryption on 'GeneralMontgomerysDDaySpeech.txt
    # with one time pad by module addition
    f1 = open('GeneralMontgomerysDDaySpeech.txt','rb')
    s1 = f1.read()
    f1.close()
    l1 = len(s1)
    print('Message length of GeneralMontgomerysDDaySpeech.txt: ',l1)
    
    k1 = os.urandom(l1)
    e1 = encryptmodb(s1,k1)
    w1 = open('ModEncryptedGeneralMontgomerysDDaySpeech.txt','wb')
    w1.write(e1)
    w1.close()
    
    fw1 = open('ModEncryptedGeneralMontgomerysDDaySpeech.txt','rb')
    re1 = fw1.read()
    de1 = decryptmodb(re1,k1)
    fw1.close()
    
    print('One time pad cipher with module addition on demonstration on "GeneralMontgomerysDDaySpeech.txt"')
    #print('----------------------------------------')
    #print("{:<20}".format('original plaintext:'),s1)
    #print("{:<20}".format('ciphertext:'), re1)
    #print("{:<20}".format('decrypted text:'), de1)
    if de1 == s1:
        print('demonstration on "GeneralMontgomerysDDaySpeech.txt" SUCCEEDED.')
    else:
        print('demonstration on "GeneralMontgomerysDDaySpeech.txt" FAILED.')
        
    ##### encryption & edecryption on 'GeneralMontgomerysDDaySpeech.txt'
    # with one time pad by bit xor
    f2 = open('GeneralMontgomerysDDaySpeech.txt','rb')
    s2 = f2.read()
    f2.close()
    l2 = len(s2)
    print('Message length of GeneralMontgomerysDDaySpeech.txt: ',l2)
    
    k2 = os.urandom(l2)
    e2 = encryptxorb(s2,k2)
    w2 = open('XorEncryptedGeneralMontgomerysDDaySpeech.txt','wb')
    w2.write(e2)
    w2.close()
    
    fw2 = open('XorEncryptedGeneralMontgomerysDDaySpeech.txt','rb')
    re2 = fw2.read()
    de2 = decryptxorb(re2,k2)
    fw2.close()
    
    print('One time pad cipher with module addition on demonstration on "GeneralMontgomerysDDaySpeech.txt"')
    #print('----------------------------------------')
    #print("{:<20}".format('original plaintext:'),s2)
    #print("{:<20}".format('ciphertext:'), re2)
    #print("{:<20}".format('decrypted text:'), de2)
    if de2 == s2:
        print('demonstration on "GeneralMontgomerysDDaySpeech.txt" SUCCEEDED.')
    else:
        print('demonstration on "GeneralMontgomerysDDaySpeech.txt" FAILED.')
        


    

