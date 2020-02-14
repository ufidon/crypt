#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encrypt(plain, key):
    """ encryption
        plain --- plain text
        key    --- symmetric key
    """
    blocksize = len(key)
    msglen = len(plain)
    if msglen % blocksize != 0:
        print("bad key!")
        return
    
    numblocks = msglen // blocksize
    cipher = []
    for b in range(numblocks):
        for i in range(blocksize):
            cipher.append(plain[b*blocksize + int(key[i])-1])

    return "".join(cipher)    

def decrypt(cipher, key):
    """ decryption
        cipher --- cipher text
        key    --- symmetric key
    """
    blocksize = len(key)
    msglen = len(cipher)
    if msglen % blocksize != 0:
        print("bad key!")
        return
    
    numblocks = msglen // blocksize
    pblk = ['0']*blocksize
    plain=[]
    for b in range(numblocks):
        for i in range(blocksize):
            pblk[int(key[i])-1]=cipher[b*blocksize + i]
        plain.extend(pblk)

    return "".join(plain)    
        

def demo(plaintext, key):
    # print("original plaintext:", plain)
    cipher = encrypt(plain, key)
    print(cipher)
    
    #test decryption
    decrypted_plain = decrypt(cipher, key)
    print(decrypted_plain)
        
if __name__ == '__main__':
    # test encryption
    plain = "on#the#mountain"
    key='31425'
    demo(plain,key)

    plain = "three#gun"
    key='312'
    demo(plain,key)
    
    plain = "aircraft"
    key = "52164387"
    demo(plain,key)
    
    plain = "weneedbullet"
    key = "312"
    demo(plain,key)
    
    plain = "flyjabovejcloudx"
    key = "57184326"
    demo(plain,key)
