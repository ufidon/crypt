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
        
    cipher = b''
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher += int((p+k) % 256).to_bytes(1,byteorder='little')
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
    
    plain = b''
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain += int((c-k) % 256).to_bytes(1,byteorder='little')
    return plain 

def bstr2lnum(bstr,dox='d'):
    num = ''
    for ch in bstr:
        if dox == 'd':
            num += '{:03d} '.format(ch)
        elif dox == 'x':
            num += '{:02X} '.format(ch)
        elif dox == 'b':
            num += '{:08b} '.format(ch)
        
    return num

def demomodb(plaintext, key):
    """ 
        plain --- plain text, binary string
        key    --- symmetric key, binary string
    """  
    print("One time pad cipher by addition module demonstration:")
    print('-----------------------------------------------------')
    print("{:<20}".format("original plaintext:"),plaintext)
    print("{:<20}".format("key:"),key)
    cipher = encryptmodb(plain, key)
    print("{:<20}".format("ciphertext:"),cipher)
    
    #test decryption
    decrypted_plain = decryptmodb(cipher, key)
    print("{:<20}".format("decrypted plaintext:"),decrypted_plain)
    
    print("\n")
    nump = bstr2lnum(plaintext)
    numk = bstr2lnum(key)
    numc = bstr2lnum(cipher)
    print("{:<20}".format("plaintext in num:"),nump)
    print("{:<20}".format("key in num:"),numk)
    print("{:<20}".format("cipher in num:"),numc)
    print("\n\n")


def encryptxorb(plain, key):
    """ encryption
        plain --- plain text, binary string
        key    --- symmetric key, binary string
    """
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        return
        
    cipher = b''
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher += int(p ^ k).to_bytes(1,byteorder='little')
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
    
    plain = b''
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain += int(c ^ k).to_bytes(1,byteorder='little')
    return plain

def demoxorb(plaintext, key):
    """ 
        plain --- plain text, binary string
        key    --- symmetric key, binary string
    """    
    print("One time pad cipher by xor demonstration:")
    print('-----------------------------------------------------')
    print("{:<20}".format("original plaintext:"),plaintext)
    print("{:<20}".format("key:"),key)
    cipher = encryptxorb(plain, key)
    print("{:<20}".format("ciphertext:"),cipher)
    
    #test decryption
    decrypted_plain = decryptxorb(cipher, key)
    print("{:<20}".format("decrypted plaintext:"),decrypted_plain)
    
    print("\n")
    nump = bstr2lnum(plaintext,'x')
    numk = bstr2lnum(key,'x')
    numc = bstr2lnum(cipher,'x')
    print("{:<20}".format("plaintext in num:"),nump)
    print("{:<20}".format("key in num:"),numk)
    print("{:<20}".format("cipher in num:"),numc)
    
    numpb = bstr2lnum(plaintext,'b')
    numkb = bstr2lnum(key,'b')
    numcb = bstr2lnum(cipher,'b')
    print("{:<20}".format("plaintext in num:"),numpb)
    print("{:<20}".format("key in num:"),numkb)
    print("{:<20}".format("cipher in num:"),numcb)
    print("\n\n")
        
if __name__ == '__main__':
    # test encryption
    plain = "hide".encode()
    key   = 'west'.encode()
    demomodb(plain,key)
    demoxorb(plain,key)

    plain = "run!".encode()
    key   = 'aha?'.encode()
    demomodb(plain,key)
    demoxorb(plain,key)
    

