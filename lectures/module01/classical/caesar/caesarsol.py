#!/usr/bin/env python
# -*- coding: utf-8 -*-

from caesar import *
#def encrypt(plain, key, alphabet):
#    """ encryption
#        plain --- plain text
#        key    --- symmetric key
#        alphabet --- a list of characters consisting the alphabet
#    """
#    realkey = 3
#    if type(key) == int :
#        realkey = key
#    else:
#        realkey = alphabet.index(key)
#        
#    numofchar = len(alphabet)
#    cipher = []
#    for ch in plain:
#        cipher.append(alphabet[(alphabet.index(ch)+realkey) % numofchar])
#    return "".join(cipher)    
#        
#def decrypt(cipher, key, alphabet):
#    """ decryption
#        cipher --- cipher text
#        key    --- symmetric key
#        alphabet --- a list of characters consisting the alphabet
#    """
#    realkey = 3
#    if type(key) == int :
#        realkey = key
#    else:
#        realkey = alphabet.index(key)    
#    
#    numofchar = len(alphabet)
#    plain = []
#    for ch in cipher:
#        plain.append(alphabet[(alphabet.index(ch)-realkey) % numofchar])
#    return "".join(plain)    
#
#def demo(alphabet, plaintext, key):
#    # print("original plaintext:", plain)
#    cipher = encrypt(plaintext, key, alphabet)
#    print(cipher)
#    
#    #test decryption
#    decrypted_plain = decrypt(cipher, key, alphabet)
#    print(decrypted_plain)
        
if __name__ == '__main__':
    # test encryption
    # alphabet = ['0','1','2','3','4','5','6','7','8','9']
    ##### encryption & edecryption on 'military plan one.txt'
    a1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    f1 = open('military plan one.txt','r')
    s1 = f1.read()
    f1.close()
    l1 = len(s1)
    print('Message length of military plan one.txt: ',l1)
    # message length is 93, key length can be 3,31,93
    k1 = 's'
    e1 = encrypt(s1,k1,a1)
    w1 = open('encrypted military plan one.txt','w')
    w1.write(e1)
    w1.close()
    
    fw1 = open('encrypted military plan one.txt','r')
    re1 = fw1.read()
    de1 = decrypt(re1,k1,a1)
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
    a2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          ' ','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@']
    f2 = open('military plan two.txt','r')
    s2 = f2.read()
    f2.close()
    l2 = len(s2)
    #print('Message length of military plan two.txt: ',l2)
    # message length is 93, key length can be 3,31,93
    k2 = 't'
    e2 = encrypt(s2,k2,a2)
    w2 = open('encrypted military plan two.txt','w')
    w2.write(e2)
    w2.close()
    
    fw2 = open('encrypted military plan two.txt','r')
    re2 = fw2.read()
    de2 = decrypt(re2,k2,a2)
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
    a3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          ' ','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', 
          '?', '@', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    f3 = open('military plan three.txt','r')
    s3 = f3.read()
    f3.close()
    l3 = len(s3)
    #print('Message length of military plan three.txt: ',l3)
    # message length is 93, key length can be 3,31,93
    k3 = 'u'
    e3 = encrypt(s3,k3,a3)
    w3 = open('encrypted military plan three.txt','w')
    w3.write(e3)
    w3.close()
    
    fw3 = open('encrypted military plan three.txt','r')
    re3 = fw3.read()
    de3 = decrypt(re3,k3,a3)
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
