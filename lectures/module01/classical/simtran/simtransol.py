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
    cipher = encrypt(plaintext, key)
    print(cipher)
    
    #test decryption
    decrypted_plain = decrypt(cipher, key)
    print(decrypted_plain)
        
if __name__ == '__main__':
    ##### encryption & edecryption on 'military plan one.txt'
    f1 = open('military plan one.txt','r')
    s1 = f1.read()
    f1.close()
    l1 = len(s1)
    print('Message length of military plan one.txt: ',l1)
    # message length is 93, key length can be 3,31,93
    k1 = '231'
    e1 = encrypt(s1,k1)
    w1 = open('encrypted military plan one.txt','w')
    w1.write(e1)
    w1.close()
    
    fw1 = open('encrypted military plan one.txt','r')
    re1 = fw1.read()
    de1 = decrypt(re1,k1)
    fw1.close()
    
    print('Demonstration on "military plan one.txt"')
    print('----------------------------------------')
    print("{:<20}".format('original plaintext:'),s1)
    print("{:<20}".format('ciphertext:'), re1)
    print("{:<20}".format('decrypted text:'), de1)
    if de1 == s1:
        print('demonstration on "military plan one.txt" SUCCEEDED.')
    else:
        print('demonstration on "military plan one.txt" FAILED.')
        
    ###### encryption & edecryption on 'military plan two.txt'
    f2 = open('military plan two.txt','r')
    s2 = f2.read()
    f2.close()
    l2 = len(s2)
    print('Message length of military plan two.txt: ',l2)
    # message length is 93, key length can be 3,31,93
    k2 = '23154'
    e2 = encrypt(s2,k2)
    w2 = open('encrypted military plan two.txt','w')
    w2.write(e2)
    w2.close()
    
    fw2 = open('encrypted military plan two.txt','r')
    re2 = fw2.read()
    de2 = decrypt(re2,k2)
    fw2.close()
    
    print('\nDemonstration on "military plan two.txt"')
    print('----------------------------------------')
    print("{:<20}".format('original plaintext:'),s2)
    print("{:<20}".format('ciphertext:'), re2)
    print("{:<20}".format('decrypted text:'), de2)
    if de2 == s2:
        print('demonstration on "military plan two.txt" SUCCEEDED.')
    else:
        print('demonstration on "military plan two.txt" FAILED.') 
        
    ###### encryption & edecryption on 'military plan three.txt'
    f3 = open('military plan three.txt','r')
    s3 = f3.read()
    f3.close()
    l3 = len(s3)
    print('Message length of military plan three.txt: ',l3)
    # message length is 93, key length can be 3,31,93
    k3 = '23154'
    e3 = encrypt(s3,k3)
    w3 = open('encrypted military plan three.txt','w')
    w3.write(e3)
    w3.close()
    
    fw3 = open('encrypted military plan three.txt','r')
    re3 = fw3.read()
    de3 = decrypt(re3,k3)
    fw3.close()
    
    print('\nDemonstration on "military plan three.txt"')
    print('----------------------------------------')
    print("{:<20}".format('original plaintext:'),s3)
    print("{:<20}".format('ciphertext:'), re3)
    print("{:<20}".format('decrypted text:'), de3)
    if de3 == s3:
        print('demonstration on "military plan three.txt" SUCCEEDED.')
    else:
        print('demonstration on "military plan three.txt" FAILED.')         
