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
    i=0
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher[i] = int((p+k) % 256) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(cipher)  
        
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
    i=0
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain[i] = int((c-k) % 256) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(plain) 


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
    i=0
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher[i] = int(p ^ k) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(cipher)
        
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
    i=0
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain[i] = int(c ^ k) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(plain)


        
if __name__ == '__main__':

    ##### encryption & edecryption on 'GeneralMontgomerysDDayPlan.bmp
    #---- with one time pad by module addition
    f1 = open('GeneralMontgomerysDDayPlan.bmp','rb')
    s1 = f1.read()
    f1.close()
    h1 = s1[:55]
    d1 = s1[55:]
    l1 = len(d1)
    
    print('Data length of GeneralMontgomerysDDayPlan.bmp: ',l1)
    
    k1 = os.urandom(l1)
    e1 = encryptmodb(d1,k1)
    w1 = open('ModEncryptedGeneralMontgomerysDDayPlan.bmp','wb')
    eb1 = h1+e1
    w1.write(eb1)
    w1.close()
    
    fw1 = open('ModEncryptedGeneralMontgomerysDDayPlan.bmp','rb')
    re1 = fw1.read()
    rh1 = re1[:55]
    rd1 = re1[55:]
    de1 = decryptmodb(rd1,k1)
    fw1.close()
    
    print('One time pad cipher with module addition on demonstration on "GeneralMontgomerysDDayPlan.bmp"')
    #print('----------------------------------------')
    #print("{:<20}".format('original plaintext:'),s1)
    #print("{:<20}".format('ciphertext:'), re1)
    #print("{:<20}".format('decrypted text:'), de1)
    db1 = rh1+de1
    if db1 == s1:
        print('demonstration on "GeneralMontgomerysDDayPlan.bmp" SUCCEEDED.')
    else:
        print('demonstration on "GeneralMontgomerysDDayPlan.bmp" FAILED.')

    #---- with one time pad by bit xor
    f2 = open('GeneralMontgomerysDDayPlan.bmp','rb')
    s2 = f2.read()
    f2.close()
    h2 = s2[:55]
    d2 = s2[55:]
    l2 = len(d2)
    
    print('Data length of GeneralMontgomerysDDayPlan.bmp: ',l2)
    
    k2 = os.urandom(l2)
    e2 = encryptmodb(d2,k2)
    w2 = open('XorEncryptedGeneralMontgomerysDDayPlan.bmp','wb')
    eb2 = h2+e2
    w2.write(eb2)
    w2.close()
    
    fw2 = open('XorEncryptedGeneralMontgomerysDDayPlan.bmp','rb')
    re2 = fw2.read()
    rh2 = re2[:55]
    rd2 = re2[55:]
    de2 = decryptmodb(rd2,k2)
    fw2.close()
    
    print('One time pad cipher with bit xor on demonstration on "GeneralMontgomerysDDayPlan.bmp"')
    #print('----------------------------------------')
    #print("{:<20}".format('original plaintext:'),s2)
    #print("{:<20}".format('ciphertext:'), re2)
    #print("{:<20}".format('decrypted text:'), de2)
    db2 = rh2+de2
    if db2 == s2:
        print('demonstration on "GeneralMontgomerysDDayPlan.bmp" SUCCEEDED.')
    else:
        print('demonstration on "GeneralMontgomerysDDayPlan.bmp" FAILED.')    

