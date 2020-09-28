# its350
course materials and references for its350

## Lab05: Secret key exchange with RSA

__Description__

Demonstrate the process `Symmetric key exchange with public cipher' using RSA for key exchange  and -aes-128-ofb for securing session communication.

_Symmetric key exchange with public cipher_

Suppose Alice wants to communicate with Bob confidentially, they follow the steps below:
1. (10%)Alice generates a pair of public/private keys
2. (5%)Alice sends her public key to Bob
3. (15%)Bob uses Alice’s public key to encrypt  the symmetric cipher’s specifics (a text file) then sends the ciphertext to Alice. The symmetric cipher's specifics includes:
  * the symmetric cipher is: -aes-128-ofb
  * a symmetric key (session key) ,  which should be generated randomly
4. (10%)Alice decrypts the ciphertext with her private key to get the
symmetric key (session key) and the symmetric cipher’s specifics
5. (40%)Alice and Bob secure their following communication (session) with the symmetric key (session key) and the symmetric cipher from the symmetric cipher’s specifics
  * (10%)Alice downloads an image from Internet and uses it as the session content. She only encrypts the _data portion_ of the image then sends the encrypted image to Bob
  * (10%)Bob received then encrypted image from Alice, then decrypts it to get the plain image
  * (10%)Bob downloads an image (should be different from Alice's) from Internet and uses it as the session content. He only encrypts the _data portion_ of the image then sends the encrypted image to Alice
  * (10%)Alice received then encrypted image from Alice, then decrypts it to get the plain image
6. The session key is discarded after the session



```bash
# convert image from any format into 24bit BMP image
convert image.any -type truecolor image.bmp

# 24bit BMP image dissection
# extract head
head -c 54 image.bmp > header
# extract data
tail -c +55 image.bmp > data
# concatenate head and data
cat header data > new.bmp
```


__Report__

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences.

_Review questions:_
1. (20%)Is it appropriate to secure communication only using RSA? Explain your answer.
   1. (10%) answer and explain
   2. (10%) performance comparison


__References__

* [openssl wiki](https://wiki.openssl.org/index.php/Main\_Page)
* [OpenSSL Command-Line HOWTO](https://www.madboa.com/geek/openssl/)
* [OpenSSL Cookbook](https://www.feistyduck.com/books/openssl-cookbook/)
* [openssl-speed, speed - test library performance](https://www.openssl.org/docs/man1.1.1/man1/openssl-speed.html)
* [How can I interpret openssl speed output?](https://stackoverflow.com/questions/17410270/how-can-i-interpret-openssl-speed-output)
