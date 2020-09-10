# its350
course materials and references for its350

## Lab04: Block cipher mode of operation

__Description__

Get familiar with block cipher mode of operation, complete the following tasks:

1. (9%, each mode 3%)Encrypting, decrypting, comparing (the decrypted with the original) a data file using different ciphers and modes, at least 3 different ones, for example
  * -aes-128-cbc
  * -aes-128-ecb
  * -aes-128-ofb
2. (10%, each image 5%)Applying encryption/decryption/comparison(the decrypted with the original)  on _ONLY the DATA_ of two image files: a complex image(9%) such as this [dragon](./data/dragon.jpg) and a monotone clipart(9%) such as this [bird](./data/bird.png), _search and download images by yourself_, with AES ECB mode and CBC mode.

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
3. Padding.
  * (16%, each mode 4%)Use ECB, CBC, CFB, and OFB modes to encrypt a file (you can pick any cipher). Compare the size of each encrypted file with the size of its plaintext file.
  * (18%, each file 6%)Create three files, which contain 5 bytes, 10 bytes, and 16 bytes of any data, respectively. Then encrypt these three files using 128-bit AES with CBC mode. Then find their paddings in these encrypted files.

4. (24%, each mode 6%)Error propagation – recover plaintext from corrupted ciphertext.
  * Create a file with exactly 60 bytes
  * Encrypt the file using the AES-128 cipher with the encryption mode ECB, CBC, CFB, or OFB, respectively
  * For each encrypted file, use the hex editor --- bless  to flip only one bit of the 17th byte
  * Decrypt the corrupted files, with [vbindiff](https://www.cjmweb.net/vbindiff/), compare the decrypted files with their corresponding unencrypted files

__Report__

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences.

_Review questions:_
1. (7%, each image 3.5%)In task 2, can you derive any useful information about the original pictures from the encrypted pictures? Please explain your observations.
2. (8%, each mode 2%)In task 3, which modes have paddings and which ones do not? For those that do not need paddings, please explain why.
3. (8%, each mode 2%)In task 4, how much information can you recover by decrypting the corrupted file, if the encryption mode is ECB, CBC, CFB, or OFB, respectively?  




__References__
* [General Montgomery’s One Page Battle Plan for D-Day Released](https://www.warhistoryonline.com/war-articles/battle-plans-d-day-released.html)
* [BMP file format](https://en.wikipedia.org/wiki/BMP\_file\_format)
* [How to convert an image to a 24-bit BMP in commandline?](https://unix.stackexchange.com/questions/394003/how-to-convert-an-image-to-a-24-bit-bmp-in-commandline)
* [openclipart](https://openclipart.org/)
* [SEED Pseudo Random Number Generation Lab](https://seedsecuritylabs.org/Labs\_16.04/Crypto/Crypto\_Random\_Number/)
* [SEED Crypto Lab -- Secret-Key Encryption](https://seedsecuritylabs.org/Labs\_16.04/Crypto/Crypto\_Encryption/)
* [Five hex editors](https://itsfoss.com/hex-editors-linux/)