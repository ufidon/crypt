#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
    # test encryption
    pass

    

